import re

from py_wa_adb.wa_sqlite import WA_SQLITE
import time

def datetime_to_epoch(datetime_obj):
    return int(float(datetime_obj.strftime("%s"))*1000)



class WA_ADB(object):
    """
    """

    WHATSAPP_ANDROID_PACKAGE_STRING = "com.whatsapp"

    MAIN_ACTIVITY_STRING_REFERENCE = ".Main"

    MESSAGES_ROW_REGEX = b"(?P<_id>\d+)\|(?P<key_remote_jid>.*?)\|(?P<key_from_me>\d+)\|(?P<key_id>.*?)\|(?P<status>\d+)\|(?P<data>[\s\S]+?)\|(?P<timestamp>\d+)\n"
    
    def __init__(self,drivers):
        self.driver = drivers
        pass

    def wrap_adb_shell(self, command_string, wrap=True, device=None):
        """
        """
        device = "" if device is None else "-s {device} "
        if wrap:
            return command_string
        return command_string


    def get_kill_whatsapp_processes_string(self):
        """
        """
        return self.wrap_adb_shell("pkill {}").format(self.WHATSAPP_ANDROID_PACKAGE_STRING)

    def get_am_start_application(self):
        return self.wrap_adb_shell("am start -n {self.WHATSAPP_ANDROID_PACKAGE_STRING}/{}").format(self.MAIN_ACTIVITY_STRING_REFERENCE)

    def get_change_wa_db_perms(self):
        return self.wrap_adb_shell("chmod 777 {}").format(WA_SQLITE.DATABASE_PATH)
    
    def get_insert_into_messages_query(self, wa_number_id, message):
        return self.wrap_adb_shell("sqlite3 {} \\\"{}\\\"").format(WA_SQLITE.DATABASE_PATH,WA_SQLITE.get_insert_into_messages_query(wa_number_id, message))
        pass

    def get_insert_into_chat_list_query(self, wa_number_id):
        return self.wrap_adb_shell("sqlite3 {} \\\"{}\\\"").format(WA_SQLITE.DATABASE_PATH,WA_SQLITE.get_insert_into_chat_list_query(wa_number_id))
        pass

    def get_update_chatlist_query(self, wa_number_id):
        return self.wrap_adb_shell("sqlite3 {} \\\"{}\\\"").format(WA_SQLITE.DATABASE_PATH,WA_SQLITE.get_update_chatlist_query(wa_number_id))
    
    def get_read_messages_query(self, **kwargs):
        """
        """
        return self.wrap_adb_shell("sqlite3 {} \"{}\"").format(WA_SQLITE.DATABASE_PATH,WA_SQLITE.get_messages(**kwargs))
        pass
    def check_output(self,code, shell=True):
        return self.driver.execute_script('mobile: shell', {
                        'command': str(code),
                        'args': [],
                        'includeStderr': True,
                        'timeout': 5000
                 })
    def send_text_message(self, wa_number_id, message, device=None):
        """

        """
        self.check_output(self.get_kill_whatsapp_processes_string(), shell=True)
        self.check_output(self.get_change_wa_db_perms(), shell=True)
        
        self.check_output(self.get_insert_into_messages_query(wa_number_id, message), shell=True)
        for _ in range(5):
            try:
                self.check_output(self.get_insert_into_chat_list_query(wa_number_id), shell=True)
                break
            except Exception as e:
                print(e)
                time.sleep(3)
                continue
        for _ in range(5):
            try:
                self.check_output(self.get_update_chatlist_query(wa_number_id), shell=True)
            except Exception as e:
                print(e)
                time.sleep(3)
                continue
                
        self.check_output(self.get_am_start_application(), shell=True)

        pass

    def get_messages(self, parse_rows=False, **kwargs):
        """
        """
        
        sqlite_query_output = self.check_output(self.get_read_messages_query(**kwargs), shell=True)
        if parse_rows:
            return re.findall(self.MESSAGES_ROW_REGEX, sqlite_query_output)
        return sqlite_query_output
    

    pass

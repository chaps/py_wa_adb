import random
import string
import pytest
from py_wa_adb.wa_adb import WA_ADB, datetime_to_epoch
from py_wa_adb.wa_sqlite import WA_SQLITE


wa_adb = WA_ADB()


def test_wrap_adb_shell():
    """
    """
    assert wa_adb.wrap_adb_shell("test string") == "adb shell \"test string\""


def test_get_kill_whatsapp_processes_string():
    """
    """
    assert wa_adb.get_kill_whatsapp_processes_string() == \
    f"adb shell \"pkill com.whatsapp\""


def test_get_am_start_application_string():
    """
    """
    assert wa_adb.get_am_start_application() == \
    f"adb shell \"am start -n {WA_ADB.WHATSAPP_ANDROID_PACKAGE_STRING}/{WA_ADB.MAIN_ACTIVITY_STRING_REFERENCE}\""

def test_get_change_wa_db_perms():
    """
    """
    assert wa_adb.get_change_wa_db_perms() == \
    f"adb shell \"chmod 777 {WA_SQLITE.DATABASE_PATH}\""

@pytest.mark.skip
def test_get_insert_into_messages_query():
    """
    """

    # retrun self.wrap_adb_shell(WA_SQLITE.get_insert_into_messages_query(wa_number_id))
    pass

@pytest.mark.skip
def test_get_insert_into_chat_list_query():
    """
    """
    # return self.wrap_adb_shell(WA_SQLITE.get_insert_into_chat_list_query(wa_number_id))
    pass

@pytest.mark.skip
def test_get_update_chatlist_query():
    """
    """
    pass



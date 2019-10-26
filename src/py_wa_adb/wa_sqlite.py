
import time
from subprocess import check_output, CalledProcessError


class WA_SQLITE(object):
    """
    Class with references to create the query strings needed to be executed through ADB 
    in order to perform actions in androids' whatsapp.
    """

    K_CONSTANT = "-1150867590"

    DATABASE_PATH = "/data/data/com.whatsapp/databases/msgstore.db"

    MESSAGES_TABLE_NAME = "messages"

    CHAT_LIST_TABLE_NAME = "chat_list"

    INSERT_INTO_MESSAGES_QUERY = "INSERT INTO {messages_table_name} "\
    "(key_remote_jid, key_from_me, key_id, status, needs_push, data, timestamp, MEDIA_URL, media_mime_type, media_wa_type, MEDIA_SIZE, media_name , latitude, longitude, thumb_image, remote_resource, received_timestamp, send_timestamp, receipt_server_timestamp, receipt_device_timestamp, raw_data, media_hash, recipient_count, media_duration, origin) "\
    "VALUES ('{remote_jid}', 1, '{key_id_to}-{k_constant}', 0, 0, '{message}', {key_id_from}, '', '', 0, 0, '', 0.0, 0.0, '', '', {key_id_from}, -1, -1, -1, 0 , '', 0, 0, 0);"

    INSERT_INTO_CHATLIST_QUERY = "INSERT INTO {chatlist_table_name} (key_remote_jid) "\
    "SELECT '{remote_jid}' WHERE not exists (SELECT 1 from chat_list where key_remote_jid='{remote_jid}');"

    UPDATE_CHATLIST_QUERY = "UPDATE {chatlist_table_name} SET message_table_id = "\
    "(SELECT max(messages._id) FROM messages) WHERE chat_list.key_remote_jid='{remote_jid}';"

    GET_MESSAGES = "SELECT _id, key_remote_jid, key_from_me, key_id, status, data, timestamp FROM {messages_table_name}"
    
    FILTER_FROM_JID = " key_remote_jid = '{key_remote_jid}' "

    FILTER_FROM_DATE = " timestamp>={filter_from_date_epoch} "

    FILTER_TO_DATE = " timestamp<={filter_to_date_epoch} "

    def __init__(self, remote_jid):
        """
        """
        self.remote_jid = remote_jid
        pass

    @classmethod
    def get_key_id_to_and_from(cls):
        """
        """
        key_id_from=int(round(time.time() * 1000))
        key_id_to=int(key_id_from / 1000)
        return  (key_id_from, key_id_to)

    @classmethod
    def get_insert_into_messages_query(cls, remote_jid, message):
        """
        """
        key_id_from, key_id_to = cls.get_key_id_to_and_from()
        return cls.INSERT_INTO_MESSAGES_QUERY.format(
            remote_jid=remote_jid,
            messages_table_name=cls.MESSAGES_TABLE_NAME,
            key_id_from=key_id_from,
            key_id_to=key_id_to,
            k_constant=cls.K_CONSTANT,
            message=message,

        )
    
    @classmethod
    def get_insert_into_chat_list_query(cls, remote_jid):
        """
        """
        return cls.INSERT_INTO_CHATLIST_QUERY.format(
            remote_jid=remote_jid,
            chatlist_table_name=cls.CHAT_LIST_TABLE_NAME
        )

    @classmethod
    def get_update_chatlist_query(cls, remote_jid):
        """
        """
        return cls.UPDATE_CHATLIST_QUERY.format(
            remote_jid=remote_jid,
            chatlist_table_name=cls.CHAT_LIST_TABLE_NAME
        )
    
    @classmethod
    def get_messages(cls, key_remote_jid=None, from_date=None, to_date=None):
        """
        """
        query_string = cls.GET_MESSAGES.format(messages_table_name=cls.MESSAGES_TABLE_NAME)
        if key_remote_jid or from_date or to_date:
            query_string += " WHERE"
            filter_list = []
            if key_remote_jid:
                filter_list.append(cls.FILTER_FROM_JID.format(key_remote_jid=key_remote_jid))
            if from_date:
                filter_list.append(cls.FILTER_FROM_DATE.format(filter_from_date_epoch=from_date))
            if to_date:
                filter_list.append(cls.FILTER_TO_DATE.format(filter_to_date_epoch=to_date))
            query_string += "AND".join(filter_list)    
        query_string += ";"
        return query_string

    # re split...
    

    pass
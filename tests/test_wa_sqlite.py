import random
import string
import time
from py_wa_adb.wa_sqlite import WA_SQLITE


TEST_JID = "5519876543210@s.whatsapp.net"

###
# Test class methods
###

def test_get_insert_into_messages_query():
    WA_SQLITE.get_insert_into_messages_query(TEST_JID, "test message")
    pass

def test_get_insert_into_chat_list_query():
    WA_SQLITE.get_insert_into_chat_list_query(TEST_JID)
    pass

def test_get_update_chatlist_query():
    """
    """
    WA_SQLITE.get_update_chatlist_query(TEST_JID)
    pass

def test_get_messages_query():
    assert WA_SQLITE.get_messages() == f"SELECT _id, key_remote_jid, key_from_me, key_id, status, data, timestamp FROM {WA_SQLITE.MESSAGES_TABLE_NAME};"


def test_get_messages_query_filter_jid():
    assert WA_SQLITE.get_messages(key_remote_jid=TEST_JID) == \
    f"SELECT _id, key_remote_jid, key_from_me, key_id, status, data, timestamp FROM {WA_SQLITE.MESSAGES_TABLE_NAME} WHERE{WA_SQLITE.FILTER_FROM_JID.format(key_remote_jid=TEST_JID)};" 


def test_get_messages_query_filter_from_date():
    """
    """
    t = time.time()
    assert WA_SQLITE.get_messages(from_date=t) == \
    f"SELECT _id, key_remote_jid, key_from_me, key_id, status, data, timestamp FROM {WA_SQLITE.MESSAGES_TABLE_NAME} WHERE{WA_SQLITE.FILTER_FROM_DATE.format(filter_from_date_epoch=t)};" 

def test_get_messages_query_filter_to_date():
    """
    """
    t = time.time()
    assert WA_SQLITE.get_messages(to_date=t) == \
    f"SELECT _id, key_remote_jid, key_from_me, key_id, status, data, timestamp FROM {WA_SQLITE.MESSAGES_TABLE_NAME} WHERE{WA_SQLITE.FILTER_TO_DATE.format(filter_to_date_epoch=t)};" 

def test_get_messages_query_filter_jid_and_from_date():
    """
    """
    t = time.time()
    assert WA_SQLITE.get_messages(key_remote_jid=TEST_JID, from_date=t) == \
    f"SELECT _id, key_remote_jid, key_from_me, key_id, status, data, timestamp FROM {WA_SQLITE.MESSAGES_TABLE_NAME} WHERE{WA_SQLITE.FILTER_FROM_JID.format(key_remote_jid=TEST_JID)}AND{WA_SQLITE.FILTER_FROM_DATE.format(filter_from_date_epoch=t)};" 


###
# Test instance methods
###

# TODO



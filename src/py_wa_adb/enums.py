from enum import Enum


class Who(Enum):
    FROM_ME = "key_from_me == 1"
    OTHERS = "key_from_me != 1"
    ALL = ""
    pass


class Type(Enum):
    GPS = 1
    IMAGE = 2
    TEXT = 3


class COLUMN(Enum):
    _id = id = 0
    key_remote_jid = 1
    key_from_me = 2
    key_id = 3
    status = 4
    needs_push = 5
    data = 6
    message = 6
    timestamp = 7
    media_url = 8
    media_mime_type = 9
    media_wa_type = 10
    media_size = 11
    media_name = 12
    media_caption = 13
    media_hash = 14
    media_duration = 15
    origin = 16
    latitude = 17
    longitude = 18
    thumb_image = 19
    remote_resource = 20
    received_timestamp = 21
    send_timestamp = 22
    receipt_server_timestamp = 23
    receipt_device_timestamp = 24
    read_device_timestamp = 25
    played_device_timestamp = 26
    raw_data = 27
    recipient_count = 28
    participant_hash = 29
    starred = 30
    quoted_row_id = 31
    mentioned_jids = 32
    multicast_id = 33
    edit_version = 34
    media_enc_hash = 35
    payment_transaction_id = 36



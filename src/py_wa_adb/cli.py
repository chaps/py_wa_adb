

import argparse
import sys
from py_wa_adb.wa_adb import WA_ADB, datetime_to_epoch

class WA_ADB_CLI_PARSER(object):
    """
    """
    def __init__(self):
        """
        """
        self.parser = argparse.ArgumentParser(description='Process some integers.')
        self.subparsers = self.parser.add_subparsers()
        self.send_message_parser = self.subparsers.add_parser("send_message")
        self.send_message_parser.set_defaults(which="send_text_message")
        self.send_message_parser.add_argument("wa_number_id")
        self.send_message_parser.add_argument("message")
        self.send_message_parser.add_argument("--device", required=False)

        
        self.read_messages_parser = self.subparsers.add_parser("get_messages")
        self.read_messages_parser.set_defaults(which="get_messages")
        
        self.read_messages_parser.add_argument("--key_remote_jid", required=False)
        self.read_messages_parser.add_argument("--from_date", required=False)
        self.read_messages_parser.add_argument("--to_date", required=False)
        
        # get_messages
        # self.read_messages_parser.set_defaults(which="read_messages_parser")

        pass

    pass

def main():
    adb_cli_parser = WA_ADB_CLI_PARSER()
    x = adb_cli_parser.parser.parse_args()

    if not hasattr(x, "which"):
        print("MISSING ARGUMENT")
        sys.exit(-1)
        pass
    wa_adb = WA_ADB()
    # Call expected method and remove which from the passed args.
    print(getattr(wa_adb, x.which)(
        **{y[0]: y[1] for y in x._get_kwargs() if y[0] != "which"}
    ))
    pass



if __name__ == "__main__":
    main()
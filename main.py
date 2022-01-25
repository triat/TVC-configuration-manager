#!/usr/bin/env python3
"""
A simple tool that execute commands to the TVC DB to update its configuration table
"""

__author__ = "Tom Riat"
__version__ = "0.1.0"
__license__ = "MIT"


import argparse

import mysql.connector
from mysql.connector import errorcode


def main(args):
    print(args)

    if args.update and (args.config is None or args.value is None):
        print("Configuration and value is required for an update")
        return

    if args.update:
        cmd = f"UPDATE FROM Configuration SET {args.config.capitalize()} = '{args.value}' WHERE "
    elif args.delete:
        cmd = "DELETE FROM Configuration WHERE "
    else:
        print(
            "Please specify the action on the configuration, either '--update' or '--delete'"
        )
        return

    symbol_count = len(args.limit)
    count = 0
    for symbol in args.limit.split(","):
        cmd = cmd + f"Symbol = '{symbol}'"
        count += 1
        if count < symbol_count:
            cmd = cmd + " OR "
    cmd = cmd + ";"
    print(cmd)


if __name__ == "__main__":
    """This is executed when run from the command line"""

    parser = argparse.ArgumentParser(
        description="Update the TVC configuration table with given params"
    )
    parser.add_argument(
        "--update", action="store_true", help="Action that update configuraitons"
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Action that delete configurations",
    )
    parser.add_argument(
        "--limit",
        default="*",
        help="Limit the actions to specific coins, separate by ','. format: BTCUSDT",
    )
    parser.add_argument(
        "--config", help="Parameter to be updated. Required for an update"
    )
    parser.add_argument(
        "--value", help="New value to be updated. Required for an update"
    )

    args = parser.parse_args()

    try:
        cnx = mysql.connector.connect(
            user="scott", password="pwd", database="wick_hunter", host="localhost", port="12345"
        )
        main(args)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
        pass

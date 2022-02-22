#!/usr/bin/env python3
"""
A simple tool that execute commands to the TVC DB to update its configuration table
"""

__author__ = "Tom Riat"
__version__ = "0.1.1"
__license__ = "MIT"


import argparse
import os
from pathlib import Path

import logzero
import mysql.connector
from dotenv import load_dotenv
from logzero import logger
from mysql.connector import errorcode

dotenv_path = Path.home().joinpath("WickHunterTVCompanion/.env")
load_dotenv(dotenv_path=dotenv_path)


def main(params, connection):
    """Main function"""
    logger.debug(params)

    if params.update and (params.config is None or params.value is None):
        raise ValueError("Configuration and value is required for an update")

    sql_cmd = build_cmd(
        params.update,
        params.config,
        params.value,
        params.delete,
        params.symbols,
        params.exchange,
    )

    logger.info(sql_cmd)
    is_valid = input("Do you want to apply the changes: (yes/[No]) ")
    if is_valid.lower() == "yes":
        run_cmd(sql_cmd, connection)
    else:
        logger.info("Aborting...")


def build_cmd(is_update, config, value, is_delete, symbols, exchange):
    """Build the SQL command"""
    if is_update:
        cmd = f"UPDATE configuration SET {config.capitalize()} = " f"'{value}'"
    elif is_delete:
        cmd = "DELETE FROM configuration"
    else:
        raise ValueError(
            "Specify the action on the configuration, either '--update' "
            "or '--delete'. Use '--help' for more information."
        )

    if symbols is not None or exchange is not None:
        cmd += " WHERE "

        if symbols is not None:
            cmd += "("
            symbols = symbols.split(",")
            symbols_count = len(symbols)
            logger.debug("Symbol count: %s", symbols_count)
            count = 0
            for symbol in symbols:
                cmd = cmd + f"Symbol = '{symbol.upper()}'"
                count += 1
                if count < symbols_count:
                    cmd = cmd + " OR "
            cmd += ")"

        if exchange is not None:
            if symbols is not None:
                cmd += " AND "
            cmd += f"Exchange = '{exchange.lower()}'"

    cmd = cmd + ";"
    return cmd


def run_cmd(cmd, connection):
    """Run the SQL command"""
    logger.debug(cmd)
    connection.cursor().execute(cmd)
    connection.commit()
    logger.info("Changes applied successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update the TVC configuration table with given params"
    )
    parser.add_argument(
        "--update", "-u", action="store_true", help="Action that update configuraitons"
    )
    parser.add_argument(
        "--delete",
        "-d",
        action="store_true",
        help="Action that delete configurations",
    )
    parser.add_argument(
        "--symbols",
        "-s",
        default=None,
        help="Limit the actions to specific coins, separate by ','. format: BTCUSDT",
    )
    parser.add_argument(
        "--exchange",
        "-e",
        default=None,
        help="Limit the actions to a specific exchange.",
    )
    parser.add_argument(
        "--config",
        "-c",
        help=(
            "Parameter to be updated. Required for an update. "
            "Use --help for more information"
        ),
    )
    parser.add_argument(
        "--value",
        "-v",
        help=(
            "New value to be updated. Required for an update. "
            "Use --help for more information"
        ),
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Enable debug logging",
    )

    args = parser.parse_args()

    if not args.debug:
        # Default is set to DEBUG
        logzero.loglevel(logzero.INFO)

    try:
        logger.debug("Connecting to the database")
        logger.debug(os.getenv("DB_HOST"), os.getenv("DB_USER"), os.getenv("DB_NAME"))
        cnx = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME"),
            host=os.getenv("DB_HOST"),
            port="3306",
        )
        main(args, cnx)
    except mysql.connector.Error as err:
        logger.debug(err)
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("Database does not exist")
        else:
            logger.error(err)
    except ValueError as err:
        logger.warning(err)
    else:
        cnx.close()

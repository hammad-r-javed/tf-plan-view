import sys
from typing import Any
from os.path import isdir, isfile
from dataclasses import dataclass
from lib.util import log, LogT, ErrorT, require
from argparse import ArgumentParser, Namespace

@dataclass
class AppConfig:
    plan_path: str
    report_output_path: str

def is_dir(path: str) -> bool | ErrorT:
    try:
        return isdir(path)
    except Exception as e:
        return ErrorT(str(e))

def is_file(path: str) -> bool | ErrorT:
    try:
        return isfile(path)
    except Exception as e:
        return ErrorT(str(e))

def create_arg_parser() -> ArgumentParser:
    arg_parser: ArgumentParser = ArgumentParser()
    arg_parser.add_argument("-p", "--plan-path", type=str, help="File path to JSON plan output", default="")
    arg_parser.add_argument("-o", "--report-output-path", type=str, help="Desired output file path for interactive report. '.html' file extension will be appended if not already in file name, in provided path", default="")
    return arg_parser

def parse_args(args: Namespace) -> AppConfig | ErrorT:
    if not (args.report_output_path and args.plan_path):
        return ErrorT("Error, no args allowed to be empty")

    report_path_is_dir: bool = require(is_dir(args.report_output_path), f"Failure when checking if '--report-output-path' arg value, is a dir or file path")
    plan_path_is_file: bool = require(is_file(args.plan_path), f"Failure when checking if '--plan-path' arg value, is a dir or file path")

    if report_path_is_dir:
        return ErrorT(f"Arg '--report-output-path' value '{args.report_output_path}' must be a file path, not a dir")
    elif not plan_path_is_file:
        return ErrorT(f"Arg '--plan-path' value '{args.plan_path}' does not exist on disk")

    return AppConfig(plan_path=args.plan_path, report_output_path=args.report_output_path)

def main() -> None:
    arg_parser: ArgumentParser = create_arg_parser()
    config: AppConfig | ErrorT = parse_args(arg_parser.parse_args())
    if isinstance(config, ErrorT):
        log(LogT.ERR, f"Error - {config.value}")
        arg_parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()

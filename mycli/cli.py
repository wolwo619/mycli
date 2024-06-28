#!/usr/bin/env python

import argparse
import json
import os
from collections import Counter


def read_json_file(file_path):
    """
    Read data from a JSON file.
    If the file does not exist or is empty, return an empty list.
    :param file_path: Path of the file.
    """
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as file:
            return json.load(file)
    return []


def write_json_file(file_path, data):
    """
    Write data to a JSON file.
    :file_path: Path where file needs to be saved
    :data: Data to be saved in file
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def convert_logs_to_single_json(log_files, json_file):
    """
    Convert multiple log files to a single JSON file.
    :log_files: List of log_file's Path to be converted
    :json_file: Path where file needs to be saved
    """
    combined_logs = read_json_file(json_file)
    for log_file in log_files:
        with open(log_file, 'r', encoding="utf-8") as file:
            for line in file:
                log_entry = line.strip()
                if log_entry:
                    log_entry_list = list(filter(None, log_entry.split(" ")))
                    log_entry_values = {}
                    if len(log_entry_list) > 9:
                        log_entry_values = {
                            "Timestamp in seconds since the epoch": log_entry_list[0],
                            "Response header size in bytes": log_entry_list[1],
                            "Client IP address": log_entry_list[2],
                            "HTTP response code": log_entry_list[3],
                            "Response size in bytes": log_entry_list[4],
                            "HTTP request method": log_entry_list[5],
                            "URL": log_entry_list[6],
                            "Username": log_entry_list[7],
                            "Type of access/destination IP address": log_entry_list[8],
                            "Response type": log_entry_list[9]
                        }
                    combined_logs.append(log_entry_values)
    write_json_file(json_file, combined_logs)
    print(f"Log files have been combined into JSON file '{json_file}'.")
    return combined_logs


def find_least_frequent_value(dict_list, key):
    """
    Find the least frequent value for a given key in a list of dictionaries.
    :param dict_list: List of dictionaries.
    :param key: Key to find the least frequent value for.
    :return: The least frequent value and its count.
    """
    # Extract the values for the specified key
    values = [d[key] for d in dict_list if key in d]

    # Count the occurrences of each value
    value_counts = Counter(values)

    # Find the least common value and its count
    least_common_value, count = value_counts.most_common()[-1]
    print(f'{least_common_value} occurred {count} times')


def find_most_frequent_value(data, key):
    """
    Find the most frequent value for a given key in a list of dictionaries.
    :param data: List of dictionaries.
    :param key: Key to find the most frequent value for.
    :return: The most frequent value and its count.
    """
    # Extract the values for the specified key
    values = [d[key] for d in data if key in d]

    # Count the occurrences of each value
    value_counts = Counter(values)

    # Find the most common value and its count
    most_common_value, count = value_counts.most_common(1)[0]

    print(f'{most_common_value} occurred {count} times')


def calculate_events_per_second(log_entries):
    """
    Calculate events per second from log entries.
    :param log_entries: List of log entries (dictionaries).
    """
    timestamps = [int(float(entry['Timestamp in seconds since the epoch']))
                  for entry in log_entries]

    # Ensure timestamps are sorted
    timestamps.sort()

    # Calculate the total time span in seconds
    time_span = timestamps[-1] - timestamps[0]
    events_per_second = len(timestamps) / \
        time_span if time_span != 0 else len(timestamps)
    print(f"Events per second: {round(events_per_second, 2)}")


def calculate_bytes_exchanged(log_entries):
    """
    Calculate total bytes exchanged from log entries.
    :param log_entries: List of log entries (dictionaries).
    """
    key_1 = "Response header size in bytes"
    key_2 = "Response size in bytes"
    total_bytes = sum(int(d.get(key_1, 0)) + int(d.get(key_2, 0))
                      for d in log_entries)
    print(f"Bytes exchanged: {total_bytes}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert multiple log files into a single JSON file.")
    parser.add_argument("log_files", nargs="+", help="Paths to the log files")
    parser.add_argument("json_file", help="Path to the output JSON file")
    # Assuming Option had to made mandatory
    parser.add_argument('--mfip', action='store_true',
                        help='Print most frequent IP')
    parser.add_argument('--lfip', action='store_true',
                        help='Print least frequent IP')
    parser.add_argument('--eps', action='store_true',
                        help='Prints events per second')
    parser.add_argument('--bytes', action='store_true',
                        help='Prints total amount of bytes exchanged')
    args = parser.parse_args()

    logs = convert_logs_to_single_json(args.log_files, args.json_file)

    if args.mfip:
        find_most_frequent_value(
            logs, "Client IP address")

    elif args.lfip:
        find_least_frequent_value(
            logs, "Client IP address")
    elif args.eps:
        calculate_events_per_second(logs)
    elif args.bytes:
        calculate_bytes_exchanged(logs)
    else:
        pass


if __name__ == "__main__":
    main()


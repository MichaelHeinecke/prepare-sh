"""Create a function merge_csv_files that accepts a directory path and an
 output filename. The function should scan the specified directory for all
 CSV files, read their contents, and combine the data into a single list of
 dictionaries. After merging, the function should write the consolidated
 data to the output CSV file. If the directory does not exist or contains
 no CSV files, the function should return an empty list."""
import csv
from pathlib import Path


def merge_csv_files(directory_path: str, output_filename: str) -> list[dict[str, str]]:
    data = []

    p = Path(directory_path)
    if not p.is_dir():
        return data

    csv_files = [f for f in p.iterdir() if f.is_file() and f.suffix == '.csv']
    if not csv_files:
        return data

    fieldnames = None
    for file in csv_files:
        try:
            with open(file, mode='r', newline='', encoding='utf-8') as f:
                csv_reader = csv.DictReader(f)
                if fieldnames is None:
                    fieldnames = csv_reader.fieldnames
                if csv_reader.fieldnames != fieldnames:
                    continue
                data.extend(list(csv_reader))
        except:
            continue

    if data and fieldnames:
        with open(output_filename, mode='w', newline='', encoding='utf-8') as f:
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data)

    return data


if __name__ == '__main__':
    input_dir = './input'
    output_file = './output/merged.csv'

    print(merge_csv_files(input_dir, output_file))

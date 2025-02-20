import csv
import os
import re
import tkinter as tk
from tkinter import filedialog

timestamp_regex = re.compile(
    r"^\d{4}-\d{2}-\d{2}"
    r"(?:[ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?){0,1}$"
)

def is_timestamp(value: str) -> bool:
    """Check if the given value matches a timestamp format."""
    return bool(timestamp_regex.match(value.strip()))

def csv_to_sql(csv_file_path, delimiter=';'):
    base_name = os.path.basename(csv_file_path)
    table_name, _ = os.path.splitext(base_name)
    output_file_path = os.path.join(os.path.dirname(csv_file_path), f"{table_name}.sql")

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        rows = list(reader)

    if not rows:
        print(f"File {csv_file_path} is empty. Skipping.")
        return

    columns = rows[0]
    if columns and columns[0].startswith('\ufeff'):
        columns[0] = columns[0].lstrip('\ufeff')

    insert_statements = []

    for row in rows[1:]:
        if len(row) != len(columns):
            print(f"Warning: row length {len(row)} does not match columns length {len(columns)} in file {csv_file_path}. Skipping row: {row}")
            continue

        values = []
        for value in row:
            value = value.strip()
            if value == "":
                values.append("NULL")
            elif is_timestamp(value):
                values.append(f"TIMESTAMP '{value}'")
            else:
                escaped_value = value.replace("'", "''")
                values.append(f"'{escaped_value}'")
        statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)});"
        insert_statements.append(statement)

    with open(output_file_path, "w", encoding='utf-8') as sqlfile:
        sqlfile.write("\n".join(insert_statements))
    
    print(f"Generated {output_file_path}")

def main():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Select CSV Files",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file_paths:
        print("No files selected. Exiting.")
        return

    for file_path in file_paths:
        csv_to_sql(file_path)

    print("All files have been processed.")

if __name__ == "__main__":
    main()

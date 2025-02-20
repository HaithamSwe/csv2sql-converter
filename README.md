# CSV2SQL Converter

CSV2SQL Converter is a Python tool that converts CSV files into SQL `INSERT` statements. It supports CSV files that use semicolons as delimiters, and it automatically detects timestamp fields (including those with fractional seconds) to output them as SQL TIMESTAMP literals.

## Features

- **Multiple File Processing:** Select and process one or more CSV files at once.
- **Timestamp Detection:** Automatically converts fields matching timestamp formats (e.g., `2024-11-25 13:43:26.768`) to SQL TIMESTAMP literals.
- **Custom Delimiter Support:** Designed to work with CSV files using semicolons (`;`).
- **Easy-to-Use:** Generates an SQL file with the same base name as the CSV in the same directory.

## Installation

To install and run CSV2SQL Converter, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/csv2sql-converter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd csv2sql-converter
   ```

This tool does not require additional dependencies beyond Python's standard library.

## Usage

Run the script using Python:

```bash
python csv2sql.py
```

Select one or more CSV files, and the script will generate corresponding SQL files containing `INSERT` statements for the data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any issues or suggestions, please open an issue on the GitHub repository.


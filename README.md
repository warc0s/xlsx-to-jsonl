# XLSX to JSONL for ChatGPT Fine-Tuning

A Python script that converts Excel (.xlsx) files into JSONL format, facilitating the creation of structured training and validation datasets for fine-tuning ChatGPT.

## 📄 Description

This repository provides a Python script designed to transform Excel files into JSONL format specifically for ChatGPT fine-tuning. The script processes an `.xlsx` file containing one or more sheets, each with at least two columns:
- **Column A**: Prompts (User Inputs)
- **Column B**: Responses (Assistant Outputs)

Each row represents a conversation pair (prompt-response). Additionally, the script prompts the user to input a system role, specify the percentage of data to be used for training, and decide whether to shuffle the data. The data from each sheet is split into training and validation datasets based on the provided percentage.

## 🚀 Features

- **Easy Conversion**: Transforms Excel sheets into JSONL files compatible with ChatGPT fine-tuning.
- **Multiple Sheets Processing**: Handles any number of sheets within an Excel file, allowing for flexible dataset organization.
- **Structured Data Handling**: Ensures each conversation pair is formatted with system, user, and assistant roles.
- **Custom Training Split**: Allows users to specify the percentage of data allocated to training versus validation.
- **Data Shuffling**: Option to shuffle data before splitting to ensure randomness.
- **Flexible Dataset Generation**: Generates distinct JSONL files for **Training** and **Validation** datasets for each sheet.
- **User Interaction**: Interactive prompts guide file selection, system role input, training split percentage, and shuffling preference.

## 🛠️ Requirements

- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

## 📦 Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/warc0s/xlsx-to-jsonl
    cd xlsx-to-jsonl
    ```

2. **Install Dependencies**
    ```bash
    pip install pandas openpyxl
    ```

## 📋 Usage

1. **Prepare Your Excel File**
    - Ensure your `.xlsx` file contains one or more sheets.
    - Each sheet should contain at least two columns:
        - **Column A**: Prompts
        - **Column B**: Responses

2. **Run the Script**
    ```bash
    python XLSX-to-jsonl.py
    ```
    - **File Selection**: If multiple `.xlsx` files are present in the directory, you will be prompted to select the desired file.
    - **System Role**: Input the system role to be included in every JSONL entry.
    - **Training Percentage**: Specify the percentage of data to allocate to the training dataset (0-100).
    - **Data Shuffling**: Choose whether to shuffle the data before splitting.

3. **Output**
    - For each sheet in the selected Excel file, the script will generate two JSONL files:
        - `<excel_filename>_<sheet_name>_train.jsonl`
        - `<excel_filename>_<sheet_name>_validation.jsonl`

## 🔧 Customization

- **System Role**: Specify the system role during script execution to tailor the JSONL entries.
- **Training Split**: Define the percentage of data to be used for training, with the remainder allocated to validation.
- **Data Shuffling**: Opt to shuffle the data before splitting to ensure a randomized distribution.
- **File Naming**: Output files are named based on the original Excel file, sheet names, and dataset type (train/validation).

## 📝 Notes

- The script requires that each sheet contains at least two columns. Sheets with fewer columns are skipped.
- Ensure that your Excel file does not contain empty rows or cells in the **Prompts** and **Responses** columns to prevent malformed JSONL entries.
- The training percentage should be a number between 0 and 100. Invalid inputs will prompt for re-entry.
- When multiple `.xlsx` files are present in the directory, ensure to input the exact filename when prompted.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

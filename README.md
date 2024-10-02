# XLSX to JSONL for ChatGPT Fine-Tuning

A Python script that converts Excel (.xlsx) files into JSONL format, facilitating the creation of structured training and validation datasets for fine-tuning ChatGPT.

## 📄 Description

This repository provides a Python script designed to transform Excel files into JSONL format specifically for ChatGPT fine-tuning. The script processes an `.xlsx` file containing two sheets—**Training** and **Validation**—each with two columns:
- **Column A**: Prompts (User Inputs)
- **Column B**: Responses (Assistant Outputs)

Each row represents a conversation pair (prompt-response). Additionally, the script prompts the user to input a system role, which is included in every JSONL entry.

## 🚀 Features

- **Easy Conversion**: Transforms Excel sheets into JSONL files compatible with ChatGPT fine-tuning.
- **Structured Data Handling**: Ensures each conversation pair is formatted with system, user, and assistant roles.
- **Separate Datasets**: Generates distinct JSONL files for **Training** and **Validation** datasets.
- **User Interaction**: Interactive prompts guide file selection and system role input.

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
    - Ensure your `.xlsx` file has two sheets named **Training** and **Validation**.
    - Each sheet should contain two columns:
        - **Column A**: Prompts
        - **Column B**: Responses

2. **Run the Script**
    ```bash
    python XLSX-to-jsonl.py
    ```
    - Follow the on-screen prompts to input the system role.

3. **Output**
    - The script will generate two JSONL files:
        - `<excel_filename>_Training.jsonl`
        - `<excel_filename>_Validation.jsonl`

## 🔧 Customization

- **System Role**: Specify the system role during script execution to tailor the JSONL entries.
- **File Naming**: Output files are named based on the original Excel file and sheet names.

## 📝 Notes

- The script requires that each sheet contains at least two columns. Sheets with fewer columns are skipped.
- Ensure that your Excel file does not contain empty rows or cells in the **Training** and **Validation** sheets to prevent malformed JSONL entries.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

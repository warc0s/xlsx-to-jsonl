import pandas as pd
import json
import os
import random

def get_xlsx_filename():
    # Get list of .xlsx files in the current directory
    xlsx_files = [f for f in os.listdir() if f.endswith('.xlsx')]
    
    if len(xlsx_files) == 0:
        raise FileNotFoundError("No .xlsx files found in the current directory.")
    elif len(xlsx_files) == 1:
        return xlsx_files[0]
    else:
        print("Multiple .xlsx files found in the directory:")
        for file in xlsx_files:
            print(f"- {file}")
        while True:
            selected_file = input("Please enter the exact name of the .xlsx file you want to use: ")
            if selected_file in xlsx_files:
                return selected_file
            else:
                print("Incorrect file name. Please try again.")

def convert_xlsx_to_jsonl(xlsx_file):
    # Read the Excel file
    excel_data = pd.ExcelFile(xlsx_file)
    
    # Ask user for the system role
    system_role = input("Please enter the system role: ")

    # Ask user for the training data percentage
    train_percentage = float(input("Enter the percentage of data for training (0-100): ")) / 100
    
    # Iterate over each sheet in the Excel file
    for sheet_name in excel_data.sheet_names:
        # Read the current sheet
        df = pd.read_excel(xlsx_file, sheet_name=sheet_name)
        
        # Check if the DataFrame has at least two columns
        if df.shape[1] < 2:
            print(f"Sheet '{sheet_name}' does not have at least two columns. Skipping this sheet.")
            continue
        
        # Shuffle the DataFrame if desired
        shuffle_data = input("Do you want to shuffle the data before processing? (yes/no): ").strip().lower()
        if shuffle_data == 'yes':
            df = df.sample(frac=1).reset_index(drop=True)

        # Split the data into training and validation
        split_index = int(len(df) * train_percentage)
        train_data = df.iloc[:split_index]
        validation_data = df.iloc[split_index:]
        
        # Convert DataFrames to JSONL
        for dataset, dataset_name in zip([train_data, validation_data], ["train", "validation"]):
            jsonl_data = []
            for index, row in dataset.iterrows():
                prompt = row.iloc[0]
                response = row.iloc[1]
                
                # Create JSON structure for each row
                message = {
                    "messages": [
                        {"role": "system", "content": system_role},
                        {"role": "user", "content": str(prompt)},
                        {"role": "assistant", "content": str(response)}
                    ]
                }
                jsonl_data.append(json.dumps(message, ensure_ascii=False))
            
            # Generate JSONL filename
            jsonl_filename = f"{os.path.splitext(xlsx_file)[0]}_{sheet_name}_{dataset_name}.jsonl"
            
            # Write JSONL to file
            with open(jsonl_filename, 'w', encoding='utf-8') as f:
                for item in jsonl_data:
                    f.write(item + "\n")
            
            print(f"JSONL file '{jsonl_filename}' generated successfully.")

# Run the script
xlsx_file = get_xlsx_filename()
convert_xlsx_to_jsonl(xlsx_file)

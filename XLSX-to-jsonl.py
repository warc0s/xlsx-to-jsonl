import pandas as pd
import json
import os

def get_xlsx_filename():
    # Obtener lista de archivos .xlsx en el directorio actual
    xlsx_files = [f for f in os.listdir() if f.endswith('.xlsx')]
    
    if len(xlsx_files) == 0:
        raise FileNotFoundError("No se encontró ningún archivo .xlsx en el directorio actual.")
    elif len(xlsx_files) == 1:
        return xlsx_files[0]
    else:
        print("Se encontraron varios archivos .xlsx en el directorio:")
        for file in xlsx_files:
            print(f"- {file}")
        while True:
            selected_file = input("Por favor, ingresa el nombre exacto del archivo .xlsx que deseas usar: ")
            if selected_file in xlsx_files:
                return selected_file
            else:
                print("Nombre de archivo incorrecto. Por favor, intenta de nuevo.")

def convert_xlsx_to_jsonl(xlsx_file):
    # Leer el archivo Excel
    excel_data = pd.ExcelFile(xlsx_file)
    
    # Preguntar al usuario por el rol del sistema
    system_role = input("Por favor, ingresa el rol del sistema: ")

    # Iterar sobre cada hoja en el archivo Excel
    for sheet_name in excel_data.sheet_names:
        # Leer la hoja actual
        df = pd.read_excel(xlsx_file, sheet_name=sheet_name)
        
        # Verificar que el DataFrame tiene al menos dos columnas
        if df.shape[1] < 2:
            print(f"La hoja '{sheet_name}' no tiene al menos dos columnas. Se omite esta hoja.")
            continue
        
        # Convertir el DataFrame a JSONL
        jsonl_data = []
        for index, row in df.iterrows():
            prompt = row.iloc[0]
            response = row.iloc[1]
            
            # Crear la estructura JSON para cada fila
            message = {
                "messages": [
                    {"role": "system", "content": system_role},
                    {"role": "user", "content": str(prompt)},
                    {"role": "assistant", "content": str(response)}
                ]
            }
            jsonl_data.append(json.dumps(message, ensure_ascii=False))
        
        # Generar el nombre del archivo JSONL
        jsonl_filename = f"{os.path.splitext(xlsx_file)[0]}_{sheet_name}.jsonl"
        
        # Escribir el JSONL al archivo
        with open(jsonl_filename, 'w', encoding='utf-8') as f:
            for item in jsonl_data:
                f.write(item + "\n")
        
        print(f"Archivo JSONL '{jsonl_filename}' generado exitosamente.")

# Uso del script
xlsx_file = get_xlsx_filename()
convert_xlsx_to_jsonl(xlsx_file)
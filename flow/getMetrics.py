import json
import glob
import os

FIELD_PATHS = {
    "macro_place__pause_step": ["macro_place__pause_step"],
    "macro_place__wirelength": ["macro_place__wirelength"],
    "macro_place__annealer_final_cost": ["macro_place__annealer_final_cost"],
    "globalplace__timing__setup__tns": ["globalplace__timing__setup__tns"],
    "globalplace__timing__setup__ws": ["globalplace__timing__setup__ws"],
    "detailedroute__route__wirelength": ["detailedroute__route__wirelength"],
    "detailedroute__route__number_of_iterations": ["detailedroute__route__number_of_iterations"],
    "detailedroute__route__drc_errors__iter:0": ["detailedroute__route__drc_errors__iter:0"],
    "finish__timing__setup__tns": ["finish__timing__setup__tns"],
    "finish__timing__setup__ws": ["finish__timing__setup__ws"]
}

FILE_PATTERN = "*.json"

def process_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        # 2. Iterate through the desired fields and extract values
        for label, path in FIELD_PATHS.items():
            current_level = data
            value = ""
            
            # Traverse the nested dictionary keys defined in the 'path' list
            try:
                for key in path:
                    current_level = current_level[key]
                value = current_level
            except (KeyError, TypeError):
                # If a key is missing or the data structure is wrong, 'value' remains "N/A"
                pass
            
            if value != "":
                print(f"{label} = {value}, ", end="")

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file: {file_path}")

# --- Main Script Execution ---

json_files = glob.glob(FILE_PATTERN)

if not json_files:
    print(f"No files found matching the pattern: {FILE_PATTERN}")
else:
    for json_file in json_files:
        process_json_file(json_file)
    print()

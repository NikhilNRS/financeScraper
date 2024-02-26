import os
import json
import pandas as pd  # Ensure pandas is imported

def create_directories_and_scripts(json_file_path, base_dir):
    """
    Creates directories and Python scripts based on keys in a JSON file. Each script will include variables
    for file paths, a list of all file path variables, blocks to load these files into pandas DataFrames, 
    and statements to print the first 5 rows of each DataFrame.

    Parameters:
    - json_file_path: Path to the JSON file containing the keys.
    - base_dir: The base directory where directories and scripts will be created.
    """
    # Load the JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for key, files in data.items():
        # Extract the last part of the key for directory name
        directory_name = key.split("/")[-1]
        directory_path = os.path.join(base_dir, directory_name)

        # Create the directory if it doesn't exist
        os.makedirs(directory_path, exist_ok=True)

        # Path for the new Python script, named after the directory with '_script' suffix
        script_path = os.path.join(directory_path, f"{directory_name}_script.py")

        # Create and populate the Python script
        with open(script_path, 'w') as script_file:
            script_file.write("import pandas as pd\n\n# Generated Python script\n")
            variables_list = []  # To hold all file path variables
            for idx, file_path in enumerate(files, start=1):
                variable_name = f"file_path_{idx}"
                variables_list.append(variable_name)  # Add the variable name to the list
                # Write each file path as a variable
                script_file.write(f"{variable_name} = '{file_path}'\n")
            
            # After all file paths, write the 'all_files' list with variable references
            script_file.write("\n# List containing all file path variables\n")
            all_files_list = ", ".join(variables_list)  # Combine all variable names into a string
            script_file.write(f"all_files = [{all_files_list}]\n")

            # Load each file into a DataFrame and print the first 5 rows of the DataFrame
            script_file.write("\n# Loading files into DataFrames and printing the first 5 rows\n")
            for idx, variable in enumerate(variables_list, start=1):
                script_file.write(f"df{idx} = pd.read_csv({variable})\n")
                script_file.write(f"print(f'\\nDataFrame {idx} - First 5 Rows:')\n")
                script_file.write(f"print(df{idx}.head())\n\n")

    print("Directories and Python scripts have been created successfully.")

def main():
    json_file_path = '/Users/nikhilrazab-sekh/Desktop/data_extraction/preprocessing_db/data_sources/grouped_csv_files.json'  # Ensure this path is correct
    base_dir = os.getcwd()  # This sets the base directory to the current working directory
    create_directories_and_scripts(json_file_path, base_dir)

if __name__ == "__main__":
    main()

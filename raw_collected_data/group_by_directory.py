import sys
import json
from collections import defaultdict
from pathlib import Path

# Group files by their parent directory
files_by_directory = defaultdict(list)

# Read file paths from stdin
for line in sys.stdin:
    file_path = Path(line.strip())
    files_by_directory[str(file_path.parent)].append(str(file_path))

# Convert the defaultdict to a regular dict for JSON serialization
files_by_directory = dict(files_by_directory)

# Define the path to the directory where the JSON file should be saved
json_output_dir = Path("../preprocessing_db/data_sources")

# Ensure the directory exists
json_output_dir.mkdir(parents=True, exist_ok=True)

# Specify the JSON output file path
json_output_file = json_output_dir / 'grouped_csv_files.json'

# Save the JSON data to a file
with open(json_output_file, 'w') as f:
    json.dump(files_by_directory, f, indent=4)

print(f"JSON data has been saved to {json_output_file}")


# Run like this
# ./find_csv.sh | python3 group_by_directory.py

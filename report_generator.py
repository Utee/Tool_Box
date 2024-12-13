import json

def save_results_to_file(data, filename='scan_results.json'):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Results successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving results: {e}")

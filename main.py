import sys
import json

def get_j_file_data(file_path):

    try:
        with open(file_path, "rt") as j_file:
            return json.load(j_file) 

    except FileNotFoundError:
        try:
            with open(file_path, "wt") as j_file:
                new_file_data = {
                    "deleted": [0], # id's for reuse
                    "added": [
                        {
                            "id": None,
                            "description": None,
                            "status": None
                        }
                    ]
                }
                json.dump(new_file_data, j_file, indent=4)
            
        except Exception as err:
            print(f"coudn't open (to write) file, error is {err}")
            sys.exit(1)

    return new_file_data

############
def main():

    str = get_j_file_data("tasks.json")
    print(str)
    return 0

main()
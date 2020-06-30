import csv
import json
import os

def json_to_tsv(j,t):
    
    with open(j, "r") as read_json:
        json_file = json.load(read_json)

    if json_file and os.path.exists(j): 
        with open(t, 'w') as res: 
            to_tsv = csv.DictWriter(res, fieldnames=json_file[0], delimiter='\t')
            to_tsv.writeheader()
            to_tsv.writerows(json_file)
        return 1
    else:
        return 0



json_to_tsv("bc_test.json", "first.tsv")

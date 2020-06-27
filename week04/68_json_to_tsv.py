import csv
import json

def json_to_tsv(j,t):
    lst = [] * 30
    
    with open(j, "r") as read_json:
        json_file = json.load(read_json)

    key_of_dict = json_file[0].keys()
    key_iter = iter(key_of_dict)

    first_key = next(key_iter)
    second_key = next(key_iter)


    # print(len(json_file))
    
    # loop 3 times 
   
    with open(t, 'w') as tsv_file: 
        tsv_writer = csv.writer(tsv_file, delimiter='\t')
        tsv_writer.writerow(['hi', 'word', 'hi'])
        tsv_writer.writerow(['hi', 'word', 'hi'])
        # for i in range(len(key_of_dict)):
        # tsv_writer.writerow([next(key_iter),next(key_iter)])
    print(first_key)
    print(second_key)



json_to_tsv("week04/bc_test.json", "first.tsv")

# Rebecca M Joseph, Mohammad Movahedi, William G Dixon, Deborah P M Symmons, 2024.

import sys, csv, re

codes = [{"code":"C10F500","system":"readv2"},{"code":"C107.11","system":"readv2"},{"code":"C107.12","system":"readv2"},{"code":"C109511","system":"readv2"},{"code":"C107200","system":"readv2"},{"code":"C109512","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('type-2-diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["type-2-diabetes-gangrene---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["type-2-diabetes-gangrene---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["type-2-diabetes-gangrene---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

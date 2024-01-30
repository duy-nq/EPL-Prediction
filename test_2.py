import csv
import support as sp
new_labels = ['h_poise', 'a_poise']
csv_file_path = 'Results/results_1516_2223.csv'
output_csv_file_path = 'final_results/02.csv'
with open(csv_file_path, 'r') as csv_file, open(output_csv_file_path, 'w', newline='') as output_csv_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(output_csv_file)
    header = next(csv_reader, None)
    if header:
        csv_writer.writerow(header + new_labels)
    count = 0
    for row in csv_reader:
        h_p = sp.last_5_matches_at(row[2],True, row[1])
        a_p = sp.last_5_matches_at(row[3],False,row[1])
        p_list = [h_p,a_p]
        new_row = row + p_list
        csv_writer.writerow(new_row)
        count+=1
        print(count)
print(f'Data written to: {output_csv_file_path}')
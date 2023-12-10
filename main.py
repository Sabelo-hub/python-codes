import csv

with open('customers.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_customer_names.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name', 'email', 'phone', 'address', 'gender', 'age', 'registered', 'orders', 'spent', 'job', 'hobbies', 'is_married']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
            # print(line)

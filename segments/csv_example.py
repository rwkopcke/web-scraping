import csv

def read_csv_file():
    '''
        pass information to main.py as a list of lists
    '''

    with open('io_main/employee_birthday.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter= ',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}')
            line_count += 1
            
    print(f'Processed {line_count} lines.')
    print()
    
    with open('io_main/employee_birthday.txt') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter= ',')
        line_count = 0
        csv_file = []
        for row in csv_reader:
            if line_count == 0:
                # produces headers
                # convert first dict (aka row) to list of headers
                csv_file.append(list(row.keys()))
                print(f'Column names are {", ".join(row)}')
            print(f'\t{row['name']} works in the {row['department']} department, and was born in {row['birthday month']}')
            line_count += 1
            # convert each dict (aka row) after 1st to list of its values
            csv_file.append(list(row.values()))
    print(f'Processed {line_count} lines.')
    return csv_file
    
    
def write_csv_file(csv_file):
    '''
        csv_file is a list of lists, with headers in row[0]
    '''
    with open('io_main/employee_file.csv', mode= 'w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter= ',',
                                     quotechar= '"',
                                     quoting= csv.QUOTE_MINIMAL)
        for row in csv_file:
            employee_writer.writerow(row)
        employee_writer.writerow(
            ['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(
            ['Erica Meyers', 'IT', 'March'])
        

def read_csv_file_2():
    '''
        pass information to main.py as a list of dicts
        with keys/headers in header_list
    '''
    with open('io_main/employee_birthday.txt') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter= ',')
        line_count = 0
        csv_file = []
        for row in csv_reader:
            if line_count == 0:
                # produces headers
                header_list = list(row.keys())
                print(f'Column names are {", ".join(row)}')
            print(f'\t{row['name']} works in the {row['department']} department, and was born in {row['birthday month']}')
            line_count += 1
            csv_file.append(row)
        
    print(f'Processed {line_count} lines.')
    return csv_file, header_list


def write_csv_file_2(csv_file, header_list):
    '''
        csv_file is a list of dicts with keys/headers in header_list
    '''
    with open('io_main/employee_file_dict.csv', mode= 'w') as employee_file:
        employee_writer = csv.DictWriter(employee_file,
                                         fieldnames= header_list)
        
        employee_writer.writeheader()
        for row in csv_file:
            employee_writer.writerow(row)
        employee_writer.writerow(
            {header_list[0]: 'John Smith', 
             header_list[1]: 'Accounting', 
             header_list[2]: 'November'})
        employee_writer.writerow(
            {header_list[0]: 'Erica Meyers', 
             header_list[1]: 'IT', 
             header_list[2]: 'March'})
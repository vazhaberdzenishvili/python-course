import csv

#Task 1
with open('titanic.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  headers = csv_reader.fieldnames
  survivors = []
  for row in csv_reader:
    if row['Survived'] == '1':
      survivors.append(row)

with open('survived.csv', 'w', newline = "") as csv_file:
  csv_dict_writer = csv.DictWriter(csv_file, fieldnames=headers)
  csv_dict_writer.writeheader()
  csv_dict_writer.writerows(survivors)

#Task 2
with open('organizations-100.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  headers = csv_reader.fieldnames
  organizations = list(csv_reader)
  sorted_organizations = sorted(organizations, key=lambda x: int(x['Number of employees']))

with open('sorted_csv.csv', 'w', newline='') as csv_sorted:
  csv_writer = csv.writer(csv_sorted) 
  csv_writer.writerow(headers)

  for index in range(len(sorted_organizations)):
    organizations = sorted_organizations[index]
    row = [index] + [organizations[header] for header in headers[1:]]
    csv_writer.writerow(row)
    
#Task 3
with open('organizations-100.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  organizations = list(csv_reader)
  companies = []

  for company in organizations:
    if company['Website'].startswith('https://'):
      companies.append({
        'Organization Id': company['Organization Id'],
        'Name': company['Name'],
        'Website': company['Website'],
        'Industry': company['Industry'],
        'Number of employees': company['Number of employees']
      })

with open('ssl_companies.csv', 'w', newline='') as https_file:
  header = ['Organization Id', 'Name', 'Website', 'Industry', 'Number of employees']
  csv_writer = csv.DictWriter(https_file, fieldnames = header)
  csv_writer.writeheader()

  for company in companies:
    csv_writer.writerow(company)
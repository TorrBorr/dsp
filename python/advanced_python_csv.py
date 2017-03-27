import csv

def write_emails(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        emails = []
        for row in reader:
            emial_address = row[" email"]
            emails.append(emial_address)
        
    writer = csv.writer((open("emails.csv","w")),delimiter="\n")
    writer.writerow(emails)

write_emails('faculty.csv')

#Question 1

import string
import csv
import re 
from collections import Counter

def degree_types(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        degree_types = []
        for row in reader:
            degree = re.sub(r'[^\w\s]','',(row[' degree']))
            degree = re.sub(r'^[ \t]+','',degree)
            if degree == '0':
                degree_types.append('N/A')
            elif " " in degree:
                multiple_degrees = degree.split()
                for new_degree in multiple_degrees:
                    degree_types.append(new_degree)
            else:
                degree_types.append(degree)               
    freqs = Counter(degree_types)
    number_of_degree_types = len(freqs)
    print 'Number of degree types: %d' % (number_of_degree_types) 
    print "frequncy of degrees: " 
    return freqs
    
    
degree_types('faculty.csv')

#Question 2

def titles(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        titles = []
        for row in reader:
            full_title = row[" title"]
            title = re.split('Professor\\s',full_title)
            title = title[0]+ "Professor"
            titles.append(title)
    freqs = Counter(titles)
    number_of_title_types = len(freqs)
    print 'Number of title types: %d' % (number_of_title_types) 
    print "frequncy of titles: " 
    return freqs
    
titles('faculty.csv')

#Question 3

def emails(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        emails = []
        for row in reader:
            emial_address = row[" email"]
            emails.append(emial_address)
        
        return emails

emails('faculty.csv')

#Question 4

def domain(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        domains = []
        for row in reader:
            emial_address = row[" email"]
            domain = emial_address.rsplit('@',1)[1]
            domains.append(domain)
    
    freqs = Counter(domains)
    
    number_of_domains = len(freqs)
    domain_list=freqs.keys()
            
    print 'Number of domains: %d' % (number_of_domains) 
    return domain_list


domain('faculty.csv')



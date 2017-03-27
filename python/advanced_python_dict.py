#Question 6

import itertools
import collections
import string
import csv
import re 
from collections import Counter

def make_dictionary(file):
    faculty_dict=dict()
    last_names = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last_name = row['name'].split()[-1]
            emial_address = row[" email"]        
            full_title = row[" title"]
            title = re.split('Professor\\s',full_title)
            title = title[0]+ "Professor"
            degree = re.sub(r'[^\w\s]','',(row[' degree']))
            degree = re.sub(r'^[ \t]+','',degree)
            subs = {'BSEd':'B.S.Ed.',"JD":"J.D.","MA":"M.A.","MD":"M.D.","MPH":"M.P.H.","MS":"M.S.","PhD":"Ph.D.","ScD":"Sc.D."}
            for i in subs.keys():
                degree = degree.replace(i, subs[i])
            if degree == 0:
                degree = 'N/A'
            else:
                pass
            faculty_info = [degree,title,emial_address]
            if last_name in faculty_dict:
                faculty_dict[last_name].append(faculty_info)
            else:
                faculty_dict[last_name] =[faculty_info]
                
    n = 3
    return{key:value for key,value in faculty_dict.items()[0:n]}
     
make_dictionary('faculty.csv')

#Question 7

def make_dictionary_updated(file):
    faculty_dict=dict()
    last_names = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last_name = row['name'].split()[-1]
            first_name = row['name'].split()[0]
            full_name = (last_name,first_name)
            emial_address = row[" email"]        
            full_title = row[" title"]
            title = re.split('Professor\\s',full_title)
            title = title[0]+ "Professor"
            degree = re.sub(r'[^\w\s]','',(row[' degree']))
            degree = re.sub(r'^[ \t]+','',degree)
            subs = {'BSEd':'B.S.Ed.',"JD":"J.D.","MA":"M.A.","MD":"M.D.","MPH":"M.P.H.","MS":"M.S.","PhD":"Ph.D.","ScD":"Sc.D."}
            for i in subs.keys():
                degree = degree.replace(i, subs[i])
            if degree == 0:
                degree = 'N/A'
            else:
                pass
            faculty_dict[full_name]=[degree,title,emial_address]

        n = 3
        return{key:value for key,value in faculty_dict.items()[0:n]}
        
make_dictionary_updated('faculty.csv')


#Question 8

def make_dictionary_sorted(file):
    faculty_dict=dict()
    last_names = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last_name = row['name'].split()[-1]
            first_name = row['name'].split()[0]
            full_name = (last_name,first_name)
            emial_address = row[" email"]        
            full_title = row[" title"]
            title = re.split('Professor\\s',full_title)
            title = title[0]+ "Professor"
            degree = re.sub(r'[^\w\s]','',(row[' degree']))
            degree = re.sub(r'^[ \t]+','',degree)
            subs = {'BSEd':'B.S.Ed.',"JD":"J.D.","MA":"M.A.","MD":"M.D.","MPH":"M.P.H.","MS":"M.S.","PhD":"Ph.D.","ScD":"Sc.D."}
            for i in subs.keys():
                degree = degree.replace(i, subs[i])
            if degree == 0:
                degree = 'N/A'
            else:
                pass
            faculty_dict[full_name]=[degree,title,emial_address]
            
        for key in sorted(faculty_dict.iterkeys()):
            print "%s: %s" % (key, faculty_dict[key])

make_dictionary_sorted('faculty.csv')

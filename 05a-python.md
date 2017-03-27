# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are sequences of values/items separated by commas. List values are not immutable and can be added, removed, replaced, sorted, etc. 
Tuples are sequences of comma-separated list of values.   Unlike lists, the elements of tuples are immutable; however, one tuple can be replaced with another tuple. 
A dictionary key must be immutable, so tuples are used as dictionary keys and lists are not.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are sequences of values/items separated by commas and can have duplicate entries. Sets are lists but with no duplicate entries.

>> It is faster to use sets while finding an element because the entire list must be searched element by element but a set has an index to allow quick searching (hash tables). Due to this, sets do not preserve the order of the added objects. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python’s lambda is an anonymous function that is defined without a name. Unlike definitions, Lambda functions are destroyed immediately after they are used. 
lambda syntax = lambda   list of variables : single block of code that defines what transformation lambda should make to the items

>> In the context of sorted, lambda can be used to tell sorted() which list elements it should sort by (called the key).  Of note, the entire list is transformed as defined by the key, then that transformed list is sorted. 

>> Ex) 
stuff_to_sort =  [(1,2,3),(4,5,6),(2,3,4),(5,6,7)] 
sorted(stuff_to_sort, key=lambda stuff_to_sort: stuff_to_sort[1])

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension allows concise list construction by describing the list in one line of code that often replace a structure of conditionals.  

>> Examples: 

>> 1. list = [x**3 for x in range(5)]

>> 2. phrase = 'List comprehension is awesome'
       words = phrase.split()
       list = [word[0] for word in words]


>> list comprehension vs. map and filter:

>> Ex 1) 
>> comprehension_list = [x**2 for x in range(1,6)]

>> numbers = [1,2,3,4,5]
>> mapping_list = map(lambda number: number**2,  numbers)

>> numbers = range(1,30)
>> filter_list = filter(lambda number: (number**(1./2.))% 1 == 0, numbers)

>> Ex 2)
>> sentence = “List comprehension is the most amazingly awesome thing ever”
>> list = sentence.split()

>> comprehension_list = [word for word in list1 if word[0] == 'a']

>> filter_list = filter(lambda word: (word[0]=='a') == True, list1)


>> List comprehensions can’t be used when the conditionals are too complicated to be expressed with "for" and "if" statements, or if the construction rule can change dynamically at runtime. In this case map() and / or filter() should be used. When both can be used, list comprehension is often preferable because it is often more efficient and easier to read.

>> Set comprehension allows concise set construction by describing the list in one line of code that often replace a structure of conditionals (like generating a list of prime numbers):
set_list = {x for x in range(2,200) if not any (x%y == 0 for y in range(2,x))}


>> A dictionary can be similarly defined:
dictionary_test = {i : i**2 for i in range(7)}

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)






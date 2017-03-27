[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Problem Statement: Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

To investigate this question I divided the weight data into two groups based on the birth order variable: firsts and others:

```python
firsts = live[live.birthord == 1]  
others = live[live.birthord != 1]
```
I then checked each group to make sure they were comparable in size and distribution:

```pythonprint("Number of first babies: %r" %len(firsts))
print("Number of other babies: %r" %len(others))

first_hist = thinkstats2.Hist(firsts.totalwgt_lb)  
other_hist = thinkstats2.Hist(others.totalwgt_lb)  

mean_firsts = firsts.totalwgt_lb.mean()  
var_firsts = firsts.totalwgt_lb.var()  
std_firsts = firsts.totalwgt_lb.std()  

mean_others = others.totalwgt_lb.mean()  
var_others = others.totalwgt_lb.var()  
std_others = others.totalwgt_lb.std()  
```
I found that the sample size and distribution was similar for each group:

```python
Number of first babies: 4413
Number of other babies: 4735

Firsts: 
 mean = 7.201094430437772 
 var = 2.0180273009157768 
 stdev = 1.4205728777207374
Others: 
 mean = 7.325855614973262 
 var = 1.9437810258964572 
 stdev = 1.3941954762143138
 ```
 
 The mean for first babies is indeed smaller than the mean for the other babies by 0.125 lbs. 
 
 I calculated the Cohen Effect size for this difference using:
 ```python
 def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

print "CohenEffectSize is "+ str(CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb))


CohenEffectSize is -0.0886729270726
```

The difference in the means of birth weight between first babies and others is 0.089 standard deviations. Though this is about 3x larger than the difference seen in pregnancy length (and it would make sense that if first babies are born earlier they would weight less on average than other babies), it is still likely not a clinically significant effect (i.e. it is not strong enough to drive a treatment decision). 
 
 

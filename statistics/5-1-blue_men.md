[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> ***Problem Statement: In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use  scipy.stats.norm.cdf.***

As the hint suggests, I used scipy.stats.norm.cdf with scale = men's µ (178 cm) and loc = men's σ (7.7 cm):   

```python
dist = scipy.stats.norm(178,7.7)

low = dist.cdf(177.8)     # 5’10” in cm
high = dist.cdf(185.42)   # 6’1” in cm
difference = dist.cdf(185.42)-dist.cdf(177.8)

print "Men who are 5'10 are in the %.1f percentile."  %(low*100)
print "Men who are 6'1 are in the %.1f percentile."  %(high*100)
print "{0:.1f}% of men are between 5'10 and 6'1.".format(difference * 100)
```

Men who are 5'10 are in the 49.0 percentile.
Men who are 6'1 are in the 83.2 percentile.
34.3% of the U.S. male population are between 5'10 and 6'1.

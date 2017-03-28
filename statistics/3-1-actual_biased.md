[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Problem Statement: ***Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.***  
***Use the NSFG respondent variable numkdhh to construct the actual distribution for the number of children under 18 in the respondents' households.***  

```python
pmf = thinkstats2.Pmf(resp.numkdhh,label='actual')
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Number of Children', ylabel='Pmf')
```
![alt text](https://github.com/TorrBorr/dsp/blob/master/statistics/Image1Q2.png)

***Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.***  
For this I used the BiasPmf function: 
```python
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    
     for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
    
￼biased_pmf = BiasPmf(pmf, label='biased')
thinkplot.Pmf(biased_pmf)
thinkplot.Config(xlabel='Number of Children', ylabel='Pmf')
```
![alt text](https://github.com/TorrBorr/dsp/blob/master/statistics/Image2Q2.png)

***Plot the actual and biased distributions, and compute their means.***  

```python
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,biased_pmf])
thinkplot.Config(xlabel='Number of Children', ylabel='PMF')
```
![alt text](https://github.com/TorrBorr/dsp/blob/master/statistics/Image3Q2.png)

```python
print('Actual mean', pmf.Mean())
print('Biased mean', biased_pmf.Mean())
```
Actual mean 1.02420515504  
Biased mean 2.40367910066  

In the biased data there are no families with zero children (as expected) and mean number of children per family is inreased by nearly 1.4. 

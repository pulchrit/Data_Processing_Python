# Data_Processing_Python
Simple data processing from csv file using Python.

The data from the csv is processed and analyzed to answer the following questions. 

1. How many schools had disbursed a total of greater than or equal
to $707,300 and less than $800,895 in loans for the time period reported
on the spreadsheet provided (“Quarterly Activity” only)?
Answer: 55

2. Consider the sum of expected total loan amount if the loans were fully disbursed 
for each school in this Quarter. For how many schools was this amount greater 
than $20,000,000?
Answer: 73

3. Amongst the schools that are considered part of Bellevue, WA 
(according to zip codes on http://zipcode.org), what was the largest 
number of recipients within a school for either DL Unsubsidized 
Undergraduate or DL Unsubsidized Graduate loans? Ignore unavailable 
data i.e. data with ‘-’ value.
Answer: 219

4. Consider the state in which the last Olympics was hosted in the USA. What is the 
sum of the expected total loan amount if the loan is fully disbursed for 
DL Subsidized loans in the public schools in this state in Q4 of 2016-2017, 
based on the data provided?
Answer: 7,912,715

5. Consider all the private nonprofit schools in WA state where the 
name of the school starts with either “s”, “u”, “v” or “w”. For 
these schools, consider the expected total loan amount if the 
loan is fully disbursed for unsubsidized undergraduate studies. 
Exclude all schools where the unsubsidized undergraduate loan 
amount is not available i.e. “-” or 0. What was the median value?
Answer: 79,524

This is a refactored version of my Ada Program Application Assessment for C10. 
This version uses object oriented programming. Classes are created for 
Schools and Loan Types.

There is a significant time savings in parsing the data from the csv file 
with this method. Equally, setting the program up with a class structure 
should make it easier to work with/expand in the future.  

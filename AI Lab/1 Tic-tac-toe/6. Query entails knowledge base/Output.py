Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: D:/5 SEM/Artificial Intelligence/AI Lab/6. Query entails knowledge base/Query entails knowledge base.py

Enter rule: (~qv~pvr)^(~q^p)^q
Enter the Query: r
Truth Table Reference
kb alpha
**********
False True
----------
False False
----------
False True
----------
False False
----------
False True
----------
False False
----------
False True
----------
False False
----------
The Knowledge Base entails query

Enter rule: (pvq)^(~rvp)
Enter the Query: r
Truth Table Reference
kb alpha
**********
True True
----------
True False
----------
The Knowledge Base does not entail query
>>> 
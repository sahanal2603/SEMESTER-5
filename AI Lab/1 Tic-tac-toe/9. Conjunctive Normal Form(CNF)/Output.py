Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:/Users/SAHANA L/OneDrive/Desktop/cnf3.py =============
Enter FOL: 
(animal(z)) and kills (x,z)) imp (neg Loves(y,z))
Steps: 
((animal(z)) and kills) (x,z)) imp (neg Loves(y,z))
neg ((animal(z)) and kills) (x,z)) or (neg Loves(y,z))
((neg animal(z)) or neg kills) (x,z)) or (neg Loves(y,z))
(neg Loves(y,z)) or (neg animal(z)) or neg kills (x,z))
>>> 
============== RESTART: C:/Users/SAHANA L/OneDrive/Desktop/cnf3.py =============
Enter FOL: 
p imp q
Steps: 
p imp q
neg p or q
neg p or q
neg p or q
>>> 
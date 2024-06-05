import numpy as np 
import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder



#IDS = TRANSACTIONS IDS
#DATASET = BOOKS ISBNs OF EACH TRANSACTION

ids = [1,2,3,4,5,6,7,8,9,10]
dataset = [[1,4],
           [1,2,4],
           [4,5,1],
           [69,1,2],
           [69,2],
           [69,1,4],
           [420,2,1],
           [88,4],
           [1,5,4],
           [420,1,2]]

#ENCODING DATA WITH TRUE/FALSE IF THEY ARE FOUND IN DATASET

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns= te.columns_, index = ids)

print(df,'\n')

ap = apriori(df,min_support= 0.1,use_colnames=True) #run apriori with 10% minimum support
print(ap,'\n')

print("TOP 3 BOOKS WITH MINIMUM SUPPORT 0.5")
ap2 = apriori(df,min_support=0.5,use_colnames=True,max_len=1)
print(ap2.head(3).sort_values('support',ascending = False))  #Top 3 books


rules = association_rules(ap,metric='confidence',min_threshold=0.5)
rules = rules[['antecedents','consequents','confidence','lift']]

print(rules.sort_values(by = 'lift',ascending = False))
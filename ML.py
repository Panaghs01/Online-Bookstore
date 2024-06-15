import numpy as np 
import pandas as pd 
#pip install mlxtend
from mlxtend.frequent_patterns import apriori, association_rules 
from mlxtend.preprocessing import TransactionEncoder
import database_connector as DB

transactions = DB.return_transactions()

#DATASET = BOOKS ISBNs OF EACH TRANSACTION
dataset = transactions

#ENCODING DATA WITH TRUE/FALSE IF THEY ARE FOUND IN DATASET

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns= te.columns_)

# print(df,'\n')

ap = apriori(df,min_support= 0.1,use_colnames=True) #run apriori with 10% minimum support

def top3():

    ap2 = apriori(df,min_support = 0.1,use_colnames=True,max_len=1)
    ap2 = ap2.sort_values('support',ascending = False).head(3)  #Top 3 books
    #print(ap2)
    books = [next(iter(x)) for x in ap2.itemsets]
    return books

#print(top3())

def recommendations(cart):
    cart = set(cart)
    a = []
    recommendation = []
    rules = association_rules(ap,metric='confidence',min_threshold=0.5)
    rules['antecedent_len'] = rules["antecedents"].apply(lambda x: len(x))
    rules = rules[["antecedents","consequents","lift","antecedent_len"]]
    print(rules,'\n')
    if rules[(rules['antecedents'] == cart) & (rules['lift'] > 1)].empty:
        for i in cart:
            rules2 = rules[(rules['antecedents'] == {i}) & (rules['lift'] > 1)]
            rules2 = rules2['consequents']
            recommendation.append(next(iter(rules2.values)))
        for i in recommendation:
            i = next(iter(i))
            a.append(i)
        return set(a)        
    else:
        rules = rules[rules['antecedents'] == cart]
        rules = rules.sort_values(by = ['lift'])
        result = rules['consequents'].head(1)
        return set(next(iter(result)))

    
print(recommendations([1,2]))



















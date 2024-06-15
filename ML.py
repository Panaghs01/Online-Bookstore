import numpy as np 
import pandas as pd 
#pip install mlxtend
import mlxtend
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import database_connector as DB

pd.set_option('display.max_rows', None)

transactions = DB.return_transactions()
#print(transactions)

#DATASET = BOOKS ISBNs OF EACH TRANSACTION
dataset = transactions

#ENCODING DATA WITH TRUE/FALSE IF THEY ARE FOUND IN DATASET

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns= te.columns_)

# print(df,'\n')

ap = apriori(df,min_support= 0.1,use_colnames=True) #run apriori with 10% minimum support

def top3():
    #Applying apriori with max_len 1 so we get 1 antecedent length
    #Returns a list of the top 3 books (str)
    ap2 = apriori(df,min_support = 0.1,use_colnames=True,max_len=1)
    ap2 = ap2.sort_values('support',ascending = False).head(3)  #Top 3 books
    books = [next(iter(x)) for x in ap2.itemsets]   #Un-frozenset-ing
    return books

#print(top3())

def recommendations(cart):

    cart = set(cart)
    a = []
    recommendation = {}
    rules = association_rules(ap,metric='lift')
    rules = rules[["antecedents","consequents","lift","confidence"]]
    rules['consequents_len'] = rules['consequents'].apply(lambda x: len(x))
    if rules[(rules['antecedents'] == cart) & (rules['lift'] > 1)].empty:
        for i in cart:
            rules2 = rules[
                (rules['antecedents'] == {i}) &
                (rules['lift'] > 1) &
                (rules['consequents_len'] == 1)]
            rules2 = rules2.sort_values(by = 'lift' , ascending = False).head(1)
            # print(rules2)
            if not rules2['lift'].empty:
                recommendation[i] = rules2['lift'].item()
            # print(recommendation)
        # rules2 = rules2.sort_values(by = 'lift', ascending = False)
        # rules2 = rules2['consequents']
        recommendation['1'] = 1.0234
        recommendation = sorted(recommendation.items(), key = lambda x: x[1],reverse = True)
        return recommendation[0][0]
    else:
        rules = rules[rules['antecedents'] == cart]
        rules = rules.sort_values(by = ['lift'], ascending = False)
        rules = rules[(rules['consequents_len'] == 1)].head(1)
        result = rules['consequents'].item()
        return next(iter(result))

    
#print(recommendations(['13','07']))



















# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:28:39 2023

@author: abdlb
"""

import pandas as pd
import numpy as np
import json 
import csv
import sklearn.metrics


with open('pochtron.json') as json_data:
    data_dict = json.load(json_data)


students=[]
products=[]
quantity=[]


for emp in data_dict:
  if 'fields' in emp:
    a=emp["fields"]
    if 'student' in a and 'good' in a:
      students.append(a["student"])
      products.append(a["good"])
      quantity.append(a["quantity"])

data_file = open('data_file.csv', 'w')
csv_writer = csv.writer(data_file)
count=0
for emp in students:
    if count == 0:
        # Writing headers of CSV file
        header = ['Student','Product']
        csv_writer.writerow(header)
        count += 1
    # Writing data of CSV file
    csv_writer.writerow([1])


dar=np.array([students,products],)

df = pd.DataFrame((zip(students, products,quantity)), columns = ['Student', 'Product','Quantity'])

dar=np.array([students,products],)

df = pd.DataFrame((zip(students, products,quantity)), columns = ['Student', 'Product','Quantity'])


buys_matrix = df.pivot_table(
    index='Student', 
    columns='Product', 
    values='Quantity',
    aggfunc='sum'
)

buys_matrix = buys_matrix.applymap(lambda x: 1 if x > 0 else 0)
pd.DataFrame(sklearn.metrics.pairwise.cosine_similarity(buys_matrix))

from sklearn import tree, model_selection, metrics

def similarity(customer_matrix):
  user_user_sim_matrix = pd.DataFrame(sklearn.metrics.pairwise.cosine_similarity(customer_matrix))
  user_user_sim_matrix.columns = customer_matrix.index
  user_user_sim_matrix['CustomerID'] = customer_matrix.index
  user_user_sim_matrix = user_user_sim_matrix.set_index('CustomerID')
  similarity_item_matrix= pd.DataFrame(sklearn.metrics.pairwise.cosine_similarity(buys_matrix.T))
  similarity_item_matrix.columns = customer_matrix.T.index
  similarity_item_matrix['Product'] = customer_matrix.T.index
  similarity_item_matrix = similarity_item_matrix.set_index('Product')
  return user_user_sim_matrix,similarity_item_matrix

similarity_user_matrix,similarity_item_matrix=similarity(buys_matrix)

L=similarity_user_matrix.loc[471].sort_values(ascending=False)

def recommandation(user_ID):
  L=similarity_user_matrix.loc[user_ID].sort_values(ascending=False)
  if len(L)>1:
    L_user=L.index[1]
    L1=buys_matrix.loc[user_ID]
    L2=buys_matrix.loc[L_user]
    L_user=set(L1.iloc[L1.to_numpy().nonzero()].index)
    L_similar=set(L2.iloc[L2.to_numpy().nonzero()].index)
    L_products=L_similar-L_user
    if len(L_products)==1:
      return L_products[0]
    else:
      for i in L_similar:
        if (i not in L_user):
          return i

recommandation(471)

#les identifiants sont : 
    #306,309,316,320,334,356,363,370,373,378,393,402,405,411,428,444,459,471
    #490,582




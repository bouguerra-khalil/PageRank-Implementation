import re
import os
from SparceMatrix import * 
from generate_edgelist import * 
from PageRank import *
dir_path="./toyset/"

#Ranking of graph from a file
(edgeList,mapper,inv_mapper)=generate_edgeList_csv("graph.txt")
nbrOfVertex=len(mapper)

sparseM=generate_sparse_matrix(edgeList)
Ranking=pageRank(0.001,1,nbrOfVertex,sparseM)

#Ranking of graph from a directory
(edgeList,mapper,inv_mapper)=generate_edgeList_directory(dir_path)
nbrOfVertex=len(mapper)
sparseM=generate_sparse_matrix(edgeList)
Ranking=pageRank(0.001,0.8,nbrOfVertex,sparseM)


(edgeList,mapper,inv_mapper)=generate_edgeList_csv("data/lesmis.csv")
nbrOfVertex=len(mapper)

sparseM=generate_sparse_matrix(edgeList)
Ranking=pageRank(0.001,0.8,nbrOfVertex,sparseM)


Ranking=[(rank,i)  for i,rank in enumerate(Ranking)]
Ranking.sort(reverse=True  )


for (rank,i) in Ranking:
    print(inv_mapper[i],':',rank)
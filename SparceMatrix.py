
def generate_sparse_matrix(edgeList):
    sparce_matrix=dict()
    sigout=dict([(i,0) for i,j in edgeList])
    for i,j in edgeList:
        sigout[i]=sigout[i]+1
    for j,i in edgeList:
        sparce_matrix[(i,j)]=1/sigout[j]
    return sparce_matrix
    
def Multiply(Matrix,vector):
    ret_vector=[0]*len(vector)
    for coordinates,value in Matrix.items():
        (i,j)=coordinates
        ret_vector[i]+=value*vector[j]
    return ret_vector
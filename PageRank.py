from SparceMatrix import * 

def Norme(vector_1,vector_2):
    return sum([abs(coordinate_1-coordinate_2) for (coordinate_1,coordinate_2) in zip(vector_1,vector_2)])

def Sum_vectors(vector_1,vector_2):
    return [i+j for i,j in zip(vector_1,vector_2)]

def Multiply_const(vector, const):
    return [const* i for i in vector]
    
def pageRank(eps,beta,nbrOfVertex,M):
    vect=[1/nbrOfVertex]*nbrOfVertex
    r_new=vect
    while(1):
        r_old=r_new
        r_new=Sum_vectors(Multiply_const(Multiply(M,r_old),beta),Multiply_const(vect,1-beta))
        if(Norme(r_new,r_old)<eps):
            break 
    return r_new

def print_valid_output(v):
    for i in range(len(v)): 
        print(v[i],end="")
        if(i!=(len(v)-1)):
            print(" ",end=" ")

import numpy as np
def create_matrix(mc):
    print("\n Arrray "+str(mc)+"Elements:")
    array1=map(int,input().split())
    array1=np.array(list(array1))
    print("\nArray "+str(mc)+"row column:") 
    row,column=map(int,input().split())
    if(len(array1)!=(row*column)):
        print("\n Row andd the column size not matchimg with the total elements\\retry")
        return create_matrix(mc)
    array1=array1.reshape(row,column)
    print("\n array "+str(mc))
    print(array1)
    return array1
arr1=create_matrix(1)
arr2=create_matrix(2)
if(arr1.shape==arr2.shape):
    print("\ndot product")
    print(np.dot(arr1,arr2))
else:
    print("\n dimention mot matchinggg")

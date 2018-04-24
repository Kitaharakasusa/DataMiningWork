import numpy as np
# from sklearn.preprocessing import normalize
#
# print(np.ones([5,1])*np.array([2,1]))
# # print(np.ones(5,1)*np.array([2,1]))
# x = np.random.rand(1000)*10
# print(x)
# norm1 = x / np.linalg.norm(x)
# norm2 = normalize(x[:,np.newaxis], axis=0).ravel()
# print(norm1)
# print("\n")
# print(norm2)
# print (np.all(norm1 == norm2))
if __name__=="__main__":
    s="1,1,1,2"
    print(s.split(',')[0:-1])
    # x1=np.array([5.9,3])
    # x2=np.array([6.9,3.1])
    # print(2*x1)
    # a=np.linalg.norm(x1-x2)
    # print(a)
    # print(np.linalg.norm([1,0.1]))
import numpy as np




# activate functions

 
def sigmoid(x):
    return 1/(1+np.exp(-x))


def softmax(x):
    c = np.max(x)     # オーバーフロー対策
    return np.exp(x - c)/np.sum(np.exp(x - c))
    
    
    

    


    
# loss functions


def cross_entropy_error(y, t):
    if y.ndim == 1:  # ndim=1(ベクトル) つまり単一観測値が入力されたら ndim=2(行列) に整形
        y = y.reshape(1, y.shape[0])
        t = t.reshape(1, t.shape[0])
    return - (1/y.shape[0]) * np.sum(t * np.log(y + 1e-7))
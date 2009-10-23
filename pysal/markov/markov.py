import numpy as num
class Markov:
    """Classic Markov transition matrices"""
    def __init__(self,trans,classes=[]):
        """
        Examples:
        ---------

        >>> c=num.array([['b','a','c'],['c','c','a'],['c','b','c'],['a','a','b'],['a','b','c']])
        >>> m=Markov(c)
        >>> m.classes
        array(['a', 'b', 'c'], 
              dtype='|S1')
        >>> m.p
        matrix([[ 0.25      ,  0.5       ,  0.25      ],
                [ 0.33333333,  0.        ,  0.66666667],
                [ 0.33333333,  0.33333333,  0.33333333]])
        """

        if classes:
            self.classes=classes
        else:
            self.classes=num.unique1d(trans)

        n,k=trans.shape
        js=range(k-1)

        classIds=self.classes.tolist()
        transitions=num.zeros((k,k))
        for state_0 in js:
            state_1=state_0+1
            state_0=trans[:,state_0]
            state_1=trans[:,state_1]
            initial=num.unique1d(state_0)
            for i in initial:
                ending=state_1[state_0==i]
                uending=num.unique(ending)
                row=classIds.index(i)
                for j in uending:
                    col=classIds.index(j)
                    transitions[row,col]+=sum(ending==j)
        self.transitions=transitions
        row_sum=transitions.sum(axis=1)
        p=num.dot(num.diag(1/(row_sum+(row_sum==0))),transitions)
        self.p=num.matrix(p)

                
def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()




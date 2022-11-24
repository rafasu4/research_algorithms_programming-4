'''
 This class represents an iterator, that retrieve all the subsets of a given list,
 that sums up to no more then a given threshold.
'''
class bounded_subsets:
    '''
        Constructor
        @params s - a list of positive numbers (including zero)
        @params c - a threshold
    '''
    def __init__(self, s, c):
        for num in s:
            if num < 0: raise Exception('Only positive numbers are allowed!')
        self.s = s
        self.c = c

if __name__ == '__main__':
    bounded_subsets((1, 2, 3, -1), 1)


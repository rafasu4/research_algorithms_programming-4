import copy
import doctest

'''
 This class represents an iterator, that retrieve all the subsets of a given list,
 that sums up to no more then a given threshold.
'''


class bounded_subsets:
    '''
        ----------------------------------------------------------------------TESTS----------------------------------------------------------------------
       simple case
        >>> for subset in bounded_subsets([1, 2, 3, 4], 4): print(subset, end =" ")             
        [] [1] [2] [3] [4] [1, 2] [1, 3] 

       empty case
       >>> for subset in bounded_subsets([1, 2, 3, 4], 0): print(subset, end =" ")
       [] 

       advanced case
       >>> for subset in bounded_subsets(range(10), 5): print(subset, end =" ")
       [] [0] [1] [2] [3] [4] [5] [0, 1] [0, 2] [0, 3] [0, 4] [0, 5] [1, 2] [1, 3] [1, 4] [2, 3] [0, 1, 2] [0, 1, 3] [0, 1, 4] [0, 2, 3] 
    '''
    '''
        Constructor
        @params s - a list of different and positive numbers (including zero)
        @params c - a threshold
    '''

    def __init__(self, s: list, c: int):
        for num in s:
            if num < 0:
                raise Exception('Only positive numbers are allowed!')
        self.s = s
        self.threshold = c
        # will hold all the subsets under the given threshold
        self.subsets = [[]]
        # enlist all given numbers in the list under the constraint
        for num in s:
            if num < c:
                current_list = [num]
                self.subsets.append(current_list)
        self.create_subsets(self.subsets)
        self.current = -1  # points to the current element in the subsets
        self.high = len(self.subsets)  # points to the end of the subsets

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.high:
            return self.subsets[self.current]
        raise StopIteration

    def create_subsets(self, s: list):
        '''
            Create subsets of a given list of lists, under this bounded_subsets threshold
        '''
        current_subsets = []  # holds the new subsets under the constraint founded in this call
        for subset in s:
            current_sum = sum(subset)
            # if constraints isn't met here - no need to search for further matches for it
            if current_sum >= self.threshold:
                continue
            for num in self.s:
                if (num not in subset) and (current_sum + num) <= self.threshold:
                    new_subset = copy.deepcopy(subset)
                    new_subset.append(num)
                    new_subset.sort()
                    # if an equal subset isn't exist - prevent duplicates
                    if new_subset not in self.subsets:
                        current_subsets.append(new_subset)
                        self.subsets.append(new_subset)
        # recursive call to all of the newly found subsets
        if len(current_subsets) != 0:
            self.create_subsets(current_subsets)


if __name__ == '__main__':
    doctest.testmod()

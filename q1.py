import copy
'''
 This class represents an iterator, that retrieve all the subsets of a given list,
 that sums up to no more then a given threshold.
'''


class bounded_subsets:
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
        self.subsets = [[]] #will hold all the subsets under the given threshold 
        # enlist all given numbers in the list under the constraint 
        for num in s:
            if num < c:
                current_list = [num]
                self.subsets.append(current_list)
        self.create_subsets(self.subsets)
        self.current = -1 #points to the current element in the subsets
        self.high = len(self.subsets) #points to the end of the subsets

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.high:
            return self.subsets[self.current]
        raise StopIteration

    def create_subsets(self, s: list):
        current_subsets = [] #holds the new subsets under the constraint founded in this call
        for subset in s:
            current_sum = sum(subset)
            #if constraints isn't met here - no need to search for further matches for it
            if current_sum >= self.threshold:
                continue
            for num in self.s:
                if (num not in subset) and (current_sum + num) <= self.threshold:
                    new_subset = copy.deepcopy(subset)
                    new_subset.append(num)
                    new_subset.sort()
                    #if an equal subset isn't exist - prevent duplicates
                    if new_subset not in self.subsets:
                        current_subsets.append(new_subset)
                        self.subsets.append(new_subset)
        #recursive call to all of the newly found subsets                
        if len(current_subsets) != 0:
            self.create_subsets(current_subsets)


if __name__ == '__main__':
    for s in bounded_subsets(range(50,150), 103):
        print(s)
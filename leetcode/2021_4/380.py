import random
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_dict={}
        self.data_list=[]
        self.data_num=0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data_dict:
            return False
        else:
            self.data_dict[val] = self.data_num
            self.data_num += 1
            self.data_list.append(val)
            return True

    def remove(self, val) :
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data_dict:
            last_val, idx = self.data_list[-1], self.data_dict[val]
            self.data_dict[last_val] = idx
            self.data_list[idx] = last_val
            del self.data_dict[val]
            self.data_list.pop()
            self.data_num -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.data_list)

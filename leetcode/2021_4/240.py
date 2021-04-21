class Solution:
    def searchMatrix(self, matrix, target):
        self.n = len(matrix[0])
        for line in matrix:
            if self.search_t(line, target):
                return True
        return False

    def search_t(self, line, target):
        i, j = 0, self.n - 1
        while i < j:
            mid = int((i + j) / 2)
            mid_val = line[mid]
            if mid_val == target:
                return True
            elif mid_val < target:
                i = mid + 1
            else:
                j = mid - 1
        if i == j:
            if line[i] == target:
                return True
            elif line[i] < target:
                return False
            else:
                return False
        else:
            return False

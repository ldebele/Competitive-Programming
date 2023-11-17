import math

class Solution:
    def kClosest(self, points, k):
        r = []
        for i in range(len(points)):
            # for j in range(len(points[0])):
            result = points[i][0] ** 2 + points[i][1]**2
            r.append(result)
                
        
        


if __name__ == "__main__":

    sln = Solution()

    points = [[1,3], [-2, 2]]
    c = sln.kClosest(points, 1)
    print(c)



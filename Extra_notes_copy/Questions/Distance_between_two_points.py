import math

class Finder:
    def __init__(self, x, y):
        self.x= x
        self.y= y
    
    def display(self):
        print(self.x_distance, self.y_distance)

    def find_distance(self, other_point):
        x_distance= self.x-other_point.x
        y_distance= self.y-other_point.y

        return math.sqrt(x_distance**2+y_distance**2)
    
    def calculate_distances(self, points):
        distances= []

        for point in points:
            distances.append(self.find_distance(point))
        
        return distances
    
if __name__=='__main__':
    points= []
    n= int(input("Enter number of points: "))
    
    for i in range(n):
        points.append(Finder(int(input("Enter X-Coordinate: ")), int(input("Enter Y-Coordinate: "))))
    
    finder_instance= Finder(0,0)
    distances= finder_instance.calculate_distances(points)
    print(*distances)
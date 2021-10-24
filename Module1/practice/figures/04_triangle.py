class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
            return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3


    def perimeter(self, p1,p2,p3):
        return self.dist_to(p1,p2)+self.dist_to(p2,p3)+self.dist_to(p1,p3)

    def area(self, p1,p2,p3):
        half_perimeter = (self.dist_to(p1,p2)+self.dist_to(p2,p3)+self.dist_to(p1,p3))*0.5
        return ((half_perimeter-self.dist_to(p1,p2))*(half_perimeter-self.dist_to(p1,p2)))*0.5

        # Для нахождения площади, используйте формулу
        # Герона S = (p − a) * (p − b), где a, b — катеты,
        # p — полупериметр, который рассчитывается по формуле p = (a + b + c) : 2

triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и периметр треугольника, реализовав методы


print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())

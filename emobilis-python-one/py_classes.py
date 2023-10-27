class Circle:
    def __init__(self, radius):
        self.circle_radius = radius

    def calc_area(self):
        a = 22/7 * self.circle_radius ** 2
        print(f"Area is {a}")

    def calc_perimeter(self):
        p = 22/7 * self.circle_radius * 2
        print(f"Circumference is {p}")
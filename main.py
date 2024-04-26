import math
import random

# Noktaların tanımlanması
points = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(5)]

# Öklid mesafesi için fonksiyon tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonucun yazdırılması
print("Noktalar:", points)
print("Minimum mesafe:", min_distance)

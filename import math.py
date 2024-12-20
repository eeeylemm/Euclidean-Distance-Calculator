import math

# İki nokta arasındaki Öklid mesafesini hesaplamak için fonksiyon
def euclideanDistance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# q^2 + r^2 = p^2 denklemini sağlayan p, q, r değerlerini bulalım
def find_pqr(q, r):
    p = math.sqrt(q**2 + r**2)  # p'yi Pisagor teoreminden hesaplıyoruz
    return p

# 2p = a^2 + r^2 denklemine göre a'yı hesaplayalım
def find_a(p, r):
    a = math.sqrt(2*p - r**2)  # a'yı bu denklemden çözerek buluyoruz
    return a

# Örnek noktalar
x1, y1 = 1, 2
x2, y2 = 4, 6

# Öklid mesafesini hesaplayalım
r = euclideanDistance(x1, y1, x2, y2)
print(f"Öklid Mesafesi (r): {r}")

# q ve r için örnek değerler (örneğin, q = 3, r = hesapladığımız mesafe)
q = 3

# p'yi hesaplayalım
p = find_pqr(q, r)
print(f"p değeri: {p}")

# a'yı hesaplayalım
a = find_a(p, r)
print(f"a değeri: {a}")

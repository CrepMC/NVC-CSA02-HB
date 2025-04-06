A = {1, 2, 3}
B = {3, 4, 5}

union = A.union(B)
print("Hợp của A và B:", union)

intersection = A.intersection(B)
print("Giao của A và B:", intersection)

difference = A.difference(B)
print("Hiệu của A và B (A - B):", difference)

U = {1, 2, 3, 4, 5, 6}
A_complement = U - A
print("Bù của A:", A_complement)
B_complement = U - B
print("Bù của B:", B_complement)
de_morgan_left = A_complement.intersection(B_complement)
de_morgan_right = U - (A.union(B))
print("De Morgan: (A ∪ B)^c =", de_morgan_right)
print("De Morgan: A^c ∩ B^c =", de_morgan_left)
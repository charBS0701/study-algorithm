matrix = [[3, 7, 9,],
         [4, 2, 6],
         [8, 1, 5]]
        
trails = []

for r in range(3):
    for c in range(3):
        trails.append(matrix[c][r])
    
print(trails)

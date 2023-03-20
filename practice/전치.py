matrix = [[3, 7, 9],
		      [4, 2, 6],
	    	  [8, 1, 5]]

for r in range(3):
    for c in range(3):
        if r > c: # r < c 로 해도 됩니다.
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
	
for i in range(3):
    print(matrix[i])

matrix2 = [[3, 7, 9],
		      [4, 2, 6],
	    	  [8, 1, 5]]
    
# zip을 활용한 전치 => 원소가 튜플이 됨
zipped_matrix = list(zip(*matrix2))
print(zipped_matrix)

matrix3 = [[3, 7, 9],
		      [4, 2, 6],
	    	  [8, 1, 5]]

# 전치 완료 후, 원소를 리스트로 활용하고 싶을 때
tranposed_matrix = list(map(list, zip(*matrix3)))
print(tranposed_matrix)
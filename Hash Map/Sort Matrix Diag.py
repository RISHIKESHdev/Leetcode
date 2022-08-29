def diagonalSort(mat):
        
        diag = {}
        m = len(mat)
        n = len(mat[0])
        
        for row in range(m):
            for col in range(n):
                diag.setdefault(col-row, [])
                diag[col-row].append(mat[row][col])
        print(diag)
        for key, val in diag.items():
            diag[key] = sorted(val)
        
        for row in range(m):
            for col in range(n):
                mat[row][col] = diag[col-row].pop(0)
        
        return mat
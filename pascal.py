tri = [[1], [1,1]]

def pascal(n):
    if n < 1:
        print('Invalid Number of rows')
    elif n == 1:
        print(tri[0])

    else: 
        row_number = 2
        while len(tri) > n:
            row = []
            row_prev = tri[row_number -1]

            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)

                elif i > 0 and i < length-1:
                    row.append(tri[row_number - 1][i-1]+tri[row_number-1][i])

                else :
                    row.append(1)
                    tri.append(row)
                    row_number += 1

        for row in tri:
            print(row)
pascal(8)
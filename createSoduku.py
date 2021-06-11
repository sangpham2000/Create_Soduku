import sys
import random

random.seed(5180430)

def addperm(x, arr):                                                  
    return [arr[0:i] + [x] + arr[i:] for i in range(len(arr)+1)]      
                              
def perm(arr):                                                        
    if len(arr) == 0:                                                 
        return [[]]
    return [x for y in perm(arr[1:]) for x in addperm(arr[0], y)]      

def latinList(arr):
    latin = []  # Chứa các bộ 3 hoán vị
    List = perm(arr)
    for i in List:
        for j in List:
            for k in List:
                a = i[0] + j[0] + k[0]
                b = i[1] + j[1] + k[1]
                c = i[2] + j[2] + k[2]
                if a == b == c:
                    latin.append([i, j, k])
    return latin

def swap(a, b):
    return b, a


def printGrid(arr):
    for i in range(len(arr)):
        if i == 0:
            print("┎-----------┬-----------┬-----------┒")
        if i % 3 == 0 and i != 0:
            print("|-----------|-----------|-----------|")
        print(
            "|", arr[i//3*3+0][i % 3], "|",
            arr[i//3*3+1][i % 3], "|",
            arr[i//3*3+2][i % 3], "|"
        )
    print("┖-----------┴-----------┴-----------┚")


def sudokuPuzzel(n):
    print("Tất cả các bộ Latin Squares:")
    print(latinList([0, 1, 2]))
    print()
    print("Lấy ngẫu nhiên 9 bộ:")
    matrix = random.sample(latinList([0, 1, 2]), 9)
    printGrid(matrix)
    print("======================================")

    print("┎-----------┒")
    for i in matrix[random.randint(0, 8)]:
        print("|",i,"|")
    print("┖-----------┚")

    print("======================================")
    print()

    temp = random.choice(matrix)
    arr = []
    for i in temp:
        for j in i:
            arr.append(j)

    print("Solve:")
# Tính toán từng phần tử
    resultMatrix = []
    count = 0
    for i in matrix:
        temp = []
        for j in i:
            x = arr[count]*3 + j[0] + 1
            y = arr[count]*3 + j[1] + 1
            z = arr[count]*3 + j[2] + 1
            temp.append([x, y, z])
        count += 1
        resultMatrix.append(temp)
    printGrid(resultMatrix)


    # Swap dong 2 voi 3, 3 voi 7, 6 voi 8
    resultMatrix[0][1], resultMatrix[3][0] = resultMatrix[3][0], resultMatrix[0][1]
    resultMatrix[1][1], resultMatrix[4][0] = resultMatrix[4][0], resultMatrix[1][1]
    resultMatrix[2][1], resultMatrix[5][0] = resultMatrix[5][0], resultMatrix[2][1]

    resultMatrix[0][2], resultMatrix[6][0] = resultMatrix[6][0], resultMatrix[0][2]
    resultMatrix[1][2], resultMatrix[7][0] = resultMatrix[7][0], resultMatrix[1][2]
    resultMatrix[2][2], resultMatrix[8][0] = resultMatrix[8][0], resultMatrix[2][2]

    resultMatrix[3][2], resultMatrix[6][1] = resultMatrix[6][1], resultMatrix[3][2]
    resultMatrix[4][2], resultMatrix[7][1] = resultMatrix[7][1], resultMatrix[4][2]
    resultMatrix[5][2], resultMatrix[8][1] = resultMatrix[8][1], resultMatrix[5][2]
    print()
    print("After swap:")
    printGrid(resultMatrix)

    print("Tạo lổ:")
    if n > 81:
        print("Số lổ bạn chọn nhiều hơn kích số lổ tối đa")
    else:
        while n>0:
            j = random.randint(0, 8)
            col = random.randint(0, 2)
            row = random.randint(0, 2)
            if resultMatrix[j][row][col] != 0:
                resultMatrix[j][row][col] = 0
                n = n - 1
            else:
                n = n 
    printGrid(resultMatrix)

#Phần dùng để in file
    arr1 = []
    for i in resultMatrix:
        arr2 = i[0] + i[1] + i[2]
        arr1.append(arr2) 
    with open(sys.argv[2],'w',encoding = 'utf-8') as f:
        for i in arr1:
            for j in i[:8]:
                f.write(str(j)+", ")
            f.write(str(i[8]))
            f.write("\n")
                


if __name__ == "__main__":
    sudokuPuzzel(int(sys.argv[1]))
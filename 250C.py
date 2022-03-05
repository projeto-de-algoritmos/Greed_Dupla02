# Deu tle e ainda tá meio gambiarra. Vou tentar arrumar depois.

def findMininumStress (n, k, movies, stress):
    for i in range(k):
        j = 0
        while j < n:
            if movies[j] != i + 1:
                t = j + 1
                if t < n:
                    while t < n and (movies[t] == i + 1):
                        t = t + 1            
                    if t < n and movies[j] != movies[t]:
                        stress[i] = stress[i] + 1
                j = t
            else:
                j = j + 1
            
    minimumValue = 1000000
    minimumPosition = 0
    for i in range(k):
        if(stress[i] < minimumValue):
            minimumValue = stress[i]
            minimumPosition = i + 1
    print(minimumPosition)


if __name__ == '__main__':
    n, k = map(int, input().split())
    movies = list(map(int, input().split()))

    stress = [0] * k

    findMininumStress(n, k, movies, stress)



 

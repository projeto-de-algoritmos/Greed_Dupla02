def findMininumStress (newMovies, k):
    stress = 0

    for i in range(len(newMovies)):
        if i < len(newMovies) - 1:
            if newMovies[i] != newMovies[i + 1]:
                stress = stress + 1

    fewerStresses = [stress] * k
    minimumValue = stress
    minimumPosition = 0

    for i in range(len(newMovies)):
        if i > 0 and i < len(newMovies) - 1:
            if newMovies[i - 1] != newMovies[i + 1]:
                fewerStresses[newMovies[i] - 1] = fewerStresses[newMovies[i] - 1] - 1
            else:
                fewerStresses[newMovies[i] - 1] = fewerStresses[newMovies[i] - 1] - 2
        else:
            fewerStresses[newMovies[i] - 1] = fewerStresses[newMovies[i] - 1] - 1

    for i in range(k):
        if fewerStresses[i] < minimumValue:
            minimumValue =  fewerStresses[i]
            minimumPosition = i + 1
            
    print(minimumPosition)

def excludeConsecutiveRepetitions(n, movies, newMovies):
    for i in range(n):
        if i < n - 2:
            if movies[i] != movies[i + 1]:
                newMovies.append(movies[i])
        elif i == n - 2:
            if movies[i] != movies[i+1]:
                newMovies.append(movies[i])
                newMovies.append(movies[i + 1])
            else:
                newMovies.append(movies[i])


if __name__ == '__main__':
    n, k = map(int, input().split())
    movies = list(map(int, input().split()))

    newMovies = []

    excludeConsecutiveRepetitions(n, movies, newMovies)

    findMininumStress (newMovies, k)
 

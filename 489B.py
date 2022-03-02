

def findPairs(girls, boys, lengirls, lenboys, pairs):
    # Recebe vetores ordenados pela proficiencia em dança
    if lengirls == 0 or lenboys == 0:                               # Se algum vetor zerar, todas possiveis duplas foram encontradas
        print(pairs)
    elif abs(girls[0] - boys[0]) < 2:                               # Se a diferença de proficiencia for < 2 formamos uma dupla
        findPairs(girls[1:], boys[1:], lengirls - 1, lenboys - 1, pairs + 1)
    elif girls[0] < boys[0]:                                        # Se a diferença for maior que 2 e a primeira garota tiver proficiente maior
        findPairs(girls[1:], boys, lengirls - 1, lenboys, pairs)    # que o primeiro garoto, o primeiro garoto não forma um par
    else:
        findPairs(girls, boys[1:], lengirls, lenboys - 1, pairs)    # Se a diferença for maior que 2 e o primeiro garoto tiver proficiente maior
                                                                    # que a primeira garota, a primeira garota não forma um par


if __name__ == '__main__':
    n = int(input())
    boys = sorted(map(int, input().split()))
    m = int(input())
    girls = sorted(map(int, input().split()))

    findPairs(girls, boys, m, n, 0)
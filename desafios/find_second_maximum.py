if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()), reverse = True)
    without_max_value = list(filter(lambda x: x != max(arr), arr))
    print(without_max_value[0])
    
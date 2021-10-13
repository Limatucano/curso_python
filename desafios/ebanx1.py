from functools import reduce

#
# Complete the 'compute_ranking' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING scores as parameter.
#

def compute_ranking(scores):
    scores = scores.replace(' ','')
    scores_array = scores.split(',')
    score_point = []
    for index,score in enumerate(scores_array):
        score_point.append([])
        for score_value in score:
            score_point[index].append(score_value)

    final_value = []
    for index,point in enumerate(score_point):
        final_value.append([])
        value = [int(val) for index, val in enumerate(point) if index != 0]
        sum = reduce((lambda first,second: first + second),value)
        final_value[index].append(point[0])
        final_value[index].append(sum)

    final_value_sorted = sorted(final_value,key=lambda x: x[1],reverse=True)    
    
    final = str()
    len_list = len(final_value_sorted)
    for index,final_value in enumerate(final_value_sorted):
        if(index == len_list-1):
            final += f"{final_value[0]} {final_value[1]}"
        else:
            final += f"{final_value[0]} {final_value[1]}, "

    return final

if __name__ == '__main__':
    teste = "1 1 1 1 1 1 1 1 1 1 1, 2 0 0 0 0 0 0 0 0 0 0, 3 1 1 1 1 1 0 0 0 0 0"

    result = compute_ranking(teste)
    print(result)


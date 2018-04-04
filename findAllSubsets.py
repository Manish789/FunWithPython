# Finding all subsets of a given set or list

arr = [x for x in input().split()]
N = len(arr)
def generate_all_subsets(arr,N):
    for i in range(1<<N):
        for j in range(N):
            if (i & (1<<j)):
                print(arr[j], end=" ")
        print()

generate_all_subsets(arr,N)

from itertools import combinations_with_replacement 
  
def rSubset(arr, r):
    return combinations_with_replacement(arr, r)
if __name__ == "__main__":
    OUT=rSubset('ACHK', 2)
    for i in OUT:
        print(''.join(i))



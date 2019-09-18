import copy
def bina(arr, a):
    imsi_base = copy.deepcopy(arr)
    for q in range(len(bi)):
        if bi[q] != imsi_base[a]:
            imsi_base[a] = bi[q]
            imsi = 0
            for idx in range(0,len(imsi_base)):
                imsi += int(imsi_base[idx]) * (2 ** (len(imsi_base)-idx-1))
            result_a.append(imsi)
            imsi_base[a] = arr[a]

def binb(arr, a):
    imsi_base = copy.deepcopy(arr)
    for q in range(len(th)):
        if th[q] != imsi_base[a]:
            imsi_base[a] = th[q]
            imsi = 0
            for idx in range(0, len(imsi_base)):
                imsi += int(imsi_base[idx]) * (3 **(len(imsi_base)-idx-1))
            result_b.append(imsi)
            imsi_base[a] = arr[a]

for tc in range(int(input())):
    bi = [0,1]
    th = [0,1,2]
    result_a = []
    result_b = []
    a = list(map(int,input()))
    b = list(map(int, input()))
    for i in range(len(a)):
        bina(a,i)
    for j in range(len(b)):
        binb(b,j)
    for r_a in result_a:
        for r_b in result_b:
            if r_a == r_b:
                print("#{0} {1}".format(tc+1, r_a))
                break

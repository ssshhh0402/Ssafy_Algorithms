def solution(dataSource, tags):
    answer = []
    base = {}
    dicted = []
    for tag in tags:
        for data in dataSource:
            if tag in data:
                if data[0] in base.keys():
                    base[data[0]] += 1
                else:
                    base[data[0]] = 1
    for item in base:
        dicted.append([item,base[item]])
    imsi = sorted(dicted,key=lambda item: (-item[1],item[0]))
    for item in imsi:
        answer.append(item[0])

    print(answer)



dataSource = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]

tag = ["t1", "t2", "t3"]

a = solution(dataSource, tag)
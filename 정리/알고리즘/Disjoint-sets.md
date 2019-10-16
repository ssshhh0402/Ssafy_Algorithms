# Disjoint-sets

### 구성 함수:

​	Make-Set(x): x라는 원소를 포함하는 집합 return

​	Find-Set(a): a라는 원소가 속한 set의 식별값 return

​	Union(a,b): a가 속한 집합과 b가 속한 집합 합치기

### Disjoint Set 만드는 법:

1) 집합 안에 있는 각각의 원소를 Make-Set을 사용하여 자신을 원소로 가지는 집합으로 형성

2) Union을 사용하여 하나씩 연결

3) 그 후 연결된 집합에서 대표값 탐색

4) 2~3 반복

### Tree를 활용한 Disjoint Set

* 구현 시 부모 자식의 위치만 저장하는 방식

* 트리의 루트값은 대표값!!
* Union 시에는 둘 중 한쪽 루트의 부모 값을 다른 노드 값으로 연결



### 함수

* Make-Set(x)

```python
def Make-Set(x)
	P[x] = x		#P는 각각의 원소에 대하여 부모의 위치를 저장하고있는 배열
```

* Find_Set(x)

```python
def Find_Set(x):
    If x == p[x]:			#x의 부모가 자기자신일 경우(x가 대표값일 경우)
        return x
    else:					#아닐 경우 대표 값을 찾아 위로 ㄱㄱ
        return Find_Set(p[x])
```

* Union(x,y):

```python
def Union(x,y):
    p[Find-Set(y)] = Find-Set(x)
```



### 연산 효율 높이는 법

* Rank 활용하여 Union
  * 자신이 루트인 Tree의 높이를 저장하는 Rank Tree 형성
  * 두 집합을 합칠때 Rank Tree값이 낮은 아이를 높은 아이한테 붙인다
  * 합쳐졌을 때 트리의 높이 최소화

* Path Compression
  * Find-Set을 진행할 때 합치는 아이의 서브트리의 부모를 합쳐지는 아이의 루트값으로 설정한다.



### 효율성을 높인 함수

* Make_Set(x):

```python
p[x]
rank[x]:
def Make_Set(x):
   	p[x] = x
	rank[x] = 0
```



* Find_Set(x):

```python
def Find_Set(x):
    If x != p[x]:
        p[x] = Find_Set(p[x])
    return p[x]
```

* Union(x,y):

```python
def Union(x, y):
    Link( Find_Set(x), Find_Set(y))
```

```python
def Link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
     else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1
```




#!/usr/bin/env python
# coding: utf-8

# # 1.정렬 레코드 들을 키의 순서로 재배열 하는것
# # 레코드 정렬시켜야 할 대상  
# # 여러개의 필드로 이루어짐  
# # 정렬 키 정렬의 기준이 되는 필드  

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[1]:


def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i;
        for j in range(i+1, n) :  
            if (A[j]<A[least]) : #비교연산
                least = j         #최소항목 갱신
        A[i], A[least] = A[least], A[i]      #배열 항목 교환
        printStep(A, i + 1);   
def printStep(arr, val) :  #중간 과정 출력용 함수
    print("  Step %2d = " % val, end='')
    print(arr)
    
data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)

selection_sort(data)
print("Selection :", data)


# 1-2 삽입정렬 비교 이동

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[2]:


def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i;
        for j in range(i+1, n) :  
            if (A[j]<A[least]) : #비교연산
                least = j         #최소항목 갱신
        A[i], A[least] = A[least], A[i]      #배열 항목 교환
        printStep(A, i + 1);   
def printStep(arr, val) :  #중간 과정 출력용 함수
    print("  Step %2d = " % val, end='')
    print(arr)
data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)
selection_sort(data)
print("Selection :", data)
def insertion_sort(A) :
    n = len(A)
    for i in range(1, n):   #외부 루프 1,2,...,n-1
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :  #내부루프
            A[j + 1] = A[j]   # 항목들을 뒤로 한 칸씩 이동
            j -= 1
        A[j + 1] = key    # 항목 삽입
        printStep(A, i)
        
data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)
insertion_sort(data)
print("Selection :", data)


# 특징
# 
# 많은 이동 필요 -> 레코드가 큰 경우 불리  
# 안정된 정렬방법  
# 대부분 정렬되어있으면 매우 효율적

# 1-3 버블정렬  
# 인접한 2개의 레코드를 비교하여 순서대로 서로교환  
# 비교-교환 과정을 리스트의 전체에 수행(스캔)  
#   
# 비교-교환 과정이한번 완료되면 한번의 스캔(스캔1)  
# 
# 한번의 스캔이 완료되면 리스트의 오른쪽 끝에 가장 큰 레코드  
# 끝으로 이동한 레코드를 제외하고 다시 스캔 반복  

# In[3]:


def bubble_sort(A) :
    n = len(A)
    for i in range(n-1, 0, -1) :
        bChanged = False
        for j in range (i) :
            if (A[j]>A[j+1]) :
                A[j], A[j+1] = A[j+1], A[j] 
                bChanged = True
        if not bChanged: break;
        printStep(A, n - i);
        
        
        
data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)
bubble_sort(data)
print("Selection :", data)


# #비교횟수(최상,평균,최악의 경우 모두 일정) O(n^2)  
# 버블 정렬은 매우 단순하지만효율적이지 않다.  
# 입력 데이터가 어느정도 정렬되어 있는 경우에효과적  

# # 정렬 응용 : 집합을 정렬의 개념 사용  
# 집합의 원소들을 항상 정렬된 순으로 저장 -> 삽입연산 변경(복잡)  
# 집합의 비교나 합집합, 차집합, 교집합 -> 효율적 구현 가능  
# 
# # 비교연산: eq  
# 
# o(n2) -> o(n)으로 계산  
# 두집합의 비교방법  
# 두 집합의 원소의 개수가 같아야 같은 집합이 됨  
# 집합이 정렬되어 있으므로  

# In[ ]:





# # 합집합/교집합/차집합  
# o(n2) -> o(n)으로 개선   
# 합집합 연산 가장 작은 원소들로 부터 비교하여 더작은 원소를 새로운 집합에 넣고   
# 그 집합의 인덱스를 증가시킴  
# 만약 두집합의 현재 원소가 같으면 하나만을 넣음 인덱스는 모두 증가시킴  
# 한쪽 집합이 모두 처리되면 나머지 집합의 남은 모든 원소를 순서대로 새 집합에 넣음  

# In[4]:



class Set:       
    def __init__( self ):
        self.items = []    
    def display(self, msg):
        print(msg, self.items)
    def insert(self, elem) :                
        if elem in self.items : return      
        for idx in range(len(self.items)) : 
            if elem < self.items[idx] :     #삽입할 위치 idx를 찾음
                self.items.insert(idx, elem)  #그 위치에 삽입
                return
        self.items.append(elem)      #맨 뒤에 삽입           
    def __eq__( self, setB ):       # self, setB가 같은 집합인가?  
        if self.size() != setB.size() :  # 원소의 개수가 같아야 함
            return False
        for idx in range(len(self.items)): #loop: n번   𝑂(𝑛^2 ) --> 𝑂(𝑛)으로 개선
            if self.items[idx] != setB.items[idx] :   #원소별로 같은지 검사
                return False
        return True
    def union( self, setB ):       
        newSet = Set()
        a = 0
        b = 0
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB :
                newSet.items.append( valueA )
                a += 1
            elif valueA > valueB :
                newSet.items.append( valueB )
                b += 1
            else : 
                newSet.items.append( valueA )
                a += 1
                b += 1
        while a < len( self.items ):
             newSet.items.append( self.items[a] )
             a += 1
        while b < len( setB.items) :
             newSet.items.append( setB.items[b] )
             b += 1
        return newSet
    def delete(self, elem) :
        if elem in self.items :  #O(n)
            self.items.remove(elem)
    
    
setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')
setB = Set()
setB .insert('빗')
setB .insert('파이썬 자료구조')
setB .insert('야구공')
setB .insert('지갑')
setB.display('Set B:')
setA.delete('손수건')
setB.delete('지갑')
setA.display('Set A:')
setB.display('Set B:')
setA.union(setB).display('A U B:')


# # 2 탐색 맵 엔트리 딕셔너리  
# ### 탐색
# 
# 테이블에서 원하는탐색키를 가진 레코드를 찿는 작업  
# #### 맵 또는 딕셔너리  
# 탐색을 위한 자료구조  
# 엔트리 또는 키를 가진 레코드 의 집합  
# ##### 엔트리  
# 키 영어단어와 같은레코드를 구분할수있는 탐색키  
# 값 단어의 의미와 같이 탐색키와 관련된 값  
# ### 파이썬의 딕셔너리  
# 파이썬은 내장 자료형으로 딕셔너리 제공, 이것은 자료구조 맵을 구현한 하나의 예  

# ![image.png](attachment:image.png)

# In[ ]:





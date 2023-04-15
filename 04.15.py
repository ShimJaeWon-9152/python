#예제 1
colors = ['red','blue','green','yellow']
result = ''.join(colors) # 리스트의 각 요소를 빈칸 없이 붙이는 것

print(result)

#예제 2
example = 'python,jquery,javascript'
example.split(',')

a,b,c = example.split(',')
print(a,b,c)

example = 'theteamlab.univ.edu'
subomain, domain, tld = example.split('.')
print(subomain, domain, tld)

#예제 3 리스트 컴프리헨션
result = [i for i in range(10) if i % 2 == 0]
print(result)

#예제 4 리스트 컴프리헨션2
result = [i if i % 2 == 0 else 10 for i in range(10)]
print(result)

#중첩 반복문
word_1 = "Hello"
word_2 = "World"
 
result =[i + j for i in word_1 for j in word_2]
print(result)

#중첩 반복문2 if문 추가
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i + j for i in case_1 for j in case_2 if not (i == j)]
print(result)

#이차원리스트
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)]for w in words] # 뒤 for문이 고정된다!!
print(stuff)

#이차원리스트2
case_1 = ["A","B","C"]
case_2 = ["D","E","A"]
 
result = [[i+j for i in case_1]for j in case_2]
print(result)




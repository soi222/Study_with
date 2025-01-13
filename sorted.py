import os

# 원본 폴더 경로
file_path = "C:/Users/dnltj/OneDrive/바탕 화면/토스 노트"

# 1. 폴더 내 파일 리스트 불러오기
file_list = os.listdir(file_path)

# 2. 파일 리스트 정렬 (기본 정렬: 오름차순)
file_list = sorted(file_list)

# 3. 파일 이름 변경 
file_num = len(file_list)  
for index, file_name in enumerate(file_list, start=1):
    old_space = os.path.join(file_path, file_name)
    
    new_number = file_num - index + 1 
    new_name = f"part5_{new_number}.jpg"
    
    new_space = os.path.join(file_path, new_name)
    
    try:
        os.rename(old_space, new_space)
    except Exception as e:
        print(f"Failed to rename {file_name}: {e}")


"""
1. os.listdir
폴더 내 항목들을 확장자 상관없이 불러와 리스트로 생성됨


2. reserved와 list.reserve의 차이
내가 진행하고자 한 코드는 아래 두 줄이었음
file_list = reserved(file_list)
file_num = len(file_list)


-> TypeError: object of type 'list_reverseiterator' has no len() 발생
이유 :
list.reserve() vs reserved()의 차이
list.reserve()는 리스트를 리버브한 형태로 저장하여, 공간을 효율적으로 사용 가능
그러나 reserved()는 리버브된 형태로 반복 가능 객체로 부르는 것이며, 다른 이름으로 저장되어야 사용할 수 있고 이는 재호출이 불가능

- list.reserve()
numbers = [1, 2, 3, 4]
numbers.reverse()  
print(numbers)     # 출력: [4, 3, 2, 1]

- revserved()
numbers = [1, 2, 3, 4]
rev_iter = reversed(numbers)
print(list(rev_iter))  # [4, 3, 2, 1]
print(list(rev_iter))  # 빈 리스트 출력([]): 이미 소멸됨


3. os.path.join(file_path, new_name)
파일의 경로나 디렉토리를 운영체제에 맞게 수정해줌

- os.path()
-> TypeError: 'module' object is not callable
자바와 달리 파이썬에서는 모듈을 불러올 수 없음

- os.path.join(A, B) #출력 : A\B
A와 B를 운영체제에 맞게 경로를 작성
"""
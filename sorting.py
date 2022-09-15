# 선택 정렬
# array = [7,5,9,0,3,1,6,2,4,8]
#
# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1 , len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
#
# print(array)

# 삽입 정렬
# array = [7,5,9,0,3,1,6,2,4,8]
#
# for i in range(1,len(array)):
#     for j in range(i,0,-1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break
# print(array)

# 퀵정렬
# array = [7,5,9,0,3,1,6,2,4,8]
#
# def qucik_sort(array):
#     if len(array) <=1:   # 리스트가 하나 이하의 원소를 담고 있다면 종료
#         return array
#
#     pivot = array[0]
#     tail = array[1:]
#
#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]
#
#     return qucik_sort(left_side) + [pivot] + qucik_sort(right_side)
#
# print(qucik_sort(array))

# 계수 정렬
# array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
#
# count = [0] * (max(array)+1)  # 모든 범위를 포함하는 리스트 선언(0으로 초기화)
#
# for i in range(len(array)):
#     count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가
#
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=' ')

# sorted 소스코드
# array = [5,7,9,0,3,1,6,2,4,8]
#
# result = sorted(array)
# print(result)

# 정렬 라이브러리에서 key를 활용한 소스코드
# array ={('바나나',2), ('사과',5), ('당근',3)}
#
# def setting(data):
#     return data[1]
# result = sorted(array,key=setting)
# print(result)

# 위에서 아래로
# n = int(input())
#
# array = []
# for i in range(n):
#     array.append(int(input())
#
# array = sorted(array, reverse=True)
#
# for i in array:
#     print(i, end=' ')

# 성적이 낮은 순서로 학생 출력하기
# n = int(input())
#
# array = []
# for i in range(n):
#     input_data = input().split()
#     array.append((input_data[0], int(input_data[1]))) # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
#
# array = sorted(array, key = lambda student:student[1]) # 키를 이용하여, 점수를 기준으로 정렬
#
# for student in array:
#     print(student[0], end=' ')
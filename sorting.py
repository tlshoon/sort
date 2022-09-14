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
# array = [5,7,9,0,3,1,6,2,4,8]
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
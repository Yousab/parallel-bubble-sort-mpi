from operator import itemgetter

test_list = [[0, 5, 9], [2, 4], [3, 6], [1, 7, 8]]
iterator_number = [0,0,0, 0]
final_array=[]

for my_index in range(0,9):
  iterator = iterator = [ (i, (9999999 if iterator_number[i] >= len(test_list[i]) else test_list[i][iterator_number[i]]) ) for i in range(0, len(test_list))]
  res = min(iterator, key = itemgetter(1))
  iterator_number[res[0]] = iterator_number[res[0]] + 1
  final_array.append(res[1])
  iterator=[]

print(str(final_array))
exit()

#iterator = [ (i, (9999999 if iterator_number[i] >= len(test_list) else test_list[i][iterator_number[i]]) ) for i in range(0, len(test_list))]
#iterator = [ (i, test_list[i][iterator_number[i]]) for i in range(0, len(test_list))]
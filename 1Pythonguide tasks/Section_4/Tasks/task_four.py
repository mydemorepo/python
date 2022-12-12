test_str = "1 2 3 4 5"

test_list = test_str.split(' ')
test_list.reverse()
print(int(''.join(test_list)))

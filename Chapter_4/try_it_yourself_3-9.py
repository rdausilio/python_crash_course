#4-3 Counting to Twenty
for number in range(1, 21):
    print(number)

#4-4 One Million
num_list = [value for value in range(1,1000001)]
print(num_list)

#4-5 Summing a Million
print(min(num_list))
print(max(num_list))
print(sum(num_list))

#4-6 Odd Numbers
for number in range(1, 21, 2):
    print(number)

#4-7 Threes
num_list1 = [value*3 for value in range(1, 11)]
for num in num_list1:
    print(num)

#4-8 Cubes
num_list2 = [value**3 for value in range(1, 11)]
for num in num_list2:
    print(num)

#4-9 Cube Comprehension
print(num_list2)
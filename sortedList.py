
def merge_list(test_input_list1, test_input_list2):

    # return sorted(test_input_list1+test_input_list2)

    list3=[]
    i = 0
    j = 0

    while i < len(test_input_list1) and j < len(test_input_list2):
        if test_input_list1[i] < test_input_list2[j]:
            list3.append(test_input_list1[i])
            i+=1
        else:
            list3.append(test_input_list2[j])
            j+=1

    while i < len(test_input_list1):
        list3.append(test_input_list1[i])
        i += 1

    while j < len(test_input_list2):
        list3.append(test_input_list1[j])
        j += 1

    return list3

#print(merge_list([1,3,5], [2,4]))

def get_prime_numbers(nums):

    list1 = []

    # for num in nums:
    #     if num == 2 or num == 3:
    #         list1.append(num)
    #     elif num % 2 != 0:
    #         rem = 0
    #         for i in range(3, num, +2):
    #             rem = num % i
    #             if rem == 0:
    #                 break
    #         if rem != 0:
    #             list1.append(num)

    def isPrime(num):

        if num == 2 or num == 3:
            return True
        elif num % 2 == 0 or num <= 1:
            return False

        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False

        return True

    for num in nums:
        if isPrime(num):
            list1.append(num)

    return list1
#print(get_prime_numbers([1,2,3,4,5,6,7,29,8,9,10,11,12,13,14,15,16,17,18,23,31,33,35,37,41,43]))


import pandas as pd


def grades_colors(students_df: pd.DataFrame):

    # return students_df.loc[((students_df['favorite_color'] == 'green') |
    #                        (students_df['favorite_color'] == 'red')) &
    #                        (students_df['grade'] > 90)]

    return students_df.loc[(students_df['favorite_color'].isin(['green','red'])) &
                        (students_df['grade'] > 90)]

cols = ['name','age','favorite_color','grade']
list1 = [['Tim Voss',19,'red',91],
    ['Nicole Johnson',20,'yellow',95],
    ['Elsa Williams',21,'green',82],
    ['John James',20,'blue',75],
    ['Catherine Jones',23,'green',93]]
# df1 = pd.DataFrame(list1, columns=cols)
# print(grades_colors(df1))


x =[2,0,1,3]
y = x.pop(0)
x.append(y)
print(x)





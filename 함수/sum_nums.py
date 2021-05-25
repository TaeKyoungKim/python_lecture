
# def sum_nums(*args):
#     data = 0
#     for i in args:
#         data += i
#     data_mean = data / len(args)
#     return data , data_mean

# a , b = sum_nums(10 , 20 , 30)
# print(f'합은 : {a} , 평균은 {b}')

# a , b = sum_nums(10 , 20 , 30 , 40 , 50)
# print(f'합은 : {a} , 평균은 {b}')

def sum_nums(*args):
    data = 0
    for i in args:
        data += i
    data_mean = data / len(args)
    print(f'합은 : {data} , 평균은 {data_mean}')
    return data , data_mean

sum_nums(10 , 20 , 30)
sum_nums(10 , 20 , 30 , 40 , 50)
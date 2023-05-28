import csv
import sys
from collections import deque

# csv table을 dictionary로 바꿔주는 func
def table_to_dic(filename):
    with open(filename, mode='r', encoding='UTF8') as file:
        reader = csv.reader(file)
        attrs = []
        table = []
        for row in reader:
            if len(attrs) < 1:
                attrs = row
                continue
            temp_row_dict = dict()
            for key, value in zip(attrs, row):
                temp_row_dict[key] = value
            table.append(temp_row_dict)
    return table

# 메인
if __name__ == "__main__":

    # argv 설정
    argument = sys.argv
    del argument[0] # 첫번째 인자는 파일 이름이 되기 때문에 지운다.

    if not argument:
        input_file = "example.txt" # default input file name
    else:
        input_file = argument[0]
    
    action_table = table_to_dic('action.csv')
    print(action_table[0]['vtype'])
    goto_table = table_to_dic('goto.csv')
    print(goto_table[0]['VDECL'])
    table = table_to_dic('table.csv')

    with open(input_file,"r", encoding="UTF8") as f:
        data = f.read()
        print(data)
    input_data = deque(data.split()) # popleft하기 위해서 deque으로 변환

    input_data.append("$")
    print(input_data)
    stack = [0] # stack 선언

    while(len(input_data) != 1):
        x = input_data.popleft()
        # 1) shift 연산인 경우
        # 2) reduce 연산인 경우
        table[stack[-1]][x]
        

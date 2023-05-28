import csv
import sys

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


    with open(input_file,"r", encoding="UTF8") as f:
        data = f.read()
        print(data)
    tokens = data.split() # list로 변환

    stack = [0]

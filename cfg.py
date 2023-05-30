import csv
import sys
from collections import deque, defaultdict

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
                temp_row_dict[key.strip()] = value.strip()
            table.append(temp_row_dict)
    return table

def cfg_data(filename):
    data = []
    with open(filename, mode='r', encoding='UTF8') as file:
        while True:
            line = file.readline() 
            
            if not line:
                break
            temp = line.strip().split('->')
            production= temp[1].strip().split()
            data.append([temp[0].strip()])
            data[-1].append(production)
    # data = [['CODE ', ['VDECL', 'CODE']], ['CODE ', ['FDECL', 'CODE']], ['CODE ', ['CDECL', 'CODE']], ...]
    print(data)
    return data


# 메인
if __name__ == "__main__":

    # argv 설정
    argument = sys.argv
    del argument[0] # 첫번째 인자는 파일 이름이 되기 때문에 지운다.

    if not argument:
        input_file = "example.txt" # default input file name
    else:
        input_file = argument[0]
    
    # action_table = table_to_dic('action.csv')
    # print(action_table[0]['vtype'])
    # goto_table = table_to_dic('goto.csv')
    # print(goto_table[0]['VDECL'])
    table = table_to_dic('table.csv')

    # cfg data
    cfg = cfg_data("cfg.txt")
    # 파일 열기
    with open(input_file,"r", encoding="UTF8") as f:
        data = f.read()
        
    print(table[1]['vtype'])
    # input_data 생성
    input_data = deque(data.split()) # popleft하기 위해서 deque으로 변환
    input_data.append("$")
    stack = [0] # stack 선언
    reduce = [] # reduce한 연산 넣어주기
    try:
        while(len(input_data) != 0):
            print("Input: ",*input_data)
            
            x = input_data.popleft()
            
            command = table[stack[-1]][x]
            print(f"command: {command}")
            
            # 1) shift 연산인 경우
            if command[0] == "s":
                stack.append(x)
                stack.append(int(command[1:]))

                print(f"shift: {stack}")
                print()
            # 2) reduce 연산인 경우
            elif command[0] == "r":
                input_data.appendleft(x) # 값을 다시 넣어줌
                
                l = (0 if cfg[int(command[1:])][1]==["''"] else len(cfg[int(command[1:])][1])) # 빈 문자열이면 0으로 해준다. 아니면 길이만큼
                # 길이의 두배만큼 pop 해줘야함
                temp_reduce = []
                for i in range(l*2):
                    
                    stack.pop()
                stack.append(cfg[int(command[1:])][0]) # reduce한거 append
                reduce.append([cfg[int(command[1:])][0]])
                reduce[-1].append(cfg[int(command[1:])][1])
                print(f"reduce: {stack}")
                print()

                # goto 연산 실행
                print("Input: ", *input_data)
                print(f"command: {table[stack[-2]][stack[-1]]}")
                stack.append(int(table[stack[-2]][stack[-1]]))
                print(f"goto: {stack}")
                print()
    except:
        print("reject")
    print(stack)
    
    # stack에 있는거 채워넣기
    temp = []
    for i in stack:
        if not isinstance(i, int):
            temp.append(i)
    reduce.append(["CODE"])
    reduce[-1].append(temp)
    print(reduce)
    # reduce = [['RHS', ['literal']], ['ASSIGN', ['id', 'assign', 'RHS']], ['VDECL', ['vtype', 'ASSIGN', 'semi']], ['ODECL', ["''"]], ...]]] 
    
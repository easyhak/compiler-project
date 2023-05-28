action = [
{ 
    "vtype": "s2" # 0
},
{
    "vtype": "s6", "class": "s7", "$":"r3" # 1
},
{
    "id": "s8" # 2
},
{
    "$":"acc" # 3
},
{
    "vtype":"s6", "vtype": "s7" # 4
},
{
    "vtype": "s6" # 5
},
{
    "id": "s12" # 6
},
{
    "id": "s13" # 7
},
{
    "semi": "s14", 
    "assign": "s15" # 8
},
{
    "semi" :"s16" # 9
},
{
    "$": "r1" # 10
},
{
    "$": "r2" # 11
},
{
    "semi": "s14", # 12
    "assign": "s15"
},
{
    "lbrace": "s18" # 13
},
{
    "vtype": "r4", # 14
    "id": "r4",
    "rbrace": "r4",
    "if": "r4",
    "while": "r4",
    "return": "r4",
    "class": "r4",
    "$":"r4"
},
{
    "id": "s26", # 15
    "literal": "s21",
    "character": "s22",
    "boolstr":"s23",
    "lparen":"s25",
    "num":"s27",
},
{
    "vtype": "r5", # 16
    "id": "r5",
    "rbrace": "r5",
    "if":"r5",
    "while":"r5",
    "return":"r5",
    "class":"r5",
    "$":"r5"
},
{
    "vtype":"s29", # 17
    "rparen":"r19"
},
{
    "vtype": "s6", # 18
    "rbrace":"r36" 
},
{
    "semi" : "r6", # 19
},
{
    "semi" : "r7" # 20
},
{
    "semi": "r8" # 21
}

] 
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import pandas as pd

page = open('table.html','rt',encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')
data = soup.find("table")
table = parser_functions.make2d(data)

df = pd.DataFrame(data=table[1:], columns=table[0])
df.to_csv("table.csv", mode='w')
# print(table.find_all('td'))
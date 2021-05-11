#wall 0
#road 1
#数字を表示に適した記号へconvert
def convert(num):
    if num == 1:
        return "□"
    if num == 0:
        return "■"

#mapを表示
def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            print(convert(map[i][j]),end = '')
        print()

#(i,j)の近傍セルを調べ、[wallの個数, roadの個数]を出力
def around_cell(map, i, j):
    #ans=[wall,road]
    ans = [0,0]
    if (i > 0 and i < len(map) - 1):
        ans[map[i - 1][j]] += 1
        ans[map[i + 1][j]] += 1
    if (j != 0 and j != len(map[0]) - 1):
        ans[map[i][j - 1]] += 1
        ans[map[i][j + 1]] += 1
    return ans

#注目セルがroadで近傍セルが3つwallの場合、wallへ変換
def rule(map):
    flag = 0
    new_map = map
    for i in range(len(map)):
        for j in range(len(map[0])):
            around = around_cell(map,i,j)
            if(map[i][j] == 1):
                if(around[0] + around[1] == 4 and around[0] == 3):
                    new_map[i][j] = 0
                    flag = 1
    return (flag)
                       
map =[
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],
[0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0],
[0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0],
[0,1,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0],
[0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,0],
[0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0],
[0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0],
[0,0,0,0,1,1,0,1,1,0,1,0,1,0,0,1,0],
[0,1,1,1,1,0,0,0,1,1,1,0,0,0,1,1,0],
[0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0],
[0,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0],
[0,1,0,0,0,1,0,1,0,0,0,0,1,1,1,1,0],
[0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,1,0],
[0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0],
[0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

print("start")
print_map(map)
i = 1
while(rule(map) == 1):
    print("step",i)
    i += 1
    print_map(map)
    print()




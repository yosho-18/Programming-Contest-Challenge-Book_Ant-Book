n, m = int(input().split())
field = [s for s in input()]

#現在位置(y,x)
def dfs(y, x):
    field[y][x] = "."

    #移動する8方向をループ
    for dy in range(-1, 1):
        for dx in range(-1, 1):
            #y方向にdy，x方向にdx移動した場所を(ny,nx)とする
            nx = x + dx; ny = y + dy
            #nyとnxが庭の範囲内かどうかとfield[ny][nx]が水たまりかどうかを判定
            if 0 <= ny < n and 0 <= nx < m and field[ny][nx] == "W":
                dfs(ny, nx)

def solve():
    print()
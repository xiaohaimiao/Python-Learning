def solve_maze(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    if start[0] < 0 or start[0] >= rows:
        return False
    if start[1] < 0 or start[1] >= cols:
        return False
    if start == end:
        print(end)
        return True
    
    value = maze[start[0]][start[1]]
    
    if value == 1:                          # 判断是否是墙
        return False
    
    if value == -1:                         # 判断是否走过
        return False
    
    maze[start[0]][start[1]] = -1           # 标记走过的路
    print(start, end = " => ")
        
    if solve_maze(maze, (start[0] + 1, start[1]), end):
        return True
    if solve_maze(maze, (start[0] - 1, start[1]), end):
        return True
    if solve_maze(maze, (start[0], start[1] + 1), end):
        return True
    if solve_maze(maze, (start[0], start[1] - 1), end):
        return True
    return False

# 迷宫示例，0表示空格，1表示墙壁
if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]

    start = (0, 0)  # 起点位置
    end = (4, 4)  # 终点位置

    # 调用解答函数
    if solve_maze(maze, start, end):
        print("存在从起点到终点的路径")
    else:
        print("不存在从起点到终点的路径")
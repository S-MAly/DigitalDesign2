import re


def filling(route, src, tar, n):
    i = 1
    route[src[1]][src[2]][src[0] - 1] = i
    print(src)
    L=[]  # the queues used to get the positions in the matrix
    X=[]
    Y=[]
    L.append(src[0] - 1)
    X.append(src[1])  # initialize the queues with the start position
    Y.append(src[2])
    #l, x, y, ll, xx, yy = 0
    while (len(X) > 0):  # while there are still positions in the queue

        l = L[0]  # set the current position
        x = X[0]
        y = Y[0]
        i = route[x][y][l]

        if (l == tar[0] - 1 and x == tar[1] and y == tar[2]):
            return i

        if (l == 0):
            if (y + 1 >= 0 and y + 1 < n and route[x][y + 1][l] == 0):
                L.append(l)
                X.append(x)
                Y.append(y + 1)
                route[x][y + 1][l] = i + 1

            if (y - 1 >= 0 and y - 1 < n and route[x][y - 1][l] == 0):
                L.append(l)
                X.append(x)
                Y.append(y - 1)
                route[x][y - 1][l] = i + 10

            if (route[x][y][l + 1] == 0):
                L.append(l + 1)
                X.append(x)
                Y.append(y)
                route[x][y][l + 1] = i + 10


        elif (l == 1):

            if (x - 1 >= 0 and x - 1 < n and route[x - 1][y][l] == 0):
                L.append(l)
                X.append(x - 1)
                Y.append(y)
                route[x - 1][y][l] = i + 1

            if (x + 1 >= 0 and x + 1 < n and route[x + 1][y][l] == 0):
                L.append(l)
                X.append(x + 1)
                Y.append(y)
                route[x + 1][y][l] = i + 10

            if (route[x][y][l - 1] == 0):
                L.append(l - 1)
                X.append(x)
                Y.append(y)
                route[x][y][l - 1] = i + 10

        L.pop(0)
        X.pop(0)  # eliminate the first position, as you have no more use for it
        Y.pop(0)

    return -1


def BackPropagation(grid, matrix, src,tar, n) :

    l = tar[0] - 1
    x = tar[1]
    y = tar[2]
    matrix[x][y][l] = 1
    while (not (l == src[0] - 1 and x == src[1] and y == src[2])):

        if (grid[x][y] == 1):break

        if (y - 1 >= 0 and y - 1 < n and grid[x][y] - grid[x][y - 1] == 1):

            y = y - 1
            matrix[x][y][l] = 1

        elif (x-1 >= 0  and  x - 1 < n and grid[x][y] - grid[x - 1][y] == 10):
            x = x - 1
            matrix[x][y][l] = 1

        elif (y + 1 >= 0 and y + 1 < n and grid[x][y] - grid[x][y + 1] == 10):

            y = y + 1
            matrix[x][y][l] = 1

        elif (x + 1 >= 0 and x + 1 < n and grid[x][y] - grid[x + 1][y] == 1):\

            x = x + 1
            matrix[x][y][l] = 1

        elif (x - 1 >= 0 and x - 1 < n and grid[x][y] - grid[x - 1][y] == 11):

            l = pow(l - 1, 2)
            matrix[x][y][l] = 1
            x = x - 1
            matrix[x][y][l] = 1

        elif (y - 1 >= 0 and y - 1 < n and grid[x][y] - grid[x][y - 1] == 11):

            l = pow(l - 1, 2)
            matrix[x][y][l] = 1
            y = y - 1
            matrix[x][y][l] = 1

        elif (x - 1 >= 0 and x - 1 < n and grid[x][y] - grid[x - 1][y] == 11):

            l = pow(l - 1, 2)
            matrix[x][y][l] = 1
            x = x - 1
            matrix[x][y][l] = 1

        elif (x - 1 >= 0 and x - 1 < n and grid[x][y] - grid[x - 1][y] == 20):

            l = pow(l - 1, 2)
            matrix[x][y][l] = 1
            x = x - 1
            matrix[x][y][l] = 1

        elif (y + 1 >= 0 and y + 1 < n and grid[x][y] - grid[x][y + 1] == 20):

            l = (l - 1)**2
            matrix[x][y][l] = 1
            y = y + 1
            matrix[x][y][l] = 1

        elif (x + 1 >= 0 and x + 1 < n and grid[x][y] - grid[x + 1][y] == 20):

            l = pow(l - 1, 2)
            matrix[x][y][l] = 1
            x = x + 1
            matrix[x][y][l] = 1



# noinspection PyTupleAssignmentBalance
if __name__ == '__main__':
    global rows,cols,n
    #rows=1000
    #cols=1000
    n=50
    fileName = 'test1.txt'

    infile = open(fileName, 'r+')
    content = infile.readlines()
    area = content[0].replace('\n', '')
    rows = int(area.split('x')[0])
    cols = int(area.split('x')[1])
    obstacles = []
    for i in content:
        if re.search('OBS', i) is not None:
            obstacles.append(i.replace('OBS ', '').replace('(', '').replace(')', '').replace('\n', '').split(', '))
        # print(i.replace('OBS ','').replace('(','').replace(')','').replace('\n','').split(', '))
    nets = {}
    for i in content:
        if re.search('net', i) is not None:
            nets[re.split('net', i)[1][0]] = []
            y = re.split('net', i)[1]
            val = re.split('[0-9]? ', y, 1)[1].split(')')
            for im in range(0, len(val)):
                val[im] = val[im].replace('(', '')
                if val[im] != ' ' and val[im] != '\n' and val[im] != '':
                    nets[re.split('net', i)[1][0]].append(val[im].split(','))

    print(nets)


    #print(route[0])
    for i in nets.keys():
        for cells in nets[i]:
            if cells==[' \n']:
                nets[i].remove(cells)
    global grid
    grid = []
    for x in range(n):
        grid.append([])
        for y in range(n):
            grid[x].append(0)

    global matrix
    matrix = []
    for x in range(n):
        matrix.append([])
        for y in range(n):
            matrix[x].append([])
            for z in range(2):
                matrix[x][y].append(0)

    for i in nets.keys():
        netsout= {}
        netsout[i]=[]
        for cells in range(0,len(nets[i])-1):
            #print(i)
            nets[i][cells][0]=int(nets[i][cells][0])
            nets[i][cells][1]=int(nets[i][cells][1])
            nets[i][cells][2]=int(nets[i][cells][2])

            nets[i][cells+1][0] = int(nets[i][cells+1][0])
            nets[i][cells+1][1] = int(nets[i][cells+1][1])
            nets[i][cells+1][2] = int(nets[i][cells+1][2])
            #minCost = fill(route, cells, res[x][y + 1], n)

            #print(cells)
            print(nets[i][cells], ":",nets[i][cells+1])

            route = []
            for x in range(n):
                route.append([])
                for y in range(n):
                    route[x].append([])
                    for z in range(2):
                        route[x][y].append(0)

            minCost = filling(route, nets[i][cells], nets[i][cells+1], n)
            print(minCost)

            for  r in range(0,n):
                for b in range(0,n):
                    if (route[r][b][0] == 0):
                        t = route[r][b][1]
                    elif (route[r][b][1] == 0):
                       t = route[r][b][0]
                    else:
                        t = min(route[r][b][0], route[r][b][1])

                    grid[r][b] = t

            BackPropagation(grid, matrix, nets[i][cells],nets[i][cells+1], n)

            for r in range(n):
               for b in range(n):
                   if matrix[r][b][0]:
                        netsout[i].append([1,r,b])
                        print('1', end=' ')

                   elif matrix[r][b][1]:
                       netsout[i].append([2, r, b])
                       print('1',end=' ')

                   else:print('0',end=' ')

               print()

        #for (int x = 0 x < res.size() x++) {
        #for (int y = 0 y < res[x].size() - 1 y++) {
       # vector < vector < vector < int >> > route(n, vector < vector < int >> (n, vector < int > (2, 0)))
        print(netsout)
       # minCost = fill(route, res[x][y], res[x][y + 1], n)

        # print(len(re.split('[0-9]? ',y,1)[1].split(')')))
        # for i in range(0,):
        #   print(y.split(')')[i].split('('))

        # print(y)
        # print(y.split(')')[0].split('('))
        # x=re.split("\(([A-Za-z0-9_]+)\)",y)
        # print(x)
        # print(re.split("net", i)[1][0])




    # writing to output file
    #  infile.truncate(0)
    # infile = open('output1.txt', 'w')
    # result=routing()
    # infile.writelines(result)
    # infile.close()
    #except Exception as e:
    #    print('Failed to perfrom function. Cause: ', str(e).replace("'", ''))

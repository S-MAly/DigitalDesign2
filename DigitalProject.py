import re


def filling(route, src, tar, rows,cols,layer):
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
        #print('i: ',i)

        if (l == tar[0] - 1 and x == tar[1] and y == tar[2]):
           # print('L,X,Y: ',L , X , Y)
            return i

        #if (l == 0):
        if (y + 1 >= 0 and y + 1 < cols and route[x][y + 1][l] == 0):
            L.append(l)
            X.append(x)
            Y.append(y + 1)
            route[x][y + 1][l] = i + 1

        if (y - 1 >= 0 and y - 1 < cols and route[x][y - 1][l] == 0):
            L.append(l)
            X.append(x)
            Y.append(y - 1)
            route[x][y - 1][l] = i + 1

        if (x - 1 >= 0 and x - 1 < rows and route[x - 1][y][l] == 0):
            L.append(l)
            X.append(x - 1)
            Y.append(y)
            route[x - 1][y][l] = i + 1

        if (x + 1 >= 0 and x + 1 < rows and route[x + 1][y][l] == 0):
            L.append(l)
            X.append(x + 1)
            Y.append(y)
            route[x + 1][y][l] = i + 1

        if ( l + 1 >= 0 and l+1 < layer and route[x][y][l + 1] == 0):
            L.append(l + 1)
            X.append(x)
            Y.append(y)
            route[x][y][l + 1] = i + 10


        if (l - 1 >= 0 and l - 1 < layer  and route[x][y][l - 1] == 0):
            L.append(l - 1)
            X.append(x)
            Y.append(y)
            route[x][y][l - 1] = i + 10

        L.pop(0)
        X.pop(0)  # eliminate the first position, as you have no more use for it
        Y.pop(0)

    return -1


def BackPropagation(grid, matrix, src,tar, rows,cols) :

    l = tar[0] - 1
    x = tar[1]
    y = tar[2]
    matrix[x][y][l] = 1
    while (not (l == src[0] - 1 and x == src[1] and y == src[2])):
       # print('x: ',x,'y: ', y)
      #  print(grid[x][y])
      #  print(grid[x][y][l])
        if (grid[x][y][l] == 1 ):break  # or grid[x][y]=='X'

        if ( y - 1 >= 0 and y - 1 < cols  and grid[x][y-1][l] != 'X' and grid[x][y][l] - grid[x][y - 1][l] == 1):

            y = y - 1
            matrix[x][y][l] = 1

        elif (y + 1 >= 0 and y + 1 < cols and grid[x][y + 1][l] != 'X' and grid[x][y][l] - grid[x][y + 1][l] == 1):

            y = y + 1
            matrix[x][y][l] = 1

        elif ( x-1 >= 0  and  x - 1 < rows and grid[x-1][y][l] != 'X'  and grid[x][y][l] - grid[x - 1][y][l] == 1):
            x = x - 1
            matrix[x][y][l] = 1

        elif (x + 1 >= 0 and x + 1 < rows and grid[x+1][y][l] != 'X' and grid[x][y][l]- grid[x + 1][y][l] == 1):

            x = x + 1
            matrix[x][y][l] = 1
        #else:

        elif (l - 1 >= 0 and l - 1 < layer and grid[x][y][l-1] != 'X' and grid[x][y][l] - grid[x][y][l-1] == 10):

            l = l-1

            matrix[x][y][l] = 1

            #x = x - 1

            #matrix[x][y][l] = 1


        elif (l + 1 >= 0 and l + 1 < layer  and grid[x][y][l+1] != 'X' and grid[x][y][l]- grid[x][y][l+1] == 10):

            l = l+1

            matrix[x][y][l] = 1

            #y = y - 1

           # matrix[x][y][l] = 1


       # elif (x + 1 >= 0 and x + 1 < rows and grid[x + 1][y] != 'X' and grid[x][y] - grid[x + 1][y] == 10):

        #    l = pow(l - 1, 2)

         #   matrix[x][y][l] = 1

          #  x = x + 1

           # matrix[x][y][l] = 1


      #  elif (y + 1 >= 0 and y + 1 < rows and grid[x][y + 1] != 'X' and grid[x][y] - grid[x][y + 1] == 10):

      #      l = pow(l - 1, 2)

      #     matrix[x][y][l] = 1

      #      y = y + 1

       #     matrix[x][y][l] = 1


# noinspection PyTupleAssignmentBalance
if __name__ == '__main__':
    global rows,cols,n
    #rows=1000
    #cols=1000
    n=50            # grid dimension
    layer=4         # of layers
    fileName = 'test1.txt'

    infile = open(fileName, 'r+')
    content = infile.readlines()
    infile.close()
    area = content[0].replace('\n', '')
    rows = int(area.split('x')[0])
    cols = int(area.split('x')[1])
    obstacles = []
    for i in content:
        if re.search('OBS', i) is not None:
            ok=i.replace('OBS ', '').replace('(', '').replace(')', '').replace('\n', '').split(', ')
            ok[0]=int(ok[0])
            ok[1]=int(ok[1])
            obstacles.append(ok)
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

   # print(nets)



    #print(route[0])
    for i in nets.keys():
        for cells in nets[i]:
            if cells==[' \n']:
                nets[i].remove(cells)
    global grid
    grid = []
    for x in range(rows):
        grid.append([])
        for y in range(cols):
            grid[x].append([])
            for l in range(layer):
                grid[x][y].append(0)

    global matrix
    matrix = []
    for x in range(rows):
        matrix.append([])
        for y in range(cols):
            matrix[x].append([])
            for z in range(layer):
                matrix[x][y].append(0)
    netsout = {}

    for i in nets.keys():
        netsout[i]=[]
        for cells in range(0,len(nets[i])-1):
            #print(i)
            nets[i][cells][0]=int(nets[i][cells][0])    # intailize  the source cell and change to int
            nets[i][cells][1]=int(nets[i][cells][1])
            nets[i][cells][2]=int(nets[i][cells][2])

            nets[i][cells+1][0] = int(nets[i][cells+1][0]) # intialize the target cell and change it to int
            nets[i][cells+1][1] = int(nets[i][cells+1][1])
            nets[i][cells+1][2] = int(nets[i][cells+1][2])
            #minCost = fill(route, cells, res[x][y + 1], n)

            #print(cells)
            #print(nets[i][cells], ":",nets[i][cells+1])

           # print('obstacles: ', obstacles)
            route = []                  # intailize a 3d array of 2 layers each layer is of size nxn
            for z in range(layer):
                for x in range(rows):
                    route.append([])
                    for y in range(cols):
                        route[x].append([])
                       # print([z,x,y])
                       # print(netsout[str(2 - 1)])

                        if [x,y] in obstacles:
                            route[x][y].append('X')
                        elif i != '1' :
                            flag=1
                            for m in range(1,int(i)):
                                if [z,x,y] in netsout[str(int(i)-1)]:
                                    print('x')
                                    route[x][y].append('X')
                                    flag=0
                                    break
                            if flag ==1:
                                route[x][y].append(0)
                        else:
                            route[x][y].append(0)


           # L=[]
            #X=[]
            #Y=[]
            minCost= filling(route, nets[i][cells], nets[i][cells+1], rows,cols,layer)

# printing the routes filled ; works correctly
            for l in range(layer):
                for x in range(rows):
                    for y in range(cols):
                            print(route[x][y][l],end=' ')
                    print()
                print()
           # for x in range(rows):
            #    for y in range(cols):
             #       print(route[x][y][1], end=' ')
              #  print()

###########################################################
           # for o in range(len(X)):
            #    print('X[o]:', X[o], 'Y[o]: ', Y[o])
             #   matrix[X[o]][Y[o]][L[o]]=1

          #  for x in range(rows):
           #     for y in range(cols):
            #        if matrix[x][y][0] or matrix[x][y][1]:
                    # matrix[x][y][0]=1
             #           print(1,end=' ')
              #      elif [x,y] in obstacles:
               #         print('X', end=' ')
                #    else:
                 #       print(0, end=' ')
               # print()
           # for x in range(rows):
              #  for y in range(cols):
               #     if route[x][y][0] or route[x][y][1]:
                #        matrix[x][y][0]=1
                 #   elif route[x][y][0] == 'X' or route[x][y][1]== 'X':
                  #      matrix[x][y][0] = 1
                   # for z in range(1):
                    #    print(route[x][y][0],end=' ')
                #print()
            if minCost == -1:
                print("Unsuccessful!")
                break
            print(minCost)
            #break
            #for r in range(0,rows):
             #   for b in range(0,cols):
                   # for z in range(layer):
              #      print('layer: ', layer)
               #     if (route[r][b][0] == 0 ):
                #        t = route[r][b][1]
                 #   elif (route[r][b][1] == 0 ):
                  #      t = route[r][b][0]
                  #  elif (route[r][b][1]=='X' or route[r][b][0]=='X'):
                   #     t='X'
                   # else:
                    #    t = min(route[r][b][0], route[r][b][1])

                   # grid[r][b] = t
            matrix = []
            for x in range(rows):
                matrix.append([])
                for y in range(cols):
                    matrix[x].append([])
                    for z in range(layer):
                        matrix[x][y].append(0)

            BackPropagation(route, matrix, nets[i][cells],nets[i][cells+1], rows , cols)

            #print('nets: ',int(nets[i][cells][1]))

# printing final grid and saving the cells in nets ; works correctly
            for l in range(layer):
                for r in range(rows):
                   for b in range(cols):
                       #for l in range(layer):
                           if r == int(nets[i][cells][1]) and int(nets[i][cells][2])==b and int(nets[i][cells][0])==l+1:
                               netsout[i].append([l, r, b])

                               print('S',end=' ')
                           elif r == int(nets[i][cells+1][1]) and int(nets[i][cells+1][2]) == b and int(nets[i][cells + 1][0])==l+1:
                               netsout[i].append([l, r, b])

                               print('T', end=' ')
                           elif matrix[r][b][l]==1:
                                netsout[i].append([l,r,b])
                                print('1', end=' ')
                           elif  [r,b] in obstacles:
                               print('X',end=' ')
                           else:print('0',end=' ')
                   print()

                print()
            for l in range(layer):
                for x in range(rows):
                    for y in range(cols):
                        if matrix[x][y][l]==1:
                            grid[x][y][l]=1


#################################################################################################
           # for r in range(rows):
            #    for b in range(cols):
             #           if r == int(nets[i][cells][1]) and int(nets[i][cells][2]) == b and int(nets[i][cells][0]) == 2:
              #              print('S', end=' ')
               #             netsout[i].append([2,r,b])

                #        elif r == int(nets[i][cells + 1][1]) and int(nets[i][cells + 1][2]) == b and int(nets[i][cells + 1][0]) == 2:
                 #           print('T', end=' ')
                  #          netsout[i].append([2,r,b])

                   #     elif matrix[r][b][1] == 1:
                    #        netsout[i].append([2, r, b])
                     #       print('1', end=' ')

                        # elif matrix[r][b][1]==1:
                        #    netsout[i].append([2, r, b])
                        #    print('1',end=' ')
                      #  elif [r, b] in obstacles:
                       #     print('X', end=' ')

                       # else:
                       #     print('0', end=' ')

               # print()

        #for (int x = 0 x < res.size() x++) {
        #for (int y = 0 y < res[x].size() - 1 y++) {
       # vector < vector < vector < int >> > route(n, vector < vector < int >> (n, vector < int > (2, 0)))

        for l in range(layer):
            for r in range(rows):
                for b in range(cols):
                    # for l in range(layer):
                    if r == int(nets[i][cells][1]) and int(nets[i][cells][2]) == b and int(nets[i][cells][0]) == l + 1:

                        print('S', end=' ')
                    elif r == int(nets[i][cells + 1][1]) and int(nets[i][cells + 1][2]) == b and int(
                            nets[i][cells + 1][0]) == l + 1:

                        print('T', end=' ')
                    elif grid[r][b][l] == 1:
                        print('1', end=' ')
                    elif [r, b] in obstacles:
                        print('X', end=' ')
                    else:
                        print('0', end=' ')
                print()
            print()

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

# writes back to file  the result; works correctly
    lines=[]
    for i in netsout.keys():
        line=''
        #print('net'+str(i),end=' ')
        line+='net'+str(i)+' '
        for cells in netsout[i]:
           line+= '('+str(cells[0]+1)+', '+str(cells[1])+', '+str(cells[2])+') '
        lines.append(line)
        lines.append('\n')
        print(line)
        #line=''

    outfile = open('output1.txt', 'w')
    outfile.writelines(lines)
    outfile.close()


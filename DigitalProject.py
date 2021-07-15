import re


def filling(route, src, tar, rows,cols,layer):
    i = 1
    route[src[1]][src[2]][src[0] - 1] = i
    L=[]  # the queues used to get the positions in the matrix
    X=[]
    Y=[]
    L.append(src[0] - 1)
    X.append(src[1])  # initialize the queues with the start position
    Y.append(src[2])

    while (len(X) > 0):  # while there are still positions in the queue

        l = L[0]  # set the current position
        x = X[0]
        y = Y[0]
        i = route[x][y][l]

        if (l == tar[0] - 1 and x == tar[1] and y == tar[2]):
            return i

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
            route[x-1][y][l] = i + 1

        if (x + 1 >= 0 and x + 1 < rows and route[x + 1][y][l] == 0):
            L.append(l)
            X.append(x + 1)
            Y.append(y)
            route[x+1][y][l] = i + 1

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

        if (grid[x][y][l] == 1 ):break

        if ( y - 1 >= 0 and y - 1 < cols  and grid[x][y-1][l] != 'X' and grid[x][y][l] - grid[x][y - 1][l] == 1):

            y = y - 1
            matrix[x][y][l] = 1

        elif ( y + 1 >= 0 and y + 1 < cols and grid[x][y + 1][l] != 'X' and grid[x][y][l] - grid[x][y + 1][l] == 1):

            y = y + 1
            matrix[x][y][l] = 1

        elif ( x-1 >= 0  and  x - 1 < rows and grid[x-1][y][l] != 'X'  and grid[x][y][l] - grid[x - 1][y][l] == 1):
            x = x - 1
            matrix[x][y][l] = 1

        elif (x + 1 >= 0 and x + 1 < rows and grid[x+1][y][l] != 'X' and grid[x][y][l]- grid[x + 1][y][l] == 1):

            x = x + 1
            matrix[x][y][l] = 1

        elif (l - 1 >= 0 and l - 1 < layer and grid[x][y][l-1] != 'X' and grid[x][y][l] - grid[x][y][l-1] == 10):

            l = l-1

            matrix[x][y][l] = 1

        elif (l + 1 >= 0 and l + 1 < layer  and grid[x][y][l+1] != 'X' and grid[x][y][l]- grid[x][y][l+1] == 10):

            l = l+1

            matrix[x][y][l] = 1




if __name__ == '__main__':
    global rows,cols


    layer=4        # of layers to be changed for different tests
    fileName = 'test1.txt'

    infile = open(fileName, 'r+')
    content = infile.readlines()
    infile.close()
    area = content[0].replace('\n', '')
    rows = int(area.split('x')[0])
    cols = int(area.split('x')[1])


    #Parsing the test file and putting the obstacle cells in a list as well as the cells of each net put in a dictionary

    obstacles = []
    for i in content:
        if re.search('OBS', i) is not None:
            ok=i.replace('OBS ', '').replace('(', '').replace(')', '').replace('\n', '').split(', ')
            ok[0]=int(ok[0])
            ok[1]=int(ok[1])
            obstacles.append(ok)
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

    # Making sure there is no new line character in the nets' cells list

    for i in nets.keys():
        for cells in nets[i]:
            if cells==[' \n']:
                nets[i].remove(cells)


    # declaring a grid  3d array to incoperate all solutions

    global grid
    grid = []
    for x in range(rows):
        grid.append([])
        for y in range(cols):
            grid[x].append([])
            for l in range(layer):
                grid[x][y].append(0)


    netsout = {}

    for i in nets.keys():
        netsout[i]=[]
        for cells in range(0,len(nets[i])-1):
            nets[i][cells][0]=int(nets[i][cells][0])        # intailize  the source cell and change to int
            nets[i][cells][1]=int(nets[i][cells][1])
            nets[i][cells][2]=int(nets[i][cells][2])

            nets[i][cells+1][0] = int(nets[i][cells+1][0])  # intialize the target cell and change it to int
            nets[i][cells+1][1] = int(nets[i][cells+1][1])
            nets[i][cells+1][2] = int(nets[i][cells+1][2])



            route = []                  # intailize a 3d array route  of size layer x rows x cols
            for z in range(layer):
                for x in range(rows):
                    route.append([])
                    for y in range(cols):
                        route[x].append([])

         # Add obstacles in the route 3d array as well as the net cells  that can't be passed

                        if [x,y] in obstacles:
                            route[x][y].append('X')
                        elif i != '1' :
                            flag=1
                            for m in range(1,int(i)):
                                if [z,x,y] in netsout[str(int(i)-1)]:
                                    route[x][y].append('X')
                                    flag=0
                                    break
                            if flag ==1:
                                route[x][y].append(0)
                        else:
                            route[x][y].append(0)

            # Call the filling function that fills the route array with the cost of moving to each cell and return the minimum cost

            minCost= filling(route, nets[i][cells], nets[i][cells+1], rows,cols,layer)



            # Check Minimum cost if -1 than no path was found
            if minCost == -1:
                print("Unsuccessful!")
                break


            # Intialize a 3d matrix to back track from the route
            global matrix
            matrix = []
            for x in range(rows):
                matrix.append([])
                for y in range(cols):
                    matrix[x].append([])
                    for z in range(layer):
                        matrix[x][y].append(0)

            BackPropagation(route, matrix, nets[i][cells],nets[i][cells+1], rows , cols)


#  saving the cells in nets list; works correctly
            for l in range(layer):
                for r in range(rows):
                   for b in range(cols):
                           if r == int(nets[i][cells][1]) and int(nets[i][cells][2])==b and int(nets[i][cells][0])==l+1:
                               netsout[i].append([l, r, b])
                           elif r == int(nets[i][cells+1][1]) and int(nets[i][cells+1][2]) == b and int(nets[i][cells + 1][0])==l+1:
                               netsout[i].append([l, r, b])
                           elif matrix[r][b][l]==1:
                                netsout[i].append([l,r,b])



            for l in range(layer):
                for x in range(rows):
                    for y in range(cols):
                        if matrix[x][y][l]==1:
                            grid[x][y][l]=1


# Print final grid

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




# writes back to file  the result; works correctly
    lines=[]
    for i in netsout.keys():
        line=''
        line+='net'+str(i)+' '
        for cells in netsout[i]:
           line+= '('+str(cells[0]+1)+', '+str(cells[1])+', '+str(cells[2])+') '
        lines.append(line)
        lines.append('\n')
        print(line)

    outfile = open('output1.txt', 'w')
    outfile.writelines(lines)
    outfile.close()


#演算法分析機側
#學號 : 10724128
#姓名 : 吳宇哲
#中原大學資訊工程系
import time
class Hamiltonian_Cycle :
 def __init__(self,arr,node_num,line_num):
    self.path = []
    self.graph = arr
    self.node_num = node_num
    self.line_num = line_num

 def hamCycle(self):
    node_path= [] #save used node
    for i in range(node_num) : #check past
        node_path.append(False)
        self.path.append(0)
    if self.hamPath(0,node_path) == False :
       print("Solution does not exist")
       return False
    self.printResult()
    print("done")
    return True

        
 def hamPath(self,num, node_path) :
    if num == (self.node_num) : #回到原點
       for i in range(self.line_num) :
          if self.graph[i][0] == self.path[num-1] :
            if self.graph[i][1]== self.path[0] :
               return True
          if self.graph[i][1] == self.path[num-1] :
            if self.graph[i][0]== self.path[0] :
               return True
       return False
               
    for i in range(self.node_num) :
       if num == 0 :
          for j in range(node_num) :
             node_path[j] = False
             self.path[j] = 0
          self.path[num] = i+1
          node_path[i] = True
          if i == 0 :
           if self.hamPath(num+1,node_path) == True :
            return True

       for j in range(self.line_num) : 
               if ((self.graph[j][0] == self.path[num-1])&(self.graph[j][1] == (i+1))) :
                  if ( node_path[i] == False) :
                     node_path1 = []
                     node_path1 = node_path[:]
                     self.path[num] = self.graph[j][1]
                     node_path[self.graph[j][1]-1] = True
                     if self.hamPath(num+1,node_path) == True :
                        
                        return True
                     else :
                        node_path = node_path1[:]
                        node_path[self.graph[j][1]-1] = False
                        self.path[num] = 0
               elif ((self.graph[j][1] == self.path[num-1])&(self.graph[j][0] == (i+1))) :
                  if ( node_path[i] == False) :
                     node_path1 = []
                     node_path1 = node_path[:]
                     self.path[num] = self.graph[j][0]
                     node_path[self.graph[j][0]-1] = True
                     if self.hamPath(num+1,node_path) == True :
                        
                        return True
                     else :
                        node_path = node_path1[:]
                        node_path[self.graph[j][0]-1] = False
                        self.path[num] = 0

                        
    return False # not have node
   # print(arr)

 def printResult(self) :
      self.path.append(self.path[0])
      print(self.path)


print("漢密爾頓迴圈(Hamiltonian Cycle)")
node_num, line_num = map( int , input("請輸入節點數量、邊的數量 : ").split())
arr = []
input_arr = []
haveError = False 
while ( len(input_arr) != 2 ) :
    input_arr = input().split()
while (int(input_arr[0]) != 0) & (int(input_arr[1]) != 0): #input graph
    int_list = list(map(int, input_arr))
    arr.append(int_list)
    #print(arr)
    input_arr = input().split()
    while ( len(input_arr) != 2 ) :
        print("error 請重新輸入")
        input_arr = input().split()
if len(arr) != line_num : # check line error
    print("line error!! ")
    haveError = True
if haveError == False : # check node error
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
          if int(arr[i][j]) > node_num :
            print("node error")
            haveError = True
            break
        if haveError:
            break
if haveError == False : # run
    r1 = Hamiltonian_Cycle(arr,node_num,line_num)
    start_time = time.time()
    r1.hamCycle()
    total_time = time.time() - start_time
    print ( "run time : ",total_time )

"""
8 12
1 2
1 3
1 5
2 4
2 6
3 4
3 7
4 8
5 6
5 7
6 8
7 8
0 0
1 2 4 3 7 8 6 5 1
5 
5
1 2
2 3
3 4
4 5
1 5
0 0
4
3
1 2
2 3
3 4
0 0
"""
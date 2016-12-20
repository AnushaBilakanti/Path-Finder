'''
Created on September 21, 2016
@author: Anusha Bilakanti
'''

from collections import defaultdict
import collections
import sys

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class Stack:
	def __init__(self):
	    self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
	    self.items.insert(0,item)
	def pop(self):
		return self.items.pop(0)

class DictQueue:
    	
	def __init__(self):
        	self.items = [] 
		self.dict={}

    	def is_empty(self):
        	return not self.items

    	def insert(self,node,parent,path_cost):
		if(parent==-1):
			self.items.append(node)
        		self.dict[node]=0
		else: 
			self.items.append(node)
			self.dict[node]=self.dict[parent]+int(path_cost)

    	def remove(self,node):
		for i in self.items:
			if i==node:
				list_index=self.items.index(i)
				del self.items[list_index] 

	def size(self):
		return len(self.items)
	
	def path_cost(self,node):
		return self.dict[node]

class DictQueue_A:
    	
	def __init__(self):
        	self.items = [] 
		self.dict={} 

    	def is_empty(self):
        	return not self.items

    	def insert(self,node,parent,path_cost):
		if(parent==-1):
			self.items.append(node)
        		self.dict[node]=path_cost
		else: 
			self.items.append(node)
			self.dict[node]=int(path_cost)

    	def remove(self,node):
		for i in self.items:
			if i==node:
				list_index=self.items.index(i)
				del self.items[list_index] 

	def size(self):
		return len(self.items)
	
	def path_cost(self,node):
		return self.dict[node]


class Vertex:
	
	def __init__(self,key):
        	self.id = key
        	self.connectedTo = collections.OrderedDict()

	def addNeighbor(self,nbr,weight):
        	self.connectedTo[nbr] = weight

	def getConnections(self):
        	return self.connectedTo.keys()
    
	def getValues(self):
        	return self.connectedTo.values()

	def getId(self):
        	return self.id

	def getWeight(self,nbr):
        	return self.connectedTo[nbr]
	
	def __str__(self):
        	return str(self.id)



class Graph:
	
	def __init__(self):
        	self.vertList = collections.OrderedDict()
        	self.numVertices = 0

	def addVertex(self,key):
		if key not in self.vertList:
			self.numVertices = self.numVertices + 1
			newVertex = Vertex(key)
			self.vertList[key] = newVertex
			return newVertex

    	def getVertex(self,n):   
        	if n in self.vertList:
            		return self.vertList[n]
        	else:
            		return None

    	def __contains__(self,n):
        	return n in self.vertList

    	def addEdge(self,f,t,cost):
        	if f not in self.vertList:
            		nv = self.addVertex(f)
        	if t not in self.vertList:
            		nv = self.addVertex(t)
        	self.vertList[f].addNeighbor(self.vertList[t], cost)
 

    	def getVertices(self):
        	return self.vertList.keys()

    	def __iter__(self):
        	return iter(self.vertList.values())

'''**************************************************************************************************'''
def bfs(g,start,dest):
	count=0;
    	sequence=[]
	parent_dict = collections.OrderedDict()
	out_file=open("output.txt","w")
    	if start == dest: 
        	#print start," ",0
		out_file.write(start.id+" "+str(0)+"\n")
        	return
    	vertQueue = Queue()
    	vertQueue.enqueue(start)
    	explored_bfs=[]
    	count=0
    	while vertQueue.size() > 0:
        	currentVert = vertQueue.dequeue()
		if currentVert.id==dest.id:
			temp=currentVert.id
			while temp!=start.id:
				sequence.append(parent_dict[temp][0])
				temp=parent_dict[temp][0]
			sequence.reverse()
			for i in sequence:
				out_file.write(i+" "+str(count)+"\n")
				#print i+" "+str(count)
				count=count+1
			#print dest.id+" "+str(count)
			out_file.write(dest.id+" "+str(count)+"\n")
			out_file.close()
			return 
		explored_bfs.append(currentVert.id)
        	for x in currentVert.connectedTo.keys():
			parent_dict.setdefault(x.id,[]).append(currentVert.id)
            		if x.id not in explored_bfs:
				explored_bfs.append(x.id)
                		vertQueue.enqueue(x)

'''**************************************************************************************************'''
def dfs(g,start,dest):
	count=0; 
    	sequence=[]
	parent_dict = collections.OrderedDict()
	out_file=open("output.txt","w")
    	if start == dest: 
        	#print start," ",0
		out_file.write(start.id+" "+str(0)+"\n")
        	return
    	vertStack = Stack()
    	vertStack.push(start)
	temp_child=[]
    	explored_dfs=[]
    	explored_dfs.append(start.id)
    	while not(vertStack.isEmpty()):
        	currentVert = vertStack.pop() 
		if currentVert.id == dest.id:
				temp=currentVert.id
				while temp!=start.id:
					sequence.append(parent_dict[temp][0])
					temp=parent_dict[temp][0]
				sequence.reverse()
				for i in sequence:
					out_file.write(i+" "+str(count)+"\n")
					#print i+" "+str(count)
					count=count+1
				#print dest.id+" "+str(count)
				out_file.write(dest.id+" "+str(count)+"\n")
				out_file.close()
				return 
		
		for x in currentVert.connectedTo.keys():
			if x.id not in explored_dfs:		
				explored_dfs.append(x.id)
				temp_child.append(x)
				parent_dict.setdefault(x.id,[]).append(currentVert.id)
		temp_child.reverse()
		for i in temp_child:
			vertStack.push(i)
		del temp_child[:] 
	
'''**************************************************************************************************'''
def ucs(g,start,dest):
	count=0;
    	sequence=[]
	parent_dict = {}
	vertPQ = DictQueue()
	explored_ucs=[]
	out_file=open("output.txt","w")
    	if start == dest:
        	#print start," ",0
		out_file.write(start.id+" "+str(0)+"\n")
        	return
    	vertPQ.insert(start,-1,0)
	count = 0
	while vertPQ.size()>0:
		currentVert=vertPQ.items[0]
		vertPQ.remove(currentVert)
		if currentVert.id==dest.id:
			temp=currentVert.id
			while temp!=start.id:
				sequence.append(parent_dict[temp])
				temp=parent_dict[temp]
			sequence.reverse()
			for i in sequence:
				node=g.getVertex(i)
				out_file.write(i+" "+str(vertPQ.dict[node])+"\n")
				#print i+" "+str(vertPQ.dict[node])
			out_file.write(dest.id+" "+str(vertPQ.dict[dest])+"\n")
			out_file.close()
			#print dest.id+" "+str(vertPQ.dict[dest])
			return
		for x in currentVert.connectedTo.keys():
			temp=x
			dist=currentVert.getWeight(x)
			if x not in vertPQ.items and x not in explored_ucs:
				vertPQ.insert(x,currentVert,dist)
				parent_dict[x.id]=currentVert.id
				
			elif x in vertPQ.items:
				parent_cost=vertPQ.path_cost(currentVert)
				child_cost_queue=vertPQ.path_cost(x)
				child_cost=parent_cost+int(dist)
				if child_cost<child_cost_queue:
					parent_dict[x.id]=currentVert.id
					vertPQ.remove(temp)
					vertPQ.insert(temp,currentVert,dist)

			elif x in explored_ucs:
				parent_cost=vertPQ.path_cost(currentVert)
				child_cost=parent_cost+int(dist)
				child_cost_queue=vertPQ.path_cost(x)
				if child_cost<child_cost_queue:
					explored_ucs.remove(temp)
					vertPQ.insert(x,currentVert,dist)
					parent_dict[x.id]=currentVert.id
		explored_ucs.append(currentVert)
		vertPQ.items = sorted(vertPQ.items, key=vertPQ.dict.__getitem__)
'''**************************************************************************************************'''
def A(g,start,dest,sun_routes):
	count=0; 
    	sequence=[]
	parent_dict = {}
	vertPQ = DictQueue_A()
	explored_a=[]
	out_file=open("output.txt","w")
    	if start == dest:
        	#print start," ",sun_routes[start]
		out_file.write(start.id+" "+str(0)+"\n")
        	return
    	vertPQ.insert(start,-1,sun_routes[start])
	while vertPQ.size()>0:
		currentVert=vertPQ.items[0]
		vertPQ.remove(currentVert)
		if currentVert.id==dest.id:
			temp=currentVert.id
			while temp!=start.id:
				sequence.append(parent_dict[temp])
				temp=parent_dict[temp]
			sequence.reverse()
			for i in sequence:
				node=g.getVertex(i)
				#print i+" "+str(int(vertPQ.dict[node])-int(sun_routes[node]))
				if i == start.id:
					out_file.write(start.id+" "+str(0)+"\n")
				else:
					out_file.write(i+" "+str(int(vertPQ.dict[node])-int(sun_routes[node]))+"\n")
			out_file.write(dest.id+" "+str(int(vertPQ.dict[dest])-int(sun_routes[dest]))+"\n")
			out_file.close()
			#print dest.id+" "+str(vertPQ.dict[dest]-int(sun_routes[dest]))
			return
		for x in currentVert.connectedTo.keys():
			temp=x
			parent_cost=int(vertPQ.path_cost(currentVert))-int(sun_routes[currentVert]) 
			dist=int(currentVert.getWeight(x))+int(sun_routes[x])+int(parent_cost)
			if x not in vertPQ.items and x not in explored_a:
				vertPQ.insert(x,currentVert,dist)
				parent_dict[x.id]=currentVert.id

			elif x in vertPQ.items:
				parent_cost=vertPQ.path_cost(currentVert)
				child_cost_queue=vertPQ.path_cost(x)
				child_cost=dist
				temp_path=vertPQ.path_cost(x)
				if child_cost<child_cost_queue:
					parent_dict[x.id]=currentVert.id
					vertPQ.remove(temp)
					vertPQ.insert(temp,currentVert,dist)
			
			elif x in explored_a:
				parent_cost=vertPQ.path_cost(currentVert)
				child_cost=dist
				child_cost_queue=vertPQ.path_cost(x)
				if child_cost<child_cost_queue:
					explored_a.remove(temp)
					vertPQ.insert(x,currentVert,dist)
					parent_dict[x.id]=currentVert.id
		
		explored_a.append(currentVert)
		vertPQ.items = sorted(vertPQ.items, key=vertPQ.dict.__getitem__)
'''**************************************************************************************************'''
obj=open('input.txt','r')
algo=obj.readline().strip()
start=obj.readline().strip()
dest=obj.readline().strip()
no_of_routes=obj.readline().strip()

g = Graph() 
i=1
while(i<=int(no_of_routes)):
	route=obj.readline()
	start_1,end_1,cost = route.strip().split(" ")
    	g.addVertex(start_1)
    	g.addVertex(end_1)
    	g.addEdge(start_1,end_1,cost)
    	i=i+1

start_vertex = g.getVertex(start)
dest_vertex = g.getVertex(dest)

sun_routes = collections.OrderedDict()
no_of_sun_traffic_lines=obj.readline().strip()
j=1
while(j<=int(no_of_sun_traffic_lines)):
	temp=obj.readline()
	node,cost1=temp.strip().split(" ")
	temp_node=g.getVertex(node)
	sun_routes[temp_node]=cost1
	j=j+1
    
if algo in ['BFS','bfs']:
	bfs(g,start_vertex,dest_vertex)
elif algo in ['DFS','dfs']:
	dfs(g,start_vertex,dest_vertex)
elif algo in ['UCS','ucs']:
	ucs(g,start_vertex,dest_vertex) 
elif algo in ['A*','a*']:	
	A(g,start_vertex,dest_vertex,sun_routes)
else:
	sys.exit(0)       

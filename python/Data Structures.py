#Data structures allows programmers to store, process and manipulate data for efficient access and modification.

#Python has 4 built-in Data Structures.
#They are third party or user-defined data structures as well, ie in the collections module that serves
#more specialized use-cases.

#The 4 built-in Data structures in python:

  #1. List (Similar to array in other languages).  <-- CHECK: Lists
      #Lists are mutable, meaning you can modify them.
      #Lists are used to store data in a sequencial manner, they can have heterogenous data types in them as well, and they are mutable

      #The difference between array and list is: Arrays store homogenous data types, unlike lists.

  #2. Tuples.   <-- CHECK: Tuples
      #Tuples are immutable, meaning they cannot be modified once declared on memory.
      #Tuples are similar to lists, except that they are not mutable. They are also faster than lists.

  #3. Set.  <-- CHECK: Sets
      #Sets are data structures that contain unique elements.
      #Sets are unordered collections of unique elements. They are mutable.

  #4. Dictionary.  <-- CHECK: Dictionary
      #Contain key/value pairs and are mutable


#Other user-defined data structure comprises of:
 #Stack, Queue, Tree, LinkedList, Graph, HashMap

 #1. Stack:

     #Stacks are made from arrays (learn import arrays in python), or lists in python.
     #Stacks follow the LIFO (Last In First Out) principle.
     #They have a pointer called TOP which is to track the top of the element.

     #Adding element to a stack is known as PUSHING, removing element from a stack is known as POPPING

 #2. Queues:

     #Queues are made from arrays (learn import arrays in python), or lists in python, or 'from collections import deque'
     #Queues follow the FIFO (First Input First Output) principle.
     #Operations can be performed from the front or back of the queue.
     #They have 2 pointers known as HEAD and TAIL, which is to track the topmost(first) element and last element respectively.

     #Adding element to a queue is known as EN-QUEUE, removing element from a queue is known as DE-QUEUE.

 #3. Trees:

     #Trees are helpful to define hierarchy.
     #The tree starts with the root node and goes further down.
     #The last nodes are known as the child nodes.

 #4. LinkedList:

     #LinkedLists are made up of two fields, the data and the next field.
     #The data field holds data and the next field points to the next node.
     #The first node is known as the head.

 #5. Graphs:

     #Graphs are used to show vertices and edges
     #Graphs closely represent real world geographical locations.
     #They have vertices and edges
     #They can be used to find shortest path and help in finding least cost

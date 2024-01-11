from matplotlib import pyplot as plt
from  matplotlib import style
style.use('ggplot')

#Matplotlib is a python package used for 2D graphics

#Plot graph
x = [1,2,3,4,5]
y = [10,20,30,20,10]
plt.plot(x,y)
plt.show()


#Add label and title to graph
x = [1,2,3,4,5]
y = [10,20,30,20,10]
plt.plot(x,y)
plt.title('GRAPH TITLE')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.grid(False)
plt.show()


#Add style to graph
#from matplotlib import style

style.use("ggplot")

x = [1,2,3,4,5]
y = [10,20,30,20,10]
a = [1,2,3,4,5]
b = [1,3,5,7,9]

plt.plot(x,y,'g',label="First Line", linewidth=5)
plt.plot(a,b,'y', label="Second Line", linewidth=2)
plt.legend()
plt.title('GRAPH TITLE')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.grid(True,color='#FF0000')
plt.show()


#PLOT A BAR GRAPH
x = [1,3,5,7,9]
y = [10,20,30,20,10]
a = [2,4,6,8,10]
b = [1,3,5,7,9]

plt.bar(x,y, label='First bar graph')
plt.bar(a,b, label='Second bar graph', color='green')
plt.legend()
plt.title('BAR GRAPH TITLE')
plt.xlabel('HORIZONTAL AXIS')
plt.ylabel('BAR HEIGHT')
plt.show()

#SCATTER PLOT
x = [1,3,5,7,9]
y = [10,20,30,20,10]

plt.scatter(x,y, label="Scatter plot", color='blue')
plt.legend()
plt.title('SCATTER PLOT')
plt.xlabel('HORIZONTAL AXIS')
plt.ylabel('BAR HEIGHT')
plt.show()

#PIE CHART
ITEMS = ["Orange", "Fish", "Mango", 'Garlic', "Yam"]
VALUES = [3,8,2,4,1]

plt.pie(VALUES,
        labels=ITEMS,
        startangle=90,
        shadow=True)
plt.title("PIE CHART")
plt.show()

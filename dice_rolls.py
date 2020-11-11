import numpy.random as rand
import matplotlib.pyplot as plt
import pandas as pd

n1 = 100000
n2 = 100

a1 = []

for i in range(n1):
    a1.append(rand.randint(1,7))
    
a2 = []

for i in range(n2):
    a2.append(rand.randint(1,7))
    
b1 = []

for i in range(1, 7):
    b1.append(a1.count(i)/n1*100)
    
b2 = []

for i in range(1, 7):
    b2.append(a2.count(i)/n2*100)
    
x = range(1,7)

df = pd.DataFrame({'x': x , 'y_1': b1, 'y_2': b2})
    
plt.plot('x', 'y_1', data=df , color='skyblue', linewidth=2)

plt.plot('x', 'y_2', data=df , color='olive', linewidth=2)
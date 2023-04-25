import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
y=np.sin(x)
y2=np.cos(x)
y3=x**2
fig=plt.figure(figsize=(20,10))
a =fig.add_subplot(2,3,3)
a.plot(x,y)
a.plot(x,y2)
a.set_xlabel('sin')
a.set_ylabel('cos')
a.set_title('line plot')

ax2=fig.add_subplot(2,3,2)
ax2.scatter(x,y,label='sin(x)')
ax2.scatter(x,y2,label='cos(x)')
ax2.set_title('scatter plot')

ax2.set_xlabel('sin')
ax2.set_ylabel('cos')

data = np.random.randn(100)
ax4=fig.add_subplot(2,3,1)
ax4.hist(data,bins=30)

ax4.set_xlabel('sin')
ax4.set_ylabel('cos')

ax4.set_title('histogram')
a5=fig.add_subplot(2,3,6)
a5.boxplot(data)
a5.set_title('boxplot')
plt.show()


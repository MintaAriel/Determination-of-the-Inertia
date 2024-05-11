
import numpy as np
import matplotlib.pyplot as plt

class m_inertia:
    def __init__(self, aceleration, torque, radius):
            self.aceleration = aceleration
            self.torque = torque
            self.radius = radius
    
    def inertia(self):
        inertia = np.polyfit(self.aceleration, self.torque, 1)
        myline = np.linspace(1, 12, 100)
        mymodel = np.poly1d(inertia)
        plt.text(10, 9.5*inertia[0], f'$r = {self.radius}$', fontsize = 10)
        plt.plot(myline, mymodel(myline),)
        plt.scatter(self.aceleration,self.torque, 
                    s=30, marker='o', color = 'red' )
        print(f' y = {inertia[0]:.4f}x + {inertia[1]:.2e}')
        
print('Where y is the Torque and X the angular aceleration')    
 
I1 = m_inertia([2.1,4.14,4.97,5.79,6.19], 
               [0.0184,0.0355,0.0425,0.0494,0.0526], 13)

I2 = m_inertia([2.84,3.97,6.68],[0.0184,0.02545,0.0422], 11)

I3 = m_inertia([5,6.91,11.52],[0.0183,0.0253,0.0417], 8)
 
I1.inertia()
I2.inertia()
I3.inertia()

plt.title('Зависимость угловое ускорение от момента силы')
plt.xlabel(' Угловое ускорение (рад/с2)')
plt.ylabel('Момент силы (Н*м)')
plt.grid()
plt.savefig('my_plot2.png', dpi=300)  
 

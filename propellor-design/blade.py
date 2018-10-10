
from airfoils import ellipse, airfoil
import bezier
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def zSpace(numPoints,numProfiles,length,lf=False):
    """
    Creates z-space for the wing profile [needs work]
    """
    if lf==True:
        z=np.zeros(2*numPoints-2)
        for k in range(1,numProfiles+3):
            z=np.concatenate( [ z, np.full( (2*numPoints-2,), (length/(numProfiles+2))*k ) ] )
    elif lf==False:
        z=[0]
        for k in range(1,numProfiles+3):
            z.append( (length/((numProfiles+2))*k ) )

    return z

def attackAngles(numProfiles,angle0,angle1):
    N=numProfiles+2
    v = (angle0 - angle1)/float(N)
    thetas=[angle0]
    for k in range(1,N+1):
        thetas.append( thetas[k-1]-v)
    return thetas

class Wing:


###class variables:
#why arent these working?
    # numProfiles=6
    # numPoints=150

###List methods

    def __init__(self,length,theta0,theta1):
        """
        initializes Airfoil with the necessary parameters, length, largest
        camber length 1st angle of attack, 2nd angle of attack
        """
        self.length, self.theta0, self.theta1 = length, theta0, theta1

    # def build_wing_generic_single(self):
    #     numProfiles=6
    #     numPoints=150
    #
    #     l=self.length
    #     cambers=[l*0.08,l*0.08,l*0.1, l*0.14, l*0.16, l*0.14,l*0.1,l*0.06,l*0.01]
    #     z=zSpace(numPoints,numProfiles,l)
    #     thetas=attackAngles(numProfiles,self.theta0,self.theta1)
    #
    #     e1,e2=ellipse(2*numPoints-2,cambers[0],thetas[0]), ellipse(2*numPoints-2,cambers[1],thetas[1])
    #     x,y = np.concatenate([e1[0],e2[0]]),np.concatenate([e1[1],e2[1]])
    #
    #     for i in range(2,numProfiles+2):
    #         P=airfoil(numPoints,RT=15,camber=cambers[i],theta=thetas[i])
    #         x,y=np.concatenate([x,P[0]]),np.concatenate([x,P[1]])
    #
    #
    #     e3=ellipse(2*numPoints-2,cambers[8],thetas[8])
    #     x,y=np.concatenate([x,e3[0]]),np.concatenate([x,e3[1]])
    #     self.wing_profile=[x,y,z]
    #     return self.wing_profile

    def build_wing_generic_multiple(self):
        numProfiles=6
        numPoints=150

        l=self.length
        cambers=[l*0.08,l*0.08,l*0.1, l*0.14, l*0.16, l*0.14,l*0.1,l*0.06,l*0.01]
        z=zSpace(numPoints,numProfiles,l)
        thetas=attackAngles(numProfiles,self.theta0,self.theta1)

        W=[ellipse(2*numPoints-2,cambers[0],thetas[0],z[0]), ellipse(2*numPoints-2,cambers[1],thetas[1],z[1])]
        for i in range(2,numProfiles+2):
            W.append( airfoil(numPoints,15,cambers[i],thetas[i],z[i]) )
        W.append(ellipse(2*numPoints-2,cambers[8],thetas[8],z[8]))

        self.wing_profile=W

        print(len(W))

        return self.wing_profile


    def export_profile_as_txt(self, name = 'airfoil'):
        """
        This method exports the wing profile as a .txt file in 3 rows ordered
        x y z.
        """
        iter=0
        for h in self.wing_profile:
            f = open(name + str(iter) + '.txt','w')
            x,y,z = h[0],h[1],h[2]
            for i in range(len(x)):
                f.write( str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) )
                f.write('\n')
            f.close()
            iter=iter+1
        return print(name + ".txt file generated")

    def plot_profile(self):
        """
        This plots the 3d airfoil profile using matplotlib
        """
        wp=self.wing_profile

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        maxX,maxY,=0,0
        minX,minY,=0,0
        for i in range(len(wp)):
            x,y=wp[i][0],wp[i][1]
            ax.plot(x,y, zs=wp[i][2])
            if max(x)>maxX:
                maxX=max(x)
            if max(y)>maxY:
                maxY=max(y)
            if min(x)<minX:
                minX=min(x)
            if min(y)<minY:
                minY=min(y)
        #
        limMax,limMin=maxX+maxX*0.1,minX-minX*0.1
        ax.set_xlim3d(limMin,limMax), ax.set_ylim3d(limMin,limMax), ax.set_zlim3d(0,self.length)
        plt.show()

"""
Examine code:
"""

w = Wing(4,15,1)
print(w)
w.build_wing_generic_multiple()
w.plot_profile()
#w.export_profile_as_txt()

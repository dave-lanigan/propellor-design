
"""
This library

"""
import bezier
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
We want to create a library that make an airfoil class with attributes

thetaBase=thetaEnd

--> make option for inches or metric
"""
def airfoil(numPoints,RT,camber,theta,zd):

    N=150
    RT_rad=math.radians(RT)
    theta_rad=math.radians(theta)
    #Ref Dims
    Rc1_endpx,Rc1_endpy=camber*math.cos(RT_rad),camber*math.sin(RT_rad)

    Rc1_p3x = Rc1_endpx*(1-0.02) #+ offset
    Rc1_p3y = Rc1_endpy*(1+0.3) #+ offset
    Rc1_p2x = Rc1_p3x*0.8 #+ offset
    Rc1_p2y = Rc1_p3y*1.8 #+ offset

    Rc2_p3x = Rc1_endpx*(1+0.03) #+ offset
    Rc2_p3y = Rc1_endpy*(1-0.35) #+ offset
    Rc2_p2x = Rc1_p3x*0.9 #+ offset
    Rc2_p2y = Rc1_p3y*0.1 #+ offset

    #Actual
    c1_endpx,c1_endpy=camber*math.cos(theta_rad),camber*math.sin(theta_rad)

    c1_p3x = c1_endpx - Rc1_endpx*(0.02)
    c1_p3y = c1_endpy + Rc1_endpy*(0.3)
    c1_p2x = c1_p3x - Rc1_p3x*0.2
    c1_p2y = c1_p3y + Rc1_p3y*0.8

    c2_p3x = c1_endpx + Rc1_endpx*(0.03)
    c2_p3y = c1_endpy - Rc1_endpy*(0.35)
    c2_p2x = c1_p3x - Rc1_p3x*0.1
    c2_p2y = c1_p3y - Rc1_p3y*0.9


    nodes1 = np.asfortranarray([[0.0, c1_p2x, c1_p3x , c1_endpx],[0.0, c1_p2y, c1_p3y, c1_endpy],])
    nodes2 = np.asfortranarray([[0.0, c2_p2x, c2_p3x , c1_endpx],[0.0, c2_p2y, c2_p3y, c1_endpy],])

    top,bottom= bezier.Curve(nodes1, degree=3), bezier.Curve(nodes2, degree=3)
    s_vals = np.linspace(0,1,N)
    top,bottom = top.evaluate_multi(s_vals), bottom.evaluate_multi(s_vals)

    x=np.concatenate( [ top[0],bottom[0][1:len(bottom[0])-1][::-1] ] )
    y=np.concatenate( [ top[1],bottom[1][1:len(bottom[1])-1][::-1] ] )

    #C=[np.array(x) - max(x)/2, np.array(y) - max(y)/2]

    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # # ax.plot( C[0],C[1])
    # # #ax.plot( [0.2,3,4], [2,3,4], [1,5,6])
    # # plt.show()

    return [np.array(x)-max(x)/2,np.array(y)-max(y)/2,np.full((2*numPoints-2,),zd)]

def ellipse(numPoints,camber, aoa,zd):
    """
    Create an ellipse in xyz space based on given camber z coord and angle
    of attack (aoa)
    """
    a,b,theta0,N=camber/2,camber/4,math.radians(aoa),numPoints

    #formula for rotated ellipse
    x=[a*math.cos(t)*math.cos(theta0)-b*math.sin(t)*math.sin(theta0) for t in np.linspace(0,2*3.14,N)]
    y=[a*math.cos(t)*math.sin(theta0)+b*math.sin(t)*math.cos(theta0) for t in np.linspace(0,2*3.14,N)]

    return np.array([x,y,np.full( (numPoints,),zd)] )

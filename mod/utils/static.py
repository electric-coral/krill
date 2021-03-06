"""
utilities for the main krill script
includes:
getting jacobi integral at a specified libration point

jacobi integral at L1 is 3.1885282305574663
jacobi integral at L2 is 3.1730187952481117
jacobi integral at L3 is 3.01215069525063
jacobi integral at L4 is 2.987993719716
L4 and L5 energy is same due to symmetry
J > J1 = 3.2
J2 < J < J1 = 3.180
J3 < J < J2 = 3.10
J4 < J < J3 = 2.99
"""

import mod.consts as consts

def get_J_point(point):
    """
    gets the jacobi integral at a specified libration point

    args:
        - point: string (L1-L5)
    
    returns:
        - J: jacobi integral
    """

    if point == "L1":
        rx = 1-(consts.MU/3)**(1/3)
        ry = 0
    elif point == "L2":
        rx = (1-consts.MU)*(1+(consts.MU/3)**(1/3))
        ry = 0
    elif point == "L3":
        rx = -(1-consts.MU)*(1+17/12 * consts.MU)
        ry = 0
    elif point == "L4":
        rx = 1/2-consts.MU
        ry = 3**(1/2)/2
    elif point == "L5":
        rx = 1/2-consts.MU
        ry = -3**(1/2)/2
    else:
        print(f"no point exists for argument {point}")
        exit(-1)

    r1 = ((rx+consts.MU)**2 + ry**2)**(1/2)
    r2 = ((rx-(1-consts.MU))**2 + ry**2)**(1/2)

    J = rx**2 + ry**2 + (2*(1-consts.MU))/r1 + (2*consts.MU)/r2
    return J

def get_J_state(x):
    """
    gets the jacobi integral at a specified state

    args:
        - x: state [rx,ry,vx,vy]

    returns:
        - J: jacobi integral
    """

    r1 = ((x[0]+consts.MU)**2 + x[1]**2)**(1/2)
    r2 = ((x[0]-(1-consts.MU))**2 + x[1]**2)**(1/2)

    #J = x[0]**2 + x[1]**2 + (2*(1-consts.MU))/r1 + (2*consts.MU)/r2 - (x[2]**2 + x[3]**2)
    J = -(x[2]**2 + x[3]**2)/2 + 2*((x[0]**2 + x[1]**2)/2 + (1-consts.MU)/r1 + consts.MU/r2)

    return J

def get_vel_mag(x, J):
    """
    computes the magnitude of the velocity vector

    args:
        - x: state [rx,ry,vx,vy]

    returns:
        - vel: velocity
    """

    r1 = ((x[0]+consts.MU)**2 + x[1]**2)**(1/2) 
    r2 = ((x[0]-(1-consts.MU))**2 + x[1]**2)**(1/2) 

    potential = (1/2)*(x[0]**2 + x[1]**2) + (1-consts.MU)/r1 + consts.MU/r2

    vel = (2*potential - J)**2
    return vel

# Imports

from math import sin, cos, tan, pi, radians

# Variables

circ = 0

request = 0

revcirc = 0

time = 0

passpass = True

acc = 0

# Functions

def wcalc_time():
        
    global revcirc
    
    revcirc = (2 * pi)

    w_timerev = revcirc / omega

    print('The time taken for one revolution is ',w_timerev,' seconds.')

def vcalc_time():

    global circ
    
    circ = (2 * pi * radius)

    v_timerev = circ / tvelocity

    print('The time taken for one revolution is ',v_timerev,' seconds.')
       

def angular_velocity():

    global omega

    radianam = totalrevs * (2 * pi)

    angvel = (radianam / time)

    print('Angular velocity is ',angvel,' radians per second.')

    omega = angvel


def tang_velocity():

    global tvelocity

    tangvel = (omega * radius)

    print('Tangential velocity is ',tangvel,'metres per second.')


def tacceleration():

    acc = ((tvelocity**2) / radius)

    print('Centripetal acceleration is',acc,'metres per second squared.')


def oacceleration():

    acc = ((omega**2) * radius)

    print('Centripetal acceleration is',acc,'metres per second squared.')
   

def radius_axis():

    axial_radius = (sphradius) * cos(radians(latitude))

    print('Radius about axis of rotation is ',axial_radius,'metres.')


# Program

print('Standard Form guidance: Use y(e(x)), e.g. 4x10^6 = 4e06.\n')

print('[1] Time for one revolution with angular velocity. \n[2] Time for one revolution with tangential velocity. \n[3] Angular velocity. \n[4] Tangential velocity. \n[5] Centripetal acceleration with tangential velocity. \n[6] Centripetal acceleration with angular velocity. \n[7] Radius about axis of rotation (use only for objects that are not perfect spheres, such as planets).')

while passpass:

    request = input('\nWhat would you like to calculate?: ')

    if (request == '1'):

        omega = float(input('Enter angular velocity: '))

        wcalc_time()
        
        request = 0

    elif (request == '2'):

        radius = float(input('Enter radius of circle: '))

        tvelocity = float(input('Enter tangential velocity: '))

        vcalc_time()
        
        request = 0

    elif (request == '3'):

        totalrevs = float(input('Enter number of revolutions completed: '))

        time = float(input('Enter time passed: '))

        angular_velocity()
        
        request = 0

    elif (request == '4'):

        radius = float(input('Enter radius of circle: '))

        omega = float(input('Enter angular velocity: '))

        tang_velocity()

        request = 0

    elif (request == '5'):

        radius = float(input('Enter radius of circle: '))

        tvelocity = float(input('Enter tangential velocity: '))

        tacceleration()

        request = 0

    elif (request == '6'):

        radius = float(input('Enter radius of circle: '))

        omega = float(input('Enter angular velocity: '))

        oacceleration()

        request = 0

    elif (request == '7'):

        sphradius = float(input('Enter radius of sphere at equator: '))

        latitude = float(input('Enter latitude of point: '))

        radius_axis()

        request = 0

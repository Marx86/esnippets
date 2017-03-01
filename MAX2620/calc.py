#!/usb/bin/env python3

from math import sqrt, pi
           
C3 = 270e-12
C4 = 270e-12
C03 = C04 = 2.4e-12

Cn = ((C3+C03)*(C4+C04))/(C3+C03+C4+C04)

C5 = 150e-12
C6 = 33e-12
C17 = 33e-12
Cd1 = 100e-12 # Varicap
L1 = 2.2e-6

Cstray = 1e-12

Fo = 1 / (2 * pi * sqrt(L1 * (Cstray + ((C17 * Cd1) / (C17 + Cd1)) + C6 + ((C5 * Cn) / (C5 + Cn)))))

print('Frequency: {} Hz'.format(Fo))

import numpy as np
from math import *
PI = 3.14159265359

def GM2_1s1sF(v, xi, b,eta, force):
    v -= np.array([(-160*b**2*xi**3/9 + 8*xi)*force[0]/(8*PI**(3/2)*eta), (-160*b**2*xi**3/9 + 8*xi)*force[1]/(8*PI**(3/2)*eta), (-160*b**2*xi**3/9 + 8*xi)*force[2]/(8*PI**(3/2)*eta)])
    return

def GM2_2a1sF(o, xi, b,eta, force):
    o -= 0.5/b*np.array([0, 0, 0])
    return

def GM2_1s2aT(v, xi, b,eta, torque):
    v -= 1./b*np.array([0, 0, 0])
    return

def GM2_2a2aT(o, xi, b,eta, torque):
    o -= 0.5/(b*b)*np.array([10*b**2*xi**3*torque[0]/(3*PI**(3/2)*eta), 10*b**2*xi**3*torque[1]/(3*PI**(3/2)*eta), 10*b**2*xi**3*torque[2]/(3*PI**(3/2)*eta)])
    return

def GM2_H1sF(gh1sf, xi, b,eta, force):
    gh1sf[:] -= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return

def GM2_H2aT(gh2at, xi, b,eta, torque):
    gh2at[:] -= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return

def KM2_HHVH(khhvh, xi, b,eta, VH):
    khhvh[:] -= [b**3*(-672*b**2*xi**5/25 + 32*xi**3/3)*(2*VH[0] + VH[3])/(3*sqrt(PI)) + b**3*(336*b**2*xi**5/25 - 16*xi**3/3)*(VH[0] + 2*VH[3])/(3*sqrt(PI)), 2*b**3*(-504*b**2*xi**5/25 + 8*xi**3)*VH[1]/(3*sqrt(PI)), 2*b**3*(-504*b**2*xi**5/25 + 8*xi**3)*VH[2]/(3*sqrt(PI)), b**3*(-672*b**2*xi**5/25 + 32*xi**3/3)*(VH[0] + 2*VH[3])/(3*sqrt(PI)) + b**3*(336*b**2*xi**5/25 - 16*xi**3/3)*(2*VH[0] + VH[3])/(3*sqrt(PI)), 2*b**3*(-504*b**2*xi**5/25 + 8*xi**3)*VH[4]/(3*sqrt(PI)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return

def GM2_HHFH(ghhfh, xi, b,eta, FH):
    ghhfh[:] -= [b**2*(-672*b**2*xi**5/25 + 32*xi**3/3)*(2*FH[0] + FH[3])/(8*PI**(3/2)*eta) + b**2*(336*b**2*xi**5/25 - 16*xi**3/3)*(FH[0] + 2*FH[3])/(8*PI**(3/2)*eta), b**2*(-504*b**2*xi**5/25 + 8*xi**3)*FH[1]/(4*PI**(3/2)*eta), b**2*(-504*b**2*xi**5/25 + 8*xi**3)*FH[2]/(4*PI**(3/2)*eta), b**2*(-672*b**2*xi**5/25 + 32*xi**3/3)*(FH[0] + 2*FH[3])/(8*PI**(3/2)*eta) + b**2*(336*b**2*xi**5/25 - 16*xi**3/3)*(2*FH[0] + FH[3])/(8*PI**(3/2)*eta), b**2*(-504*b**2*xi**5/25 + 8*xi**3)*FH[4]/(4*PI**(3/2)*eta), 0, 0, 0, -28*b**4*xi**5*(FH[8] + 2*FH[11])/(5*PI**(3/2)*eta) + 56*b**4*xi**5*(2*FH[8] + FH[11])/(5*PI**(3/2)*eta), 84*b**4*xi**5*FH[9]/(5*PI**(3/2)*eta), 84*b**4*xi**5*FH[10]/(5*PI**(3/2)*eta), 56*b**4*xi**5*(FH[8] + 2*FH[11])/(5*PI**(3/2)*eta) - 28*b**4*xi**5*(2*FH[8] + FH[11])/(5*PI**(3/2)*eta), 84*b**4*xi**5*FH[12]/(5*PI**(3/2)*eta), 56*b**4*xi**5*FH[12]/(5*PI**(3/2)*eta) + b**4*(-18432*b**2*xi**7/245 + 768*xi**5/25)*(4*FH[13] + 3*FH[16])/(8*PI**(3/2)*eta) + b**4*(9216*b**2*xi**7/245 - 384*xi**5/25)*(3*FH[13] + 6*FH[16])/(8*PI**(3/2)*eta), -56*b**4*xi**5*FH[10]/(15*PI**(3/2)*eta) + b**4*(-12288*b**2*xi**7/245 + 512*xi**5/25)*(6*FH[14] + 3*FH[18])/(8*PI**(3/2)*eta) + b**4*(9216*b**2*xi**7/245 - 384*xi**5/25)*(3*FH[14] + 4*FH[18])/(8*PI**(3/2)*eta), 56*b**4*xi**5*FH[9]/(15*PI**(3/2)*eta) + b**4*(-12288*b**2*xi**7/245 + 512*xi**5/25)*(4*FH[15] + FH[19])/(8*PI**(3/2)*eta) + b**4*(3072*b**2*xi**7/245 - 128*xi**5/25)*(FH[15] + 4*FH[19])/(8*PI**(3/2)*eta), 56*b**4*xi**5*FH[12]/(15*PI**(3/2)*eta) + b**4*(-12288*b**2*xi**7/245 + 512*xi**5/25)*(3*FH[13] + 6*FH[16])/(8*PI**(3/2)*eta) + b**4*(9216*b**2*xi**7/245 - 384*xi**5/25)*(4*FH[13] + 3*FH[16])/(8*PI**(3/2)*eta), 3*b**4*(-1536*b**2*xi**7/49 + 64*xi**5/5)*FH[17]/(4*PI**(3/2)*eta), -56*b**4*xi**5*FH[10]/(5*PI**(3/2)*eta) + b**4*(-18432*b**2*xi**7/245 + 768*xi**5/25)*(3*FH[14] + 4*FH[18])/(8*PI**(3/2)*eta) + b**4*(9216*b**2*xi**7/245 - 384*xi**5/25)*(6*FH[14] + 3*FH[18])/(8*PI**(3/2)*eta), 56*b**4*xi**5*FH[9]/(15*PI**(3/2)*eta) + b**4*(-12288*b**2*xi**7/245 + 512*xi**5/25)*(FH[15] + 4*FH[19])/(8*PI**(3/2)*eta) + b**4*(3072*b**2*xi**7/245 - 128*xi**5/25)*(4*FH[15] + FH[19])/(8*PI**(3/2)*eta)]
    return

def GM2_1sHFH(v, xi, b,eta, FH):
    v += np.array([4*b**2*xi**3*FH[5]/(3*PI**(3/2)*eta) - 40*b**2*xi**3*FH[12]/(27*PI**(3/2)*eta), 4*b**2*xi**3*FH[6]/(3*PI**(3/2)*eta) + 40*b**2*xi**3*FH[10]/(27*PI**(3/2)*eta), 4*b**2*xi**3*FH[7]/(3*PI**(3/2)*eta) - 40*b**2*xi**3*FH[9]/(27*PI**(3/2)*eta)])
    return

def GM2_2aHFH(o, xi, b,eta, FH):
    o += 0.5/b*np.array([0, 0, 0])
    return

def KM2_1sHVH(v, xi, b,eta, VH):
    v -= np.array([8*b**3*xi**3*VH[5]/(5*sqrt(PI)), 8*b**3*xi**3*VH[6]/(5*sqrt(PI)), 8*b**3*xi**3*VH[7]/(5*sqrt(PI))])
    return

def KM2_2aHVH(o, xi, b,eta, VH):
    o -= 0.5/b*np.array([0, 0, 0])
    return


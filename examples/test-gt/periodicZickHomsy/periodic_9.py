import numpy as np
from math import *
PI = 3.14159265359

def G1s1sF(v, L, b,eta, force):
    v += np.array([(5694269330719*L**2/(566162087400*PI**2) - 1456*b**2/9)*force[0]/(L**3*eta), (5694269330719*L**2/(566162087400*PI**2) - 1456*b**2/9)*force[1]/(L**3*eta), (5694269330719*L**2/(566162087400*PI**2) - 1456*b**2/9)*force[2]/(L**3*eta)])
    return

def G2a1sF(o, L, b,eta, force):
    o += 0.5/b*np.array([0, 0, 0])
    return

def G1s2aT(v, L, b,eta, torque):
    v += 1./b*np.array([0, 0, 0])
    return

def G2a2aT(o, L, b,eta, torque):
    o += 0.5/(b*b)*np.array([728*b**2*torque[0]/(3*L**3*eta), 728*b**2*torque[1]/(3*L**3*eta), 728*b**2*torque[2]/(3*L**3*eta)])
    return

def GH1sF(gh1sf, L, b,eta, force):
    gh1sf[:] += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (-1712727969204285333632*b**2/118757595453361239375 + 7850824072928*PI**2*b**4/(17299397115*L**2))*force[0]/(L**3*eta), (856363984602142666816*b**2/118757595453361239375 - 3925412036464*PI**2*b**4/(17299397115*L**2))*force[1]/(L**3*eta), (856363984602142666816*b**2/118757595453361239375 - 3925412036464*PI**2*b**4/(17299397115*L**2))*force[2]/(L**3*eta), (856363984602142666816*b**2/118757595453361239375 - 3925412036464*PI**2*b**4/(17299397115*L**2))*force[0]/(L**3*eta), 0, (-1712727969204285333632*b**2/118757595453361239375 + 7850824072928*PI**2*b**4/(17299397115*L**2))*force[1]/(L**3*eta), (856363984602142666816*b**2/118757595453361239375 - 3925412036464*PI**2*b**4/(17299397115*L**2))*force[2]/(L**3*eta)]
    return

def GH2aT(gh2at, L, b,eta, torque):
    gh2at[:] += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return

def KoHHVH(khhvh, b,eta, VH):
    khhvh[:] -= [3*VH[0]/5, 3*VH[1]/5, 3*VH[2]/5, 3*VH[3]/5, 3*VH[4]/5, 2*VH[5]/5, 2*VH[6]/5, 2*VH[7]/5, 4*VH[8]/5, 4*VH[9]/5, 4*VH[10]/5, 4*VH[11]/5, 4*VH[12]/5, 19*VH[13]/35, 19*VH[14]/35, 19*VH[15]/35, 19*VH[16]/35, 19*VH[17]/35, 19*VH[18]/35, 19*VH[19]/35]
    return

def KHHVH(khhvh, L, b,eta, VH):
    khhvh[:] += [8*PI*b*(-6620065950605274817816*b**2/118757595453361239375 + 19939711080064*PI**2*b**4/(20594520375*L**2))*(VH[0] + 2*VH[3])/(3*L**3) + 8*PI*b*(13240131901210549635632*b**2/118757595453361239375 - 39879422160128*PI**2*b**4/(20594520375*L**2))*(2*VH[0] + VH[3])/(3*L**3), 16*PI*b*(7789188964402555559684*b**2/118757595453361239375 - 20096036528936*PI**2*b**4/(20594520375*L**2))*VH[1]/(3*L**3), 16*PI*b*(7789188964402555559684*b**2/118757595453361239375 - 20096036528936*PI**2*b**4/(20594520375*L**2))*VH[2]/(3*L**3), 8*PI*b*(-6620065950605274817816*b**2/118757595453361239375 + 19939711080064*PI**2*b**4/(20594520375*L**2))*(2*VH[0] + VH[3])/(3*L**3) + 8*PI*b*(13240131901210549635632*b**2/118757595453361239375 - 39879422160128*PI**2*b**4/(20594520375*L**2))*(VH[0] + 2*VH[3])/(3*L**3), 16*PI*b*(7789188964402555559684*b**2/118757595453361239375 - 20096036528936*PI**2*b**4/(20594520375*L**2))*VH[4]/(3*L**3), 0, 0, 0, 0, 0, 0, 0, 0, -15701648145856*PI**3*b**5*VH[5]/(34324200625*L**5), 7850824072928*PI**3*b**5*VH[6]/(34324200625*L**5), 7850824072928*PI**3*b**5*VH[7]/(34324200625*L**5), 7850824072928*PI**3*b**5*VH[5]/(34324200625*L**5), 0, -15701648145856*PI**3*b**5*VH[6]/(34324200625*L**5), 7850824072928*PI**3*b**5*VH[7]/(34324200625*L**5)]
    return

def GoHHFH(ghhfh, b,eta, FH):
    ghhfh[:] += [-(FH[0] + 2*FH[3])/(20*PI*b*eta) + (2*FH[0] + FH[3])/(10*PI*b*eta), 3*FH[1]/(20*PI*b*eta), 3*FH[2]/(20*PI*b*eta), (FH[0] + 2*FH[3])/(10*PI*b*eta) - (2*FH[0] + FH[3])/(20*PI*b*eta), 3*FH[4]/(20*PI*b*eta), FH[5]/(2*PI*b*eta), FH[6]/(2*PI*b*eta), FH[7]/(2*PI*b*eta), -(FH[8] + 2*FH[11])/(2*PI*b*eta) + (2*FH[8] + FH[11])/(PI*b*eta), 3*FH[9]/(2*PI*b*eta), 3*FH[10]/(2*PI*b*eta), (FH[8] + 2*FH[11])/(PI*b*eta) - (2*FH[8] + FH[11])/(2*PI*b*eta), 3*FH[12]/(2*PI*b*eta), -6*(3*FH[13] + 6*FH[16])/(35*PI*b*eta) + 12*(4*FH[13] + 3*FH[16])/(35*PI*b*eta), -6*(3*FH[14] + 4*FH[18])/(35*PI*b*eta) + 8*(6*FH[14] + 3*FH[18])/(35*PI*b*eta), -2*(FH[15] + 4*FH[19])/(35*PI*b*eta) + 8*(4*FH[15] + FH[19])/(35*PI*b*eta), 8*(3*FH[13] + 6*FH[16])/(35*PI*b*eta) - 6*(4*FH[13] + 3*FH[16])/(35*PI*b*eta), 6*FH[17]/(7*PI*b*eta), 12*(3*FH[14] + 4*FH[18])/(35*PI*b*eta) - 6*(6*FH[14] + 3*FH[18])/(35*PI*b*eta), 8*(FH[15] + 4*FH[19])/(35*PI*b*eta) - 2*(4*FH[15] + FH[19])/(35*PI*b*eta)]
    return

def GHHFH(ghhfh, L, b,eta, FH):
    ghhfh[:] += [(-6620065950605274817816*b**2/118757595453361239375 + 19939711080064*PI**2*b**4/(20594520375*L**2))*(FH[0] + 2*FH[3])/(L**3*eta) + (13240131901210549635632*b**2/118757595453361239375 - 39879422160128*PI**2*b**4/(20594520375*L**2))*(2*FH[0] + FH[3])/(L**3*eta), 2*(7789188964402555559684*b**2/118757595453361239375 - 20096036528936*PI**2*b**4/(20594520375*L**2))*FH[1]/(L**3*eta), 2*(7789188964402555559684*b**2/118757595453361239375 - 20096036528936*PI**2*b**4/(20594520375*L**2))*FH[2]/(L**3*eta), (-6620065950605274817816*b**2/118757595453361239375 + 19939711080064*PI**2*b**4/(20594520375*L**2))*(2*FH[0] + FH[3])/(L**3*eta) + (13240131901210549635632*b**2/118757595453361239375 - 39879422160128*PI**2*b**4/(20594520375*L**2))*(FH[0] + 2*FH[3])/(L**3*eta), 2*(7789188964402555559684*b**2/118757595453361239375 - 20096036528936*PI**2*b**4/(20594520375*L**2))*FH[4]/(L**3*eta), 0, 0, 0, -39879422160128*PI**2*b**4*(FH[8] + 2*FH[11])/(12356712225*L**5*eta) + 79758844320256*PI**2*b**4*(2*FH[8] + FH[11])/(12356712225*L**5*eta), -1962706018232*PI**2*b**4*(FH[15] + 4*FH[19])/(2471342445*L**5*eta) + 1962706018232*PI**2*b**4*(4*FH[15] + FH[19])/(2471342445*L**5*eta) + 80384146115744*PI**2*b**4*FH[9]/(12356712225*L**5*eta), -1962706018232*PI**2*b**4*(6*FH[14] + 3*FH[18])/(2471342445*L**5*eta) + 80384146115744*PI**2*b**4*FH[10]/(12356712225*L**5*eta), 79758844320256*PI**2*b**4*(FH[8] + 2*FH[11])/(12356712225*L**5*eta) - 39879422160128*PI**2*b**4*(2*FH[8] + FH[11])/(12356712225*L**5*eta), 1962706018232*PI**2*b**4*(3*FH[13] + 6*FH[16])/(2471342445*L**5*eta) + 80384146115744*PI**2*b**4*FH[12]/(12356712225*L**5*eta), (-135150627667491624516784*PI**2*b**4/(166260633634705735125*L**2) + 2230894382871488*PI**4*b**6/(201826299675*L**4))*(3*FH[13] + 6*FH[16])/(L**3*eta) + (270301255334983249033568*PI**2*b**4/(166260633634705735125*L**2) - 4461788765742976*PI**4*b**6/(201826299675*L**4))*(4*FH[13] + 3*FH[16])/(L**3*eta) - 7850824072928*PI**2*b**4*FH[5]/(20594520375*L**5*eta) + 207873236669056*PI**2*b**4*FH[12]/(37070136675*L**5*eta), (-135150627667491624516784*PI**2*b**4/(166260633634705735125*L**2) + 2230894382871488*PI**4*b**6/(201826299675*L**4))*(3*FH[14] + 4*FH[18])/(L**3*eta) + (607695563085122955745936*PI**2*b**4/(498781900904117205375*L**2) - 3616246483927744*PI**4*b**6/(201826299675*L**4))*(6*FH[14] + 3*FH[18])/(L**3*eta) + 3925412036464*PI**2*b**4*FH[6]/(20594520375*L**5*eta) - 95460492466112*PI**2*b**4*FH[10]/(37070136675*L**5*eta), (-202243680082648082195584*PI**2*b**4/(498781900904117205375*L**2) + 1385352101056256*PI**4*b**6/(201826299675*L**4))*(FH[15] + 4*FH[19])/(L**3*eta) + (607695563085122955745936*PI**2*b**4/(498781900904117205375*L**2) - 3616246483927744*PI**4*b**6/(201826299675*L**4))*(4*FH[15] + FH[19])/(L**3*eta) + 3925412036464*PI**2*b**4*FH[7]/(20594520375*L**5*eta) + 95460492466112*PI**2*b**4*FH[9]/(37070136675*L**5*eta), (-135150627667491624516784*PI**2*b**4/(166260633634705735125*L**2) + 2230894382871488*PI**4*b**6/(201826299675*L**4))*(4*FH[13] + 3*FH[16])/(L**3*eta) + (607695563085122955745936*PI**2*b**4/(498781900904117205375*L**2) - 3616246483927744*PI**4*b**6/(201826299675*L**4))*(3*FH[13] + 6*FH[16])/(L**3*eta) + 3925412036464*PI**2*b**4*FH[5]/(20594520375*L**5*eta) + 95460492466112*PI**2*b**4*FH[12]/(37070136675*L**5*eta), 6*(23809786801939990125056*PI**2*b**4/(33252126726941147025*L**2) - 77870435784448*PI**4*b**6/(8073051987*L**4))*FH[17]/(L**3*eta), (-135150627667491624516784*PI**2*b**4/(166260633634705735125*L**2) + 2230894382871488*PI**4*b**6/(201826299675*L**4))*(6*FH[14] + 3*FH[18])/(L**3*eta) + (270301255334983249033568*PI**2*b**4/(166260633634705735125*L**2) - 4461788765742976*PI**4*b**6/(201826299675*L**4))*(3*FH[14] + 4*FH[18])/(L**3*eta) - 7850824072928*PI**2*b**4*FH[6]/(20594520375*L**5*eta) - 207873236669056*PI**2*b**4*FH[10]/(37070136675*L**5*eta), (-202243680082648082195584*PI**2*b**4/(498781900904117205375*L**2) + 1385352101056256*PI**4*b**6/(201826299675*L**4))*(4*FH[15] + FH[19])/(L**3*eta) + (607695563085122955745936*PI**2*b**4/(498781900904117205375*L**2) - 3616246483927744*PI**4*b**6/(201826299675*L**4))*(FH[15] + 4*FH[19])/(L**3*eta) + 3925412036464*PI**2*b**4*FH[7]/(20594520375*L**5*eta) + 5650750578944*PI**2*b**4*FH[9]/(12356712225*L**5*eta)]
    return

def G1sHFH(v, L, b,eta, FH):
    v -= np.array([1456*b**2*FH[5]/(15*L**3*eta) - 2912*b**2*FH[12]/(27*L**3*eta) + (-1712727969204285333632*b**2/118757595453361239375 + 7850824072928*PI**2*b**4/(17299397115*L**2))*(4*FH[13] + 3*FH[16])/(L**3*eta) + (856363984602142666816*b**2/118757595453361239375 - 3925412036464*PI**2*b**4/(17299397115*L**2))*(3*FH[13] + 6*FH[16])/(L**3*eta), 1456*b**2*FH[6]/(15*L**3*eta) + 2912*b**2*FH[10]/(27*L**3*eta) + (-1712727969204285333632*b**2/118757595453361239375 + 7850824072928*PI**2*b**4/(17299397115*L**2))*(3*FH[14] + 4*FH[18])/(L**3*eta) + (856363984602142666816*b**2/118757595453361239375 - 3925412036464*PI**2*b**4/(17299397115*L**2))*(6*FH[14] + 3*FH[18])/(L**3*eta), 1456*b**2*FH[7]/(15*L**3*eta) - 2912*b**2*FH[9]/(27*L**3*eta) + (856363984602142666816*b**2/118757595453361239375 - 3925412036464*PI**2*b**4/(17299397115*L**2))*(FH[15] + 4*FH[19])/(L**3*eta) + (856363984602142666816*b**2/118757595453361239375 - 3925412036464*PI**2*b**4/(17299397115*L**2))*(4*FH[15] + FH[19])/(L**3*eta)])
    return

def G2aHFH(o, L, b,eta, FH):
    o -= 0.5/b*np.array([0, 0, 0])
    return

def K1sHVH(v, L, b,eta, VH):
    v += np.array([2912*PI*b**3*VH[5]/(25*L**3), 2912*PI*b**3*VH[6]/(25*L**3), 2912*PI*b**3*VH[7]/(25*L**3)])
    return

def K2aHVH(o, L, b,eta, VH):
    o += 0.5/b*np.array([0, 0, 0])
    return


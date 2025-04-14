cimport cython
from libc.math cimport sqrt
from cython.parallel import prange
import numpy as np
cimport numpy as np
cdef double PI = 3.14159265359

@cython.wraparound(False)
@cython.boundscheck(False)
@cython.cdivision(True)
@cython.nonecheck(False)
cdef class Rbm:
    cdef double b, eta, mu, muv, mur
    cdef int N 
    cdef readonly np.ndarray Mobility

    cpdef mobilityTT(self, double [:] v,  double [:] r, double [:] F)
               
   
    cpdef mobilityTR(self,    double [:] v,  double [:] r, double [:] T)
    
    
    cpdef propulsionT2s(self, double [:] v,  double [:] r, double [:] V2s)


    cpdef propulsionT3t(self, double [:] v,  double [:] r, double [:] V3t)


    cpdef propulsionT3a(self, double [:] v,  double [:] r, double [:] V3a)


    cpdef propulsionT3s(self, double [:] v,  double [:] r, double [:] V3s)


    cpdef propulsionT4a(self, double [:] v,  double [:] r, double [:] V4a)


    ## Angular velocities


    cpdef mobilityRT(self, double [:] o,  double [:] r, double [:] F)

               
    cpdef mobilityRR(   self, double [:] o,  double [:] r, double [:] T)

    
    cpdef propulsionR2s(self, double [:] o,  double [:] r, double [:] V2s)
    
    
    cpdef propulsionR3a(  self, double [:] o,  double [:] r, double [:] V3a)


    cpdef propulsionR3s(  self, double [:] o,  double [:] r, double [:] V3s)


    cpdef propulsionR4a(  self, double [:] o,  double [:] r, double [:] V4a) 



@cython.wraparound(False)
@cython.boundscheck(False)
@cython.cdivision(True)
@cython.nonecheck(False)
cdef class Flow:
    cdef double b, eta
    cdef int N
    cdef int Nt

    cpdef flowField1s(self, double [:] vv, double [:] rt, double [:] r, double [:] F, double maskR=?)
               
    cpdef flowField2a(   self, double [:] vv, double [:] rt, double [:] r, double [:] T, double maskR=?)

    cpdef flowField2s(self, double [:] vv, double [:] rt, double [:] r, double [:] V2s, double maskR=?)


    cpdef flowField3t(self, double [:] vv, double [:] rt, double [:] r, double [:] V3t, double maskR=?)


    cpdef flowField3s(self,   double [:] vv, double [:] rt, double [:] r, double [:] V3s, double maskR=?)


    cpdef flowField3a(self,   double [:] vv, double [:] rt, double [:] r, double [:] V3a, double maskR=?)


    cpdef flowField4a(self,   double [:] vv, double [:] rt, double [:] r, double [:] V4a, double maskR=?)



@cython.wraparound(False)
@cython.boundscheck(False)
@cython.cdivision(True)
@cython.nonecheck(False)
cdef class PD:
    cdef double b, eta, gammaT, gammaR, mu, muv, mur
    cdef int N 
    cdef readonly np.ndarray Mobility

    cpdef frictionTT(self, double depsilon, double [:] v, double [:] r)
               
   
    cpdef frictionTR(self, double depsilon, double [:] v, double [:] o, double [:] r)
    
    
    cpdef frictionT2s(self, double depsilon, double [:] V1s, double [:] V2s, double [:] r)


    cpdef frictionT3t(self, double depsilon, double [:] V1s, double [:] V3t, double [:] r)


    ## Angular velocities


    cpdef frictionRT(self, double depsilon, double [:] v, double [:] o, double [:] r)

               
    cpdef frictionRR(self, double depsilon, double [:] o, double [:] r)

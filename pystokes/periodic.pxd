cimport cython
from cython.parallel import prange


@cython.wraparound(False)
@cython.boundscheck(False)
@cython.cdivision(True)
@cython.nonecheck(False)
cdef class Rbm:
    cdef int N
    cdef double b, eta, L, mu, xi, muv, mur

    cpdef mobilityTT(self, double [:] v, double [:] r, double [:] F, int Nb=?, int Nm=?, double xi0=?)
    
    
    cpdef mobilityTR(self, double [:] v, double [:] r, double [:] T, int Nb=?, int Nm=?, double xi0=?)
    
    
    cpdef propulsionT2s(self, double [:] v, double [:] r, double [:] V2s, int Nb=?, int Nm=?, double xi0=?)


    cpdef propulsionT3t(self, double [:] v, double [:] r, double [:] V3t, int Nb=?, int Nm=?, double xi0=?)


    cpdef propulsionT3s(  self, double [:] v, double [:] r, double [:] V3s, int Nb=?, int Nm=?, double xi0=?)

    
    cpdef propulsionT3a(  self, double [:] v, double [:] r, double [:] V3a, int Nb=?, int Nm=?, double xi0=?)


    cpdef propulsionT4a(  self, double [:] v, double [:] r, double [:] V4a, int Nb=?, int Nm=?, double xi0=?)


    ## Angular velocities


    cpdef mobilityRT(self, double [:] o, double [:] r, double [:] F, int Nb=?, int Nm=?, double xi0=?)


    cpdef mobilityRR(self, double [:] o, double [:] r, double [:] T, int Nb=?, int Nm=?, double xi0=?)

    
    cpdef propulsionR2s(self, double [:] o, double [:] r, double [:] V2s, int Nb=?, int Nm=?, double xi0=?)


    cpdef propulsionR3a(self, double [:] o, double [:] r, double [:] V3a, int Nb=?, int Nm=?, double xi0=?)

    
    cpdef propulsionR3s(self, double [:] o, double [:] r, double [:] V3s, int Nb=?, int Nm=?, double xi0=?)


    cpdef propulsionR4a(self, double [:] o, double [:] r, double [:] V4a, int Nb=?, int Nm=?, double xi0=?)



@cython.wraparound(False)
@cython.boundscheck(False)
@cython.cdivision(True)
@cython.nonecheck(False)
cdef class Flow:
    cdef double b
    cdef int N, Nt
    cdef double L, eta, xi

    cpdef flowField1s(self, double [:] v, double [:] rt, double [:] r, double [:] F, int Nb=?, int Nm=?, double xi0=?)

    
    cpdef flowField2s(self, double [:] v, double [:] rt, double [:] r, double [:] V2s, int Nb=?, int Nm=?, double xi0=?)

    
    cpdef flowField3t(self, double [:] v, double [:] rt, double [:] r, double [:] V3t, int Nb=?, int Nm=?, double xi0=?)

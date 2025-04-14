import numpy as np
from math import *
from scipy.sparse.linalg import bicgstab, LinearOperator
import periodic_4 as me

PI = 3.14159265359

class Rbm:
    
    def __init__(self, radius=1., viscosity=1.0, boxSize=10, tolerance=1e-05):
        self.b  = radius
        self.eta = viscosity
        self.L = boxSize 
        
        ## tolerance for Krylov iterative solver
        self.tol = tolerance
        
        ## single-layer matrix elements for i=j (not gamma)
        self.g1s = 1./(6*PI*self.eta*self.b)
        self.g2a = 1./(4*PI*self.eta*self.b)
        
        ## total dim of higher modes 
        self.dimH = 20
        
        ## used dimensions of 2s
        self.dim2s = 5
        
        ## for starting point of Krylov solver: free space solution
        self.gamma2s = 4*PI*self.eta*self.b
        self.gamma3t = 4*PI*self.eta*self.b/5.
        self.gamma3a = 8*PI*self.eta*self.b/15.
        self.gamma3s = 19*PI*self.eta*self.b/30.
        
        self.gammaH = np.concatenate([np.full(self.dim2s, self.gamma2s),
                                      np.full(3, self.gamma3t),
                                      np.full(self.dim2s, self.gamma3a),
                                      np.full(self.dimH-2*self.dim2s-3, self.gamma3s)])
        
        
        
    def krylovSolve(self, v, o, F, T, S, D):
        b = self.b
        eta = self.eta
        L = self.L
        
        VH = np.zeros(self.dimH)
        FH, exitCode = self.get_FH(F, T, S, D)
        # FH = np.zeros(self.dimH)
                    
        VH[0:self.dim2s]  = S
        VH[self.dim2s:self.dim2s+3]  = D 
        
        ## interactions with periodic lattice
        me.G1s1sF(v, L,b,eta, F)
        me.G1s2aT(v, L,b,eta, T)
        me.G1sHFH(v, L,b,eta, FH)
        me.K1sHVH(v, L,b,eta, VH) 
        
        me.G2a1sF(o, L,b,eta, F)
        me.G2a2aT(o, L,b,eta, T)
        me.G2aHFH(o, L,b,eta, FH)
        me.K2aHVH(o, L,b,eta, VH)
        
        
        ## self-interaction
        v += self.g1s*F + 0.2*D 
        o += 0.5/(b*b) * self.g2a*T
        
        return
    
    
    def get_FH(self, F, T, S, D):
        b = self.b
        eta = self.eta
        L = self.L

        ## dimH is dimension of 2s + 3t + 3a + 3s
        VH = np.zeros(self.dimH)
        
        KHHVH = np.zeros([self.dimH])
        GH1sF = np.zeros([self.dimH])
        GH2aT = np.zeros([self.dimH])
                    
        VH[0:self.dim2s]  = S
        VH[self.dim2s:self.dim2s+3]  = D
        
        ## interactions with periodic lattice
        me.KHHVH(KHHVH, L,b,eta, VH)
        me.GH1sF(GH1sF, L,b,eta, F)
        me.GH2aT(GH2aT, L,b,eta, T)

        ## self-interaction
        me.KoHHVH(KHHVH, b,eta, VH)
            
        rhs = KHHVH + GH1sF + 1./b * GH2aT 
        FH0 = -self.gammaH*VH  #start at the one-body solution
        
        GHHFH = LinearOperator((self.dimH, self.dimH), matvec = self.GHHFH)
            
        return bicgstab(GHHFH, rhs, x0=FH0, tol=self.tol)
    
    
    def GHHFH(self, FH):
        b = self.b
        eta = self.eta
        L = self.L
        
        GHHFH = np.zeros(self.dimH)
        
        ## interactions with periodic lattice
        me.GHHFH(GHHFH, L,b,eta, FH)
        
        ## self-interaction
        me.GoHHFH(GHHFH, b,eta, FH) 
                    
        return GHHFH
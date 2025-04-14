import numpy as np
import matelms as me

PI = 3.14159265359


class DS:
    
    def __init__(self, radius=1., particles=1, viscosity=1.0):
        self.b  = radius
        self.Np = particles
        self.eta = viscosity
        
        ## matrix elements for i=j
        self.g1s = 1./(6*PI*self.eta*self.b)
        self.g2a = 1./(4*PI*self.eta*self.b)
        
        ## friction coefficients for i=j
        self.gamma2s = 4*PI*self.eta*self.b
        self.gamma3t = 0.8*PI*self.eta*self.b
        self.halfMinusKoHH = 0.6
        
    def directSolve_new(self, v, o, r, F, T, S, D, rcond=1e-5):
        b = self.b
        Np = self.Np
        eta = self.eta
        for i in range(Np):
            v_ = np.zeros([3])
            o_ = np.zeros([3])
            for j in range(Np):
                if j!=i:
                    xij = r[i]    - r[j] 
                    yij = r[i+Np]  - r[j+Np]
                    zij = r[i+2*Np]  - r[j+2*Np]
                    
                    force_j  = np.array([F[j],F[j+Np], F[j+2*Np]])
                    torque_j = np.array([T[j],T[j+Np], T[j+2*Np]])
                    S_j  = np.array([S[j],S[j+Np],S[j+2*Np],S[j+3*Np],S[j+4*Np]])
                    D_j  = np.array([D[j],D[j+Np],D[j+2*Np]])
                    VH_j = np.concatenate([S_j,D_j,np.zeros(12)]) 
                    
                    hatFH_j = np.zeros(17)
                    rhs = np.zeros(17)
                    for k in range(Np):
                        if k!=i:
                            xik = r[i]       - r[k] ##move them here, more consistent
                            yik = r[i+Np]    - r[k+Np]
                            zik = r[i+2*Np]  - r[k+2*Np]
                            
                            force_k  = np.array([F[k],F[k+Np], F[k+2*Np]])
                            torque_k = np.array([T[k],T[k+Np], T[k+2*Np]])
                            S_k = np.array([S[k],S[k+Np],S[k+2*Np],S[k+3*Np],S[k+4*Np]])
                            D_k = np.array([D[k],D[k+Np],D[k+2*Np]])
                            
                            hatVH_k = np.concatenate([S_k,np.zeros(12)])
                            
                            rhs += (np.dot(me.hatGH1s(xik,yik,zik, b,eta), force_k)
                                    + 1./b * np.dot(me.hatGH2a(xik,yik,zik, b,eta), torque_k)
                                    + np.dot(me.hatKHH(xik,yik,zik, b,eta),hatVH_k)
                                    + self.gamma3t * np.dot(me.hatGH3t(xik,yik,zik, b,eta), D_k))
                        else: #k=i
                            S_i = np.array([S[i],S[i+Np],S[i+2*Np],S[i+3*Np],S[i+4*Np]])
                            hatVH_i = np.concatenate([self.halfMinusKoHH * S_i, np.zeros(12)])
                            
                            rhs += - hatVH_i
                    
                    lhs_inv = np.linalg.pinv(me.hatGHH(xij,yij,zij, b,eta), rcond=rcond)
                    hatFH_j = np.dot(lhs_inv, rhs)
                    F3t_j = -self.gamma3t*D_j
                    FH_j = np.concatenate([hatFH_j[0:5], F3t_j, hatFH_j[5:]])
                    
                    v_ += (np.dot(me.G1s1s(xij,yij,zij, b,eta), force_j)
                          + 1./b * np.dot(me.G1s2a(xij,yij,zij, b,eta), torque_j)
                          - np.dot(me.G1sH(xij,yij,zij, b,eta), FH_j)
                          + np.dot(me.K1sH(xij,yij,zij, b,eta), VH_j))
                    
                    o_ += 0.5/b*(np.dot(me.G2a1s(xij,yij,zij, b,eta), force_j)
                                 + 1./b * np.dot(me.G2a2a(xij,yij,zij, b,eta), torque_j)
                                 - np.dot(me.G2aH(xij,yij,zij, b,eta), FH_j)
                                 + np.dot(me.K2aH(xij,yij,zij, b,eta), VH_j))
                    
                           
                else: #j=i
                    force_i  = np.array([F[i],F[i+Np], F[i+2*Np]])
                    torque_i = np.array([T[i],T[i+Np], T[i+2*Np]])
                    D_i      = np.array([D[i],D[i+Np],D[i+2*Np]])
                    
                    ## This is a solution for V = V^A + muTT*force
                    ## We know that V^A = 1/5*V^(3t) for squirmer model
                    v_ += self.g1s*force_i + 0.2*D_i
                    o_ += 0.5/(b*b) * self.g2a*torque_i
                    
                    
            v[i]      += v_[0]
            v[i+Np]   += v_[1]
            v[i+2*Np] += v_[2]
            
            o[i]      += o_[0]
            o[i+Np]   += o_[1]
            o[i+2*Np] += o_[2]
        return
                            
                    
    
        
        
    def directSolve(self, v, o, r, F, T, S, D, rcond=1e-5):
        b = self.b
        Np = self.Np
        eta = self.eta
        for i in range(Np):
            ## This velocity and angular velocity is actually V-V^A, so have to add
            ## self-propulsion speed manually
            v_ = np.zeros([3])
            o_ = np.zeros([3])
            for j in range(Np):
                #xij = r[i]    - r[j]
                #yij = r[i+Np]  - r[j+Np]
                #zij = r[i+2*Np]  - r[j+2*Np]
                if j!=i:
                    xij = r[i]    - r[j] ##move them here, more consistent
                    yij = r[i+Np]  - r[j+Np]
                    zij = r[i+2*Np]  - r[j+2*Np]
                    force  = np.array([F[j],F[j+Np], F[j+2*Np]])
                    torque = np.array([T[j],T[j+Np], T[j+2*Np]])
                    S_j  = np.array([S[j],S[j+Np],S[j+2*Np],S[j+3*Np],S[j+4*Np]])
                    D_j  = np.array([D[j],D[j+Np],D[j+2*Np]])
                    VH_j = np.concatenate([S_j,D_j,np.zeros(12)]) 
                    
                    rhs = np.zeros(20)
                    FH = np.zeros(20)
                    for k in range(Np):
                        #xjk = r[j]    - r[k]
                        #yjk = r[j+Np]  - r[k+Np]
                        #zjk = r[j+2*Np]  - r[k+2*Np]
                        if k!=j:
                            ## FH induced via FL and VH on other particles
                            xjk = r[j]    - r[k] ##move them here, more consistent
                            yjk = r[j+Np]  - r[k+Np]
                            zjk = r[j+2*Np]  - r[k+2*Np]
                            
                            force_k  = np.array([F[k],F[k+Np], F[k+2*Np]])
                            torque_k = np.array([T[k],T[k+Np], T[k+2*Np]])
                            S_k = np.array([S[k],S[k+Np],S[k+2*Np],S[k+3*Np],S[k+4*Np]])
                            D_k = np.array([D[k],D[k+Np],D[k+2*Np]])
                            VH_k = np.concatenate([S_k,D_k,np.zeros(12)])

                            rhs += (np.dot(me.GH1s(xjk,yjk,zjk, b,eta), force_k) 
                                   + 1./b * np.dot(me.GH2a(xjk,yjk,zjk, b,eta), torque_k)
                                   - np.dot(me.halfMinusKHH(xjk,yjk,zjk, b,eta), VH_k)) ## this cannot be quite right? All other 3t terms are zero
                                                                                        ## so equ would read 0 = V^(3t)
                        else:
                            ## FH induced via VH on same particle
                            F2s = -self.gamma2s*S_j
                            F3t = -self.gamma3t*D_j
                            FH += np.concatenate([F2s,F3t,np.zeros(12)])
                                    
                    ## If this is singular, use pseudo-inverse instead 
                    ## otherwise can try to cancel 3t rows (more elegant
                    ## and probably faster
                    lhs_inv = np.linalg.pinv(me.GHH(xij,yij,zij, b,eta), rcond=rcond)
                    FH += np.dot(lhs_inv, rhs)
                    
                    v_ += (np.dot(me.G1s1s(xij,yij,zij, b,eta), force)
                          + 1./b * np.dot(me.G1s2a(xij,yij,zij, b,eta), torque)
                          - np.dot(me.G1sH(xij,yij,zij, b,eta),FH)
                          + np.dot(me.K1sH(xij,yij,zij, b,eta),VH_j))
                    
                    o_ += 0.5/b*(np.dot(me.G2a1s(xij,yij,zij, b,eta), force)
                                 + 1./b * np.dot(me.G2a2a(xij,yij,zij, b,eta), torque)
                                 - np.dot(me.G2aH(xij,yij,zij, b,eta),FH)
                                 + np.dot(me.K2aH(xij,yij,zij, b,eta),VH_j))
                    
                           
                else:
                    force  = np.array([F[j],F[j+Np], F[j+2*Np]])
                    torque = np.array([T[j],T[j+Np], T[j+2*Np]])
                    D_j  = np.array([D[j],D[j+Np],D[j+2*Np]])
                    
                    ## This is a solution for V = V^A + muTT*force
                    ## We know that V^A = 1/5*V^(3t) for squirmer model
                    v_ += self.g1s*force + 0.2*D_j
                    o_ += 0.5/(b*b) * self.g2a*torque
                    
                    
            v[i]      += v_[0]
            v[i+Np]   += v_[1]
            v[i+2*Np] += v_[2]
            
            o[i]      += o_[0]
            o[i+Np]   += o_[1]
            o[i+2*Np] += o_[2]
        return
        
        
    
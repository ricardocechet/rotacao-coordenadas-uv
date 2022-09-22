# -*- coding: utf-8 -*-
"""

@author: CKT
"""

import numpy as np
        

def veldir_uv(velocidade, direcao):
    """
    Tranforma velocidade e direção em componentes u e v
        veldir_uv(velocidade, direcao)
        
            Parametros Entrada:
                velocidade, direção
                
            Retorna componentes:
                u, v
    """
    
    u = velocidade * np.sin(direcao * (np.pi / 180))
    v = velocidade * np.cos(direcao * (np.pi / 180))

    return u,v



def uv_uTvT(u, v, theta):
    """
    Tranforma componentes u e v em componentes u e v + Theta
        uv_uTvT(u, v, theta)
        
            Parametros Entrada:
                u, v, theta(ângulo de adequamento)
                
            Retorna componentes:
                u, v
    """
    # Adequa u e v + theta
    uT = (u * np.cos(np.deg2rad(theta))) + (v * np.sin(np.deg2rad(theta)))
    vT = (u * -np.sin(np.deg2rad(theta))) + (v * np.cos(np.deg2rad(theta)))  
    
    ## Caso seja necessário utilizar theta negativo (theta = -45)
    # cros0 = (u0 * np.cos(np.deg2rad(theta))) + (v0 * -np.sin(np.deg2rad(theta)))
    # long0 = (u0 * np.sin(np.deg2rad(theta))) + (v0 * np.cos(np.deg2rad(theta)))  

    return uT, vT



def uv_veldir(u,v):
    """
    Tranforma componentes u e v em velocidade e direção
        uv_veldir(u,v)
        
            Parametros Entrada:
                u, v, theta(ângulo de adequamento)
                
            Retorna componentes:
                velocidade, direção
    """
    if u == 0 and v != 0: 
        u = 0.00000001;
    elif v == 0 and u != 0:
        v = 0.00000001;
    elif u == 0 and v == 0:
        u = 0.00000001;
        
    if u > 0 and v > 0:
        direcao = np.arctan(abs(u / v)) * (180 / np.pi)
    elif u < 0 and v > 0:
        direcao = 360 - np.arctan(abs(u / v)) * (180 / np.pi)
    elif u < 0 and v < 0:
        direcao = 180 + np.arctan(abs(u / v)) * (180 / np.pi)
    elif u > 0 and v < 0:
        direcao = 180 - np.arctan(abs(u / v)) * (180 / np.pi)              
    elif u==0 and v==0:
        direcao = np.NaN

    velocidade = np.sqrt(u**2 + v**2)
        
    return velocidade, direcao



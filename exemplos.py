# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:59:29 2022

@author: CKT
"""

import numpy as np
import matplotlib.pyplot as plt
from windrose import WindroseAxes
import matplotlib.cm as cm

import vel_dir_u_v 



# =============================================================================
# Teste 
# =============================================================================

# Direções 
dirX = [0,12,45,90,135,180,245,270,300,359,360]
# Velocidades 
velX = np.ones(len(dirX))
velX = [12,24,12,24,12,24,12,24,12,24,12]

# Defasagem ou adequamento das direções
theta = 45


# Variáveis utilizadas
u, v = [],[]
uT, vT = [],[]
for i in range(len(dirX)):
    
    # Tranforma velocidade e direção em componentes u e v
    u0, v0 = vel_dir_u_v.veldir_uv(velX[i], dirX[i])

    u = np.append(u, u0)
    v = np.append(v, v0)
    

    # Adequa u e v + tetha
    uT0, vT0 = vel_dir_u_v.uv_uTvT(u0, v0, theta)
    uT = np.append(uT, uT0)
    vT = np.append(vT, vT0)
    
    del u0, v0, uT0, vT0

    
# Validação
vel, dire = [],[]
velT, direT = [],[]
for i in range(len(u)):
    velo, direc = vel_dir_u_v.uv_veldir(u[i], v[i])
    
    vel = np.append(vel,velo)
    dire = np.append(dire,direc)
    
    veloT, direcT = vel_dir_u_v.uv_veldir(uT[i], vT[i])

    velT = np.append(velT, veloT)
    direT = np.append(direT, direcT)
    
    del velo, direc, veloT, direcT
    
    
    
    
    
# PLOTS

fig = plt.figure(figsize=(15,12))
ax1 = plt.subplot(221)
ax1.quiver(u, v, color='k')
ax1.plot(u, color='r', marker='.', linestyle = '--')
ax1.plot(v, color='b', marker='.', linestyle = '--')
ax1.axhline(y = 0, color='grey', linestyle = '--', alpha =0.2)
ax1.legend(['Vetores', 'Componente u', 'Componente v'], loc = 'lower left')
ax1.set_title('Componentes u - v ')

_=[ax1.text(i, max([u.max(), v.max()]) + 1, f'{"{:1.0f}".format(dire[i])}º\
\n{"{:1.1f}".format(vel[i])}', horizontalalignment = 'center', size=8, color='gray') for i in range(len(dire))]
ax1.set_ylim([min([u.min(), v.min()]) - 10, max([u.max(), v.max()]) + 10])
ax1.set_xlim([-3., len(dire)])
ax1.text(-2.8, max([u.max(), v.max()]) + 1, 'Direção º:\
\nVelocidade cm/s:', multialignment = 'left', size=8, color='gray')
ax1.set_xticks([])
ax1.set_ylabel('Intensidades u - v \ncm/s')


ax2 = plt.subplot(223)
ax2.quiver(uT, vT, color='k')
ax2.plot(uT, color='r', marker='.', linestyle = '--')
ax2.plot(vT, color='b', marker='.', linestyle = '--')
ax2.axhline(y = 0, color='grey', linestyle = '--', alpha =0.2)
ax2.legend(['Vetores', 'Componente u + tetha', 'Componente v + tetha'], loc = 'lower left')
ax2.set_title(f'Componentes u - v -> tetha({theta})')

_=[ax2.text(i, max([uT.max(), vT.max()]) + 1, f'{"{:1.0f}".format(direT[i])}º\
\n{"{:1.1f}".format(velT[i])}', multialignment = 'center', size=8, color='gray') for i in range(len(direT))]
ax2.set_ylim([min([uT.min(), vT.min()]) - 10, max([uT.max(), vT.max()]) + 10])
ax2.set_xlim([-3., len(direT)])
ax2.text(-2.8, max([uT.max(), vT.max()]) + 1, 'Direção º:\
\nVelocidade cm/s:', multialignment = 'left', size=8, color='gray')
ax2.set_xticks([])
ax2.set_ylabel('Intensidades u - v \ncm/s')


bins = np.arange(10, 30, 1)

ax11 = fig.add_subplot(222, projection='windrose')
ax11.bar(dire, vel, normed=True, opening=0.9, edgecolor='white', blowto = False)
# ax11.contourf(dire, vel, bins=bins, cmap=cm.hot, normed=False, edgecolor='white', blowto = False)


ax22 = fig.add_subplot(224, projection='windrose')
ax22.bar(direT, velT, normed=True, opening=0.9, edgecolor='white', blowto = False)
# ax22.contourf(dire, vel, bins=bins, cmap=cm.hot, normed=False, edgecolor='white', blowto = False)





    
    
    
    
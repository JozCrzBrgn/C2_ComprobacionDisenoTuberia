'''
Función:
    Comprobación de diseño de tuberías simples.

Descripción:
    En éste tipo de problemas se conocen las propiedades del material de la tubería (rugosidad absoluta,
    longitud,diámetro) al igual que todos sus accesorios, sus coeficientes de pérdidas menores, las 
    propiedades del fluido (densidad y viscosidad dinámica). Además se conoce la energía impulsora, 
    ya sea una altura gravitacional (H) o una bomba.

Estructura de la función:
    Q_ComprobacionDiseno(L,d,ks,H,km,p,u,z2)

Inputs:
    L   = Longitud de la tubería (metros).
    d   = Diámetro de la tubería (metros).
    ks  = Rugosidad Absoluta (metros).
    H   = Diferencia de nivel entre los tnques de abastecimiento de agua (metros).
    km  = Coeficiente global de pérdidas menores de los accesorios (adimensional).
    u   = Viscosidad dinámica (m^2/seg)
    z2  = Diferencia de altura vertical entre la toma de la tubería y la planta (metros).

Output:
    Q   = Caudal que fluye por la tubería (Lps)

Programado por:
    Ing. Josue Emmanuel Cruz Barragan
'''

'''Librerias'''
import math

'''Función principal'''
def Q_ComprobacionDiseno(L,d,ks,H,km,u,z2):

    ''' Constantes '''
    g = 9.807 # Aceleración de la gravedad

    '''
    Velocidad del caudal que pasa por la tubería
    '''
    def velocidad(ks,d,u,L,g,hf):
        v1 = ks / (3.7 * d)
        v21 = 2.51 * u * math.sqrt(L)
        v22 = d * math.sqrt(2 * g * d * hf)
        v3 = v1 + v21 / v22
        v4 = math.log(v3, 10)
        v5 = -2 * math.sqrt(2 * g * d * hf) / math.sqrt(L)
        return v5 * v4

    '''
    Energía por unidad de peso perdida en los accesorios
    '''
    def Suma_hm(km, V, g):
        return km * (V ** 2) / (2 * g)

    '''
    Pérdidas de energía por fricción
    '''
    def Perd_friccion(H, z2, S_hm):
        return H - z2 - S_hm

    '''
    Área de la tubería
    '''
    def Area(d):
        return 0.25 * math.pi * (d ** 2)

    '''
    Caudal que se mueve por la tubería
    '''
    def Gasto(A, V):
        return A * V

    '''
    Pérdida de energía por fricción
    '''
    tol = 0.0001  # Tolerancia de error en el cíclo While
    error = 100  # Error inicial
    cont = 0 # Contador
    while error >= tol:
        if cont < 1:
            hf = Perd_friccion(H, z2, 0)
            V = velocidad(ks, d, u, L, g, hf)
            S_hm = Suma_hm(km, V, g)
            cont += 1
        else:
            hf1 = hf
            hf2 = Perd_friccion(H, z2, S_hm)
            hf = hf2
            V = velocidad(ks, d, u, L, g, hf)
            S_hm = Suma_hm(km, V, g)
            error = abs((hf2 - hf1) / hf2) * 100

    A = Area(d)
    Q = Gasto(A, V)
    return [Q * 1000,V]
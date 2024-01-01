from flask import request
import math


def calcul_entrop(probabilities):
    N = len(probabilities)
    H = 0
    for i in range(N):
        H += probabilities[i]*math.log2(1/probabilities[i])
    print(H)
    return H


def calcul_entropie_conj(sources):
    entropie = 0
    i = 0
    while i < len(sources):
        j = 0
        while j < len(sources[i]):
            entropie += round(-sources[i][j] * math.log2(sources[i][j]), 2)
            j += 1
        i += 1
    return entropie


def calcul_quantité_info(probabilites):
    for i in range(len(probabilites)):
        I = round(-probabilites[i] * math.log2(probabilites[i]), 2)
    return I


def calcul_quantité_info_mutuelle(sources, Source_X, Source_Y):
    quantInfo = 0
    i = 0
    while i < len(sources):
        j = 0
        while j < len(sources[i]):
            quantInfo += round(sources[i][j] * math.log2(sources[i]
                               [j] / (Source_X[i] * Source_Y[j])), 2)
            j += 1
        i += 1
    return quantInfo


def calcul_entropie_cond_x_y(srcY, srcXY):
    Hx_y = calcul_entropie_conj(srcXY) - calcul_entrop(srcY)
    return Hx_y


def calcul_entropie_cond_y_x(srcX, srcXY):
    Hy_x = calcul_entropie_conj(srcXY) - calcul_entrop(srcX)
    return Hy_x

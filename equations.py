import constants as c
import math


def energyWithVel(V, r):
    return (pow(V, 2)/2) - (c.mu/r)


def energyWithSemi(a):
    return -c.mu/(2*a)


def visVivaVel(r, a):
    return math.sqrt(c.mu*((2/r)-(1/a)))


def semiLatusRectum(a, e):
    return a*(1-pow(e, 2))


def radiusPeriapsis(a, e):
    return a*(1-e)


def radiusApoapsis(a, e):
    return a*(1+e)


def eccentricity(H, a):
    return math.sqrt(1-(pow(H, 2)/(a*c.mu)))


def trueAnomaly(a, e, r):
    return math.acos((semiLatusRectum(a, e)/(r*e))-(1/e))


def radiusOrbitEqq(e, a, ta):
    return semiLatusRectum(a, e)/(1+e*math.cos(ta))


def radisVector(r, ta):
    r = [r*math.cos(ta), r*math.sin(ta)]
    return r

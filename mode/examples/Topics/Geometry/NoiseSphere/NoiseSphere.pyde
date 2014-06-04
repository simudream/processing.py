"""
Noise Sphere
by David Pena.

Uniform random distribution on the surface of a sphere.
"""
from Pelo import Pelo

halfWidth = None
halfHeight = None
radius = None
lista = None
cuantos = 4000
rx = 0
ry = 0


def setup():
    size(640, 360, P3D)
    halfWidth = width / 2
    halfHeight = height / 2
    radius = height / 3
    lista = [Pelo(radius) for _ in range(cuantos)]
    noiseDetail(3)


def draw():
    background(0)
    translate(halfWidth, halfHeight)

    rxp = ((mouseX - (halfWidth)) * 0.005)
    ryp = ((mouseY - (halfHeight)) * 0.005)
    rx = (rx * 0.9) + (rxp * 0.1)
    ry = (ry * 0.9) + (ryp * 0.1)
    rotateY(rx)
    rotateX(ry)
    fill(0)
    noStroke()
    sphere(radius)

    for i in range(cuantos):
        lista[i].dibujar()

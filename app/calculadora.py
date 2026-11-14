"""Operaciones aritméticas de la calculadora."""

# IMPORTANTE: reemplaza ??? con los nombres completos de los 3 integrantes,
# separados por " | " y en el mismo orden de la sección Integrantes del README.
# Ejemplo: "Ana María Pérez | Luis Andrés Gómez | Sara Restrepo Ríos"
AUTOR = "Quinnie Villarreal | Lina Ballesteros | Alejandro Rios"


def sumar(a, b):
    """Devuelve la suma de los dos números."""
    return a + b


def restar(a, b):
    """Devuelve la diferencia de los dos números."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de los dos números."""
    return a * b


def dividir(a, b):
    """Devuelve el cociente o rechaza la división por cero."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

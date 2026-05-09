import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# VARIABLE

x = sp.symbols('x')

# CHOISIR UNE FONCTION

# Tu peux changer ici la fonction
f = x**3 - 3*x**2 + 2

print("Fonction f(x) = ", f)

# DOMAINE DE DEFINITION

domaine = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)

print("\nDomaine de définition :")
print(domaine)


# DERIVEE

f_prime = sp.diff(f, x)

print("\nDérivée f'(x) = ")
print(f_prime)


# POINTS CRITIQUES

points_critiques = sp.solve(f_prime, x)

print("\nPoints critiques :")
print(points_critiques)


# ETUDE DU SIGNE

print("\nEtude de variation :")

for point in points_critiques:

    test_gauche = point - 1
    test_droite = point + 1

    val_gauche = f_prime.subs(x, test_gauche)
    val_droite = f_prime.subs(x, test_droite)

    if val_gauche > 0 and val_droite < 0:
        print(f"Maximum local en x = {point}")
        print("Valeur :", f.subs(x, point))

    elif val_gauche < 0 and val_droite > 0:
        print(f"Minimum local en x = {point}")
        print("Valeur :", f.subs(x, point))


# CROISSANCE / DECROISSANCE

intervals = sp.solve_univariate_inequality(f_prime > 0, x)

print("\nFonction croissante sur :")
print(intervals)

intervals2 = sp.solve_univariate_inequality(f_prime < 0, x)

print("\nFonction décroissante sur :")
print(intervals2)


# GRAPHIQUE


# Transformer la fonction sympy en fonction numpy
f_numpy = sp.lambdify(x, f, "numpy")

# Valeurs x
X = np.linspace(-2, 4, 400)

# Valeurs y
Y = f_numpy(X)

# Dessin
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])

plt.title("Test graphique")

plt.savefig("graphique.png", dpi=300)
print("Fichier sauvegardé !")

plt.show()
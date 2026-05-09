import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# --- VARIABLE ---
x = sp.symbols('x')

# --- CHOISIR UNE FONCTION ---
f = x**3 - 3*x**2 + 2
print("Fonction f(x) = ", f)

# --- DOMAINE DE DEFINITION ---
domaine = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)
print("\nDomaine de définition :")
print(domaine)

# --- DERIVEE ---
f_prime = sp.diff(f, x)
print("\nDérivée f'(x) = ")
print(f_prime)

# --- POINTS CRITIQUES ---
points_critiques = sp.solve(f_prime, x)
print("\nPoints critiques :")
print(points_critiques)

# --- ETUDE DU SIGNE ---
print("\nEtude de variation :")
for point in points_critiques:
    test_gauche = point - 0.1
    test_droite = point + 0.1
    val_gauche = f_prime.subs(x, test_gauche)
    val_droite = f_prime.subs(x, test_droite)

    if val_gauche > 0 and val_droite < 0:
        print(f"Maximum local en x = {point}")
        print("Valeur :", f.subs(x, point))
    elif val_gauche < 0 and val_droite > 0:
        print(f"Minimum local en x = {point}")
        print("Valeur :", f.subs(x, point))

# --- CROISSANCE / DECROISSANCE ---
intervals = sp.solve_univariate_inequality(f_prime > 0, x)
print("\nFonction croissante sur :")
print(intervals)

intervals2 = sp.solve_univariate_inequality(f_prime < 0, x)
print("\nFonction décroissante sur :")
print(intervals2)

# --- GRAPHIQUE (LA CORRECTION EST ICI) ---

# 1. On transforme la fonction Sympy en fonction numérique (Numpy)
f_numpy = sp.lambdify(x, f, "numpy")

# 2. On génère 400 points pour avoir une courbe lisse
# On élargit l'intervalle de -2 à 4 pour bien voir les variations
X_fine = np.linspace(-2, 4, 400)

# 3. On calcule les Y correspondants
Y_fine = f_numpy(X_fine)

# 4. Dessin
plt.figure(figsize=(8, 5))
plt.plot(X_fine, Y_fine, label="f(x)", color='blue', linewidth=2)

# Ajout des axes pour la clarté
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.title("Graphique de la fonction f(x) = x³ - 3x² + 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Sauvegarde et affichage
plt.savefig("graphique.png")
print("\nGraphique mis à jour et sauvegardé dans 'graphique.png' !")
plt.show()
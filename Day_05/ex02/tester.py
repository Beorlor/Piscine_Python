from callLimit import callLimit


@callLimit(3)  # Décore la fonction avec une limite de 3 appels
def f():
    print("f()")


@callLimit(1)  # Décore la fonction avec une limite de 1 appel
def g():
    print("g()")


for i in range(3):
    f()  # Appelé trois fois, la troisième passe encore
    g()  # Appelé une seule fois, les deux appels suivants affichent une erreur

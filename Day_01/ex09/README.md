# ft_package

Ce package **ft_package** est un exemple minimal pour la Piscine Python.  
Il définit une fonction `count_in_list(lst, item)` qui compte le nombre d’occurrences de `item` dans la liste `lst`.

## Caractéristiques

- Nom : **ft_package**
- Version : **0.0.1**
- Auteur : **jedurand**
- Licence : **MIT**

## Récupérer le package

Pour récupérer les sources, vous pouvez cloner ou télécharger ce dépôt, puis exécuter la commande de build.

```bash
python -m build
```

Cela va générer des archives dans le dossier `dist/` (par exemple `ft_package-0.0.1-py3-none-any.whl`).

## Installation

Pour installer le package via `pip` localement :

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

ou, si vous préférez le sdist :

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Vérifier l'installation

Une fois le package installé, vous pouvez lister les paquets installés :

```bash
pip list
```

et/ou afficher toutes les métadonnées :

```bash
pip show -v ft_package
```

## Exemple de programme de test

Créez un fichier `test_count.py` avec le contenu suivant :

```python
from ft_package import count_in_list

def main():
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # Doit afficher 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Doit afficher 0

if __name__ == "__main__":
    main()
```

Ensuite, exécutez :

```bash
python test_count.py
```

Le programme devrait afficher :

```text
2
0
```


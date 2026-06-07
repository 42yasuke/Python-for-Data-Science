# Python for Data Science - 42 School Piscine

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-brightgreen.svg)](https://flake8.pycqa.org/)
[![Data Oriented Design](https://img.shields.io/badge/Module-DOD-purple.svg)](https://github.com/42yasuke/Python-for-Data-Science)

Ce dépôt contient l'intégralité de mon travail pour la **Piscine Python for Data Science** de l'école 42. Ce programme intensif couvre les fondamentaux de Python jusqu'à la manipulation de données, en passant par la programmation orientée objet et les décorateurs.

## 📚 Table des matières
- [Python 0 - Starting](#python-0---starting)
- [Python 1 - Array](#python-1---array)
- [Python 2 - DataTable](#python-2---datatable)
- [Python 3 - OOP](#python-3---oop)
- [Python 4 - Data Oriented Design (DOD)](#python-4---data-oriented-design-dod)

## 🗂️ Modules

### Python 0 - Starting
Les bases de la syntaxe Python : fonctions, boucles, listes en compréhension, et gestion d'erreurs.

| Exercice | Concept | Statut |
| :--- | :--- | :---: |
| `ex00` | `*args`, `**kwargs`, statistiques de base | ✅ |
| `ex01` | Fonctions, portée des variables | ✅ |
| `ex02` | Récursivité, structures de données | ✅ |
| `ex03` | Filtres, `map`, `lambda` | ✅ |
| `ex04` | Manipulation de dictionnaires | ✅ |
| `ex05` | `any`, `all`, compréhension | ✅ |
| `ex06` | Jeu de la vie (Game of Life) | ✅ |
| `ex07` | Algorithmes de tri | ✅ |

### Python 1 - Array
Introduction à la manipulation de listes et de tableaux, avec un focus sur les performances.

| Exercice | Concept | Statut |
| :--- | :--- | :---: |
| `ex00` | Somme, produit, moyenne sur `list` | ✅ |
| `ex01` | Vecteurs, produit scalaire | ✅ |
| `ex02` | Matrices, multiplication | ✅ |
| `ex03` | Slicing avancé | ✅ |
| `ex04` | Compréhension de listes vs `map` | ✅ |
| `ex05` | Génération de nombres pseudo-aléatoires | ✅ |

### Python 2 - DataTable
Découverte de la bibliothèque **Pandas** pour l'analyse de données tabulaires.

| Exercice | Concept | Statut |
| :--- | :--- | :---: |
| `ex00` | Chargement de fichiers CSV | ✅ |
| `ex01` | Sélection et filtrage (`loc`, `iloc`) | ✅ |
| `ex02` | Nettoyage et transformation de données | ✅ |
| `ex03` | Agrégations et pivot tables | ✅ |
| `ex04` | Fusion de DataFrames (`merge`, `join`) | ✅ |

### Python 3 - OOP
Programmation Orientée Objet : classes, héritage, encapsulation et polymorphisme.

| Exercice | Concept | Statut |
| :--- | :--- | :---: |
| `ex00` | Premières classes | ✅ |
| `ex01` | Getters, setters, propriétés | ✅ |
| `ex02` | Héritage simple | ✅ |
| `ex03` | Héritage multiple, MRO | ✅ |
| `ex04` | Méthodes magiques (`__str__`, `__add__`) | ✅ |

### Python 4 - Data Oriented Design (DOD)
Conception orientée données, décorateurs, dataclasses et closures.

| Exercice | Fichier(s) | Concept | Statut |
| :--- | :--- | :--- | :---: |
| **`ex00`** | `statistics.py` | Calcul de statistiques (moyenne, médiane, quartiles, variance, std) avec `*args` / `**kwargs` | ✅ |
| **`ex01`** | `in_out.py` | Closure : fonction retournant une fonction accumulatrice (`square`, `pow`) | ✅ |
| **`ex02`** | `callLimit.py` | Décorateur paramétré limitant le nombre d'appels d'une fonction | ✅ |
| **`ex03`** | `new_student.py` | Dataclass `Student` avec génération automatique de `login` et `id` | ✅ |

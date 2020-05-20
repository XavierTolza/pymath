# Auteur: Xavier Tolza (xto@ffly4u.com)
# date: 20/05/20
#
# Ce fichier de setup facilite la conception de modules python:
# Il permet de récupérer les dépendances directement dans le fichier requirements.txt,
# de compiler des fichiers C et Cython s'il y en a.
# Pour l'utiliser correctement, veuillez mettre vos dépendances dans un fichier requirements.txt
# à la racine du projet au format suivant:
# git+(ssh|https)://git@github.com/xxxxx/xxxxxx#egg=package_name

# Pour compiler les fichiers C ou Cython pour les tester (déjà vérifier que cython est installé: pip install cython)
# puis la commande est la suivante:
# python setup.py build_ext --inplace

import os
import re
from distutils.extension import Extension
from multiprocessing import cpu_count
from os import listdir
from os.path import join, splitext, basename

from setuptools import setup

name = "pymath"  # Le nom du paquet python
base_folder = name  # Le nom du dossier qui contient le module python

info = dict(
    name=name,
    version='1.0',
    description='Wrapper around numpy to add some useful functions',
    author='Xavier Tolza',
    author_email='tolza.xavier@gmail.com',
)

# On regarde si le mode debug est activé
DEBUG = os.environ.get("DEBUG")
DEBUG = DEBUG is not None and DEBUG == "1"
if DEBUG:
    print("Debug enabled")

# En cas de compilation de code C il faut connaitre le chemin vers les librairies numpy
try:
    import numpy

    numpy_include_path = numpy.get_include()
except ImportError:
    import sys

    numpy_include_path = join(sys.executable, "site-packages/numpy/core/include/numpy")


# Compilation de code C. Cette section cherche des fichiers cython à compiler
def generate_extensions(filenames):
    extra_compile_args = ['-fopenmp']
    if DEBUG:
        extra_compile_args.append("-O0")
    extensions = []
    for i in filenames:
        if splitext(basename(i))[1] == ".pyx":
            ext = cythonize(join(base_folder, i), annotate=DEBUG, gdb_debug=DEBUG, nthreads=cpu_count())[0]
        else:
            ext = Extension(join(base_folder, i.split(".")[0]).replace("/", "."), [join(base_folder, i)],
                            language="c++", extra_compile_args=extra_compile_args, include_dirs=[numpy_include_path],
                            extra_link_args=['-fopenmp'])
        extensions.append(ext)
    return extensions


kwargs = {}
files = listdir(base_folder)
try:
    from Cython.Build import cythonize

    r = re.compile(".+\.pyx")
    try:
        cython_files = [i for i in listdir(base_folder) if r.fullmatch(i) is not None]
    except AttributeError:
        cython_files = [i for i in listdir(base_folder) if r.match(i) is not None]
    if len(cython_files):
        extensions = generate_extensions(cython_files)
        kwargs.update(dict(
            ext_modules=extensions
        ))
except ImportError:
    # Cython not present, compiling C files only
    r = re.compile(".+\.c(pp)?")
    c_files = [i for i in files if r.fullmatch(i)]
    extensions = generate_extensions(c_files)
    kwargs.update(dict(
        ext_modules=extensions,
    ))

# On récupère la liste des requirements depuis le fichier requirements
with open("requirements.txt", "r") as fp:
    requirements = fp.read().splitlines()

# On transforme les requirements qui sont des urls Git
required = []
EGG_MARK = '#egg='
for line in requirements:
    if line.startswith('-e git:') or line.startswith('-e git+') or \
            line.startswith('git:') or line.startswith('git+'):
        if EGG_MARK in line:
            package_name = line[line.find(EGG_MARK) + len(EGG_MARK):]
            required.append(f"{package_name} @ {line.split(EGG_MARK)[0]}")
            # dependency_links.append(line)
        else:
            raise ValueError('Dependency to a git repository should have the format:\n'
                             'git+ssh://git@github.com/xxxxx/xxxxxx#egg=package_name')
    else:
        required.append(line)

setup(
    packages=[base_folder],
    install_requires=required,
    **info,
    **kwargs
)

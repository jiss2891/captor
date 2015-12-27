#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


def main():
    """
    Note: Its important to set the correct language according to the system;
    to ensure the correct search on dpkg list of dependencies.
    """
    lang = 'ES'
    if lang == 'ES':
        prompt = 'Paquete a descargar: '
        depends_word = 'Depende'
        success = "Los paquetes se descargaron correctamente. Ahora puedes instalarlo \n " + \
                  "usando dpkg -i *.deb dentro del directorio creado."
    else:
        prompt = 'Package to download: '
        depends_word = 'Depends'  # TODO: check if Depends is correct.
        success = "Packages succesfully downloaded. Now you can install it \n " + \
                  "using dpkg -i *.deb inside the created directory"

    pack_name = raw_input(prompt)
    pack_dir = pack_name + '__captor'

    try:
        os.mkdir(pack_dir)
    except Exception:
        print 'Se usará el directorio ya existente..'
    os.chdir(pack_dir)

    # downloading package
    os.system("sudo aptitude download " + pack_name)
    # catching list of dependencies
    os.system("sudo apt-cache depends " + pack_name + " | grep " + depends_word + " | awk '{ print $2 }' | xargs aptitude download $1")

    print(success)

if __name__ == '__main__':
    main()

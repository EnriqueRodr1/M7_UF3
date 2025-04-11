#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def main():
    """Punto de entrada principal para la administración de Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TIC_BCN_inicials.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y disponible en su entorno PYTHONPATH?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
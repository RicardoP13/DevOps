## Tarea 2

- Descomprimir el SDK de VirtualBox
- Buscar en el archivo descomprimido la carpeta "installer" y abrir terminal
- Ejecutar el comando `python vboxapisetup.py install` o `python3 vboxapisetup.py install` 
- Variables de entorno:
	- `export PYTHONPATH=$PYTHONPATH:/usr/lib/virtualbox/:/usr/lib/virtualbox/sdk/bindings/xpcom/python/`
	- `export VBOX_INSTALL_PATH=$(which virtualbox)`


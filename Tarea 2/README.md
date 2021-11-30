## Tarea 2

- Descomprimir el SDK de VirtualBox
- Buscar en el archivo descomprimido la carpeta "installer" y abrir terminal
- Ejecutar el comando `python vboxapisetup.py install` o `python3 vboxapisetup.py install` 
- Variables de entorno:
	- `export PYTHONPATH=$PYTHONPATH:/usr/lib/virtualbox/:/usr/lib/virtualbox/sdk/bindings/xpcom/python/`
	- `export VBOX_INSTALL_PATH=$(which virtualbox)`
- COMANDO SLI:
	- Listar maquinas virtuales: `python app.py list` o `python3 python app.py list`
	- Crear maquina virtual: `python app.py create <nombre_nueva_VM>` o `python3 python app.py create <nombre_nueva_VM>`
	- Levantar maquina virtual: `python app.py up <nombre_VM_existente>` o `python3 python app.py create <nombre_VM_existente>`
	- Eliminar maquina virtual: `python app.py delete <nombre_VM_existente>` o `python3 python app.py delete <nombre_VM_existente>`
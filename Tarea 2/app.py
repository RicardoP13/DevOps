import virtualbox
import os
import sys

vbox = virtualbox.VirtualBox()

if len(sys.argv)>1 :
	if sys.argv[1] == 'list':
		print("****MY VMS****")
		[print(m.name) for m in vbox.machines]
	elif sys.argv[1] == 'up':
		print("Standing up VM...")
		try:
			session = virtualbox.Session()
			machine = vbox.find_machine(sys.argv[2])
			progress = machine.launch_vm_process(session, "headless", [])
			progress.wait_for_completion()
		except:
  			print("Couldn't Stand up the VM")
	elif sys.argv[1] == 'delete':
		print("Deleting VM...")
		try:
			os.system('vboxmanage unregistervm "'+sys.argv[2]+'" --delete')
		except:
  			print("Couldn't delete the VM")
	elif sys.argv[1] == 'create':
		print("Creating VM...")
		try:
			os.system('vboxmanage createvm --name '+sys.argv[2]+' --register')
		except:
			print("Couldn't create the VM")
	else :
		print ("Invalid argument")
else:
	print("No Arguments")
#FedoraServer34
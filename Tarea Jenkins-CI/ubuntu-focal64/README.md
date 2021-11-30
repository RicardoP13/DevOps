# Development Machine

This vagrant implementation is intended to be used by the members of a software Development team, it reproduces locally a CI and deployment nodes that could be located remotely.

## Requirements

- VirtualBox 6.1+
- Vagrant

Once Vagrant is installed, install docker-compose plugin:

```
vagrant plugin install vagrant-docker-compose
```

## Startup

Go to the directory where the `Vagrantfile` files are and execute the following commands:

```sh
VAGRANT_VAGRANTFILE=Vagrantfile.CI vagrant up
```

## Notes

- Make sure the image is being downloaded to a hard disk.
- Make sure no other VMs or services are using the ports and/or network settings (like IP addresses) specified in the Vagrantfile(s).

### For Windows users

  - Sometimes the VM is not fully loaded, wait until the system prompt is showed in the VBox terminal, then execute the `vagrant up` command from the **Startup** section.


Vagrant.configure(2) do |config|
  config.vm.provider "virtualbox" do |v|
  	v.memory = 2048
  end
  config.vm.box = "fedora/24-cloud-base"
  config.vm.hostname = 's3.server'
  config.vm.network "private_network", ip: "192.168.50.4"
  config.vm.network "forwarded_port", guest: 80, host: 15000
  config.vm.provision "shell", inline: "sudo dnf install python python-dnf libselinux-python -y"  
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "create_scality.yml"
  end
end

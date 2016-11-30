
Vagrant.configure(2) do |config|
  config.vm.provider "virtualbox" do |v|
  	v.memory = 2048
  end
  config.vm.box = "fedora/24-cloud-base"
  config.vm.hostname = 's3.server'
  config.vm.network "private_network", ip: "192.168.50.4"
  config.vm.network "forwarded_port", guest: 80, host: 15000

  config.vm.provision "shell", inline: "sudo dnf install python python-dnf libselinux-python -y"
  config.vm.provision "shell", inline: "yum install make gcc* -y"
  config.vm.provision "shell", inline: "sudo dnf install git -y"
  config.vm.provision "shell", inline: "sudo dnf install npm -y"
  config.vm.provision "shell", inline: "sudo pip install awscli"
  config.vm.provision "shell", inline: "sudo pip install boto"
  config.vm.provision "shell", inline: "git clone https://github.com/scality/S3"
  config.vm.provision "shell", inline: "sudo dnf install vim -y"
  config.vm.provision "shell", inline: "cd S3 && sudo npm install"
  config.vm.provision "shell", inline: "cd S3 && sed -i '26s/.*/       \042bootstrap\042: [\042192.168.50.4\042]  /' config.json"
end

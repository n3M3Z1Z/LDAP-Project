Vagrant.configure("2") do |config|
  # VM: LDAP Server
  config.vm.define "LDAP_Server" do |ldap|
    ldap.vm.box = "ubuntu/bionic64"
    ldap.vm.network "private_network", ip: "192.168.56.100"
    ldap.vm.provider "virtualbox" do |vb|
      vb.name = "LDAP_Server"
      vb.memory = 2048  # Set memory as needed
      vb.cpus = 2
    end
  end
end

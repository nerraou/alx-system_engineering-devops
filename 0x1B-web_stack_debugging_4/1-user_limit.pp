# update holberton nofile

# update hard nofile
exec { 'Update hard nofile':
  command => "sed -i 's/nofile 5$/nofile 4096/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# update soft nofile
exec { 'Update soft nofile':
  command => "sed -i 's/nofile 4$/nofile 4096/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

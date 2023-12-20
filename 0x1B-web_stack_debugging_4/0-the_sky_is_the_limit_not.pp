# Increase max nginx max open files limit

# edit ULMIT
exec { 'nginx set max open files':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
-> exec { 'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

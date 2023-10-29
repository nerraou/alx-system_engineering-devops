# Create ssh_config

$ssh_config_content = @(EOF)
IdentityFile ~/.ssh/school
PasswordAuthentication no
EOF 

file { 'ssh config':
  ensure  => file,
  path    => '/etc/ssh/ssh_config',
  content => $ssh_config_content,
}

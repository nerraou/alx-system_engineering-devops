# execute command

exec { 'kill process':
  command  => 'pkill killmenow',
  provider => shell,
  path     => ['/usr/bin']
}

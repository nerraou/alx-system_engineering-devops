# fix apache 500 response

exec { 'fix worpress wp-settings.php':
  command  => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
  provider => shell,
  path     => ['/bin']
}

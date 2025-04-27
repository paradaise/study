<?php
define('DB_NAME', 'testdb');
define('DB_USER', 'testuser');
define('DB_PASSWORD', 'new_testpass');
define('DB_HOST', 'mysql');
define('DB_CHARSET', 'utf8mb4');
define('DB_COLLATE', '');

$table_prefix = 'wp_';

define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);

if (!defined('ABSPATH')) {
    define('ABSPATH', __DIR__ . '/');
}

require_once ABSPATH . 'wp-settings.php';

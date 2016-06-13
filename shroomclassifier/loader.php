<?php
/**
 * Created by PhpStorm.
 * User: Admin
 * Date: 2016-05-15
 * Time: 13:49
 */
spl_autoload_register(function ($class_name) {
    include './classes/' . strtolower($class_name) . '.php';
});
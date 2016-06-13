<?php

/**
 * Created by PhpStorm.
 * User: Admin
 * Date: 2016-05-15
 * Time: 13:55
 */
class Basket
{
    private static $allowedCapacity;

    public $mushrooms;

    public function __construct($mushrooms) {
        $mushrooms = json_decode(file_get_contents($mushrooms), true);
        $mushrooms = $mushrooms['actor']['basket']['contains'];

        $this->mushrooms = array_map( function($data) {
            return new Mushroom($data);
        }, $mushrooms);
    }

    public static function setCapacity($capacity) {
        self::$allowedCapacity = $capacity;
    }

    public static function getMaxCapacity() {
        return (int)self::$allowedCapacity;
    }
}
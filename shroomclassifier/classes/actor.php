<?php
/**
 * Created by PhpStorm.
 * User: Admin
 * Date: 2016-05-15
 * Time: 13:55
 */
class Actor
{
    public $basket;

    public function __construct($path) {
        $this->basket = new Basket($path);
    }
}
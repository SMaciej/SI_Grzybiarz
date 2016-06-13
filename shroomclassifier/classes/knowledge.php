<?php

/**
 * Created by PhpStorm.
 * User: Admin
 * Date: 2016-05-15
 * Time: 17:49
 */
class Knowledge
{
    private $mushroom;

    public function __construct($path) {
        $this->config = json_decode(file_get_contents($path), true);

        $this->mushroom = array_map( function($data) {
            $mushroom = new Mushroom($data);
            $mushroom->save();
            return $mushroom;
        }, $this->config['actor']['basket']['contains']);
    }

    public function getMushrooms() {
        return $this->mushroom;
    }
}
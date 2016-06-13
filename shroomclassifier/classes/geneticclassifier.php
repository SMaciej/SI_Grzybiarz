<?php

/**
 * Created by PhpStorm.
 * User: Admin
 * Date: 2016-05-16
 * Time: 11:12
 */
class GeneticClassifier
{
    private $maxPopulation = 10;
    private $maxGenerations = 10;

    private $basket;
    private $result;

    public function __construct($basket) {
        $this->basket = $basket;
        foreach ($basket as $i => $ix ) {
            foreach ($ix as $index => $mushroom) {
                echo'Mushroom #'.($index + 1).
                    ' is '.$mushroom->getProbablyName().
                    ', with tastiness: '.$mushroom->getTastiness().
                    "\n";
            }
        }
    }

    public function produceNew() {

    }
}
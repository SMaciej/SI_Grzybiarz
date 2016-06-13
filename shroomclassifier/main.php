<?php

require_once './loader.php';

$config = new Config('../config.json');
$actor = new Actor($argv[1]);

if (isset($argv[2]) && $argv[2] === 'kn') {
    $knowledge = new Knowledge('./knowledge.json');
}

# $classifier = new GeneticClassifier($actor->basket);
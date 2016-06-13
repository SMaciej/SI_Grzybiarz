<?php

require_once './loader.php';

$config = new Config('../config.json');
$actor = new Actor($argv[1]);

if (isset($argv[2]) && $argv[2] === 'kn') {
    $knowledge = new Knowledge('./knowledge.json');
}
<<<<<<< HEAD
else {
    $classifier = new GeneticClassifier($actor->basket);
}
=======

# $classifier = new GeneticClassifier($actor->basket);
>>>>>>> bcfa321190e62db773d2aa7a8f10ee8a2f5f8df3

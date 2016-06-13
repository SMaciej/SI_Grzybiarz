<?php
define('ALLOWED_TOTAL_DIFF', 13);
class Mushroom
{
    private static $allowedType;
    private static $allowedPoisonous;
    private static $allowedWeightRange;
    private static $allowedPileus;
    private static $allowedStipe;

    private $type;
    private $isPoisonous;
    private $weight;
    private $pileus;
    private $stipe;

    private $fitness;

    public function __construct($mushroomData) {
        $this->checkType($mushroomData['type']);
        $this->checkIsPoisonous($mushroomData['poisonous']);
        $this->checkWeightRange($mushroomData['weight']);
        $this->checkPileus($mushroomData['pileus']);
        $this->checkStipe($mushroomData['stipe']);
        $this->setFitness();
    }

    public function save() {
        $pileus = $this->pileus;
        $stipe = $this->stipe;
        Config::query(
            "INSERT INTO mushrooms 
              ('type', 'weight', 'pileus_color', 'pileus_shape',
              'stipe_info', 'stipe_height', 'poison')
              VALUES (
              '$this->type', $this->weight,
              '$pileus[color]', '$pileus[shape]',
              '$stipe[info]', $stipe[height], '$this->isPoisonous'
              )");
    }

    public function setFitness() {
        $this->fitness = 0;

        if ($this->isNotKnown()) {
            $res = $this->findSimiliar();
            $this->type = $res['name'];
            $this->isPoisonous = $res['poison'];
        }

        if ($this->type !== '?') {
            $color = 100 * $this->PercentWithSimiliarColor();
            $height = 1.5 * $this->PointsForHeight();
            $weight = (int)$this->weight;

            $this->fitness = $color + ($height * $weight);

            if ($this->isPoisonous === '?') {
                $this->fitness *= 0.20;
            }
            elseif ($this->isPoisonous === 'yes') {
                $this->fitness *= 0.01;
            }
        } else {
            $this->fitness = -1;
        }
    }

    private function PointsForHeight() {
        $height = $this->stipe['height'];

        $query = Config::query(
            "SELECT stipe_height, avg(stipe_height) as avg
            FROM mushrooms
            WHERE type = '$this->type'"
        );

        $total = 0;
        $temp = 0;
        foreach ($query as $hg) {
            $temp += pow(($hg['stipe_height'] - $hg['avg']), 2);
        }
        $total = sqrt($temp / count($query));

        if ((int)$total === 0) {
            return 0;
        }
        return (1 / $total);
    }

    private function findSimiliar() {
        $stipe_height = $this->stipe['height'];
        $totalKnownShrooms = Config::query(
            "SELECT type,
            ($this->weight / avg(weight)) as wg,
            ($stipe_height / avg(stipe_height)) as hg,
            poison,
            count(*) as cnt
            FROM mushrooms
            GROUP BY type, pileus_color, pileus_shape, stipe_info
            ORDER BY cnt DESC"
        );

        $result = array(
            'name' => '?',
            'wg' => 1000,
            'hg' => 1000,
            'cnt' => 0,
            'poison' => '?'
        );

        $total = 0;
        foreach ($totalKnownShrooms as $probably) {
            $totalDiff = abs($probably['wg']) + abs($probably['hg']);
            $total += (int)$probably['cnt'];
            if ($totalDiff < ALLOWED_TOTAL_DIFF &&
                (abs($result['wg']) + abs($result['hg'])) > $totalDiff) {
                $result = array(
                    'name' => $probably['type'],
                    'wg' => $probably['wg'],
                    'hg' => $probably['hg'],
                    'cnt' => $probably['cnt'],
                    'poison' => $probably['poison']
                );
            }
        }
        return array(
            'name' => $result['name'],
            'cnt' => $result['cnt'] / $total,
            'poison' => $result['poison']
        );
    }

    private function isNotKnown() {
        return ($this->type === '?');
    }

    private function PercentWithSimiliarColor() {
        $color = $this->pileus['color'];

        $query = Config::query(
            "SELECT pileus_color, count(pileus_color) as cnt
            FROM mushrooms
            WHERE type = '$this->type'
            GROUP BY pileus_color"
        );

        $total = 0;
        $clr = 0;
        foreach ($query as $res) {
            $total += $res['cnt'];
            if ( $res['pileus_color'] === $color ) {
                $clr = $res['cnt'];
            }
        }

        return ($total < 1) ? 0 : ($clr / $total);
    }

    private function checkType($type) {
        if (array_search($type, self::$allowedType) !== FALSE) {
            $this->type = $type;
        }
        else
        {
            Throw new Exception();
        }
    }

    private function checkIsPoisonous($poison) {
        if (array_search($poison, self::$allowedPoisonous) !== FALSE) {
            $this->isPoisonous = $poison;
        }
        else
        {
            Throw new Exception();
        }
    }

    private function checkWeightRange($weight) {
        if ((int)$weight <= self::$allowedWeightRange['max'] &&
            (int)$weight >= self::$allowedWeightRange['min'] ) {
            $this->weight = (int)$weight;
        }
        else
        {
            Throw new Exception();
        }
    }

    private function checkPileus($pileus) {
        if (array_search($pileus['color'], self::$allowedPileus['color']) !== FALSE &&
            array_search($pileus['shape'], self::$allowedPileus['shape']) !== FALSE)
        {
            $this->pileus = $pileus;
        }
        else
        {
            $this->pileus = $pileus;
        }
    }

    private function checkStipe($stipe) {
        if (array_search($stipe['info'], self::$allowedStipe['info']) !== FALSE &&
            (int)$stipe['height'] <= (int)self::$allowedStipe['height']['max'] &&
            (int)$stipe['height'] >= (int)self::$allowedStipe['height']['min']) {
            $this->stipe = array(
                'info' => $stipe['info'],
                'height' => (int)$stipe['height']
            );
        }
        else
        {
            Throw new Exception();
        }
    }

    public function getProbablyName() {
        return $this->type;
    }

    public static function setAllowedType($type) {
        self::$allowedType = $type;
    }

    public static function setAllowedPoisonous($poisonous) {
        self::$allowedPoisonous = $poisonous;
    }

    public static function setAllowedWeightRange($range) {
        self::$allowedWeightRange = $range;
    }

    public static function setAllowedPileus($pileus) {
        self::$allowedPileus = $pileus;
    }

    public static function setAllowedStipe($stipe) {
        self::$allowedStipe = $stipe;
    }

}
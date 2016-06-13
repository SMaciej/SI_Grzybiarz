<?php
class Config
{
    private static $dbHandle;

    public function __construct($path) {
        $this->config = json_decode(file_get_contents($path), true);

        $this->connectToDB();

        $mushroom = $this->config['mushroom'];
        $basket = $this->config['actor']['basket'];

        Mushroom::setAllowedType($mushroom['type']);
        Mushroom::setAllowedPileus($mushroom['pileus']);
        Mushroom::setAllowedPoisonous($mushroom['poisonous']);
        Mushroom::setAllowedStipe($mushroom['stipe']);
        Mushroom::setAllowedWeightRange($mushroom['weight']);

        Basket::setCapacity($basket['capacity']['max']);
    }

    private function connectToDB() {
        self::$dbHandle = new SQLite3('shrooms_db.db');
    }

    /**
     * @param string $query
     * @return SQLite3Result
     */
    public static function query($query) {
        $query = self::$dbHandle->query($query);

        $result = array();
        while ($res = $query->fetchArray(SQLITE3_ASSOC)) {
            $result[] = $res;
        }

        return $result;
    }

}
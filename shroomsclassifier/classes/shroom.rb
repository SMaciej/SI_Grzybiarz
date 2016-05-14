class Shroom

  include AllowedValues

  attr_reader :allowed_type, :allowed_pileus, :allowed_stipe,
              :allowed_poisonous, :allowed_weight,
              :type, :pileus, :stipe, :poisonous, :weight

  def initialize( hash )
    raise WrongValueEror unless is_allowed?( hash )
  end

  def self.allow( hash )
    @allowed_type = hash['type']
    @allowed_poisonous = hash['poisonous']
    @allowed_weight = hash['weight']
    @allowed_pileus = hash['pileus']
    @allowed_stipe = hash['stipe']
  end

end
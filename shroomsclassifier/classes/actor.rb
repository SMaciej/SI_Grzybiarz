class Actor

  attr_reader :allowed_basket

  def initialize( config )
    @allowed_basket = Basket.new( config )
  end

  def self.allow( hash )
    Basket::allow( hash['basket'] )
  end

end
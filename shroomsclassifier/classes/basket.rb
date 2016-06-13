class Basket

  attr_reader :allowed_capacity,
              :content

  def initialize(config)
    @content =
        config['actor']['basket']['contains'].each { |shroom| Shroom.new(shroom) }
  end

  def self.allow(hash)
    @allowed_capacity = hash['capacity']
  end

end
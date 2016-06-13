class Config

  attr_reader :config

  def initialize(config_path)
    @config = AllowedValues::set_allowed( File.read(config_path) )
    Actor.allow( @config['actor'] )
    Shroom.allow( @config['mushroom'] )
  end

end
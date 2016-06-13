module AllowedValues

  def self.set_allowed( json )
    JSON.parse( json )
  end

  def is_allowed?( hash )
    hash.each do |index, content|
      return false unless variable_is_allowed?( index, content )
    end
    true
  end

  def variable_is_allowed?( name, value )
    #puts name
    #puts value
    puts self::allowed_type
    puts instance_variable_get("@name")
    puts instance_variables
    true
  end

end
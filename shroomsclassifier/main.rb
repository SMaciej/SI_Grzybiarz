#!/usr/bin/env ruby

require 'json'
require 'C:/Ruby22/lib/ruby/gems/2.2.0/gems/activerecord-4.2.6/lib/active_record.rb'

Dir.glob('./classes/*').each { |fileName| require fileName }

config = Config.new( '../config.json' )

actor = Actor.new( JSON.parse( File.read( 'knowledge.json' ) ) )
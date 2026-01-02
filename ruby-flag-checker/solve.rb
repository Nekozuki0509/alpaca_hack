require 'prime'
primes = Prime::Generator23.new.take(23)
encrypted = "Coufhlj@bixm|UF\\JCjP^P<"
flag = primes.zip(encrypted.bytes).map{|x,y| x^y}.pack("C*")
puts flag

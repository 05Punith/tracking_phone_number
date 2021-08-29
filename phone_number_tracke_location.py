#install pippip install phonenumbers
import phonenumbers
from text import number
#to find which country name of phone number belongs to
from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))
#to find service provider of number
from phonenumbers import carrier
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))
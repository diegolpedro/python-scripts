#!bin/python3
#-----------------------------------------------------------------------------#
# geoLocate.py - Google API geoCoder                    by Pedro, Diego  2018 #
# Version:                                                                    #
# 1.0 _ Primer implementacion. Clase para geocode.                            #
# 1.1 _ Envio de direccion por parametro.                                     #
#-----------------------------------------------------------------------------#
VERSION=1.1

# Importamos libreria.
import googlemaps

# Parametros de configuracion.
api_key='api_key'


#--------------------- Clase para menejo de geocodificacion ------------------
class Geocoder:
  '''Geocodificador - A partir de una direccion obtiene las coordenadas'''
  def __init__(self, api_key):
    self.gmaps = googlemaps.Client(key=api_key)

  def geoCode(self, direccion):
    ''' Geocodificamos direccion '''
    try:
      # Geocodear una direccion
      self.result = self.gmaps.geocode(direccion)
    except:
      print("API ERROR!")
      exit()

  def show(self):
    ''' Mostramos resultado '''
    lat = self.result[0]["geometry"]["location"]["lat"]
    lon = self.result[0]["geometry"]["location"]["lng"]
    print (lat,lon)


#-------------------------------- Inicio Main --------------------------------
direccion = Geocoder(api_key)
direccion.geoCode('1600 Amphitheatre Parkway, Mountain View, CA')
direccion.show()
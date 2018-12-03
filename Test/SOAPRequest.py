"""This module will contain example regarding calling SOAP based web service using zeep module"""
import zeep
import datetime
#wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
#client = zeep.Client(wsdl=wsdl)
#print(client.service.Method1('Zeep', 'is cool'))

"""
http://www.thomas-bayer.com/axis2/services/BLZService?wsdl
"""
currDateTime=datetime.datetime.now()

wsdl="http://www.gcomputer.net/webservices/dilbert.asmx?WSDL"
client=zeep.Client(wsdl=wsdl)
print(client.service.DailyDilbert(currDateTime))
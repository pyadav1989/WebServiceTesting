"""this module will contain example for calling soap web service using requests module"""
import requests
import datetime
currDateTime=str(datetime.datetime.now())
requestXML="""
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <DailyDilbert xmlns="http://gcomputer.net/webservices/">
      <ADate>2018-07-29 09:17:13.812189</ADate>
    </DailyDilbert>
  </soap:Body>
</soap:Envelope>"""

url="http://www.gcomputer.net/webservices/dilbert.asmx";

headers = {'SOAPAction': 'http://gcomputer.net/webservices/DailyDilbert','Content-Type':'text/xml;charset=UTF-8'}

response=requests.post(url,requestXML)
print(response.content)
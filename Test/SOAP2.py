"""this module will contain example for calling soap web service using requests module"""
import requests

requestXML="""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Add xmlns="http://tempuri.org/">
      <intA>3</intA>
      <intB>2</intB>
    </Add>
  </soap:Body>
</soap:Envelope>"""

url="http://www.dneonline.com/calculator.asmx?WSDL";

headers = {'Content-Type':'text/xml;charset=UTF-8'}

response=requests.post(url=url,data=requestXML,headers=headers)
print(response.status_code)
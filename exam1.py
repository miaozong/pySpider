import  urllib.request     
import  urllib.parse

data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')
print(data)
#response = urllib.request.urlopen('http://httpbin.org/post',data= data)
#print(response.read().decode('utf-8'))
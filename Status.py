import http.client

host = input("Inserire Ip del sistema target :")
port =input("Inserire porta del sistema target (default:80):")

if(port == ''):
        port = 80
try:
        connection = http.client.HTTPConnection(host, port)
        connection.request('GET', 'http://192.168.50.101/phpMyAdmin/')
        response = connection.getresponse()
        print("I metodi abilitati sono:",response.status)
        connection.close()
except ConnectionRefusedError:
        print("connessione fallita")

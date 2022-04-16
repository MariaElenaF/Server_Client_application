import socket
import pickle
import random           #Pentru numarul ales aleatoriu

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socketul de intampinare
        self.server_socket.bind(('127.0.0.1', 1111))
        self.server_socket.listen(1)                                           #1 = coada de asteptare client
        self.connection_socket, self.addr = self.server_socket.accept()        #Serverul accepta conexiunea

    def send(self, message):
        self.connection_socket.send(pickle.dumps(message))                     #Trimitem un mesaj clientului

    def receive(self):
        return pickle.loads(self.connection_socket.recv(1024))                 #Primim mesajul de la client


if __name__ == '__main__':
    server = Server()
    data = server.receive()             #Primim mesajul de la client

    if data == 'START':                 #Daca mesajul primit este 'START', atunci putem incepe jocul

        data = 'Ghiceste! \n'
        server.send(data.upper())

    else:
        exit(0) #ca sa inceapa cu Start

    nr = random.randint(1, 100)     #alegem un numar la intamplare

    nr_inc=1    #il initializam cu 1 pentru ca deja am ghicit odata (imediat dupa "GHICESTE!")

    while True:
        data = server.receive()     #preluam numarul introdus de la tastatura
        x=int(data)                 #il convertim in int ca sa putem compara numarul

        if x==nr:                                                #verificarea
            data = f'Ai castigat din {nr_inc} incercari!'
            server.send(data.upper())
            break
        else:
            if x < nr:
                data = 'Prea mic, incearca din nou...'
                server.send(data.upper())
            else:
                data='Prea mare, incearca din nou...'
                server.send(data.upper())

        nr_inc+=1   #incrementam numarul de incercari
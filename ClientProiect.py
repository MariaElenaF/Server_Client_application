import socket
import pickle


class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          #Socketul de intampinare
        self.client_socket.connect(('127.0.0.1', 1111))

    def send(self, message):                                                            #Trimitem un mesaj catre server
        self.client_socket.send(pickle.dumps(message))

    def receive(self):                                                                  #Primim un mesaj de la server
        return pickle.loads(self.client_socket.recv(1024))


if __name__ == '__main__':
    client = Client()

    print('Tastati START pentru a incepe jocul: ')
    client.send(input())   #Tastam START pentru a incepe si trimitem mesajul serverului

    data=client.receive()  #primim mesajul "GHICESTE!" de la server
    print(data)            #il afisam
    while True:
        data = input('Introduceti numarul: ')
        client.send(data)
        data = client.receive()
        print(data)
        print('\n')
        if 'CASTIGAT' in data:      #daca am castigat, sa iesim din while ca sa se opreasca si clientul
            break

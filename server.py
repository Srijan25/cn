import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print("Process initiated");

except socket.error as err:
    print("Socket creation failed");

port = 12345;

# bind the server to listen for requests

s.bind(('', port));
print("Socket binded to: ", port);

s.listen(5);
print("Socket is listening");

while True:

    conn, add = s.accept();
    with conn:
        print("Got connection from ", add);
        conn.send(b"Connection successful");
        while True:
            data = conn.recv(1024);

            if not data:
                break;
            print(">> ", data.decode());
            # Enter message you want to send to client
            data_sent = (input("<< ")).encode()
            conn.sendall(data_sent);
        print("Connection closed");
s.close()
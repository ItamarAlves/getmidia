#/bin/python3
from pytube import YouTube

link = input('Informe o link do youtube: ')

def main():
    YouTube(link).streams.first().download()



main()

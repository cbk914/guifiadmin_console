#!/usr/bin/python
#-*-coding: utf-8-*-
# Consola d'Admin de Guifi.net
# Version 0.1-33 pre-alpha - 21/10/2015
# Coded by cbk
# Copyleft 2015
# TO-DO:
# 	traceroute
#	ping
# 	msf
#	configurar interfaz de red
import os
import sys,traceback
import socket

def clearScreen():
	if os.name == "nt":
		os.system("cls")
		sistema="windows"
	elif os.name == "posix":
		os.system("clear")
		sistema="posix"
		
def nm():
	from subprocess import Popen
	os.system("nmap -h")
	ip=raw_input("IP o rango: ")
	nm = Popen(['sudo nmap', '-sX -P0 -T5 -oN /var/log/nmapscan.log','+ip+'])
	nm.wait()

def sysinfo():
	print os.system	
	os.system("sudo lsb_release -a")
	if os.name =="nt":
                        print"Sistema Operativo: Windows"
        elif os.name =="posix":
                        print "Sistema Operativo: Linux/MAC"
        else:
                        print "Sistema Operativo Desconocido"
			
def main():
	clearScreen()
	print chr(27)+"[0;33m"+"v0.1 - GuifiAdmin Panel"
	print "~~~~~~~~~~~~~~~~~~~~~~~"
	print chr(27)+"[0;00m"
	print chr(27)+"[0;00m"
	print chr(27)+"[1;16m"+"(er) "+chr(27)+"[0;00m"+"Escaneo de Red"
	print chr(27)+"[1;16m"+"(es) "+chr(27)+"[0;00m"+"Escaneo de Seguridad"
	print chr(27)+"[1;16m"+"(in) "+chr(27)+"[0;00m"+"Informacion del Sistema"
	print chr(27)+"[1;16m"+"(ia) "+chr(27)+"[0;00m"+"Iniciar Apache WWW Server"
	print chr(27)+"[1;16m"+"(is) "+chr(27)+"[0;00m"+"Iniciar Squid Proxy"
	print chr(27)+"[1;16m"+"(nm) "+chr(27)+"[0;00m"+"Escaneo Profundo de Red"
	print chr(27)+"[1;16m"+"(ra) "+chr(27)+"[0;00m"+"Reiniciar Apache WWW Server"
	print chr(27)+"[1;16m"+"(rs) "+chr(27)+"[0;00m"+"Reiniciar Squid Proxy"
	print chr(27)+"[1;16m"+"(sos) "+chr(27)+"[0;00m"+"Ayuda"
	print chr(27)+"[1;16m"+"(ssh) "+chr(27)+"[0;00m"+"Conectar por SSH a Usuario@IP"
	print chr(27)+"[1;16m"+"(up) "+chr(27)+"[0;00m"+"Actualizar Sistema"
	print chr(27)+"[1;16m"+"(xt) "+chr(27)+"[0;00m"+"Salir"
	print chr(27)+"[0;00m"
	opcion = raw_input("Comando: ")

# Esto es la jungla amigo!!
	if opcion == "sos":
		clearScreen()
		print "You're fucked my friend!!!"
		main()
# Actualizar sistema

	if opcion == "up":
		cmd1 = os.system("sudo /usr/local/bin/actualizar")
		main()
# Iniciar Apache
	if opcion == "ia":
		cmd1 = os.system("sudo /etc/init.d/apache2 start")
		main()
# Informacion del sistema
	if opcion == "in":
		sysinfo()
		main()	

# Iniciar Squid Proxy Server
	if opcion == "is":
		cmd1 = os.system("sudo /etc/init.d/squid3 start")
		main()
		
# Conectar via SSH
	if opcion == "ssh" or opcion == "SSH":
		servernet= raw_input("usuario@IP ")
		port = raw_input("Puerto ")
		cmd1 = os.system("ssh "+servernet+" -p "+port)
		main()

# Escanear con Lynis
	if opcion == "es":
		cmd1 = os.system("sudo /usr/sbin/lynis audit system")
		an1=raw_input("Analizar Manualmente los Resultados? S/N ")
		if an1 == "S":
			cmd2=os.system("sudo vim /var/log/lynis.log")
		else:
			if an1 == "N":
				print "Saliendo al Menu Principal"
				main()
# Escaneo de red
	if opcion == "er":
		cmd1 = os.system("sudo /usr/sbin/netdiscover")
		main()

	else:
		print "Comando no válido"
		main()
# Escaneo profundo de red
	if opcion == "nm":
		cmd1 = nm()
		nm.wait()
		main()
		
# Reiniciar Apache WWW Server
	if opcion == "ra":
		cmd1 = os.system("sudo /etc/init.d/apache2 restart")
		main()		
# Reiniciar Squid Proxy Server
	if opcion == "rs":
		cmd1 = os.system("sudo /etc/init.d/squid3 restart")
		main()
# Salir
	if opcion == "xt":
		sys.exit()
main()

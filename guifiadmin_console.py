#!/usr/bin/python
#-*-coding: utf-8-*-
# Consola d'Admin de Guifi.net
# Version 0.1-51 pre-alpha - 21/10/2015
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
	if os.path_exists("/usr/bin/nmap"):
		instalado = 1
	else:
		print "Nmap no esta instalado en la ruta por defecto."
		instalar=raw_input("Pulsa (I) para instalar Nmap, cualquier otra tecla para volver al menú principal.")
			if instalar = "I" or instalar = "i":
				cmd1 = os.system("aptitude update && aptitude -y install nmap")
			else:
				main()
	from subprocess import Popen
	os.system("nmap -h")
	ip=raw_input("Opciones + IP o rango: ")
	nm = os.system("sudo nmap -oN /var/log/netscan.log "+ip)
	an1=raw_input("Analizar Manualmente los Resultados? S/N ")
        if an1 == "S":
               cmd2=os.system("sudo vim /var/log/netscan.log")
        else:
	        if an1 == "N":
        	        print "Saliendo al Menu Principal"
                	main()
	raw_input("Pulsa una tecla para continuar...")
	main()

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
	print chr(27)+"[1;16m"+"(cr) "+chr(27)+"[0;00m"+"Conexiones de la red"
	print chr(27)+"[1;16m"+"(er) "+chr(27)+"[0;00m"+"Escaneo de Red"
	print chr(27)+"[1;16m"+"(es) "+chr(27)+"[0;00m"+"Escaneo Local de Seguridad"
	print chr(27)+"[1;16m"+"(in) "+chr(27)+"[0;00m"+"Informacion del Sistema"
	print chr(27)+"[1;16m"+"(ia) "+chr(27)+"[0;00m"+"Iniciar Apache WWW Server"
	print chr(27)+"[1;16m"+"(is) "+chr(27)+"[0;00m"+"Iniciar Squid Proxy"
	print chr(27)+"[1;16m"+"(nm) "+chr(27)+"[0;00m"+"Escaneo Profundo de Red"
	print chr(27)+"[1;16m"+"(pi) "+chr(27)+"[0;00m"+"Ping IP/host"
	print chr(27)+"[1;16m"+"(ra) "+chr(27)+"[0;00m"+"Reiniciar Apache WWW Server"
	print chr(27)+"[1;16m"+"(rs) "+chr(27)+"[0;00m"+"Reiniciar Squid Proxy"
	print chr(27)+"[1;16m"+"(sos) "+chr(27)+"[0;00m"+"Ayuda"
	print chr(27)+"[1;16m"+"(ssh) "+chr(27)+"[0;00m"+"Conectar por SSH a Usuario@IP"
	print chr(27)+"[1;16m"+"(tr) "+chr(27)+"[0;00m"+"Traceroute IP/host"
	print chr(27)+"[1;16m"+"(up) "+chr(27)+"[0;00m"+"Actualizar Sistema"
	print chr(27)+"[1;16m"+"(xt) "+chr(27)+"[0;00m"+"Salir"
	print chr(27)+"[0;00m"
	opcion = raw_input("Comando: ")

# Esto es la jungla amigo!!
	if opcion == "sos":
		clearScreen()
		print "You're fucked my friend!!!"
		print ""
		raw_input("Pulsa una tecla para continuar...")
		main()

# Actualizar sistema
	if opcion == "up":
		clearScreen()
		cmd1 = os.system("sudo /usr/local/bin/actualizar")
		print "Sistema actualizado"
		raw_input("Pulsa una tecla para continuar...")
		main()

# Iniciar Apache
	if opcion == "ia":
		clearScreen()	
		cmd1 = os.system("sudo /etc/init.d/apache2 start")
		print "Servidor web Apache iniciado"
		print ""
		raw_input("Pulsa una tecla para continuar...")
		main()

# Informacion del sistema
	if opcion == "in":
		sysinfo()
		raw_input("Pulsa una tecla para continuar...")
		main()	

# Iniciar Squid Proxy Server
	if opcion == "is":
		cmd1 = os.system("sudo /etc/init.d/squid3 start")
		print "Squid Proxy Server iniciado"
		print ""
		raw_input("Pulsa una tecla para continuar...")
		main()
# Ping
	if opcion == "pi":
		clearScreen()
		IP = raw_input("IP o host ")
		cmd1 = os.system("ping -c 10 "+IP)
		raw_input("Pulsa una tecla para continuar...")
		main() 		

# Conectar via SSH
	if opcion == "ssh" or opcion == "SSH":
		clearScreen()
		servernet= raw_input("usuario@IP ")
		port = raw_input("Puerto ")
		cmd1 = os.system("ssh "+servernet+" -p "+port)
		print "Estableciendo conexion..."
		main()
		
# Traceroute
	if opcion == "tr":
		IP = raw_input("IP o host ")
		cmd1 = os.system("mtr "+IP)
		main()

# Escanear con Lynis
	if opcion == "es":
		clearScreen()	
		cmd1 = os.system("sudo /usr/sbin/lynis audit system")
		an1=raw_input("Analizar Manualmente los Resultados? S/N ")
		if an1 == "S":
			cmd2=os.system("sudo vim /var/log/lynis.log")
		else:
			if an1 == "N":
				print "Saliendo al Menu Principal"
				main()
				
# Escaneo profundo de red
	if opcion == "nm":
		clearScreen()
		cmd1 = nm()
		nm.wait()
		raw_input("Pulsa una tecla para continuar...")
		main()

# Estado de las conexiones de red
	if opcion == "cr":
		clearScreen()
		cmd1 = os.system("netstat -putan | less")
		raw_input("Pulsa una tecla para continuar...")
		main()
	
# Reiniciar Apache WWW Server
	if opcion == "ra":
		cmd1 = os.system("sudo /etc/init.d/apache2 restart")
		print "Servidor web Apache reiniciado"
		raw_input("Pulsa una tecla para continuar...")
		main()		
# Reiniciar Squid Proxy Server
	if opcion == "rs":
		cmd1 = os.system("sudo /etc/init.d/squid3 restart")
		print "Servidor Proxy Squid reiniciado"
		raw_input("Pulsa una tecla para continuar...")
		main()
# Salir
	if opcion == "xt":
		print "Saliendo..."
		raw_input("Pulsa una tecla para continuar...")
		clearScreen()
		sys.exit()
				
# Escaneo de red
	if opcion == "er":
		cmd1 = os.system("sudo /usr/sbin/netdiscover")
		main()

	else:
		print "Comando no válido"
		raw_input("Pulsa una tecla para continuar...")
		main()


main()








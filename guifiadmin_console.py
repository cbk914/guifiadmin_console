#!/usr/bin/python
#-*-coding: utf-8-*-
# Consola d'Admin de Guifi.net
# Version 0.2.10 beta - 22/10/2015
# Coded by cbk
# Copyleft 2015
import os
import sys,traceback
import socket
import atexit

def clearScreen():
	if os.name == "nt":
		os.system("cls")
		sistema="windows"
	elif os.name == "posix":
		os.system("clear")
		sistema="posix"
def salida():
	print "Que la fuerza te acompañe!!!"

def continuar():
	raw_input("Pulsa [ENTER] para continuar")

def checkinstall(tool):
	if tool == "netdiscover" or tool == "lynis":
		path="/usr/sbin/"
	else:
		path="/usr/bin/"

	if os.path.exists(path+tool):
		instalado = True
	else:
		print "La ruta "+path+tool+" no existe \n"
		print tool+" no esta instalado en la ruta por defecto. \n"
		instalar = raw_input("Pulsa (I) para instalar "+tool+", o cualquier tecla para volver al menu principal \n")
		instalar = instalar.lower
		if instalar == "i":
			print "Instalando "+tool
			cmd1 = os.system("aptitude update && aptitude -y install "+tool)
			continuar()
			main()
		else:
			main()

def nm():
	tool = "nmap"
	checkinstall(tool)
	from subprocess import Popen
	os.system("nmap -h | less")
	ip=raw_input("Opciones + IP o rango: ")
	nm = os.system("sudo nmap -oN /var/log/netscan.log "+ip)
	an1=raw_input("Analizar Manualmente los Resultados? S/N \n")
        if an1.upper == "S":
               cmd2=os.system("sudo vim /var/log/netscan.log")
        else:
		if an1.upper == "N":
        	        print "Saliendo al Menu Principal \n"
               		main()
	continuar()
	main()

def sysinfo():
	clearScreen()
	print chr(27)+"[0;33m"+"Nombre del sistema: "
	print chr(27)+"[0m"
	os.system("cat /proc/sys/kernel/hostname")
	print ""
	print chr(27)+"[0;33m"+"Estado arbol del sistema:" 
	print chr(27)+"[0m"
	os.system("df -h")
	print ""
	print chr(27)+"[0;33m"+"Memoria RAM disponible:"
	print chr(27)+"[0m"
	os.system("free -m")
	print ""
	print chr(27)+"[0;33m"+"Informacion del sistema"
	print chr(27)+"[0m"
	os.system("sudo lsb_release -a")
	print ""
	if os.name == "nt":
                        print chr(27)+"[0;33m"+"Sistema Operativo: Windows"+chr(27)+"[0m"
        elif os.name == "posix":
                        print chr(27)+"[0;33m"+"Sistema Operativo: Linux/MAC"+chr(27)+"[0;00m"
        else:
                        print chr(27)+"[0;33m"+"Sistema Operativo Desconocido"+chr(27)+"[0;00m"
	print ""
	tool = "lm-sensors"
	checkinstall(tool)
	print chr(27)+"[0;33m"+"Temperatura del sistema: "
	print chr(27)+"[0;00m"
			
def main():
	clearScreen()
	print chr(27)+"[0;33m"+"GuifiAdmin Panel - v0.2"
	print "~~~~~~~~~~~~~~~~~~~~~~~"
	print chr(27)+"[0;00m"
	print chr(27)+"[0;00m"
	print chr(27)+"[1;16m"+"(cr) "+chr(27)+"[0;00m"+"Conexiones de la Red Local"
	print chr(27)+"[1;16m"+"(er) "+chr(27)+"[0;00m"+"Escaneo de Red Local"
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
	print chr(27)+"[1;16m"+"(who) "+chr(27)+"[0;00m"+"Whois IP/host"
	print chr(27)+"[1;16m"+"(xt) "+chr(27)+"[0;00m"+"Salir"
	print chr(27)+"[0;00m"
	opcion = raw_input("Comando: ")

# Esto es la jungla amigo!!
	if opcion == "sos":
		clearScreen()
		print "You're fucked my friend!!!"
		print ""
		print "https://buscatelavida.com"
		continuar()
		main()

# Actualizar sistema
	if opcion == "up":
		clearScreen()
		cmd1 = os.system("sudo /usr/local/bin/actualizar")
		print "Sistema actualizado"
		continuar()
		main()

# Iniciar Apache
	if opcion == "ia":
		if os.path.exists("/usr/sbin/apache2"):
			clearScreen()	
			cmd1 = os.system("sudo /etc/init.d/apache2 start")
			print "Servidor web Apache iniciado"
			print ""
			continuar()
			main()
		else:
			print "Apache no esta instalado"
			continuar()
			main()

# Informacion del sistema
	if opcion == "in":
		sysinfo()
		continuar()
		main()	

# Iniciar Squid Proxy Server
	if opcion == "is":
		if os.path.exists("/usr/bin/squid"):
			cmd1 = os.system("sudo /etc/init.d/squid3 start")
			print "Squid Proxy Server iniciado"
			print ""
			continuar()
			main()
		else:
			print "Squid no esta instalado"
			continuar()
			main()
# Ping
	if opcion == "pi":
		clearScreen()
		IP = raw_input("IP o host ")
		cmd1 = os.system("ping -c 10 "+IP)
		continuar()
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

# Escaneo profundo de red
	if opcion == "nm":
		clearScreen()
		cmd1 = nm()
		nm.wait()
		continuar()
		main()

# Estado de las conexiones de red
	if opcion == "cr":
		clearScreen()
		cmd1 = os.system("netstat -putan | less")
		continuar()		
		main()
	
# Reiniciar Apache WWW Server
	if opcion == "ra":
		cmd1 = os.system("sudo /etc/init.d/apache2 restart")
		print "Servidor web Apache reiniciado"
		continuar()
		main()		
# Reiniciar Squid Proxy Server
	if opcion == "rs":
		cmd1 = os.system("sudo /etc/init.d/squid3 restart")
		print "Servidor Proxy Squid reiniciado"
		continuar()
		main()
# Salir
	if opcion == "xt":
		print "Saliendo..."
		continuar()
		clearScreen()
		sys.exit()
# Whois
	if opcion == "who":
		clearScreen()
		tool = "whois"
		checkinstall(tool)
		ip=raw_input("IP o host ")
		cmd1 = os.system("whois "+ip+"|less")
		continuar()	
# Escaneo de red
	if opcion == "er":
		tool = "netdiscover"
		checkinstall(tool)
		cmd1 = os.system("sudo /usr/sbin/netdiscover")
		main()

# Escanear con Lynis
        if opcion == "es":
	        clearScreen()
		tool = "lynis"
		checkinstall(tool)
        	cmd1 = os.system("sudo /usr/sbin/lynis audit system")
	        an1=raw_input("Analizar Manualmente los Resultados? S/N ")
	        if an1.upper == "S":
        	        cmd2=os.system("sudo vim /var/log/lynis.log")
        	else:
                	if an1.upper == "N":
                        	print "Saliendo al Menu Principal"
                        	main()

	else:
		print "Comando no válido"
		continuar()
		main()
try:
	main() 
except KeyboardInterrupt:
	atexit.register(salida)
	main()






































































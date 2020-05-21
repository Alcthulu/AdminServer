#!/bin/sh

#Ruta donde se guardarán los logs
DIRLOG="/var/log/rklog";

#Lo está ejecutando el usuario root?
if [ $UID==0 ];
then

	##################CHKROOTKIT###########################

	#Análisis estándar filtrando la información de salida con grep (solo líneas que aparezca la palabra INFECTED)
    # y manda la salida del análisis al archivo de log añadiéndole al nombre la fecha que se realizó.
	chkrootkit |grep INFECTED > $DIRLOG/Chkrootkit-$(date +%Y-%m-%d).log


	#Enviamos el log creado al administrador del sistema
	cat $DIRLOG/ChkCabecera.txt $DIRLOG/Chkrootkit-$(date +%Y-%m-%d).log | mail -s "Analisis diario Chkrootkit $(date +%Y-%m-%d)" AdAdRoLu@gmail.com


	##################ROOTKITHUNTER###########################

	#Chequeamos por actualizaciones 
	rkhunter --update

	#Análisis completo del sistema deshabilitando el comportamiento interactivo y manda la
    # salida del análisis al archivo de log añadiéndole al nombre la fecha que se realizó.
	rkhunter --check --enable all -sk --logfile $DIRLOG/RootkitHunter-$(date +%Y-%m-%d).log

	#Enviamos el log creado al administrador del sistema
	cat $DIRLOG/RkhCabecera.txt $DIRLOG/RootkitHunter-$(date +%Y-%m-%d).log | mail -s "Analisis diario RootkitHunter $(date +%Y-%m-%d)" AdAdRoLu@gmail.com


	#Tomamos una instantánea del estado actual de la máquina para comparar la próxima vez que ejecutemos el programa
	rkhunter --propupd

#Si no eres usuario root
else
    clear
    echo " "
    echo "Si no eres root no puedes ejecutar este script."
    echo "Ahora eres $USER."
    echo " "
    echo " "
fi
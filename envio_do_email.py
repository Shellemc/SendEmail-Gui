# -*- coding: utf-8 -*- --noconsole --admin --newspec
import smtplib
from jan import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main(ui):
	def envio():
		
		
		mailremetente = ui.lineEdit.text()
		mailpassword = ui.lineEdit_2.text()
		maildestino = ui.lineEdit_3.text()
		mailassunto = ui.lineEdit_4.text()
		server = "smtp.gmail.com:587"

		print(mailremetente)
		print(mailpassword)
		print(maildestino)
		print(mailassunto)
		
		body = ui.textEdit.toPlainText()
		print(body)

		msg = MIMEMultipart()
		msg['To'] = maildestino
		msg['From'] = mailremetente
		msg['Subject'] = mailassunto
		msg.attach(MIMEText(body, 'plain'))

		message = msg.as_string()

		server = smtplib.SMTP(server)
		server.starttls()
		server.login(mailremetente, mailpassword)
		server.sendmail(mailremetente, maildestino, message)
		server.quit()
		
		

	ui.pushButton.clicked.connect(envio)


if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	main(ui)
	sys.exit(app.exec_())
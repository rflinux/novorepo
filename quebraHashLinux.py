import crypt

senha_shadow = raw_input("Digite o hash a ser quebrado:\n")
info = senha_shadow.split(":") 
usuario = info[0] 
hash = info[1] 
salt = hash[:hash.find("$",3)+1] 

with open("lista.txt", "r") as lista:
    while True:
        senha = lista.readline().strip("\n")
        if not senha:
            break
        if crypt.crypt(senha, salt) == hash: 
            print "USER \t", usuario
            print "PASS \t", senha
            break

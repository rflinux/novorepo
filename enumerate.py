import socket
# ESTE SCRIPT ELE FAZ UMA ENUMERAÇÃO DE DNS ELE TRAS OS DOMINIOS E OS IPS DE CASA DOMINIO, DE UMA URL
# FORMA DE USO:
# python3 enumerate.py
def enumerate_dns():
    print("===========\-> Enumerate de DNS <-/===========")
    dominio = input("Digite um domínio: ")
    nomes = ["ns1", "ns2", "www", "ftp", "intranet"]

    def arquivo():
        with open("log.txt", "a") as dns:
            return dns.write("\n#Aqui estão todos os nomes e dominios\n")

    arquivo()

    for nome in nomes:
        DNS = (nome + "." + dominio)
        try:
            tudo = (DNS + ": " + socket.gethostbyname(DNS))
            print(tudo)
        except socket.gaierror:
            pass
        with open("log.txt", "a") as dns:
            dns.write("\n")
            dns.write(tudo)




enumerate_dns()

import re
n1 = input("Insira o texto:")
ref_arquivo = open("teste.txt","w")
ref_arquivo.write(n1)
ref_arquivo.close()
arq = open("teste.txt", "r")
texto = re.sub(r'[: \n]+', ' ',arq.read()).split(' ')
dict ={}
ins = {}
aux =""
while(len(texto)!= 0):
    aux = texto.pop()
    ins.clear()
    if(aux not in dict):
        ins.update(dict)
        dict.clear()
        dict = {aux: 1}
    else:
        dict[aux] = (dict.get("{0}".format(aux), 1)) + 1
        ins.update(dict)
        dict.clear()
        dict = {aux: (ins.get("{0}".format(aux), 1)) + 1}
    dict.update(ins)
print(dict)

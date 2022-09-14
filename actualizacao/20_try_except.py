import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("Erro do sistema operativo")
except ValueError:
    print("Nao foi possivel converter para inteiro")
except:
    print("Erro nao esperado", sys.exc_info()[0])
    raise
finally:
    print("Correu tudo bem!")
    print("i = " + str(i))
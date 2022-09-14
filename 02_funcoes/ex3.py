# suma 
# maior
# menor 
# media 
def main():
               x = []
               for b in range(5):
                              x.append(int(input("introducir o " + str(b) + " numero: ")))
               
               print(x)
               print("valor total da suma: " + str(sum(x)) )
               print("o numero maior é: " +  str(max(x)))
               print("o numero min é: " +  str(min(x)))
               print("a media é: " +  str(sum(x)/len(x)))
               print("numero de elementos: " + str(len(x)))

if __name__ == '__main__':
               main()
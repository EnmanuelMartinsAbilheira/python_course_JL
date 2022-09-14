import json
import sqlite3
import os

               

def main():
               db =  "ex5.db"
               try:
                              os.remove(db)
               except:
                              pass

               conn = sqlite3.connect(db)
               c = conn.cursor()


               x = "sercolor.json"
               with open(x, 'r') as json_file: 
                              data = json.load(json_file) 

               for k in data:
                              tab_name = k 
                              primeiro = True 
                              query = "Create table " + tab_name + " ("
                              for x in data[k][0]:
                                             if primeiro == False:
                                                            query = query + ","
                                             query = query + x 
                                             primeiro = False
                              query = query + ")"

                              c.execute(query)
                              conn.commit()

               
                              for y in range(len(data[k])):
                                             print(str(y))
                                             primeiro = True 
                                             query = "Insert Into " + tab_name + " values("
                                             for x in data[k][y]:
                                                            if primeiro == False:
                                                                           query = query + ","
                                                            query = query + "'" +data[k][y][x] + "'"
                                                            primeiro = False
                                             query = query + ")"
                                             print(query)
                                             c.execute(query)
                                             conn.commit()


if __name__ == '__main__':
                   main()
    

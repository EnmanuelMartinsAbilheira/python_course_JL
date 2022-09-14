import json


def main():
    f = open('large-file.json', encoding = "utf8")

    dic = json.load(f)

    print(type(dic))
    print(len(dic))

    for x in dic:
        #print(x)
        for key,value in x.items():
            print(key)

if __name__ == "__main__":
    main()
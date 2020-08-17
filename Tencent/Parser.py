import json

if __name__ == "__main__":
    fs = open("Tencent.txt", 'r', encoding='UTF-8')
    fd = open("Tencent.md", 'w', encoding='UTF-8')
    fd.write('|时间|内容|来源|\n')
    fd.write('| :-----| :---- | :---- |\n')
    for line in fs:
        Data = json.loads(line.strip().replace('\\', ' ').replace('"', ' ').replace('\'', '"'))
        # print(Data)
        fd.write(str(Data['time'])+' | '+str(Data['text']).replace('\n', ' ')+' | '+str(Data['from'])+'\n')
    fs.close()
    fd.close()
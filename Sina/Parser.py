import json

if __name__ == "__main__":
    fs = open("Sina.txt", 'r', encoding='UTF-8')
    fd = open("Sina.md", 'w', encoding='UTF-8')
    fd.write('|时间|内容|来源|\n')
    fd.write('| :-----| :---- | :---- |\n')
    for line in fs:
        Data = json.loads(line.strip().replace('\'', '"'))
        fd.write(str(Data['time'])+' | '+str(Data['text']).replace('\n', ' ')+' | '+str(Data['from'])+'\n')
    fs.close()
    fd.close()
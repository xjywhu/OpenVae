## OpenVae
### 仓库描述
这是一个搜集整理许嵩语录的仓库，如果你是嵩鼠或者觉得看了许嵩的语录觉得对你的影响很大，欢迎加入一起搜集整理维护语录仓库。  

作为一位资深嵩鼠，我大概从小学五六年级开始听嵩哥的歌。到如今已经十年有余。
其实许嵩对我的影响不仅仅是他的音乐带来的，更多也来源于他的个人性格，为人处世的态度，三观。

一直以来我都很想收集整理许嵩语录，一方面是因为嵩哥的很多语录在我人生的某些关键时刻给了我指引和鼓励，
另一方面百度上现有的语录的整理并不全且不具有实时性。

### 结构介绍
1. 各个文件夹表示语录来源：  

| 文件夹 | 描述 |  
| --- | --- |  
| Sina | 新浪微博 |  
| Tencent | 腾讯微博 |  
| Vae+ | 许嵩官方APP：Vae+  |  

2. 文件夹下面的同名.py文件表示获得动态的爬虫  
3. 文件夹下面的同名.txt文件表示动态结果。表示格式为json，以动态发布时间排序:    
{"text": 动态内容, "time": 动态时间, "from": 动态来源}  
4. 文件夹下面的同名.yl文件表示语录结果(从.txt文件中筛选获得, 表示形式同上)  
5. 文件夹下面的同名.md文件表示语录, 表示形式为表格.  
6. 文件夹下面的Parser.py文件将txt文件转化为md文件。

嵩哥语录的来源有很多, 除了上述的新浪微博，腾讯微博，Vae+，还有演唱会上面的talk，采访，直播，杂志，海上灵光，专辑描述等等，
目前我只写了新浪微博和腾讯微博动态的爬虫，其他的来源可能无法通过爬虫来获取就只能靠人工搜集了。  

### 提交说明
如果有新的语录来源, 请创建文件夹, 并在文件夹中按照json格式加入同名.yl文件。如果可以通过爬虫获取可以直接加入同名.py文件,输出结果写入同名.txt文件, 格式为json。
具体的提交说明和目前需要完成的任务见issue。


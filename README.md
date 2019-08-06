# pinyin2word

Pinyin2Chinese demo use algorithms including Trie and HMM model  
基于隐马尔科夫模型与Trie树的拼音切分与拼音转中文的简单demo实现。  

# How to run?

```shell
bash run.sh
```

This command will create the environment that needed by the models.  
This project is created on the purposes of easy-on-run.  
If you want to know the details about the models, just read code.  

# 一、项目介绍  

基于隐马尔科夫模型与Trie树的进行拼音切分与中文转换两个任务。   

# 1、拼音切分    

类似于中文分词，需要将用户输入的字母拼音转换成对应的拼音列表，如‘woaini’--> ['wo', 'ai', 'ni']，  
这是拼音转文字的第一步，这一步包括跨音节的问题，如xian,可以对应['xi', 'an'] 以及['xian']两种切分结果。  
本项目利用可能的拼音集合，构建trie字典树，随后采用字典树查找的方式完成切分。  

# 1、拼音序列切分    

input

nihaozhongguo
['ni', 'hao', 'zhong', 'guo']

woshizhongguoren
['wo', 'shi', 'zhong', 'guo', 'ren']

# 2、拼音转文字  

input

nihaozhongguo
['ni', 'hao', 'zhong', 'guo']
['你', '好', '中', '国']

woshizhongguoren
['wo', 'shi', 'zhong', 'guo', 'ren']
['我', '是', '中', '国', '人']


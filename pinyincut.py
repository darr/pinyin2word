#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : pinyincut.py
# Create date : 2019-08-06 18:50
# Modified date : 2019-08-06 21:55
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import pickle
from trie import Trie
from trie import TrieNode
from trie import SearchIndex

class PinyinCut:
    def __init__(self):
        self.trie_path = 'data/pinyin_trie.model'
        self.trie = self.load_trie(self.trie_path)

    def load_trie(self, trie_path):
        with open(trie_path, 'rb') as f:
            return pickle.load(f)

    #音节切分
    def cut(self, sent):
        #获取总长度
        len_sent = len(sent)
        #存储切分序列
        chars = []
        #存储候选序列,SearchIndex(0)表示第一个字符
        candidate_index = [SearchIndex(0)]
        #当前单词的最后一个位置
        last_index = None
        while candidate_index:
            p = candidate_index.pop()
            #如果当前字符所在索引为句子长度，那么最后一个index为本身，即直接到句子末尾。
            if p.index == len_sent:
                last_index = p
                break
            matches = self.trie.search(sent[p.index:])
            for m in matches:
                new_index = SearchIndex(len(m) + p.index, m, p)
                candidate_index.append(new_index)
        index = last_index
        while index:
            if index.parent:
                chars.insert(0, index.char)
            index = index.parent

        return chars
#
# if __name__ == '__main__':
#     trie = Trie()
#     trie.build_trie()
#     cuter = PinyinCut()
#     while(1):
#         user_input = input('enter an string to transfer:')
#         cut_result = cuter.cut(user_input)
#         print(cut_result)

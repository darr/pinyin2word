#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : trie.py
# Create date : 2019-08-06 19:07
# Modified date : 2019-08-06 19:07
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

#定义trie字典树节点
class TrieNode:
    def __init__(self):
        self.value = None
        self.children = {}
#遍历树
class SearchIndex:
    def __init__(self, index, char=None, parent=None):
        self.index = index
        self.char = char
        self.parent = parent
        
#定义Trie字典树
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.trie_path = 'data/pinyin_trie.model'
        self.pinyin_path = 'data/pinyin.txt'

    #添加树节点
    def insert(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                child = TrieNode()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.value = key

    #查找节点
    def search(self, key):
        node = self.root
        matches = []
        for char in key:
            if char not in node.children:
                break
            node = node.children[char]
            if node.value:
                matches.append(node.value)
        return matches

    def build_trie(self):
        trie = Trie()
        for line in open(self.pinyin_path):
            word = line.strip().lower()
            trie.insert(word)
        with open(self.trie_path, 'wb') as f:
            pickle.dump(trie, f)


# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:20:31 2019

@author: kj494
"""

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
       # use trie
        trie = self.constructTrie(words)
        self.final = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.generate(board, i, j, trie)
        return self.final
    
    def generate(self, board, i, j, trie):
       
        if trie.get('word'):
            self.final.append(trie['word'])
         
            trie['word'] = None
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] not in trie:
            return
        c, board[i][j] = board[i][j], '#'
        self.generate(board, i-1, j, trie[c])
        self.generate(board, i+1, j, trie[c])
        self.generate(board, i, j-1, trie[c])
        self.generate(board, i, j+1, trie[c])
        board[i][j] = c
    
    def constructTrie(self, words):
        trie = {}
        for word in words:
            cur = trie
            for char in word:
                cur = cur.setdefault(char, {})
            cur['word'] = word
        return trie
        
        
#test code

words = ["oath","pea","eat","rain"]
#words = ["neat"]
board = [
         ['o','a','a','n'],
         ['e','t','a','e'],
         ['i','h','k','r'],
         ['i','f','l','v'],
         ['e','z','p','m']

output = myobj.findWords(board,words)
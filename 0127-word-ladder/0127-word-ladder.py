from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordListDeque = deque(wordList)
        
        if endWord not in set(wordList):
            return 0
        
        wordListHashmap = dict()
        
        for i,v in enumerate(wordList):
            wordListHashmap[v] = i
            
        
        wordListDeque.appendleft(beginWord)
        N = len(wordListDeque)
        
        edges = [[] for i in range(N)]
        
        # 5000
        for word_index in range(N):
            word = wordListDeque[word_index]
            # 10
            for c_i, c in enumerate(word):
                # 26
                for k in range(26):
                    next_c = chr(ord('a') + k)
                    if next_c == c:
                        continue
                    complete_word = word[:c_i] + next_c + word[c_i+1:]
                    if complete_word in wordListHashmap:
                        edges[word_index].append(wordListHashmap[complete_word] + 1)
                        
            
                    
        visited = [0] * len(wordListDeque)
        
        q = deque()
        
        q.append((0, 0))
        
        while len(q):
            f_v, f_c = q.popleft()
            visited[f_v] = 1
            
            print(f_v, edges[f_v])
            
            if wordListDeque[f_v] == endWord:
                return f_c + 1
            for i in edges[f_v]:
                if visited[i] == 0:
                    q.append((i, f_c+1))
                    
        
        return 0
    
                    
            
            
        
        
        
        
        
        
        
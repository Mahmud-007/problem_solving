class Node:
    def __init__(self):
        self.children = [None]*26
        self.wordEnd = False

class Trie:
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        return Node()
    
    def getIndex(self, c):
        return ord(c)-ord('a')      # Assuming that trie would be with lowercase letters
    
    def insert(self, word):
        current_node = self.root
        for i in range (len(word)):
            index = self.getIndex(word[i])
            if not current_node.children[index]:
                current_node.children[index] = self.getNode()
            current_node = current_node.children[index]
        current_node.wordEnd = True

    def search (self, word):
        current_node = self.root
        for i in range(len(word)):
            index = self.getIndex(word[i])
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]
        return True

def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))

if __name__ == '__main__':
    main()
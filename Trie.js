class Node {
  constructor() {
    this.links = new Array(26);
    this.flag = false;
  }
  containsKey(ch) {
    if (this.links[ch.charCodeAt(0) - "a".charCodeAt(0)] == undefined) {
      return false;
    } else {
      return true;
    }
  }
  put(ch, node) {
    this.links[ch.charCodeAt(0) - "a".charCodeAt(0)] = node;
  }
  get(ch) {
    return this.links[ch.charCodeAt(0) - "a".charCodeAt(0)];
  }
  isEnd() {
    return this.flag;
  }
  setEnd() {
    this.flag = true;
  }
}
class Trie {
  constructor() {
    this.root = new Node();
  }
  insert(word) {
    let node = this.root;
    for (let i = 0; i < word.length; i++) {
      if (!node.containsKey(word[i])) {
        node.put(word[i], node);
      }
      node = node.get(word[i]);
    }
    node.setEnd()
  }
  search(word){
    let node = this.root;
    for (let i = 0; i < word.length; i++) {
        if (!node.containsKey(word[i])) {
            return false;
        }
        node = node.get(word[i]);
    }
    return node.isEnd();
  }
  startsWith(prefix) {
    let node = this.root;
    for (let i = 0; i < prefix.length; i++) {
        if (!node.containsKey(prefix[i])) {
            return false;
        }
        node = node.get(prefix[i])
    }
    return true;
  }
}
function main() {
    const trie = new Trie();
    console.log("Inserting words: Striver, Striving, String, Strike");
    trie.insert("striver");
    trie.insert("striving");
    trie.insert("string");
    trie.insert("strike");
    
    console.log("Search if Strawberry exists in trie: " +
    (trie.search("strawberry") ? "True" : "False"));
    
    console.log("Search if Strike exists in trie: " +
   ( trie.search("strike") ? "True" : "False" ));
    
    console.log("If words in Trie start with Stri: " +
    (trie.startsWith("stri") ? "True" : "False"));
}

// Execute main function
main();
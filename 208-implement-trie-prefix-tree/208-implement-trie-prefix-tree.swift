class TrieNode {
    var value: String?
    var nexts: [TrieNode?]
    var isTheLast: Bool?
    
    
    init(val: String, nexts: [TrieNode?], isTheLast: Bool)  {
        self.value = val
        self.nexts = nexts
        self.isTheLast = isTheLast
    }
}


let trie =  Trie();
trie.insert("apple");
print(trie.search("apple"))    // return True
print(trie.search("app"))    // return False
print(trie.startsWith("app")) // return True
trie.insert("app");
print(trie.search("app"))     // return True


class Trie {
    var root: TrieNode!
    var curr: TrieNode!
    
    init() {
        root = TrieNode(val: "", nexts: [], isTheLast: false)
    }

    
    func insert(_ word: String) {
        curr = self.root
        
        for i in 0..<word.count {
            if !curr.nexts.map({ $0?.value }).contains("\(word[i])") {
                let newNode = TrieNode(val: "\(word[i])", nexts: [], isTheLast: i == (word.count-1))
                curr.nexts.append(newNode)
                curr = newNode
            } else {
                curr = curr.nexts.first(where: { $0!.value == "\(word[i])"}) as! TrieNode
            }
        }
        
        curr.isTheLast = true
    }
    
    func search(_ word: String) -> Bool {
        curr = self.root
        
        for i in 0..<word.count {
            if !curr.nexts.map({ $0?.value }).contains("\(word[i])") {
               return false
            } else {
                curr = curr.nexts.first(where: { $0!.value == "\(word[i])"}) as! TrieNode
            }
        }
        
        return curr.isTheLast ?? false
    }
    
    func startsWith(_ prefix: String) -> Bool {
        curr = self.root
        
        for i in 0..<prefix.count {
            if curr.nexts.isEmpty || !curr.nexts.map({ $0?.value }).contains("\(prefix[i])") {
               return false
            } else {
                curr = curr.nexts.first(where: { $0!.value == "\(prefix[i])"}) as! TrieNode
            }
        }
        
        return true
    }
}


extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}


/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie()
 * obj.insert(word)
 * let ret_2: Bool = obj.search(word)
 * let ret_3: Bool = obj.startsWith(prefix)
 */
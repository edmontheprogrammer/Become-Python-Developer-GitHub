// creating a class named 'Stack' to repersents the stack data structure 
class Stack {
    var stackArray = [String]()
    // push method to add items to the top of the stack
    func push(item:String) {
        self.stackArray.append(item)
    }

    // pop method to remove items from the stack 
    func pop()->String? {
        if self.stackArray.last != nil {
            let lastString = self.stackArray.last
            self.stackArray.removeLast()
            return lastString!
        } else {
            return nil 
        }
    }

    // peek method to look at the top item of the stack 
    // Note 1; the peek() method does not remove the item at the top of the stack 
    // it just looks at the item at top of the stack 
    func peek() -> String? {
        if self.stackArray.last != nil {
            return self.stackArray.last 
        } else {
            return nil
        }
    }
}
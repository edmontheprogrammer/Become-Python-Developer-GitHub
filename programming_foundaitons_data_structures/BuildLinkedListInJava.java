// Linked List 
public class BuildLinkedListInJava {
    Node head;

    public void add(int data) {
        // LinkedList is empty
        if (this.head == null) {
            this.head = new Node(data);
        } else {
            // LinkedList is not empty
            Node nodeToNode = new Node(data);
            nodeToNode.next = this.head;
            this.head = nodeToNode;
        }
    }

    public static void main(String[] args) {
        BuildLinkedListInJava myList = new BuildLinkedListInJava();
        myList.add(10);
        myList.add(18);
        System.out.println(myList.head.data);
        System.out.println(myList.head.next.data);
    }
}

// Node
class Node {
    int data;
    Node next;

    Node(int d) {
        this.data = d;
    }
}
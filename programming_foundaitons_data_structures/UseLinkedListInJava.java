import java.util.LinkedList;

public class UseLinkedListInJava {
    public static void main(String[] args) {
        // creating a linkedlist in java
        LinkedList travelBucketList = new LinkedList<>();

        // Add Items to a linkedlist in java using the add method
        travelBucketList.add("Santorini, Greece");
        travelBucketList.addFirst("Barcelona, Spain");
        travelBucketList.addLast("Tokyo, Japan");
        travelBucketList.add(2, "Galapagos, Ecuador");

        // Printing the linkedlist to the console.
        System.out.println(travelBucketList);

        // Accessing items in a linkedlist
        System.out.println(travelBucketList.get(2));
        System.out.println(travelBucketList.getFirst());

        // Searching LinkedList for items
        // Note 1; The one line operations can be computational expensive
        System.out.println(travelBucketList.contains("Barcelona, Spain"));

        // Removing items from LinkedList
        travelBucketList.removeFirst();
        travelBucketList.removeLast();
        System.out.println(travelBucketList);

        // removing item by objecct
        travelBucketList.remove("Santorini, Greece");
        // removing item by index
        travelBucketList.remove(0);
        System.out.println(travelBucketList);
    }
}
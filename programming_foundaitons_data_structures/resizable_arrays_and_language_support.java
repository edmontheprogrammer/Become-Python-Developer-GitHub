import java.util.ArrayList;

public class resizable_arrays_and_language_support {
    public static void main(String[] args) {
        ArrayList<Integer> myArrayList = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            myArrayList.add(i);
        }
        myArrayList.add(2, 10);
        System.out.println(myArrayList);

    }
}
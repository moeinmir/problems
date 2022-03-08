// Java program to show working of user defined
// Generic classes
// We use < > to specify Parameter type
// class Deque<T> {
//     // An object of type T is declared
//     T obj;
//
//     Deque(T obj) {
//         this.obj = obj;
//     } // constructor
//
//     public T getObject() {
//         return this.obj;
//     }
//
//     public static void main(String[] args) {
//         // instance of Integer type
//         Deque<Integer> iObj = new Deque<Integer>(15);
//         System.out.println(iObj.getObject());
//
//         // instance of String type
//         Deque<String> sObj
//                 = new Deque<String>("GeeksForGeeks");
//         System.out.println(sObj.getObject());
//     }
// }

public class Deque<Item> implements Iterable<Item> {
    //
    //     // construct an empty deque
    //     public Deque()
    //
    //     // is the deque empty?
    //     public boolean isEmpty()
    //
    //     // return the number of items on the deque
    //     public int size()
    //
    //     // add the item to the front
    //     public void addFirst(Item item)
    //
    //     // add the item to the back
    //     public void addLast(Item item)
    //
    //     // remove and return the item from the front
    //     public Item removeFirst()
    //
    //     // remove and return the item from the back
    //     public Item removeLast()
    //
    //     // return an iterator over items in order from front to back
    //     public Iterator<Item> iterator()
    //
    //     // unit testing (required)
    //     public static void main(String[] args)
    //
}




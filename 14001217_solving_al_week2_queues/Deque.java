public class Deque<Item> {

    public class Node {
        public Item item;
        public Node next;
    }

    public Node first;
    public Node last;
    public Node current;
    public int size;
    
    //     // construct an empty deque
    public Deque() {
        first = null;
        last = null;
        size = 0;
        current = null;
    }

    //
    //     // is the deque empty?
    public boolean isEmpty() {
        return (size == 0);
    }

    //
    //     // return the number of items on the deque
    public int size() {
        return size;
    }

    //
    //     // add the item to the front
    public void addFirst(Item item) {
        Node oldlast = last;
        last = new Node();
        last.item = item;
        last.next = null;
        if (isEmpty()) first = last;
        else oldlast.next = last;
        size = size + 1;
    }

    //
    //     // add the item to the back
    public void addLast(Item item) {
        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;
    }

    //
    //     // remove and return the item from the front
    public Item removeFirst() {
        Item item = first.item;
        first = first.next;
        if (isEmpty()) last = null;
        return item;
    }

    //
    //     // remove and return the item from the back
    public Item removeLast() {
        Item item = first.item;
        first = first.next;
        return item;
    }
    //
    //     // return an iterator over items in order from front to back
    // public Iterator<Item> iterator() {
    //     System.out.println("hello");
    // }

    //
    //     // unit testing (required)
    public static void main(String[] args) {
        System.out.println("hello");
        Deque<Integer> my_object = new Deque<Integer>();
        for (int i = 0; i < 10; i++) {
            my_object.addFirst(i);
        }
        my_object.current = my_object.first;
        for (int i = 0; i < 5; i++) {
            my_object.current = my_object.current.next;
            System.out.println(my_object.current.item);
        }
    }
    //
}




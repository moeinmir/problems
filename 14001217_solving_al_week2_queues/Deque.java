import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    public class Node {
        public Item item;
        public Node next;
        public Node prev;
    }

    public Node first;
    public Node last;
    public Node current;
    public int size;

    public Deque() {
        first = null;
        last = null;
        size = 0;
        current = null;
    }

    public boolean isEmpty() {
        return (size == 0);
    }

    public int size() {
        return size;
    }

    public void addFirst(Item item) {
        if (isEmpty()) {
            first = new Node();
            first.item = item;
            first.next = null;
            first.prev = null;
            last = first;
        }
        else {
            // current = new Node();
            Node oldfirst = first;
            first = new Node();
            first.item = item;
            first.next = null;
            first.next = oldfirst;
            oldfirst.prev = first;
            first.prev = null;
        }
        size = size + 1;
    }

    public void addLast(Item item) {
        if (isEmpty()) {
            first = new Node();
            first.item = item;
            first.next = null;
            first.prev = null;
            last = first;
        }
        else {
            Node oldlast = last;
            last = new Node();
            last.item = item;
            oldlast.next = last;
            last.prev = oldlast;
        }
        size = size + 1;
    }

    public Item removeFirst() {
        Item item = first.item;
        first = first.next;
        if (isEmpty()) last = null;
        return item;
    }

    public Item removeLast() {
        Item item = last.item;
        last = last.prev;
        last.next = null;
        System.out.println("%%%%%%%%%%");
        System.out.println(item);
        System.out.println("************");
        return item;
    }

    public Iterator<Item> iterator() {
        System.out.println("hello");
        return new NewIterator();
    }

    private class NewIterator implements Iterator<Item> {
        private Node current1 = first;

        public boolean hasNext() {
            return current1 != null;
        }

        public Item next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            Item item = current1.item;
            current1 = current1.next;
            return item;
        }

    }

    public static void main(String[] args) {
        System.out.println("hello");
        Deque<Integer> my_object = new Deque<Integer>();
        my_object.addFirst(100);
        my_object.addFirst(101);
        my_object.addFirst(102);
        my_object.addFirst(103);
        my_object.addFirst(104);
        my_object.addFirst(105);
        my_object.addFirst(107);
        my_object.addLast(110);
        my_object.addLast(108);
        my_object.removeFirst();
        my_object.removeLast();

        Iterator<Integer> my_iter = my_object.iterator();
        while (my_iter.hasNext()) {
            System.out.println(my_iter.next());
        }
    }
}




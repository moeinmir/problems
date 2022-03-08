/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import java.util.Iterator;

public class Deque<Item> implements Iterable<Item> {
    private Node first = null;
    private Node last = null;

    private class Node {
        String item;
        Node next;
    }


    // construct an empty deque
    public Deque()

    // is the deque empty?
    public boolean isEmpty() {
        return first == null
    }

    // return the number of items on the deque
    public int size()

    // add the item to the front
    public void addFirst(Item item) {
        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;
    }

    // add the item to the back
    public void addLast(Item item) {
        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;

    }

    // remove and return the item from the front
    public Item removeFirst()

    // remove and return the item from the back
    public Item removeLast() {
        String item = first.item;
        first = first.next;
        return item;
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() {
        private Node current = first;
        public boolean hasNext () {
            return current != null;
        }
        public Item next ()
        {
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    // unit testing (required)
    public static void main(String[] args) {

    }

}

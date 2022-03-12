/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.StdRandom;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private class Node {
        private Item item;
        private Node next;
    }
    
    public RandomizedQueue() {
    }


    private Node first;
    private int size = 0;
    private Node current1;
    // construct an empty randomized queue
    // public RandomizedQueue()

    // is the randomized queue empty?
    public boolean isEmpty() {
        return (size == 0);
    }

    // return the number of items on the randomized queue
    public int size() {
        return size;
    }

    // add the item
    public void enqueue(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        if (isEmpty()) {
            first = new Node();
            first.item = item;
            first.next = null;
        }
        else {
            // current = new Node();
            Node oldfirst = first;
            first = new Node();
            first.item = item;
            first.next = null;
            first.next = oldfirst;
        }
        size = size + 1;
    }


    // remove and return a random item
    public Item dequeue() {
        if (this.isEmpty()) {
            throw new NoSuchElementException();
        }
        int rand = StdRandom.uniform(size);
        current1 = first;
        for (int i = 0; i - 1 < rand; i++) {
            current1 = current1.next;
        }
        Node current2 = current1.next;
        if (current1.next.next == null) {
            current1.next = null;
        }
        else {
            current1.next = current1.next.next;
        }
        size = size - 1;
        return current2.item;
    }

    // return a random item (but do not remove it)
    public Item sample() {
        if (this.isEmpty()) {
            throw new NoSuchElementException();
        }
        int rand = StdRandom.uniform(size);
        Node current = first;
        for (int i = 0; i < rand; i++) {
            current = current.next;
        }
        return current.item;
    }

    // return an independent iterator over items in random order
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

        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    // unit testing (required)
    public static void main(String[] args) {
        RandomizedQueue<Integer> my_object = new RandomizedQueue<Integer>();
        my_object.enqueue(101);
        my_object.enqueue(102);
        my_object.enqueue(103);
        my_object.enqueue(104);
        System.out.println("*************");
        System.out.println(my_object.sample());
        System.out.println("###########");
        my_object.enqueue(1004);
        my_object.enqueue(1005);
        my_object.enqueue(1006);
        my_object.enqueue(1007);
        my_object.enqueue(1008);
        my_object.enqueue(1009);
        my_object.dequeue();
        Iterator<Integer> my_iter = my_object.iterator();
        while (my_iter.hasNext()) {
            System.out.println(my_iter.next());
        }
    }
}
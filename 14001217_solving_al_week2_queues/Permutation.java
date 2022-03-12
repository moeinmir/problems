/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */
// the code works fine for a few time and then the java.lang.NullPointerException error raise i think i should know the differences of premetive type and reffernce type better and learn  where to use it

import edu.princeton.cs.algs4.StdIn;

import java.util.Iterator;

public class Permutation {
    public static void main(String[] args) {
        int num = Integer.parseInt(args[0]);
        RandomizedQueue<String> my_randomized_queue = new RandomizedQueue<String>();
        // String current2 = StdIn.readString();
        my_randomized_queue.enqueue(StdIn.readString());
        while (!StdIn.isEmpty()) {
            // String current = StdIn.readString();
            my_randomized_queue.enqueue(StdIn.readString());
        }
        System.out.println("***************");
        Iterator<String> my_iter = my_randomized_queue.iterator();
        while (my_iter.hasNext()) {
            System.out.println(my_iter.next());
        }
        System.out.println("***************");
        System.out.println(my_randomized_queue.dequeue());
        System.out.println("***************");
        my_iter = my_randomized_queue.iterator();
        System.out.println("***************");
        while (my_iter.hasNext()) {
            System.out.println(my_iter.next());
        }
        System.out.println("***************");
        System.out.println(my_randomized_queue.dequeue());
        System.out.println("***************");
        my_iter = my_randomized_queue.iterator();
        while (my_iter.hasNext()) {
            System.out.println(my_iter.next());
        }
        System.out.println("***************");
        System.out.println(my_randomized_queue.dequeue());
        System.out.println("***************");
        my_iter = my_randomized_queue.iterator();
        System.out.println("***************");
        while (my_iter.hasNext()) {
            System.out.println(my_iter.next());
        }
        System.out.println("***************");


        // System.out.println("&&&&&&&&&&&&&&&&&&");
        // for (int k = 0; k < num; k++) {
        //     System.out.println(my_randomized_queue.dequeue());
        // }
    }
}

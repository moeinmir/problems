/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */
// the code works fine for a few time and then the java.lang.NullPointerException error raise i think i should know the differences of premetive type and reffernce type better and learn  where to use it

import edu.princeton.cs.algs4.StdIn;

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
        for (int i = 0; i < num; i++) {
            // String current1 = my_randomized_queue.dequeue();
            System.out.println(my_randomized_queue.dequeue());
        }
    }
}

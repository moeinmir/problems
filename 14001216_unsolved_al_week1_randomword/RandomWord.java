/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */
// command for compiling: javac-algs4 RandomWord.java
// command for running: java-algs4 RandomWord < names.txt
// command for running: java-algs4 RandomWord name1 name2 name2
// problme: i cant run java-algs4 RandomWord and give inputs seperatly and break when the user type nothing and press enter
//
//


import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

import java.util.Scanner;

public class RandomWord {
    private static String champ;
    private static String tmp;
    private static Scanner my_object;

    public static void main(String[] args) {

        // StdOut.println(StdIn.isEmpty());
        if (args.length >= 1) {
            int l = args.length;
            int m = 0;
            for (int i = 0; i < l; i++) {
                m = m + 1;
                if (StdRandom.bernoulli((float) 1 / m)) {
                    champ = args[i];
                }
            }
            StdOut.println(champ);
            return;
        }
        if (args.length == 0) {
            // try {
            int n = 1;
            champ = StdIn.readString();
            while (true) {
                n = n + 1;
                tmp = StdIn.readString();
                if (StdIn.isEmpty()) {
                    StdOut.println(champ);
                    break;
                }
                if (StdRandom.bernoulli((float) 1 / n)) {
                    champ = tmp;
                }
            }
        }
        // }
        // catch (Exception e) {
        //     StdOut.println("we are here");
        //     int p = 0;
        //     while (true) {
        //         p = p + 1;
        //         my_object = new Scanner(System.in);
        //         if (!my_object.nextLine().isEmpty()) {
        //             if ((StdRandom.bernoulli((float) 1 / p))) {
        //                 champ = my_object.nextLine();
        //             }
        //         }
        //         if (my_object.nextLine().isEmpty()) {
        //             StdOut.println(champ);
        //             return;
        //         }
        //     }
        // }

    }
}
// }


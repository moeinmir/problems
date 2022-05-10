/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.TST;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class BoggleSolver {
    private Queue<String> qu;
    private TST<Boolean> dict;
    private Node[][] boardOfNodes;
    int w;
    int h;

    private class Node {
        Character val;
        int index;
        Node[] neighbers = new Node[8];
    }

    // Initializes the data structure using the given array of strings as the dictionary.
    // (You can assume each word in the dictionary contains only the uppercase letters A through Z.)
    public BoggleSolver(String[] dictionary) {
        dict = new TST<Boolean>();
        for (String s : dictionary) {
            dict.put(s, true);
        }
    }

    // Returns the set of all valid words in the given Boggle board, as an Iterable.
    public Iterable<String> getAllValidWords(BoggleBoard board) {
        boardFiller(board);
        Queue<String> queue = new Queue<String>();
        Set<Integer> tempSet = new HashSet<Integer>();
        tempSet.add(0);
        ArrayList<Node> temp = new ArrayList<Node>();
        collect(boardOfNodes[0][0], temp, queue, tempSet);
        

        return queue;
    }

    private void collect(Node x, ArrayList<Node> prefix, Queue<String> q, Set<Integer> hs) {
        if (x == null) return;
        if (x.val != null) q.enqueue(prefix);
        Set<Integer> neighberSet = new HashSet<Integer>();
        for (Node n : x.neighbers) {
            if (n != null) {
                neighberSet.add(n.index);
            }
        }
        neighberSet.removeAll(hs);
        for (int n : neighberSet
        ) {
            if (boardOfNodes[n % w][n / w] != null) {
                hs.add(boardOfNodes[n % w][n / w].index);
                collect(boardOfNodes[n % w][n / w], prefix + boardOfNodes[n % w][n / w].val, q, hs);
            }
        }

    }

    private void boardFiller(BoggleBoard board) {
        w = board.cols();
        h = board.rows();
        boardOfNodes = new Node[w][h];
        for (int i = 0; i < w; i++) {
            for (int k = 0; k < h; k++) {
                boardOfNodes[i][k] = new Node();
                boardOfNodes[i][k].index = k * w + i;
            }
        }


        for (
                int i = 0;
                i < w; i++) {
            for (int j = 0; j < h; j++) {
                boardOfNodes[i][j].val = board.getLetter(i, j);
                int indexCounter = 0;
                for (int p = 0; p < 3; p++) {
                    for (int q = 0; q < 3; q++) {
                        if (p == 1 && q == 1) {
                            continue;
                        }
                        if (i == w - 1 && p == 2) {
                            continue;
                        }
                        if (i == 0 && p == 0) {
                            continue;
                        }
                        if (j == h - 1 && q == 2) {
                            continue;
                        }
                        if (j == 0 && q == 0) {
                            continue;
                        }
                        boardOfNodes[i][j].neighbers[indexCounter] = boardOfNodes[i - 1
                                + p][
                                j - 1 + q];
                        indexCounter += 1;
                    }
                }
            }
        }
    }

    // Returns the score of the given word if it is in the dictionary, zero otherwise.
    // (You can assume the word contains only the uppercase letters A through Z.)
    // public int scoreOf(String word)

    public static void main(String[] args) {
        In in = new In(args[0]);
        String[] dictionary = in.readAllStrings();
        BoggleSolver solver = new BoggleSolver(dictionary);
        BoggleBoard board = new BoggleBoard(args[1]);
        solver.getAllValidWords(board);

        for (String s : solver.getAllValidWords(board)) {
            System.out.println(s);
        }

        // int score = 0;
        // for (String word : solver.getAllValidWords(board)) {
        //     StdOut.println(word);
        //     score += solver.scoreOf(word);
        // }
        // StdOut.println("Score = " + score);
    }
}


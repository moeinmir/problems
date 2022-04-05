/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.Queue;

public class Solver {

    private class SearchNode implements Comparable<SearchNode> {
        private SearchNode prevNode = null;
        private Board current = null;
        private int moveNumber = 0;
        private int priority = 0;
        private boolean issolveable;


        public SearchNode(Board currentB, int movesN, SearchNode preveN) {
            prevNode = preveN;
            current = currentB;
            moveNumber = movesN;
            priority = movesN + currentB.manhattan();
        }
    }


    // find a solution to the initial board (using the A* algorithm)
    public Solver(Board initial) {
        MinPQ<SearchNode> searchNodes = new MinPQ<SearchNode>();
        Queue<Board> neighbers = new Queue<Board>();
        searchNodes.insert(initial);

        while (true) {
            SearchNode cur = searchNodes.delMin();
            neighbers = cur.current.neighbors();
            if (cur.current.manhattan() == 0) {
                break;
            }
            for (Board n : neighbers) {
                SearchNode searchNo = new SearchNode();
                searchNo.current = n;
                searchNo.moveNumber = cur.moveNumber += 1;
                searchNo.prevNode = cur;
                searchNodes.insert(searchNo);
            }
        }
    }

    // is the initial board solvable? (see below)
    // public boolean isSolvable()

    // min number of moves to solve initial board; -1 if unsolvable
    // public int moves() {
    //     return
    // }

    // sequence of boards in a shortest solution; null if unsolvable
    // public Iterable<Board> solution()

    // test client (see below)
    // public static void main(String[] args) {
    //
    //     // create initial board from file
    //     In in = new In(args[0]);
    //     int n = in.readInt();
    //     int[][] tiles = new int[n][n];
    //     for (int i = 0; i < n; i++)
    //         for (int j = 0; j < n; j++)
    //             tiles[i][j] = in.readInt();
    //     Board initial = new Board(tiles);
    //
    //     // solve the puzzle
    //     Solver solver = new Solver(initial);
    //
    //     // print solution to standard output
    //     if (!solver.isSolvable())
    //         StdOut.println("No solution possible");
    //     else {
    //         StdOut.println("Minimum number of moves = " + solver.moves());
    //         for (Board board : solver.solution())
    //             StdOut.println(board);
    //     }
    // }

}

/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.Queue;

public class Solver {
    private SearchNode fin;
    private boolean solveable;

    private class SearchNode implements Comparable<SearchNode> {
        private SearchNode prevNode = null;
        private Board current = null;
        private int moveNumber = 0;
        private int priority = 0;
        private boolean issolveable;
        private Board[][] initial2;

        @Override
        public int compareTo(SearchNode that) {
			/*
			if (this.priority > o.getPriority())
				return 1;
			else if (this.priority < o.getPriority())
				return -1;
			else
				return 0;*/

            return this.priority - that.priority;
        }

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
        // MinPQ<SearchNode> searchNodes2 = new MinPQ<SearchNode>();
        // Queue<Board> neighbers2 = new Queue<Board>();


        SearchNode initial_search_node;
        // SearchNode initial_search_node2;


        initial_search_node = new SearchNode(initial, 0, null);
        searchNodes.insert(initial_search_node);

        while (true) {
            SearchNode cur = searchNodes.delMin();
            if (cur.current.manhattan() == 0) {
                this.fin = cur;
                break;
            }
            for (Board n : cur.current.neighbors()) {
                SearchNode searchNo = new SearchNode(n, cur.moveNumber + 1, cur);
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
    public static void main(String[] args) {
        In in = new In(args[0]);
        int n = in.readInt();
        int[][] tiles = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                tiles[i][j] = in.readInt();
        Board initial = new Board(tiles);

        // solve the puzzle
        Solver solver = new Solver(initial);
        System.out.println(solver.fin.moveNumber);


    }

}

/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.MinPQ;

import java.util.Iterator;

public class Solver {
    private SearchNode fin;
    private SearchNode twinFin;
    private boolean solveable;
    private MinPQ<SearchNode> searchNodes = new MinPQ<SearchNode>();
    // private Queue<Board> neighbers = new Queue<Board>();
    private MinPQ<SearchNode> twinSearchNodes = new MinPQ<SearchNode>();
    // private Queue<Board> twinNeighbers = new Queue<Board>();
    private SearchNode initial_search_node;
    private SearchNode twinInitial_search_node;
    private Board initBoard;
    private Board twinBoard;

    private class SearchNode implements Comparable<SearchNode> {
        private SearchNode prevNode = null;
        private Board current = null;
        private int moveNumber = 0;
        private int priority = 0;
        private int manhattanCatch;

        @Override
        public int compareTo(SearchNode that) {
            return this.priority - that.priority;
        }

        public SearchNode(Board currentB, int movesN, SearchNode preveN) {
            prevNode = preveN;
            current = currentB;
            moveNumber = movesN;
            manhattanCatch = currentB.manhattan();
            priority = movesN + manhattanCatch;
        }
    }


    // find a solution to the initial board (using the A* algorithm)
    public Solver(Board initial) {
        searchNodes.insert(new SearchNode(initial, 0, null));
        twinSearchNodes.insert(new SearchNode(initial.twin(), 0, null));


        while (true) {
            SearchNode cur = searchNodes.delMin();
            SearchNode twinCur = twinSearchNodes.delMin();
            for (Board n : cur.current.neighbors()) {
                if (cur.prevNode != null) {
                    if (n.equals(cur.prevNode.current)) {
                        continue;
                    }
                }
                SearchNode searchNo = new SearchNode(n, cur.moveNumber + 1, cur);
                searchNodes.insert(searchNo);
            }
            if (cur.manhattanCatch == 0) {
                this.fin = cur;
                this.solveable = true;
                break;
            }
            for (Board m : twinCur.current.neighbors()) {
                if (twinCur.prevNode != null) {
                    if (m.equals(twinCur.prevNode.current)) {
                        continue;
                    }
                }
                SearchNode twinSearchNo = new SearchNode(m, twinCur.moveNumber + 1, twinCur);
                twinSearchNodes.insert(twinSearchNo);
            }
            if (twinCur.manhattanCatch == 0) {
                this.twinFin = twinCur;
                this.solveable = false;
                break;
            }

            Iterator<SearchNode> myIter = searchNodes.iterator();
            int i = 0;
            // while (myIter.hasNext()) {
            //     System.out.println(myIter.next().current.manhattan());
            //     i++;
            // }
        }
    }

    public int moves() {
        if (!this.solveable)
            return -1;
        return this.fin.moveNumber;

    }

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

        if (solver.solveable) {
            System.out.println(solver.fin.moveNumber);
        }
        else {
            System.out.println("it is not solveable");
        }
    }
}

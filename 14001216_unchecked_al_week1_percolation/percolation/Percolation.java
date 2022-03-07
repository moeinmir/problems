import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private boolean[][] grid;
    private int size;
    private WeightedQuickUnionUF uf_grid;
    private WeightedQuickUnionUF uf_full;
    private int but;
    private int top;
    private int open_count;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("the entery is not valid");
        }
        size = n;
        grid = new boolean[size][size];
        uf_grid = new WeightedQuickUnionUF(size * size + 2);
        uf_full = new WeightedQuickUnionUF(size * size + 1);
        but = size * size + 1;
        top = size * size;
        open_count = 0;
    }


    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        if (row <= 0 || row > size || col <= 0 || col > size) {
            throw new IndexOutOfBoundsException("Index is out of range");
        }
        if (grid[row - 1][col - 1]) {
            return;
        }
        grid[row - 1][col - 1] = true;
        open_count += 1;

        if (row == 1) {
            uf_grid.union(col - 1, top);
            uf_full.union(col - 1, top);
        }
        if (row == size) {
            uf_grid.union((row - 1) * size + col - 1, but);
        }
        if (((row - 1) > 0 && (row - 1) <= size && col > 0 && col <= size) && (isOpen(row - 1,
                                                                                      col))) {
            uf_grid.union((row - 1) * size + col - 1, (row - 2) * size + col - 1);
            uf_full.union((row - 1) * size + col - 1, (row - 2) * size + col - 1);
        }
        if (((row) > 0 && (row) <= size && (col - 1) > 0 && (col - 1) <= size) && (isOpen(row, col
                - 1))) {
            uf_grid.union((row - 1) * size + col - 1, (row - 1) * size + col - 2);
            uf_full.union((row - 1) * size + col - 1, (row - 1) * size + col - 2);
        }
        if (((row) > 0 && (row) <= size && (col + 1) > 0 && (col + 1) <= size) && (isOpen(row, col
                + 1))) {
            uf_grid.union((row - 1) * size + col - 1, (row - 1) * size + col);
            uf_full.union((row - 1) * size + col - 1, (row - 1) * size + col);
        }
        if (((row + 1) > 0 && (row + 1) <= size && (col) > 0 && (col) <= size) && (isOpen(row + 1,
                                                                                          col
        ))) {
            uf_grid.union((row - 1) * size + col - 1, (row) * size + col - 1);
            uf_full.union((row - 1) * size + col - 1, (row) * size + col - 1);
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        if (row > 0 && col > 0 && row <= size && col <= size) {
            return grid[row - 1][col - 1];
        }
        else {
            return false;
        }
    }


    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        if (row > 0 && col > 0 && row <= size && col <= size) {
            return uf_full.connected(top, (row - 1) * size + col - 1);
        }
        else {
            return false;
        }
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return open_count;
    }

    // does the system percolate?
    public boolean percolates() {
        return uf_grid.connected(size * size, size * size + 1);
    }


    // test client (optional)
    public static void main(String[] args) {
        int size = Integer.parseInt(args[0]);

        Percolation percolation = new Percolation(size);
        int number_of_union = args.length;
        for (int i = 1; i < number_of_union; i += 2) {
            int row = Integer.parseInt(args[i]);
            int col = Integer.parseInt(args[i + 1]);
            StdOut.printf("%d and %d %n", row, col);
            percolation.open(row, col);
        }
        if (percolation.percolates()) {
            StdOut.printf("percolates %n");
        }
        if (!percolation.percolates()) {
            StdOut.print("Does'nt percolate %n");
        }
    }
}

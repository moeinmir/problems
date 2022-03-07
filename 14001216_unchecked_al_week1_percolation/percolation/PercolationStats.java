import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private double[] results;
    private int trial_count;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("Invalid Entry");
        }
        trial_count = trials;
        results = new double[trial_count];

        for (int i = 0; i < trials; i++) {
            Percolation percolation = new Percolation(n);
            while (!percolation.percolates()) {
                int row = StdRandom.uniform(1, n + 1);
                int col = StdRandom.uniform(1, n + 1);
                percolation.open(row, col);
            }
            results[i] = (double) percolation.numberOfOpenSites() / (n * n);
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(results);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(results);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - ((1.96 * stddev()) / Math.sqrt(trial_count));
    }


    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + ((1.96 * stddev()) / Math.sqrt(trial_count));
    }

    // test client (see below)
    public static void main(String[] args) {
        int size = 10;
        int trial_count = 10;
        if (args.length >= 2) {
            size = Integer.parseInt(args[0]);
            trial_count = Integer.parseInt(args[1]);
        }
        PercolationStats ps = new PercolationStats(size, trial_count);
        String confidence = ps.confidenceLo() + ", " + ps.confidenceHi();
        StdOut.println("mean= " + ps.mean());
        StdOut.println("std= " + ps.stddev());
        StdOut.println("95% confidence interval = " + confidence);
    }
}

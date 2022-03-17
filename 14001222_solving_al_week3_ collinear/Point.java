/******************************************************************************
 *  Compilation:  javac Point.java
 *  Execution:    java Point
 *  Dependencies: none
 *
 *  An immutable data type for points in the plane.
 *  For use on Coursera, Algorithms Part I programming assignment.
 *
 ******************************************************************************/

import edu.princeton.cs.algs4.StdDraw;

import java.util.Arrays;
import java.util.Comparator;
import java.util.InputMismatchException;

public class Point implements Comparable<Point> {

    private final int x;     // x-coordinate of this point
    private final int y;     // y-coordinate of this point
    // public String toString() {
    //     return ("x " + x + " y " + y);
    // }

    /**
     * Initializes a new point.
     *
     * @param x the <em>x</em>-coordinate of the point
     * @param y the <em>y</em>-coordinate of the point
     */
    public Point(int x, int y) {
        /* DO NOT MODIFY */
        this.x = x;
        this.y = y;
    }

    // public Comparator<Point> by_slope = new BY_SLOPE();

    /**
     * Draws this point to standard draw.
     */
    public void draw() {
        /* DO NOT MODIFY */
        StdDraw.point(x, y);
    }

    /**
     * Draws the line segment between this point and the specified point
     * to standard draw.
     *
     * @param that the other point
     */
    public void drawTo(Point that) {
        /* DO NOT MODIFY */
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    /**
     * Returns the slope between this point and the specified point.
     * Formally, if the two points are (x0, y0) and (x1, y1), then the slope
     * is (y1 - y0) / (x1 - x0). For completeness, the slope is defined to be
     * +0.0 if the line segment connecting the two points is horizontal;
     * Double.POSITIVE_INFINITY if the line segment is vertical;
     * and Double.NEGATIVE_INFINITY if (x0, y0) and (x1, y1) are equal.
     *
     * @param that the other point
     * @return the slope between this point and the specified point
     */
    public double slopeTo(Point that) {
        if (this.x != that.x) {
            return ((double) (this.y - that.y)) / ((double) (this.x - that.x));
        }
        else if (this.y > that.y) {
            return Double.POSITIVE_INFINITY;
        }
        else if (this.y < that.y) {
            return Double.NEGATIVE_INFINITY;
        }
        else {
            throw new InputMismatchException();
        }
        /* YOUR CODE HERE */
    }

    /**
     * Compares two points by y-coordinate, breaking ties by x-coordinate.
     * Formally, the invoking point (x0, y0) is less than the argument point
     * (x1, y1) if and only if either y0 < y1 or if y0 = y1 and x0 < x1.
     *
     * @param that the other point
     * @return the value <tt>0</tt> if this point is equal to the argument
     * point (x0 = x1 and y0 = y1);
     * a negative integer if this point is less than the argument
     * point; and a positive integer if this point is greater than the
     * argument point
     */
    public int compareTo(Point that) {
        if (this.y < that.y) {
            return -1;
        }
        else if (this.y > that.y) {
            return 1;
        }
        else {
            if (this.x < this.y) {
                return -1;
            }
            else if (this.x > this.y) {
                return 1;
            }
            else {
                return 0;
            }
        }
    }
    /* YOUR CODE HERE */

    //
    // * Compares two points by the slope they make with this point.
    // * The slope is defined as in the slopeTo() method.
    // *
    // * @return the Comparator that defines this ordering on points
    // */

    public Comparator<Point> slopeOrder() {
        return new my_comparator(this);
        // *//* YOUR CODE HERE *//*
    }

    private class my_comparator implements Comparator<Point> {
        private Point a;

        my_comparator(Point a) {
            this.a = a;
        }

        @Override
        public int compare(Point b, Point c) {
            if (a.slopeTo(b) > a.slopeTo(c)) {
                return 1;
            }
            else if (a.slopeTo(b) < a.slopeTo(c)) {
                return -1;
            }
            else {
                return 0;
            }
        }
    }

    @Override
    public String toString() {
        /* DO NOT MODIFY */
        // return "(" + x + ", " + y + ")";
        return ("x " + x + " y " + y);
    }

    public static void main(String[] args) {
        Point point[] = new Point[3];
        point[0] = new Point(10, 20);
        point[1] = new Point(20, 20);
        point[2] = new Point(30, 20);
        Point g = new Point(1, 1);
        Point b = new Point(2, 2);
        Point c = new Point(1, 5);
        Point d = new Point(2, 7);
        // System.out.println(g.compareTo(b));
        // System.out.println(g.slopeTo(b));
        // final Comparator<Point> by_slope = new BY_SLOPE();
        my_comparator my_comparator = d.new my_comparator(d);
        // Arrays.sort(point, by_slope);
        // System.out.println("*********");
        // System.out.println(Arrays.asList(point));
        // System.out.println("*********");
        Arrays.sort(point, my_comparator);
        System.out.println(Arrays.asList(point));
        System.out.println("*********");
        System.out.println("##########");
    }
}



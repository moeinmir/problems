/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */


import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.SET;

import java.util.Iterator;

public class PointSET {
    private SET<Point2D> pointSet;
    private Point2D nearest;
    private Double dist;

    public PointSET() {
        pointSet = new SET<Point2D>();
    }                               // construct an empty set of points

    public boolean isEmpty() {
        return (pointSet.isEmpty());
    }                      // is the set empty?

    public int size() {
        return pointSet.size();
    }                         // number of points in the set

    public void insert(Point2D p) {
        pointSet.add(p);
    }              // add the point to the set (if it is not already in the set)

    public boolean contains(Point2D p) {
        return pointSet.contains(p);
    }            // does the set contain point p?

    public void draw() {
        Point2D test = new Point2D(2, 2);
        Iterator<Point2D> iter = pointSet.iterator();
        while (iter.hasNext()) {
            iter.next().draw();
        }
    }                         // draw all points to standard draw

    //
    public Iterable<Point2D> range(
            RectHV rect) {
        Queue<Point2D> insidePoints = new Queue<Point2D>();
        RectHV containRec = rect;
        Iterator<Point2D> it = pointSet.iterator();

        while (it.hasNext()) {
            Point2D cPoint = it.next();

            if (rect.contains(cPoint)) {
                insidePoints.enqueue(cPoint);
            }
        }

        return insidePoints;

    }             // all points that are inside the rectangle (or on the boundary)

    //
    public Point2D nearest(

            Point2D p) {
        dist = Double.POSITIVE_INFINITY;
        for (Point2D pointSearch : pointSet) {
            if (pointSearch.distanceTo(p) < dist) {
                dist = pointSearch.distanceTo(p);
                nearest = pointSearch;
            }
        }
        return nearest;
    }             // a nearest neighbor in the set to point p; null if the set is empty

    //
    public static void main(
            String[] args) {
        PointSET testPointSet = new PointSET();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                testPointSet.insert(new Point2D(i, j));
            }
        }
        System.out.println(testPointSet.nearest(new Point2D(2, 2)));
        System.out.println(testPointSet.contains(new Point2D(11, 11)));
    }                 // unit testing of the methods (optional)
}

/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.Stack;

import java.util.Iterator;

public class KdTree {

    private class Node {
        private Point2D currentPoint;
        private Node leftNode;
        private Node rightNode;
        private boolean position;
    }

    private Stack<Node> stackForNode = new Stack<Node>();
    private Stack<Double> stackForDist = new Stack<Double>();
    private int size;
    private Node root;
    private Node newNode;
    // private Point2D nearestPoint;
    // private Double distanc;

    public KdTree() {
        this.size = 0;
        this.root = new Node();
        // this.root.position = true;
    }                              // construct an empty set of points

    public boolean isEmpty() {
        return (this.size == 0);
    }                     // is the set empty?

    public int size() {
        return this.size;
    }                         // number of points in the set

    public Node insert(
            Point2D p) {
        if (this.isEmpty()) {
            this.root.currentPoint = p;
            this.root.leftNode = null;
            this.root.rightNode = null;
            this.root.position = true;
            this.size += 1;
            return this.root;
        }

        Node currentNode = this.root;
        if (!this.isEmpty()) {
            boolean flag = true;
            while (flag) {
                if (currentNode.position) {
                    if (currentNode.currentPoint.x() >= p.x()) {
                        if (currentNode.leftNode != null) {
                            currentNode = currentNode.leftNode;
                        }
                        else {
                            flag = false;
                        }
                    }
                    else if (currentNode.currentPoint.x() < p.x()) {
                        if (currentNode.rightNode != null) {
                            currentNode = currentNode.rightNode;
                        }
                        else {
                            flag = false;
                        }
                    }
                }
                if (!currentNode.position) {
                    if (currentNode.currentPoint.y() >= p.y()) {
                        if (currentNode.leftNode != null) {
                            currentNode = currentNode.leftNode;
                        }
                        else {
                            flag = false;
                        }
                    }
                    if (currentNode.currentPoint.y() < p.y()) {
                        if (currentNode.rightNode != null) {
                            currentNode = currentNode.rightNode;
                        }
                        else {
                            flag = false;
                        }
                    }
                }
            }
            newNode = new Node();
            newNode.position = !currentNode.position;
            newNode.currentPoint = p;
            newNode.leftNode = null;
            newNode.rightNode = null;
            if (currentNode.position) {
                if (currentNode.currentPoint.x() >= p.x()) {
                    currentNode.leftNode = newNode;
                    size += 1;
                }
                else {
                    if (!currentNode.currentPoint.equals(p)) {
                        currentNode.rightNode = newNode;
                        size += 1;
                    }
                    else {
                        return currentNode;
                    }
                }
            }
            if (!currentNode.position) {
                if (currentNode.currentPoint.y() >= p.y()) {
                    currentNode.leftNode = newNode;
                    size += 1;
                }
                else {
                    if (!currentNode.currentPoint.equals(p)) {
                        currentNode.rightNode = newNode;
                        size += 1;
                    }
                    else {
                        return currentNode;
                    }
                }
            }
        }
        return newNode;
    }
    //

    // add the point to the set (if it is not already in the set)
    //
    public boolean contains(Point2D p) {
        boolean flag = true;
        boolean flag2 = false;
        Node curNode = this.root;
        while (flag) {
            if (curNode.currentPoint.x() == p.x() && curNode.currentPoint.y() == p.y()) {
                flag2 = true;
                flag = false;
            }
            else {
                if (curNode.position) {
                    if (curNode.currentPoint.x() > p.x()) {
                        if (curNode.leftNode != null) {
                            curNode = curNode.leftNode;
                        }
                        else {
                            flag = false;
                        }
                    }
                    if (curNode.currentPoint.x() < p.x()) {
                        if (curNode.rightNode != null) {
                            curNode = curNode.rightNode;
                        }
                        else {
                            flag = false;
                        }
                    }
                }
                if (!curNode.position) {
                    if (curNode.currentPoint.y() < p.y()) {
                        if (curNode.rightNode != null) {
                            curNode = curNode.rightNode;
                        }
                        else {
                            flag = false;
                        }
                    }
                    if (curNode.currentPoint.y() > p.y()) {
                        System.out.println("gggg");
                        if (curNode.leftNode != null) {
                            curNode = curNode.leftNode;
                        }
                        else {
                            flag = false;
                        }
                    }
                }
            }
        }
        return flag2;
    }

    // does the set contain point p?
    //
    // public void draw()                         // draw all points to standard draw
    //
    public Iterable<Point2D> range(
            RectHV rect) {
        Stack<Point2D> qPoint = new Stack<Point2D>();
        RectHV sRect = new RectHV(0.0, 0.0, 1.0, 1.0);
        range(root, sRect, rect, qPoint);
        return qPoint;
    }

    private void range(Node n, RectHV spaceRec, RectHV queryRec, Stack<Point2D> queryPoint) {
        if (n == null) {
            return;
        }
        if (queryRec.contains(n.currentPoint)) {
            queryPoint.push(n.currentPoint);
        }
        if (!spaceRec.intersects(queryRec)) {
            return;
        }
        if (n.position) {
            double yMin = spaceRec.ymin();
            double yMax = spaceRec.ymax();
            double xMin = spaceRec.xmin();
            double xMax = n.currentPoint.x();
            range(n.leftNode, new RectHV(xMin, yMin, xMax, yMax), queryRec, queryPoint);
            xMax = spaceRec.xmax();
            xMin = n.currentPoint.x();
            range(n.rightNode, new RectHV(xMin, yMin, xMax, yMax), queryRec, queryPoint);
        }
        if (!n.position) {
            double xMin = spaceRec.xmin();
            double xMax = spaceRec.xmax();
            double yMin = spaceRec.ymin();
            double yMax = n.currentPoint.y();
            range(n.leftNode, new RectHV(xMin, yMin, xMax, yMax), queryRec, queryPoint);
            yMax = spaceRec.ymax();
            yMin = n.currentPoint.y();
            range(n.rightNode, new RectHV(xMin, yMin, xMax, yMax), queryRec, queryPoint);
        }
    }

    // all points that are inside the rectangle (or on the boundary)
    //
    public Point2D nearest(
            Point2D p) {
        // Point2D nearPoint = this.root.currentPoint;
        RectHV spRect = new RectHV(0.0, 0.0, 1.0, 1.0);
        return searchNear(p, this.root, spRect);
    }

    private Point2D searchNear(Point2D p, Node n, RectHV sRect) {
        // Point2D nearestPoint;
        // Double distanc;

        System.out.println(n);
        System.out.println(stackForNode.size());
        if (n == null) {
            return stackForNode.peek().currentPoint;
        }
        // stackForNode.push();
        //
        // distanc = p.distanceTo(n.currentPoint);
        // nearestPoint = n.currentPoint;
        if (stackForNode.size() == 0) {
            stackForNode.push(n);
            stackForDist.push(n.currentPoint.distanceTo(p));
        }
        if (sRect.distanceTo(p) > stackForDist.peek()) {
            return stackForNode.peek().currentPoint;
        }
        
        // Double distanc = stackForDist.pop();

        if (p.distanceTo(n.currentPoint) < stackForDist.peek()) {
            stackForNode.push(n);
            stackForDist.push(p.distanceTo(n.currentPoint));
        }
        // else {
        //     stackForDist.push(distanc);
        // }
        if (n.position) {
            double yMin = sRect.ymin();
            double yMax = sRect.ymax();
            double xMin = sRect.xmin();
            double xMax = n.currentPoint.x();
            searchNear(p, n.leftNode, new RectHV(xMin, yMin, xMax, yMax));
            xMax = sRect.xmax();
            xMin = n.currentPoint.x();
            searchNear(p, n.rightNode, new RectHV(xMin, yMin, xMax, yMax));
        }
        if (!n.position) {
            double xMin = sRect.xmin();
            double xMax = sRect.xmax();
            double yMin = sRect.ymin();
            double yMax = n.currentPoint.y();
            searchNear(p, n.leftNode, new RectHV(xMin, yMin, xMax, yMax));
            yMax = sRect.ymax();
            yMin = n.currentPoint.y();
            searchNear(p, n.rightNode, new RectHV(xMin, yMin, xMax, yMax));
        }
        return stackForNode.peek().currentPoint;
    }

    // a nearest neighbor in the set to point p; null if the set is empty

    public static void main(String[] args) {
        KdTree kdtree = new KdTree();
        Point2D testPoint = new Point2D(0.2, 0.2);
        kdtree.insert(testPoint);
        System.out.println(kdtree.root.currentPoint.x());
        System.out.println(kdtree.root.currentPoint.y());
        System.out.println(kdtree.size());
        Point2D testPoint2 = new Point2D(0.1, 0.2);
        kdtree.insert(testPoint2);
        System.out.println(kdtree.root.leftNode.currentPoint.x());
        System.out.println(kdtree.size());
        Point2D testPoint3 = new Point2D(0, 0.6);
        kdtree.insert(testPoint3);
        System.out.println(kdtree.root.leftNode.rightNode.currentPoint.y());
        System.out.println(kdtree.root.currentPoint.x());
        System.out.println(kdtree.root.currentPoint.y());
        System.out.println(kdtree.root.rightNode);
        Point2D testPoint4 = new Point2D(0.7, 0.10);
        Point2D testPoint5 = new Point2D(0.12, 0.12);
        Point2D tettPoint6 = new Point2D(0.5, 0.5);
        kdtree.insert(testPoint4);
        kdtree.insert(tettPoint6);
        System.out.println(kdtree.root.rightNode.currentPoint.y());
        System.out.println(kdtree.contains(testPoint5));

        Iterator<Point2D> Iter = kdtree.range(new RectHV(0.1, 0.1, 0.9, 0.9)).iterator();
        while (Iter.hasNext()) {
            System.out.println(Iter.next().x());
        }
        System.out.println(kdtree.nearest(new Point2D(0.499, 0.499)));
    }
}

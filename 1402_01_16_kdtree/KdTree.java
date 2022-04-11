/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.Point2D;

public class KdTree {

    private class Node {
        public Point2D currentPoint;
        public Node leftNode;
        public Node rightNode;
        public boolean position;
    }

    private int size;
    private Node root;
    private Node newNode;


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
                    if (currentNode.currentPoint.x() > p.x()) {
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
                    if (currentNode.currentPoint.y() > p.y()) {
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
                if (currentNode.currentPoint.x() > p.x()) {
                    currentNode.leftNode = newNode;
                    size += 1;
                }
                else {
                    currentNode.rightNode = newNode;
                    size += 1;
                }
            }


            if (!currentNode.position) {
                if (currentNode.currentPoint.y() > p.y()) {
                    currentNode.leftNode = newNode;
                    size += 1;
                }
                else {
                    currentNode.rightNode = newNode;
                    size += 1;
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
    // public Iterable<Point2D> range(
    //         RectHV rect)             // all points that are inside the rectangle (or on the boundary)
    //
    // public Point2D nearest(
    //         Point2D p) {
    //     Point2D nearestNode = this.root;
    //
    // }


    // a nearest neighbor in the set to point p; null if the set is empty

    public static void main(String[] args) {
        KdTree kdtree = new KdTree();
        Point2D testPoint = new Point2D(2, 2);
        kdtree.insert(testPoint);
        System.out.println(kdtree.root.currentPoint.x());
        System.out.println(kdtree.root.currentPoint.y());
        System.out.println(kdtree.size());
        Point2D testPoint2 = new Point2D(1, 2);
        kdtree.insert(testPoint2);
        System.out.println(kdtree.root.leftNode.currentPoint.x());
        System.out.println(kdtree.size());
        Point2D testPoint3 = new Point2D(0, 6);
        kdtree.insert(testPoint3);
        System.out.println(kdtree.root.leftNode.rightNode.currentPoint.y());
        System.out.println(kdtree.root.currentPoint.x());
        System.out.println(kdtree.root.currentPoint.y());
        System.out.println(kdtree.root.rightNode);
        Point2D testPoint4 = new Point2D(7, 10);
        Point2D testPoint5 = new Point2D(12, 12);
        kdtree.insert(testPoint4);
        System.out.println(kdtree.root.rightNode.currentPoint.y());
        System.out.println(kdtree.contains(testPoint5));
        // System.out.println(kdtree.root.rightNode.currentPoint.x());
        // System.out.println(kdtree.size());
        // for (int i = 0; i < 10; i++) {
        //     for (int j = 0; j < 10; j++) {
        //         kdtree.insert(new Point2D(i, j));
        //     }
        // }
        // System.out.println(kdtree.size());
        // Point2D testPoint = new Point2D(2, 2);
        // System.out.println(kdtree.contains(testPoint));
        // Point2D testPoint2 = new Point2D(30, 40);
        // System.out.println(kdtree.contains(testPoint2));
    }
}

/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import java.util.Arrays;
import java.util.LinkedList;

public class BruteCollinearPoints {
    private LinkedList<LineSegment> line_segments;
    private int number_of_segments = 0;

    public BruteCollinearPoints(Point[] points) {
        line_segments = new LinkedList<LineSegment>();
        int n = points.length;
        System.out.println(n);
        // System.out.println(points);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    for (int l = k + 1; l < n; l++) {
                        System.out.println(points[0]);
                        System.out.println(points[1]);
                        System.out.println(points[2]);
                        System.out.println(points[3]);
                        System.out.println(points[i]);
                        System.out.println(points[j]);
                        System.out.println(points[k]);
                        System.out.println(points[l]);
                        System.out.println(points);
                        System.out.println(points[i].slopeTo(points[j]));
                        System.out.println(points[i].slopeTo(points[k]));
                        System.out.println(points[i].slopeTo(points[l]));
                        System.out.println("************");
                        System.out.println(
                                (points[i].slopeTo(points[j]) == points[i].slopeTo(points[k])));
                        if ((points[i].slopeTo(points[j]) == points[i].slopeTo(points[k]))
                                && (points[i].slopeTo(points[l])) == points[i].slopeTo(points[j])) {
                            Point temp[] = { points[i], points[j], points[k], points[l] };
                            Arrays.sort(temp);
                            line_segments.add(new LineSegment(temp[0], temp[3]));
                            number_of_segments += 1;
                        }
                    }
                }
            }
        }
    }    // finds all line segments containing 4 points

    public int numberOfSegments() {
        return number_of_segments;
    }       // the number of line segments

    public LineSegment[] segments() {
        LineSegment my_array[] = new LineSegment[this.number_of_segments];
        return line_segments.toArray(my_array);
    }


    public static void main(String[] args) {
        Point point[] = new Point[10];
        point[0] = new Point(10, 10);
        point[1] = new Point(20, 20);
        point[2] = new Point(30, 30);
        point[3] = new Point(4, 40);
        point[4] = new Point(5, 50);
        point[5] = new Point(60, 60);
        point[6] = new Point(70, 70);
        point[7] = new Point(8, 80);
        point[8] = new Point(90, 90);
        point[9] = new Point(10, 100);
        System.out.println(point.length);
        BruteCollinearPoints my_test = new BruteCollinearPoints(point);
        System.out.println(my_test.numberOfSegments());
        System.out.println(my_test.segments().length);
        System.out.println((Arrays.asList(my_test.segments())));
        System.out.println(my_test.segments()[0]);
    }
}

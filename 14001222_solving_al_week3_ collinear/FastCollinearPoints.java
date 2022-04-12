/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

public class FastCollinearPoints {
    private LinkedList<LineSegment> line_segments;
    private int number_of_segments = 0;
    public Point temp[];
    public Double temp1[];
    public Double temp2[];
    public Double[] names = { 1.234, 2.444 };
    private Point d;

    public FastCollinearPoints(Point[] points) {
        double epsilon = 0.000001d;
        int n = points.length;
        temp = points;
        temp1 = new Double[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Arrays.sort(temp, points[i].slopeOrder());
            }
            for (int k = 0; k < n; k++) {
                temp1[k] = points[i].slopeTo(temp[k]);
            }
            int q = 0;
            int m = 0;
            int p = 0;
            while (p <= n) {
                q = p + 1;
                while ((Math.abs(temp1[p] - temp1[q]) < epsilon)) {
                    q += 1;
                }
                if ((q - p) >= 4) {
                    line_segments.add(new LineSegment(temp[p], temp[q]));
                }
                p = q + 1;
            }
        }

        //
        //     Point d = new Point(0, 0);
        //     Arrays.sort(temp, d.slopeOrder());
        //     for (int i = 0; i < n; i++) {
        //         temp1[i] = d.slopeTo(temp[i]);
        //     }
        //     int j = 0;
        //     int i = 0;
        //
        //     for (int k = 0; k < n; k++) {
        //         d = temp[k];
        //         Arrays.sort(temp, d.slopeOrder());
        //         for (int p = 0; p < n; p++) {
        //             temp1[p] = d.slopeTo(temp[p]);
        //         }
        //         while (j < n - 1) {
        //             while (Math.abs(temp1[i] - temp1[j + 1]) < epsilon) {
        //                 System.out.println("is it iqual?");
        //                 System.out.println(temp1[i]);
        //                 System.out.println(temp1[j + 1]);
        //                 System.out.println(i);
        //                 System.out.println(j);
        //                 System.out.println("is it iqual?");
        //                 j = j + 1;
        //                 if (temp1[j] != temp1[j + 1]) {
        //                     if (j - i > 3) {
        //                         line_segments.add(new LineSegment(temp[k], temp[j]));
        //                         number_of_segments += 1;
        //                         i = j;
        //                     }
        //                 }
        //             }
        //             j = j + 1;
        //             i = j;
        //         }
        //     }
    }

    public int numberOfSegments() {
        return number_of_segments;
    }

    public LineSegment[] segments() {
        LineSegment my_array[] = new LineSegment[number_of_segments];
        return line_segments.toArray(my_array);
    }

    // public static void main(String[] args) {
    //     System.out.println("we are here");
    //     System.out.println("***********");
    //     In in = new In(args[0]);
    //     int n = in.readInt();
    //     Point[] points = new Point[n];
    //     for (int i = 0; i < n; i++) {
    //         int x = in.readInt();
    //         int y = in.readInt();
    //         points[i] = new Point(x, y);
    //     }
    //     FastCollinearPoints collinear = new FastCollinearPoints(points);
    //     System.out.println(Arrays.asList(collinear.temp));
    //     System.out.println(Arrays.asList(collinear.temp1));
    //     System.out.println(Arrays.asList(collinear.line_segments));
    //
    // }

    public static void main(String[] args) {

        try {
            File myObj = new File(args[0]);
            Scanner myReader = new Scanner(myObj);
            int n = myReader.nextInt();
            Point[] point = new Point[n];
            System.out.println(n);
            myReader.nextLine();
            int j = 0;
            String data;
            String[] parts;
            while (myReader.hasNextLine()) {
                data = myReader.nextLine();
                point[j] = new Point(Integer.valueOf(data.split(" ")[0]),
                                     Integer.valueOf(data.split(" ")[1]));
                j += 1;
            }
            myReader.close();
            BruteCollinearPoints my_test = new BruteCollinearPoints(point);
            System.out.println(my_test.numberOfSegments());
            System.out.println(my_test.segments().length);
            System.out.println((Arrays.asList(my_test.segments())));
            System.out.println(Arrays.asList(point));
        }
        catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
        }
    }
}


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

public class BruteCollinearPoints {
    private LinkedList<LineSegment> line_segments;
    private int number_of_segments = 0;
    private Point[] temp;

    public BruteCollinearPoints(Point[] points) {
        line_segments = new LinkedList<LineSegment>();
        int n = points.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    for (int l = k + 1; l < n; l++) {
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

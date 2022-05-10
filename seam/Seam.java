/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.IndexMinPQ;
import edu.princeton.cs.algs4.Picture;

public class Seam {
    private Picture picture;
    private Picture cPicture;
    private int rows;
    private int columns;
    private int[] edgTo;
    private double[] disTo;
    private IndexMinPQ<Double> pq;

    // create a seam carver object based on the given picture
    public Seam(Picture picture) {
        this.picture = new Picture(picture);
        rows = picture.height();
        columns = picture.width();
        cPicture = new Picture(columns, rows);
        for (int i = 0; i < columns; i++) {
            for (int j = 0; j < rows; j++) {
                cPicture.setRGB(i, j, picture.getRGB(i, j));
            }
        }
    }

    // current picture
    public Picture picture() {
        return cPicture;
    }

    // width of current picture
    public int width() {
        return cPicture.width();
    }

    // height of current picture
    public int height() {
        return cPicture.height();
    }

    // energy of pixel at column x and row y
    public double energy(int x, int y) {
        if (x == 0 || x == cPicture.width() - 1 || y == 0 || y == cPicture.height() - 1) {
            return 1000.0;
        }
        else {
            int deltaXR = cPicture.get(x - 1, y).getRed() - cPicture.get(x + 1, y).getRed();
            int deltaXB = cPicture.get(x - 1, y).getBlue() - cPicture.get(x + 1, y).getBlue();
            int deltaXG = cPicture.get(x - 1, y).getGreen() - cPicture.get(x + 1, y).getGreen();
            double delta2X = Math.pow(deltaXR, 2) + Math.pow(deltaXB, 2) + Math
                    .pow(deltaXG, 2);
            int deltaYR = cPicture.get(x, y - 1).getRed() - cPicture.get(x, y + 1).getRed();
            int deltaYB = cPicture.get(x, y - 1).getBlue() - cPicture.get(x, y + 1).getBlue();
            int deltaYG = cPicture.get(x, y - 1).getGreen() - cPicture.get(x, y + 1).getGreen();
            double delta2Y = Math.pow((double) deltaYR, 2.0) + Math.pow(deltaYB, 2.0)
                    + Math.pow((double) deltaYG, 2.0);
            return Math.pow(delta2X + delta2Y, 0.5);
        }
    }

    // sequence of indices for horizontal seam
    // public int[] findHorizontalSeam()

    // // sequence of indices for vertical seam
    public int[] findVerticalSeam() {
        int iRows = cPicture.height();
        int iColumns = cPicture.width();

        edgTo = new int[iRows * iColumns + 2];
        disTo = new double[iRows * iColumns + 2];
        pq = new IndexMinPQ<Double>(iRows * iColumns + 2);
        int[] shortPath = new int[iRows];
        disTo[0] = 0.0;
        // relaxing adjecents of 0;
        for (int p = 1; p < iRows * iColumns + 2; p++) {
            disTo[p] = Double.POSITIVE_INFINITY;
        }
        for (int v = 1; v <= iColumns; v++) {
            relax(0, v);
        }
        for (int i = 0; i < iRows - 1; i++) {
            for (int j = 0; j < iColumns; j++) {
                if (j == 0) {
                    relax(i * iColumns + 1, (i + 1) * iColumns + 2);
                    relax(i * iColumns + 1, (i + 1) * iColumns + 1);
                }
                else if (j == iColumns - 1) {
                    relax(i * iColumns + 1 + j, (i + 1) * iColumns + 1 + j);
                    relax(i * iColumns + 1 + j, (i + 1) * iColumns + 1 + j + 1);
                }
                else {
                    relax(i * iColumns + 1 + j, (i + 1) * iColumns + j);
                    relax(i * iColumns + 1 + j, (i + 1) * iColumns + j + 2);
                    relax(i * iColumns + 1 + j, (i + 1) * iColumns + j + 1);
                }
            }
        }
        for (int k = 0; k < iColumns; k++) {
            relax((iRows - 1) * iColumns + k + 1, iRows * iColumns + 1);
        }

        int t1 = iRows * iColumns + 1;
        int i = 0;
        while (t1 != 0 && (iRows - i) > 0) {
            t1 = edgTo[t1];
            i += 1;
            shortPath[iRows - i] = (t1 - 1) % iColumns;
        }
        return shortPath;
    }

    private void relax(int v, int w) {
        if (disTo[w] > disTo[v] + energy((w - 1) % cPicture.width(), (w - 1) / cPicture.width())) {
            disTo[w] = disTo[v] + energy((w - 1) % cPicture.width(), (w - 1) / cPicture.width());
            edgTo[w] = v;
            if (pq.contains(w)) pq.decreaseKey(w, disTo[w]);
            else pq.insert(w, disTo[w]);
        }
    }

    // remove horizontal seam from current picture
    // public void removeHorizontalSeam(int[] seam)

    // remove vertical seam from current picture
    public void removeVerticalSeam(int[] seam) {
        int newWidth = cPicture.width() - 1;
        int newHeight = cPicture.height();
        Picture c2Picture = new Picture(newWidth, newHeight);
        for (int i = 0; i < newWidth; i++) {
            for (int j = 0; j < newHeight; j++) {
                if (seam[j] > i) {
                    c2Picture.setRGB(i, j, cPicture.getRGB(i, j));
                }
                else if (seam[j] <= i) {
                    c2Picture.setRGB(i, j, cPicture.getRGB(i + 1, j));
                }
            }
        }
        cPicture = c2Picture;
    }

    // unit test (optional)
    public static void main(String[] args) {
        Picture testPic = new Picture("images.jfif");
        Seam testSeam = new Seam(testPic);
        testSeam.picture().save("new.png");
        for (int i = 0; i < 40; i++) {
            testSeam.removeVerticalSeam(testSeam.findVerticalSeam());
        }
        testSeam.picture().save("new3.png");
    }
}

/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.Queue;

public class Board {
    private int width;
    private int[] board;
    private int zero_index;

    // create a board from an n-by-n array of tiles,
    // where tiles[row][col] = tile at (row, col)
    public Board(int[][] tiles) {
        width = tiles[0].length;
        board = new int[width * width];

        for (int i = 0; i < width; i++) {
            for (int j = 0; j < width; j++) {
                board[i * width + j] = tiles[i][j];
                if (tiles[i][j] == 0) {
                    zero_index = i * width + j;
                }
            }
        }
    }

    //
    // string representation of this board
    public String toString() {
        StringBuilder board_string = new StringBuilder();
        board_string.append(width + "\n");
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < width; j++) {
                board_string.append(String.format("%2d ", board[i * width + j]));
            }
            board_string.append("\n");
        }
        return board_string.toString();
    }

    //
    // // board dimension n
    public int dimension() {
        return width;
    }

    //
    // // number of tiles out of place
    public int hamming() {
        int hamming_index = 0;
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < width; j++) {
                if (board[i * width + j] != i * width + j + 1) {
                    hamming_index = hamming_index + 1;
                }
            }
        }
        return hamming_index - 1;
    }

    //
    // sum of Manhattan distances between tiles and goal
    public int manhattan() {
        int manhattan_index = 0;
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < width; j++) {
                if (board[i * width + j] != 0) {
                    if (board[i * width + j] != i * width + j + 1) {
                        manhattan_index += Math.abs(((board[i * width + j] / width) - i)) + (
                                Math.abs(((board[i * width + j]) % width) - j - 1));
                    }
                }
            }
        }
        return manhattan_index;
    }

    //
    // // is this board the goal board?
    public boolean isGoal(Board board) {
        if (board.hamming() == 0) {
            return true;
        }
        else {
            return false;
        }
    }


    // // does this board equal y?
    public boolean equals(Object y) {
        if (y == this) return true;
        if (y == null) return false;
        if (y.getClass() != this.getClass()) return false;
        Board that = (Board) y;
        if (that.dimension() != this.dimension())
            return false;
        for (int i = 0; i < board.length; i++) {
            if (this.board[i] != that.board[i])
                return false;
        }
        return true;
    }

    public Board twin() {
        int[] twinBoard = new int[this.width * this.width];
        int[][] twinTile;
        for (int i = 0; i < this.width * this.width; i++) {
            twinBoard[i] = this.board[i];
        }
        for (int i = 0; i < this.width * this.width; i++) {
            if (this.board[i] != 0 && this.board[i + 1] != 0) {
                twinBoard[i] = this.board[i + 1];
                twinBoard[i + 1] = this.board[i];
                break;
            }
        }
        twinTile = new int[this.width][this.width];
        for (int j = 0; j < this.width; j++) {
            for (int k = 0; k < this.width; k++) {
                twinTile[j][k] = twinBoard[j * this.width + k];
            }
        }
        return new Board(twinTile);
    }


    //
    // // all neighboring boards
    public Iterable<Board> neighbors() {
        // int zero_index;
        // for (int i = 0; i < width * width; i++) {
        //     if (board[i] == 0) {
        //         zero_index = i;
        //     }
        // }
        Queue<Board> neighbors = new Queue<Board>();
        int[][] block;
        block = new int[width][width];
        int[] changing_index = new int[4];
        int numerator = 0;
        // if ((zero_index / width) != 0 && (zero_index / width) != width - 1
        //         && (zero_index % width) != 0 && (zero_index % width) != width - 1) {
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < width; j++) {
                if ((Math.abs((zero_index / width) - i) == 1
                        && Math.abs((zero_index % width) - j) == 0) || (
                        Math.abs((zero_index / width) - i) == 0
                                && Math.abs((zero_index % width) - j) == 1)) {
                    changing_index[numerator] = i * width + j;
                    numerator++;
                }
                else block[i][j] = board[i * width + j];
            }
        }
        for (int i = 0; i < numerator; i++) {
            block[zero_index / width][zero_index % width] = board[changing_index[i]];
            block[changing_index[i] / width][changing_index[i] % width] = 0;
            for (int j = 0; j < numerator; j++) {
                if (j != i) {
                    block[changing_index[j] / width][changing_index[j] % width]
                            = board[changing_index[j]];
                }
            }
            neighbors.enqueue(new Board(block));
            // }

        }
        return neighbors;
    }
    //
    // // a board that is obtained by exchanging any pair of tiles
    // public Board twin()

    // unit testing (not graded)
    public static void main(String[] args) {
        System.out.println("test");
        int[][] test_array = { { 8, 1, 3 }, { 4, 0, 2 }, { 7, 6, 5 } };
        int[][] test_array2 = { { 8, 1, 3 }, { 4, 0, 2 }, { 7, 6, 5 } };
        Board test_board = new Board(test_array);
        Board test_board2 = new Board(test_array2);
        System.out.println(test_board.toString());
        System.out.println(test_board.twin().toString());
        System.out.println("&&&&&&&&&&&&&&&&&&&");
        System.out.println(test_board.hamming());
        System.out.println(test_board.width);
        System.out.println(test_board.manhattan());
        System.out.println(test_board.isGoal(test_board));
        System.out.println(test_board.equals(test_board2));
        System.out.println("888888888");
        System.out.println(test_board.zero_index);
        Iterable<Board> itter_test = test_board.neighbors();
        for (Board b : itter_test) {
            System.out.println(b);
        }
    }
}

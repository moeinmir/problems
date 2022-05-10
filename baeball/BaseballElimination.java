/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.Bag;

import java.util.ArrayList;
import java.util.List;

public class BaseballElimination {
    private List<Bag<Integer>> myBagList;

    public BaseballElimination() {
        myBagList = new ArrayList<Bag<Integer>>();
        for (int i = 0; i < 3; i++) {
            myBagList.add(new Bag<Integer>());
        }
        System.out.println(myBagList.get(0));
    }


    public static void main(String[] args) {
        System.out.println("hhhhhhh");
        BaseballElimination test = new BaseballElimination();
    }
}

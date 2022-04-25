/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import java.util.HashMap;
import java.util.Map;

public class Outcast {
    private WordNet refrenceWordnet;

    public Outcast(WordNet wordnet) {
        refrenceWordnet = wordnet;
    }        // constructor takes a WordNet object

    public String outcast(String[] nouns) {
        // int[] distancse = new int[nouns.length];

        Map<String, Integer> distanceMap = new HashMap<String, Integer>();
        for (String j :
                nouns) {
            // distanceMap.put(j, 0);
            int k = 0;
            int tempDis = 0;
            while (k < nouns.length) {

                if (nouns[k] != j) {

                    tempDis += refrenceWordnet.distance(j, nouns[k]);
                }
                k += 1;
            }
            distanceMap.put(j, tempDis);
        }
        String outCast = "";
        int maxDistance = 0;
        for (
                String i : distanceMap.keySet()) {
            if (distanceMap.get(i) > maxDistance) {
                outCast = i;
            }
        }
        return outCast;
    }// given an array of WordNet nouns, return an outcast


    public static void main(String[] args) {
        String[] testArray = { "A", "A-list", "AIDS", "A-horizon" };
        WordNet test = new WordNet("synsets.txt", "hypernyms.txt");
        Outcast testCast = new Outcast(test);
        System.out.println(testCast.outcast(testArray));
    }  // see test client below
}

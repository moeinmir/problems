/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.Digraph;
import edu.princeton.cs.algs4.In;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class WordNet {
    private Digraph dicGraph;
    private String synsetsName;
    private String hyperName;
    private Map<Integer, String> dictOfSynSets;
    public Map<String, ArrayList<Integer>> dictOfNouns;
    private int numberOfVertices = 1;

    // constructor takes the name of the two input files
    public WordNet(String synsets, String hypernyms) {
        synsetsName = synsets;
        hyperName = hypernyms;
        dictOfSynSets = new HashMap<Integer, String>();
        dictOfNouns = new HashMap<String, ArrayList<Integer>>();
        this.readSyn(synsetsName);
        this.readhyp(hyperName);
    }

    private void readSyn(String synName) {
        In in = new In(synName);
        String lineToRead;
        lineToRead = in.readLine();
        dictOfSynSets.put(Integer.parseInt(lineToRead.split(",")[0]), lineToRead.split(",")[1]);
        while (true) {
            lineToRead = in.readLine();
            if (lineToRead == null) {
                break;
            }
            if (lineToRead.split(",").length >= 2) {
                dictOfSynSets
                        .put(Integer.parseInt(lineToRead.split(",")[0]),
                             lineToRead.split(",")[1]);
                numberOfVertices += 1;
                for (String noun : lineToRead.split(",")[1].split(" ")) {
                    if (dictOfNouns.containsKey(noun)) {
                        dictOfNouns.get(noun).add(Integer.parseInt(lineToRead.split(",")[0]));
                    }
                    else {
                        dictOfNouns.put(noun, new ArrayList<Integer>());
                        dictOfNouns.get(noun).add(Integer.parseInt(lineToRead.split(",")[0]));
                    }
                }
            }
        }
        dicGraph = new Digraph(numberOfVertices);
    }

    private void readhyp(String hyperName) {
        In in = new In(hyperName);
        String hypline = in.readLine();
        int id = Integer.parseInt(hypline.split(",")[0]);
        for (int i = 1; i < hypline.split(",").length; i++) {
            dicGraph.addEdge(id, Integer.parseInt(hypline.split(",")[i]));
        }
        while (true) {
            hypline = in.readLine();
            if (hypline == null) {
                break;
            }
            id = Integer.parseInt(hypline.split(",")[0]);
            for (int j = 1; j < hypline.split(",").length; j++) {
                dicGraph.addEdge(id, Integer.parseInt(hypline.split(",")[j]));
            }
        }
    }

    // // returns all WordNet nouns
    public Iterable<String> nouns() {
        return dictOfNouns.keySet();
    }

    // // // is the word a WordNet noun?
    public boolean isNoun(String word) {
        return dictOfNouns.containsKey(word);
    }

    //
    // // // distance between nounA and nounB (defined below)
    public int distance(String nounA, String nounB) {
        SAP wordNetSap = new SAP(this.dicGraph);
        return wordNetSap.length(this.dictOfNouns.get(nounA),
                                 this.dictOfNouns.get(nounB));
    }

    // // a synset (second field of synsets.txt) that is the common ancestor of nounA and nounB
    // // in a shortest ancestral path (defined below)
    public String sap(String nounA, String nounB) {
        SAP wordNetSap = new SAP(this.dicGraph);
        return dictOfSynSets.get(wordNetSap.ancestor(this.dictOfNouns.get(nounA),
                                                     this.dictOfNouns.get(nounB)));
    }

    // do unit testing of this class
    public static void main(String[] args) {
        WordNet test = new WordNet("synsets.txt", "hypernyms.txt");
        System.out.println(test.distance("A-list", "A-line"));
        System.out.println(test.sap("A-list", "A-line"));

    }
}

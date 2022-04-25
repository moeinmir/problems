import edu.princeton.cs.algs4.BreadthFirstDirectedPaths;
import edu.princeton.cs.algs4.Digraph;
import edu.princeton.cs.algs4.DirectedDFS;
import edu.princeton.cs.algs4.Queue;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */
public class SAP {
    private Digraph digraph;

    // constructor takes a digraph (not necessarily a DAG)
    public SAP(Digraph G) {
        digraph = G;
    }
    // length of shortest ancestral path between v and w; -1 if no such path

    public int length(int v, int w) {
        int z = this.ancestor(v, w);
        if (z == -1) {
            return -1;
        }
        BreadthFirstDirectedPaths bfs1 = new BreadthFirstDirectedPaths(digraph, v);
        BreadthFirstDirectedPaths bfs2 = new BreadthFirstDirectedPaths(digraph, w);
        return bfs1.distTo(z) + bfs2.distTo(z);
    }

    // a common ancestor of v and w that participates in a shortest ancestral path; -1 if no such path
    public int ancestor(int v, int w) {
        Set<Integer> intersectSet = new HashSet<Integer>();
        DirectedDFS dfs1 = new DirectedDFS(digraph, v);
        DirectedDFS dfs2 = new DirectedDFS(digraph, w);
        Digraph inducedGraph = new Digraph(digraph.V());

        for (int i = 0; i < digraph.V(); i++) {
            if (dfs1.marked(i) && dfs2.marked(i)) {
                intersectSet.add(i);
            }
        }
        if (intersectSet.size() == 0) {
            return -1;
        }
        Iterator<Integer> tempIter = intersectSet.iterator();

        int tempAncestor = intersectSet.iterator().next();

        for (int i : intersectSet) {
            Set<Integer> adjSet = new HashSet<Integer>();
            for (int j : digraph.adj(i)) {
                adjSet.add(j);
            }
            adjSet.retainAll(intersectSet);
            for (int k : adjSet) {
                inducedGraph.addEdge(i, k);
            }
        }
        for (int k : intersectSet) {
            if (inducedGraph.indegree(k) == 0) {
                tempAncestor = k;
            }
        }
        return tempAncestor;
    }


    // length of shortest ancestral path between any vertex in v and any vertex in w; -1 if no such path
    public int length(Iterable<Integer> v, Iterable<Integer> w) {
        int minDistance = (int) Double.POSITIVE_INFINITY;
        int commonAncestor = -1;
        for (int i : v) {
            for (int j : w) {
                System.out.println(i);
                if (this.length(i, j) < minDistance) {
                    System.out.println("gfhfhf");
                    minDistance = this.length(i, j);
                    commonAncestor = this.ancestor(i, j);
                }
            }
        }
        if (minDistance == (int) Double.POSITIVE_INFINITY) {
            return -1;
        }
        return minDistance;
    }


    // a common ancestor that participates in shortest ancestral path; -1 if no such path
    public int ancestor(Iterable<Integer> v, Iterable<Integer> w) {
        int minDistance = (int) Double.POSITIVE_INFINITY;
        int commonAncestor = -1;
        System.out.println(minDistance);
        for (int i : v) {
            for (int j : w) {
                if (this.length(i, j) < minDistance) {
                    minDistance = this.length(i, j);
                    commonAncestor = this.ancestor(i, j);
                }
            }
        }
        return commonAncestor;
    }

    // do unit testing of this class
    public static void main(String[] args) {
        Digraph testDigraph = new Digraph(25);
        testDigraph.addEdge(1, 0);
        testDigraph.addEdge(2, 0);
        testDigraph.addEdge(3, 1);
        testDigraph.addEdge(4, 1);
        testDigraph.addEdge(5, 2);
        testDigraph.addEdge(6, 2);
        testDigraph.addEdge(7, 3);
        testDigraph.addEdge(8, 3);
        testDigraph.addEdge(9, 3);
        testDigraph.addEdge(10, 5);
        testDigraph.addEdge(11, 5);
        testDigraph.addEdge(12, 5);
        testDigraph.addEdge(13, 7);
        testDigraph.addEdge(14, 7);
        testDigraph.addEdge(15, 9);
        testDigraph.addEdge(16, 9);
        testDigraph.addEdge(17, 10);
        testDigraph.addEdge(18, 10);
        testDigraph.addEdge(19, 12);
        testDigraph.addEdge(20, 12);
        testDigraph.addEdge(23, 20);
        testDigraph.addEdge(24, 20);
        SAP testSAP = new SAP(testDigraph);
        System.out.println(testSAP.ancestor(13, 16));
        System.out.println(testSAP.length(13, 16));
        Queue<Integer> testQueue = new Queue<Integer>();
        testQueue.enqueue(13);
        testQueue.enqueue(14);
        Queue<Integer> testQueue1 = new Queue<Integer>();
        testQueue1.enqueue(16);
        testQueue1.enqueue(24);
        System.out.println(testSAP.ancestor(testQueue, testQueue1));
        System.out.println(testSAP.length(testQueue, testQueue1));
    }
}

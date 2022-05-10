/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.Bag;
import edu.princeton.cs.algs4.FlowEdge;
import edu.princeton.cs.algs4.FlowNetwork;
import edu.princeton.cs.algs4.FordFulkerson;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.StdOut;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Base {
    FordFulkerson[] fordFulkerson;
    int teamsCount;
    int[] wins;
    int[] losses;
    int[] remainings;
    int[][] g;
    String[] teamNames;
    Boolean[] trivialElimenated;
    private int team1;
    private int team2;
    private int[] remaningPointsList;
    private List<Bag<String>> cOE;

    public Base(String filename) {
        In in = new In(filename);
        teamsCount = in.readInt();
        trivialElimenated = new Boolean[teamsCount];
        cOE = new ArrayList<Bag<String>>();
        wins = new int[teamsCount];
        losses = new int[teamsCount];
        remainings = new int[teamsCount];
        teamNames = new String[teamsCount];
        g = new int[teamsCount][teamsCount];
        remaningPointsList = new int[teamsCount];
        fordFulkerson = new FordFulkerson[teamsCount];
        for (int o = 0; o < teamsCount; o++) {
            cOE.add(new Bag<String>());
            trivialElimenated[o] = false;
            teamNames[o] = in.readString();
            wins[o] = in.readInt();
            losses[o] = in.readInt();
            remainings[o] = in.readInt();
            for (int j = 0; j < teamsCount; j++) {
                g[o][j] = in.readInt();
            }
        }
        for (int i = 0; i < teamsCount; i++) {
            boolean flag = false;
            FlowNetwork tempFelowNetwork = new FlowNetwork(teamsCount - 1 + 2 + ((teamsCount - 1)
                    * (teamsCount - 2) / 2));
            int source = teamsCount - 1;
            int target = teamsCount;
            int virtualWertex = teamsCount + 1;
            for (int j = 0; j < teamsCount; j++) {
                if (j < i) {
                    team1 = j;
                }
                else if (j > i) {
                    //the index for reaching the information for this team is still j
                    team1 = j - 1;
                }
                else {
                    continue;
                }
                if ((wins[i] + remainings[i] - wins[j]) >= 0) {
                    tempFelowNetwork.addEdge(
                            new FlowEdge(team1, target,
                                         wins[i] + remainings[i] - wins[j]));
                }
                if (((wins[i] + remainings[i] - wins[j]) < 0)) {
                    cOE.get(i).add(teamNames[j]);
                    trivialElimenated[i] = true;
                    flag = true;
                }
                for (int k = j + 1; k < teamsCount; k++) {
                    if (k < i) {
                        team2 = k;
                    }
                    else if (k > i) {
                        //the index for reaching the information for this team is still k
                        team2 = k - 1;
                    }
                    if (k == i) {
                        continue;
                    }
                    tempFelowNetwork.addEdge(new FlowEdge(source, virtualWertex, g[j][k]));
                    tempFelowNetwork.addEdge(
                            new FlowEdge(virtualWertex, team2, Double.POSITIVE_INFINITY));
                    tempFelowNetwork.addEdge(
                            new FlowEdge(virtualWertex, team1, Double.POSITIVE_INFINITY));
                    virtualWertex += 1;
                }
            }

            fordFulkerson[i] = new FordFulkerson(tempFelowNetwork, source, target);

            int reamainingPoints = 0;
            for (int q = 0; q < teamsCount; q++) {
                for (int z = q + 1; z < teamsCount; z++) {

                    if (q != i && z != i) {
                        reamainingPoints = reamainingPoints + g[q][z];
                    }
                }
            }
            if (!flag) {
                findCut(i);
            }
            remaningPointsList[i] = reamainingPoints;
        }
    }

    public int numberOfTeams() {
        return teamsCount;
    }

    public Iterable<String> teams() {
        Queue<String> queue1 = new Queue<String>();

        for (int i = 0; i < teamsCount; i++) {
            queue1.enqueue(teamNames[i]);
        }
        return queue1;
    }

    public int wins(String team) {
        return wins[Arrays.asList(teamNames).indexOf(team)];
    }

    public int losses(String team) {
        return losses
                [Arrays.asList(teamNames).indexOf(team)];
    }

    public int remaining(String team) {
        return remainings
                [Arrays.asList(teamNames).indexOf(team)];
    }

    public int against(String team01,
                       String team02) {
        return g[Arrays.asList(teamNames).indexOf(team01)][Arrays.asList(teamNames)
                                                                 .indexOf(team02)];
    }

    public boolean isEliminated(String team) {
        int teamNumber = Arrays.asList(teamNames).indexOf(team);
        if (trivialElimenated[teamNumber]) {
            return true;
        }
        else {
            return remaningPointsList[teamNumber] != fordFulkerson[teamNumber].value();
        }
    }

    private void findCut(int i) {
        for (int j = 0; j < teamsCount; j++) {
            if (fordFulkerson[i].inCut(j) && j < i) {
                System.out.println(teamNames[j]);
                cOE.get(i).add(teamNames[j]);
            }
            if (j > i) {
                if (fordFulkerson[i].inCut(j - 1) && j > i) {
                    System.out.println(teamNames[j]);
                    cOE.get(i).add(teamNames[j]);
                }
            }
        }
    }


    public Iterable<String> certificateOfElimination(String team) {
        return cOE.get(Arrays.asList(teamNames).indexOf(team));
    }

    public static void main(String[] args) {
        Base division = new Base(args[0]);
        for (String team : division.teams()) {
            if (division.isEliminated(team)) {
                StdOut.print(team + " is eliminated by the subset R = { ");
                for (String t : division.certificateOfElimination(team)) {
                    StdOut.print(t + " ");
                }
                StdOut.println("}");
            }
            else {
                StdOut.println(team + " is not eliminated");
            }
        }
    }
}

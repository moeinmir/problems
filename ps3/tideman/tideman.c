#include <cs50.h>
#include <stdio.h>
#include <stdio.h>
#include <string.h>
// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }
    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];
        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }
        record_preferences(ranks);
        printf("\n");
    }
    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();

    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            printf("%d", locked[i][j]);
        }
    }
    printf("\n");

    for (int j = 0; j < pair_count; j++)
    {
        printf("%d\n", pairs[j].winner);
        printf("%d\n", pairs[j].loser);
    }
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO

    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]] += 1;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i] && i != j)
            {
                pair p;
                p.winner = i;
                p.loser = j;
                pairs[pair_count] = p;
                pair_count = pair_count + 1;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    for (int i = 0; i < pair_count - 1; i++)
    {
        for (int j = i + 1; j < pair_count; j++)
        {
            pair p1 = pairs[i];
            pair p2 = pairs[j];
            int winner1 = p1.winner;
            int loser1 = p1.loser;
            int winner2 = p2.winner;
            int loser2 = p2.loser;
            if ((preferences[winner1][loser1] - preferences[loser1][winner1]) < (preferences[winner2][loser2] - preferences[loser2][winner2]))
            {
                pairs[i] = p2;
                pairs[j] = p1;
            }
        }
    }
    // TODO
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{

    for (int i = 0; i < pair_count; i++)
    {
        printf("fff");
        printf("%d", i);
        printf("ddddd");
        bool flag = true;
        int cur_pos = 0;
        int cur_win = pairs[i].winner;
        int cur_los = pairs[i].loser;

        for (int j = 0; j <= i; j++)
        {
            if (cur_los == pairs[j].winner)
            {
                cur_los = pairs[j].loser;
                for (int k = 0; k <= j; k++)
                {
                    if (pairs[k].winner == cur_los)
                    {
                        flag = false;
                    }
                }
                // if (cur_los == cur_win)
                // {
                //     flag = false;
                // }
            }
        }
        if (flag)
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
            printf("%d", locked[pairs[i].winner][pairs[i].loser]);
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    int winner[candidate_count];

    for (int i = 0; i < candidate_count; i++)
    {
        winner[i] = 0;
    }
    for (int j = 0; j < candidate_count; j++)
    {
        for (int k = 0; k < candidate_count; k++)
        {
            if (locked[j][k])
            {
                winner[j] = winner[j] + 1;
            }
        }
    }

    int max_vote = 0;
    for (int m = 0; m < candidate_count; m++)
    {
        if (winner[m] > max_vote)
        {
            max_vote = winner[m];
        }
    }

    for (int m = 0; m < candidate_count; m++)
    {
        if (winner[m] == max_vote)
        {
            printf("%s\n", candidates[m]);
        }
    }
}

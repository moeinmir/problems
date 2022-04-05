// Implements a dictionary's functionality

#include <ctype.h>
#include "dictionary.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;
int wordcount = 0;
// TODO: Choose number of buckets in hash table
const unsigned int N = 400;

// Hash table
node *table[N];
// Returns true if word is in dictionary, else false
bool check(const char *word)
{

    int helper2 = hash(word);
    node *helper3 = table[helper2];

    while (helper3 != NULL)
    {

        if (strcasecmp(word, helper3->word) == 0)
        {
            return true;
        }
        helper3 = helper3->next;
    }
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{

    int hash = 26;
    unsigned int helper = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        helper = helper + 40 * tolower(word[i]);
    }
    // TODO: Improve this hash function
    helper = helper % N;
    return helper;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        // TODO
        return false;
    }
    char buffer[LENGTH + 1];
    while (fscanf(file, "%s", buffer) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(file);
            return false;
        }

        else
        {

            strcpy(n->word, buffer);
            n->next = NULL;
            int index = hash(buffer);

            n->next = table[index];
            table[index] = n;
            wordcount = wordcount + 1;
        }
        /* code */
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return wordcount;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *tmp1 = table[i];
        while (tmp1 != NULL)
        {
            node *tmp2 = tmp1;
            tmp1 = tmp1->next;
            free(tmp2);
        }
    }

    return true;
}

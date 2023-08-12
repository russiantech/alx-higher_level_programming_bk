#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - print * element of listint_t list
 * @h: pointa to list head
 * Return: num of node
 */

size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* num of node */

    current = h;
    n = 0;
    while (current != NULL)
    {
	printf("%i\n", current->n);
	current = current->next;
	n++;
    }

    return (n);
}

/**
 * add_nodeint_end - add new node at end of listint_t list
 * @head: pointa to pointa of 1st node of listint_t list
 * @n: int to be added in new node
 * Return: adrs of new element or null if faied
 */

listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
	return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
	*head = new;
    else
    {
	while (current->next != NULL)
	    current = current->next;
	current->next = new;
    }

    return (new);
}

/**
 * free_listint - will free listint_t list
 * @head: pointa to list in question
 * Return: void
 */

void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
	current = head;
	head = head->next;
	free(current);
    }
}

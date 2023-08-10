#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
  *insert_node - inserts a number into a sorted singly linked lis
  *@head: the starting pointer
  *@number: the number to be intred
  *Return: the address of the new node, or NULL if it failed
  *
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;
	int check = 0;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (number < current->n)
	{
		check = 1;
		new->n = number;
		new->next = NULL;
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current != NULL && check == 0)
	{
		if (number < current->next->n)
			break;
		current = current->next;
	}

	if (check == 0)
	{
		new->n = number;
		new->next = current->next;
		current->next = new;
		return (new);
	}
	return (NULL);
}

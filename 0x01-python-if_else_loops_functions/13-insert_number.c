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
	listint_t *iterator = *head;
	int i = 0;
	int j = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	while (iterator != NULL)
	{
		i++;
		iterator = iterator->next;
	}
	i = i / 2;

	while (j < i)
	{
		current = current->next;
		j++;
	}
	new->n = number;
	new->next = current->next;
	current->next = new;
	return (new);
}

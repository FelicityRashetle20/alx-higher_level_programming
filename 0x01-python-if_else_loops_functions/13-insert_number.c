#include "lists.h"

/**
 * insert_node - inserts new node at given position
 * @head: head of a list
 * @number: index of the new node
 * returns the address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *h;
	listint_t *h_prev;

	h = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		h_prev = h;
		h = h->next;
	}

	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
	}
	else
	{
		new_node->next = h;
		if (h == *head)
			*head = new_node;
		else
			h_prev->next = new_node;
	}

	return (new_node);
}

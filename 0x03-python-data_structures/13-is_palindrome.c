#include "lists.h"

/**
 * reverse - method that reverses the second half of the list
 * @h_r: head of the second half of list
 * Returns nothing
 */
void reverse(listint_t **h_r)
{
	listint_t *previous;
	listint_t *current;
	listint_t *next;

	previous = NULL;
	current = *h_r;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*h_r = previous;
}

/**
 * compare - compares each element of the list
 * @h1: head of the first half of list
 * @h2: head of the second half of list
 * Returns 1 if they 1are equals, 0 if not
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1;
	listint_t *tmp2;

	tmp1 = h1;
	tmp2 = h2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scnd_list, *middle;
	int isp;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scnd_list = slow;
		prev_slow->next = NULL;
		reverse(&scnd_list);
		isp = compare(*head, scnd_list);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scnd_list;
		}
		else
		{
			prev_slow->next = scnd_list;
		}
	}

	return (isp);
}

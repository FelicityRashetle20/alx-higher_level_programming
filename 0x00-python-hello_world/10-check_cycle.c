#include "lists.h"

/*
 * check_cycle - methon that checks wether the list a cycle
 * @list - the list being checked
 * If list has a cycle return 1, else return 0
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;
	if(!list)
		return(0);
	while(first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if(first == second)
			return(1);
	}
	return(0);
}

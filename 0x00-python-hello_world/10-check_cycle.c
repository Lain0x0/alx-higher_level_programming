#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(s_linked_list *list)
{
	s_linked_list *slow = list;
	s_linked_list *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->n_node)
	{
		slow = slow->n_node;
		fast = fast->n_node->n_node;
		if (slow == fast)
			return (1);
	}

	return (0);
}


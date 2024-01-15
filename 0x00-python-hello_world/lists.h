#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct s_linked_list - singly linked list
 * @i: integer
 * @n_node: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct s_linked_list
{
	int i;
	struct s_linked_list *n_node;
} s_linked_list;

size_t print_s_linked_list(const s_linked_list *h);
s_linked_list *add_nodeint(s_linked_list **head, const int i);
void free_s_linked_list(s_linked_list *head);
int check_cycle(s_linked_list *list);

#endif /* LISTS_H */


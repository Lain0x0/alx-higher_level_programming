#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @insert_number: The number to insert.
 * Return: 0 If the function fails or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int insert_number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = insert_number;

	if (node == NULL || node->n >= insert_number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < insert_number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}

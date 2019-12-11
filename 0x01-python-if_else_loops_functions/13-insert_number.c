#include"lists.h"
/**
 * insert node - insert node
 * @head: pointer
 * @number: take int 
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tail = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
			new->next = NULL;
			return (new);
	}
	if (tail->n > number)
	{
		new->next = tail;
		*head = new;
		return (new);
	}
	for (; tail->next != NULL; tail = tail->next)
		if (tail->next->n > number)
			break;
	new->next = tail->next;
	tail->next = new;
	return (new);
}


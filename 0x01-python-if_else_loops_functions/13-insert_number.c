#include "lists.h"

/**
 * insert_node - inserts a number in an ordered linked list
 * @head: double pointer to the linked list
 * @number: number to insert in the new node
 *
 * Return: address of the new node(if SUCCESSFUL),
 * or NULL(ON FAILURE)
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = *head;
listint_t *new = NULL, *temp = NULL;

if (head == NULL)
	return (NULL);

new = malloc(sizeof(listint_t));
if (new == NULL)
	return (NULL);
new->n = number;
new->next = NULL;

if ((*head)->n > number || !*head)
{
	new->next = *head;
	return (*head = new);
}
else
{
while (current->n < number && current)
{
	temp = current;
	current = current->next;
}

temp->next = new;
new->next = current;
}

return (new);
}

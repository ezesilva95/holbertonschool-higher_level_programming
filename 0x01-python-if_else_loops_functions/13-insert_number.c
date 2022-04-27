#include "lists.h"
/**
 * insert_node - insert new node into sorted singly linked list
 * @head: pointer to head of linked list
 * @number: data for the new node
 * Return: address of new node, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;
	listint_t *new_node = NULL;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		(*head)->next = NULL;
		return (new_node);
	}
	if ((*head)->next == NULL)
	{
		if ((*head)->n < new_node->n)
			(*head)->next = new_node;
		else
		{
			new_node->next = *head;
			*head = new_node;
		}
		return (new_node);
	}

	tmp = *head;
	while (tmp->next != NULL)
	{
		if (new_node->n < tmp->n)
		{
			new_node->next = tmp;
			*head = new_node;
			return (new_node);
		}
		if (((new_node->n > tmp->n) && (new_node->n < (tmp->next)->n)) ||
		    (new_node->n == tmp->n))
		{
			new_node->next = tmp->next;
			tmp->next = new_node;
			return (new_node);
		}
		tmp = tmp->next;
	}
	tmp->next = new_node;
	return (new_node);
}

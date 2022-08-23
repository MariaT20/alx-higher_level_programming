#include "lists.h"

/**
 * insert_node - insert node in an ordered linked list
 * @head: the list passed in
 * @number: value of the new node
 * Return: address of new node or NULL if failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *future;

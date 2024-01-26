#include "lists.h"
/**
 * check_cycle - function checks if linked list contains a cycle
 *
 * @list: singly linked list to check
 *
 * Return: 0 if no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;
	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

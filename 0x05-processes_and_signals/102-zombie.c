#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * main - create 5 zombie processes and print a string for each
 * Return: always 0
 */

int infinite_while(void);

int main(void)
{
	fork() && fork() || fork();
	int pid = fork();

	if (pid == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
	infinite_while();
}
/**
 * infinite_while - An eternal loop
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

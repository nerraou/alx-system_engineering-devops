#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - infinite while
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - program entry point
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	int i;

	pid = fork();
	for (i = 1; i <= 4; i++)
	{
		if (pid != 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			pid = fork();
		}
	}
	if (pid != 0)
		printf("Zombie process created, PID: %d\n", pid);
	infinite_while();
	return (0);
}

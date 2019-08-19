# include <stdio.h>

int main(void) {
	int T;
	scanf_s("%d", &T);
	int depth = 0;
	char num_in[1023];
	int len = 0;
	int idx = 0;
	for (int test_case = 1; test_case <= T; test_case++) {
		scanf_s("%d", &depth);
		len = (1 << depth) - 1;
		for (int i = 0; i < len; i++) {
			scanf_s("%d", &num_in[i]);
		}
		printf("#%d ", test_case);
		for (int i = 0; i < depth; i++) {
			for (int j = 0; j < (1 << i); j++) {
				idx = (len / (1 << i + 1)) + (1 << (depth - i))*j;
				printf("%d ", num_in[idx]);
			}
			printf("\n");
		}
	}
	return 0;
}
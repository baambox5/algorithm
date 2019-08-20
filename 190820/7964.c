# include <stdio.h>

int main(void) {
	int T;
	scanf_s("%d", &T);
	int N = 0;
	int M = 0;
	char arr[1000];
	int position;
	int count;
	int input;
	for (int test_case = 1; test_case <= T; test_case++) {
		position = -1;
		count = 0;
		scanf_s("%d", &N);
		scanf_s("%d", &M);
		for (int i = 0; i < N; i++) {
			scanf_s("%d", &input);
			if (input) {
				arr[count] = i;
				count++;
			}
		}
		count = 0;
		while (position < N) {
			for (int i = position + M; i > position; i--) {
				if (arr[i]) {
					position = i;
					break;
				}
				if (i == position + 1) {
					position += M;
					count++;
				}
			}
			if (position + M >= N) {
				break;
			}
		}
		printf("#%d %d\n", test_case, count);
	}
	return 0;
}
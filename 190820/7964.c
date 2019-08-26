# include <stdio.h>

int main(void) {
	int T;
	scanf_s("%d", &T);
	int N = 0;
	int M = 0;
	int arr[10000];
	int position;
	int remain;
	int input;
	int count;
	int l;
	int m;
	for (int test_case = 1; test_case <= T; test_case++) {
		position = -1;
		remain = 0;
		scanf_s("%d", &N);
		scanf_s("%d", &M);
		for (int i = 0; i < N; i++) {
			scanf_s("%d", &input);
			if (input) {
				arr[remain] = i;
				remain++;
			}
		}
		arr[remain] = N;
		count = 0;
		l = 0;
		m = 1;
		while (position < N) {
			if (remain) {
				if ((position + 1 <= arr[l]) && (arr[l] <= position + M)) {
					position = arr[l];
					if (l == remain) {
						remain = 0;
						m = 1;
					}
					else {
						l++;
						m = 0;
					}
				}
				else {
					m = 1;
				}
			}
			if (m) {
				position += M;
				if (position < N)	count++;
			}
			if (position + M > N) {
				break;
			}
		}
		printf("#%d %d\n", test_case, count);
	}
	return 0;
}
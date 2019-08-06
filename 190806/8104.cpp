#include <stdio.h>

int main(int argc, char** argv)
{
	int test_case;
	int T = 0;
	
	FILE *fp;
	freopen_s(&fp, "8104.txt", "r", stdin);
	scanf_s("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int N = 0;
		int K = 0;
		scanf_s("%d", &N);
		scanf_s("%d", &K);
		int arr[20][10000];
		for (int i = 0; i < N; i++) {
			for (int k = 0; k < K; k++) {
				arr[k][i] = 0;
			}
		}
		for (int i = 1; i < (N + 1); i++) {
			for (int k = 1; k < (K + 1); k++) {
				if (i % 2) arr[k - 1][i - 1] = k + (i - 1) * K;
				else arr[K - k][i - 1] = k + (i - 1) * K;
			}
		}
		int sum = 0;
		printf("#%d", test_case);
		for (int i = 0; i < K; i++) {
			sum = 0;
			for (int j = 0; j < N; j++) {
				sum += arr[i][j];
			}
			printf(" %d", sum);
		}
		printf("\n");
	}
	return 0;
}

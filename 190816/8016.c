# include <stdio.h>

int main(void) {
	int test_case;
	scanf("%d", &test_case);
	unsigned int line = 0;
	unsigned long long m = 1;
	unsigned long long N = 1;
	unsigned long long K = 1;
	unsigned long long bn = 1;
	for (int i = 1; i <= test_case; i++) {
		scanf("%d", &line);
		m = 2 * (line - 1);
		bn = 1 + line * m;
		N = bn - m;
		K = bn + m;
		printf("#%d", i);
		printf(" %llu", N);
		printf(" %llu\n", K);
	}
	return 0;
}
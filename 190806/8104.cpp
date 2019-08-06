#include <stdio.h>
#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	/*
	   아래의 freopen 함수는 input.txt 를 read only 형식으로 연 후,
	   앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
	   //여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
	   freopen 함수를 이용하면 이후 cin 을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
	   따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 함수를 사용하셔도 좋습니다.
	   freopen 함수를 사용하기 위해서는 #include <cstdio>, 혹은 #include <stdio.h> 가 필요합니다.
	   단, 채점을 위해 코드를 제출하실 때에는 반드시 freopen 함수를 지우거나 주석 처리 하셔야 합니다.
	*/
	freopen("8104.txt", "r", stdin);
	cin>>T;
	
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N;
        int K;
        scanf("%d, %d", &N, &K);
		
    //     N, K = tuple(map(int, input().split()))
    // arr = []
    // for i in range(K):
    //     arr.append([0]*N)
    // for i in range(1, N+1):
    //     for k in range(1, K+1):
    //         if i % 2:
    //             arr[k-1][i-1] += k + (i-1) * K
    //         else:
    //             arr[-k][i-1] += k + (i-1) * K
    // res = ''
    // for i in range(K):
    //     res += ' ' + str(sum(arr[i]))
    // print('#{}{}'.format(test_case, res))


	}
	return 0;
}

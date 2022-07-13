import java.util.Scanner;
import java.io.FileInputStream;
public class Solution {

    public static void main(String[] args){

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int N = sc.nextInt();
            int M = sc.nextInt();

            int [][]  G = new int [N][N];

            for(int i = 0; i< N;i++){
                for (int j = 0;j<N;j++){
                    G[i][j] = sc.nextInt();
                }
            }

            int result = 0;
            // row
            for (int i =0 ;i <N;i++){
                int cnt = 0;
                for(int j = 0;j<N;j++){
                    if (G[i][j] == 0){
                        if (cnt == M){
                            result +=1;
                        }
                        cnt = 0;
                    }
                    else {
                        cnt +=1;
                    }
                }
                if (cnt == M){
                    result +=1;
                }
            }
            // col
            for (int i =0 ;i <N;i++){
                int cnt = 0;
                for(int j = 0;j<N;j++){
                    if (G[j][i] == 0){
                        if (cnt == M){
                            result +=1;
                        }
                        cnt = 0;
                    }
                    else {
                        cnt +=1;
                        
                    }
                }
                if (cnt == M){
                    result +=1;
                }
            }
            System.out.println("#"+test_case +" "+result);
		}
	}
}
import java.util.Scanner;
import java.io.FileInputStream;

public class Solution {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int [][] G = new int[9][9];
            boolean is_true = true;

            for (int i = 0; i<9;i++){
                for (int j = 0; j<9;j++){
                    G[i][j] = sc.nextInt();
                }
            }

            // row
            for (int i = 0; i<9;i++){
                int [] check  = new int[10];
                for (int j =0;j<9;j++){
                    check[G[i][j]] +=1;
                }
                for (int j =1; j<10;j++){
                    if (check[j]  ==0 ){
                        is_true = false;
                    }
                }
            }
            // col
            for (int i = 0; i<9;i++){
                int [] check  = new int[10];
                for (int j =0;j<9;j++){
                    check[G[j][i]] +=1;
                }
                for (int j =1; j<10;j++){
                    if (check[j]  ==0 ){
                        is_true = false;
                    }
                }
            }
            // room
            for (int i =0; i<9; i = i+3){
                for (int j = 0;j<9 ;j =j+3){
                    int [] check = new int[10];
                    for (int x = 0; x<3;x++){
                        for (int y = 0;y<3;y++){
                            check[G[i+x][j+y]]++;
                        }
                    }
                    for (int p = 1;p<10;p++){
                        if (check[p] ==0){
                            is_true = false;
                        }
                    }
                }
            }
            if(is_true){
                System.out.println("#"+test_case+" "+1);
            }
            else{
                System.out.println("#"+test_case+" "+0);

            }
		}
	}
}

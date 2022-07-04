import java.util.Scanner;

public class Main {

    public static void main(String args[]) throws Exception
	{
		/*
		   �Ʒ��� �޼ҵ� ȣ���� ������ ǥ�� �Է�(Ű����) ��� input.txt ���Ϸκ��� �о���ڴٴ� �ǹ��� �ڵ��Դϴ�.
		   �������� �ۼ��� �ڵ带 �׽�Ʈ �� ��, ���Ǹ� ���ؼ� input.txt�� �Է��� ������ ��,
		   �� �ڵ带 ���α׷��� ó�� �κп� �߰��ϸ� ���� �Է��� ������ �� ǥ�� �Է� ��� ���Ϸκ��� �Է��� �޾ƿ� �� �ֽ��ϴ�.
		   ���� �׽�Ʈ�� ������ ������ �Ʒ� �ּ��� ����� �� �޼ҵ带 ����ϼŵ� �����ϴ�.
		   ��, ä���� ���� �ڵ带 �����Ͻ� ������ �ݵ�� �� �޼ҵ带 ����ų� �ּ� ó�� �ϼž� �մϴ�.
		 */
		//System.setIn(new FileInputStream("res/input.txt"));

		/*
		   ǥ���Է� System.in ���κ��� ��ĳ�ʸ� ����� �����͸� �о�ɴϴ�.
		 */
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		/*
		   ���� ���� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int N = sc.nextInt();
            int M = sc.nextInt();
            
            int[] A_arr = new int[N];
            int[] B_arr = new int[M];
            for(int i = 0;i < N; i++){
            	A_arr[i] = sc.nextInt();
            }
            for (int i = 0;i <M; i++){
            	B_arr[i] = sc.nextInt();
            }
            int[] small;
            int[] big;
            int diff ;

            
            if (A_arr.length < B_arr.length ){
            	diff  = B_arr.length - A_arr.length;
                small = A_arr;
                big = B_arr;
            } else{
             	diff = A_arr.length - B_arr.length;
                small = B_arr;
                big = A_arr;
            }
            // System.out.println("SMALL : "+small.length +" BIG : "+big.length+" diff :"+diff);

            int max_sum = 0 ;
            for (int k = 0; k<=diff;k++){
                int sum = 0;
                for (int i =0;i<small.length;i++){
                 	   sum += small[i] * big[i+k] ;
                }
                if (k ==0){
                	max_sum = sum;
                }
                if (sum > max_sum){
                	max_sum = sum;	
                }
                
            }
            
            System.out.println("#"+test_case+" "+max_sum);
            
            
         
		
			/////////////////////////////////////////////////////////////////////////////////////////////
			/*
				 �� �κп� �������� �˰��� ������ ���ϴ�.
			 */
			/////////////////////////////////////////////////////////////////////////////////////////////

		}
	}
    
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine()," ");
        int[] arr = new int[N];
        int[] sum = new int[N+1];
        for (int i = 0;i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
            sum[i+1] = sum[i] + arr[i];
        }

        int max_sum = -100 *N;
        for (int i = K;i<=N;i++){
            if(max_sum < sum[i]-sum[i-K])
                max_sum = sum[i] - sum[i-K]; 
        }
        System.out.println(max_sum);
    }
    
}

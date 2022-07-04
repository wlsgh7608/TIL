import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] remains = new int[M];
        int[] arr = new int[N];
        st = new  StringTokenizer(br.readLine());
        int sum = 0;
        for(int i = 0; i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
            sum = (sum+arr[i])%M;
            remains[sum] ++;
        }
        long cnt = remains[0];
        for(int i =0;i<M;i++){
            cnt += (long)remains[i]*(remains[i]-1)/2;
        }
        System.out.println(cnt);
    }
    
}

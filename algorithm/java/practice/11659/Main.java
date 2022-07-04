import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int sum(int[] sum_arr,int start,int end){
        int result  = sum_arr[end] - sum_arr[start-1];
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        int[] arr = new int[N];
        for(int i =0;i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int[] sum_arr = new int[N+1];
        sum_arr[0] = 0;
        for (int i = 1;i<N+1;i++){
            sum_arr[i] = sum_arr[i-1] + arr[i-1];
        }
        for(int i = 0; i<M;i++){
            st = new StringTokenizer(br.readLine(), " ");
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int result = sum(sum_arr,start,end);
            System.out.println(result);
        }
    }
}

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
        
        int[][] G = new int[N][N];
        int[][] sum = new int[N+1][N+1];
        
        for (int i = 0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0;j<N;j++){
                G[i][j] = Integer.parseInt(st.nextToken());
                sum[i+1][j+1] = sum[i][j+1]+sum[i+1][j] +G[i][j]-sum[i][j];
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            sb.append(sum[x2][y2]-sum[x1-1][y2]-sum[x2][y1-1]+sum[x1-1][y1-1]).append('\n');
        }

        System.out.println(sb);
    }
    
}

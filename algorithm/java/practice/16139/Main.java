import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static void init_sum(String str,int[][] sum){

        for(int k =0; k<26;k++){
            for(int i =0;i<str.length();i++){
                char c= str.charAt(i);
                sum[k][i+1] = sum[k][i];
                if (c == (char)((int)('a')+k )){
                    sum[k][i+1] = sum[k][i+1] +1;
                }
            }
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        int iter = Integer.parseInt(br.readLine());

        int[][] sum = new int[26][input.length()+1];
        boolean is_first = true;
        StringBuilder sb = new StringBuilder();
        while (iter-- > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());

            char alphabet = st.nextToken().charAt(0);
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            if (is_first){
                init_sum(input,sum);
                is_first = false;
            }
            int result  = sum[alphabet-'a'][end+1]- sum[alphabet-'a'][start];
            sb.append(result).append('\n');
        }

        System.out.println(sb);
    }
}

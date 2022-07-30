import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

// https://www.acmicpc.net/problem/10845


public class Main{
    public static void main(String[] args){
        Queue <Integer>  q = new LinkedList<>();


        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int test_case = sc.nextInt();
        int last  = 0;


        for (int i = 0; i <test_case;i++){
            String commands = sc.next();

            if (commands.equals("push") ){
                int n = sc.nextInt();
                q.add(n);
                last = n; // 큐의 마지막
            }else if (commands.equals("pop")){
                if ( q.size() > 0 ){
                    sb.append(q.remove()+"\n");
                }
                else{
                    sb.append("-1\n");
                }

            }else if(commands.equals("front")){
                if (q.size() >0){
                    sb.append(q.element()+"\n");
                }
                else{
                    sb.append(-1+"\n");
                }

            }else if(commands.equals("back")){
                if (q.size() >0){
                    sb.append(last+"\n");
                }
                else{
                    sb.append(-1+"\n");
                }

            }else if (commands.equals("size")){
                sb.append(q.size()+"\n");

            }else if (commands.equals("empty")){
                if(q.size() >0){
                    sb.append(0+"\n");
                }
                else{
                    sb.append(1+"\n");
                }                
            }
        }

    System.out.println(sb);
    }
}


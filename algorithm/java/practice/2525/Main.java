import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int time = sc.nextInt();

        int extra_hour = (m+time)/60;
        m = (m+time)%60;
        h = (h+extra_hour)%24;

        System.out.println(h+" "+ m);



    }
    
}

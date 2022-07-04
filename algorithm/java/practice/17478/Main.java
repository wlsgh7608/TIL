import java.util.Scanner;


public class Main {
    static void recursion(int current, int target){
        String depth = "____";
        if (current == target){
            System.out.println(depth.repeat(current) +"\"����Լ��� ������?\"");
            System.out.println(depth.repeat(current) + "\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"");
            System.out.println(depth.repeat(current) +"��� �亯�Ͽ���.");
        }
        else{
            System.out.println(depth.repeat(current) +"\"����Լ��� ������?\"");
            System.out.println(depth.repeat(current) +"\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���.");
            System.out.println(depth.repeat(current) +"���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���.");
            System.out.println(depth.repeat(current) +"���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"");
            recursion(current+1, target);
            System.out.println(depth.repeat(current) +"��� �亯�Ͽ���.");
            
        }

    }


    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println("��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������.");
        recursion(0, n);
        
    }
    
}

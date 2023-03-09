public class Projeto2 extends Thread{

    public  void run(){
        System.out.println("Hello from a Thread");
    }

    public static void main(String[] args){
        Projeto2 p1 = new Projeto2();
        p1.start();
    
    }
}


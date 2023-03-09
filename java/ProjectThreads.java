public class ProjectThreads extends Thread {
    public static int amount = 0;
    public static void main(String[] args) {
   System.out.println("Hello World");
    ProjectThreads pt = new ProjectThreads();
    Thread th = new Thread(pt);
    th.start();
    }

    @Override
    public void run(){
        System.out.println("Hello World from a Thread");
    }
}
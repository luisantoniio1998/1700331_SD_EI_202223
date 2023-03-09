public class Project3 {
    String paises[] = {"Portugal", "Suica", "EUA", "Espanha"};
    public static void main (String[] args) throws InterruptedException{
        Project3 p1 = new Project3();
        for(int i = 0; i<4; i++){
            System.out.println(p1.paises[i]);
            Thread.sleep(5000);
        }
    }
}
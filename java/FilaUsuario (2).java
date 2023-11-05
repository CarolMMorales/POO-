import java.util.Scanner;

public class FilaUsuario{
    private int[ ] fila;
    private int index;
    private int nUsuarios;
    
    public FilaUsuario() {
        this.fila= new int [20];
        this.index = 0;
        this.nUsuarios=0;
    }
    
    public FilaUsuario (int n) {
        this.fila = new int [n];
        this.index=0;
        this.nUsuarios=0;
    }
    
    public void llenarFila() {
        int user=0;
        if(fila[fila.length-1] == 0){
            if(index < fila.length) {
                fila[index] = ++nUsuarios;
                index++;
            }
        }else{
            System.out.println("La fila esta llena");
        }
        imprimirFila();
    }
    
    public void retirarUsuarioFila ( ) {
        if (index != 0) {
            for (int i = 0; i < fila.length-1; i++) {
                fila [i]=fila [i+1];
            }
            fila[fila.length -1] = 0;
            index--;imprimirFila ();
        }else{
        System.out.println("La fila esta vacia");
        }
    imprimirFila();
    }

    public boolean estaVacia () {
        if (fila [0]==0) {
            return true;
        }
        return false;
    }
    
    public void imprimirFila ( ) {
        System.out.println("");
        for (int i = 0; i < fila. length; i++) {
            System.out.println(fila[i]+" ");
        }
        System.out.println("");
    }
    public static void main (String []args) {
        int usuarios = 5;
        TestFila app = new TestFila(usuarios);
        app.procesarOperacionesFila();
    }
}
class TestFila {
    private FilaUsuario unaFila;
    private Scanner sc;

    public TestFila (int n){
        if (n > 0){
            this.unaFila = new FilaUsuario (n);
            this.sc = new Scanner (System.in);
        }
    }
    
    public void procesarOperacionesFila (){
        String menu = "1. Agregar usuario fila. \n2. Imprimir fila\n"
                        + "3. Retirar usuario fila\n4. Estado de la filaln"
                        + "5. Salir\n\nSeleccione opcion";
        int opc = 1;
        
        do {
            System.out.println (menu);
            opc = sc.nextInt ();
            switch (opc) {
                case 1: unaFila.llenarFila ();
                    break;
                case 2: unaFila.imprimirFila ();
                    break;
                case 3: unaFila.retirarUsuarioFila ();
                    break;
                case 4: verificarEstado ();
                    break;
            }
        }while (opc!=5);
    }
    
    private void verificarEstado () {
        if (unaFila.estaVacia ()) {
            System.out.println("La fila esta vacia");
        }else {
            System.out.println("en la fila hay usuarios");
        }
    }
}
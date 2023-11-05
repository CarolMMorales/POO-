import java.util.Scanner;
public class Pila {
    private int[] pila;
    private int index;
    private int nProceso;
    
    //se crea un arreglo
    public Pila(){
        this.pila = new int[20];
        this.index = pila.length - 1;
        this.nProceso=0;
    }
    
    public Pila(int n){
        this.pila = new int [n];
        this.index = pila.length - 1;
        this.nProceso = 0;
    }
    
    //metodo que anexa datos a la pila
    public void llenarPila(){
        if(index > pila.length){
            index = pila.length - 1;
        }
        if(index >= 0){
            pila[index] = ++nProceso;
            index--;
        }else{
            int i = index;
            while (pila[i] !=0){
                pila[i - 1]=pila[i];
                i++;
            }
            pila[i-1] = ++nProceso;
            index--;
        }
        imprimirPila();
    }
    public void retirarUsuarioPila(){
        boolean estado = true;
        int i = 0;
        while(estado && i<pila.length){
            if(pila[i] != 0){
                estado = false;
                pila[i] = 0;
                --nProceso;
                ++index;
            }
            i++;
        }
        imprimirPila();
    }
    public String consultarEstadoPila(){
        String estado = "";
        if(pila[0] != 0){
            estado = "la pila esta llena";
        }else if(pila[pila.length - 1] == 0){
            estado= "la pila esta vacia";
        }else if(nProceso != 0){
            estado = "la pila tiene datos";
        }
        return estado;
    }
    //metodo que imprime datos en la fila 
    public void imprimirPila(){
        System.out.println("");
        for (int i= 0; i < pila.length; i++){
            System.out.println(pila[i]+" ");
        }
        System.out.println("");
    }
    public static void main (String []args){
        int usuarios = 5;
        Main app = new Main(usuarios);
        app.procesarOperacionesPila();
    }
}
class Main{
    //instanciar variables 
    private Pila unaPila;
    private Scanner sc;
    
    public Main(int n){
        if(n > 0){
            this.unaPila = new Pila(n);
            this.sc = new Scanner (System.in);
        }
    }
    public void procesarOperacionesPila(){
        String menu = "1. Agregar usuario pila. \n2. Imprimir pila\n"
                        + "3. Retirar usuario pila\n4. Estado de la pila\n5. Salir"
                        + "\n\nSeleccione opcion";
        int opc = 1;
        
        do {
            System.out.println (menu);
            opc = sc.nextInt ();
            switch (opc) {
                case 1: unaPila.llenarPila ();
                    break;
                case 2: unaPila.imprimirPila ();
                    break;
                case 3: unaPila.retirarUsuarioPila ();
                    break;
                case 4: System.out.println(unaPila.consultarEstadoPila()+"\n");
                    break;
                default:
                    System.out.println("Opción errada");
                    break;
            }
        }while (opc!=5);
    }
    
}


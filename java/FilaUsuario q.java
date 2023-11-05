import java.util.Queue;
import java.util.LinkedList;

public class FilaUsuario{
    private Queue<Integer> q;
    private Integer user;
    
    //se crea un arreglo
    
    public FilaUsuario(){
        this.q = new LinkedList<>();
        this.user = 1;
    }
    
    //metodo que anexa usuarios en la Fila
    public void llenarFila(){
        q.add(user);
        user++;
        imprimirFila();
    }
    //metodo que retira un usuario de la Fila
    public void retirarUsuarioFila(){
        if (q.peek () !=null){
            System.out.println("Valor: " + q.poll());
        }
        imprimirFila();
    }
    //metodo que evalua si la cola esta vacia
    public boolean estaVacia(){
        if(q.isEmpty()){
            return true;
        }
        return false;
    }
    //metodo que imprime los usuarios de la fila 
    public void imprimirFila(){
        System,out.printIn("");
        for (Integer dato : q){
            System.out.print(""+dato);
        }
        System.out.printIn("");
    }
}

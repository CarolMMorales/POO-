// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

class Libro
{
    public:
        string titulo;
        string autor;
        int anoPublicacion;
        int numPaginas; 
        int estado;
        void mostrarInformacion();
        void prestarLibro();
        void devolverLibro();
        void estaPrestado();
        
    Libro(string, string, int, int);
};
Libro::Libro (string _titulo, string _autor, int _anoPublicacion, int _numPaginas)
{
    titulo= _titulo;
    autor= _autor;
    anoPublicacion= _anoPublicacion;
    numPaginas= _numPaginas;
}
        void Libro::mostrarInformacion(){
            cout<<"el libro es: "<< titulo<<" escrito por "<< autor<<" publicado en el "<< anoPublicacion<<" con "<< numPaginas<<" paginas."<<endl;
        }
        void Libro::prestarLibro(){
            cout<<"seleccione 1 si prestara el libro ";
            cin>>estado;
            if (estado == 1){
                cout<<"libro prestado"<<endl;
            }else if ( estado != 1){
                cout<<"el libro no se presto"<<endl;
            }
        }
        void Libro::estaPrestado(){
            if (estado == 1){
                cout<<"true " <<true <<endl;
            }else if (estado != 1){
                cout<<"false "<< false <<endl;
            }
        }
        void Libro::devolverLibro(){
            if (estado == 1){
                cout<<"seleccione 2 si devolvera el libro ";
                cin>>estado;
                if (estado == 2){
                    cout<<"libro devuelto" <<endl;
                }else if(estado != 2){
                    cout<<"el libro no se devolvio"<<endl;
             }
            }
        }
        


int main() {
    Libro book1("lenguajes","carol",2004,124);
    book1.mostrarInformacion();
    book1.prestarLibro();
    book1.estaPrestado();
    book1.devolverLibro();
    book1.estaPrestado();
    
    Libro book2("programacion","michell",2023,655);
    book2.mostrarInformacion();
    book2.prestarLibro();
    book2.estaPrestado();
    book2.devolverLibro();
    book2.estaPrestado();
    return 0;
}

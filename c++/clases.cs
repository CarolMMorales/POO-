// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
class Persona{
    private:
        string nombre;
        int edad;
    public:
        Persona(string n, int e):nombre(n), edad(e){
        
        }
        string getNombre(){
            return nombre;
        }
        int getEdad(){
            return edad;
        }
        void setEdad(int nuevaEdad){
            if(nuevaEdad>=0){
                edad = nuevaEdad;
        }
    }
};
class Animal{
    public:
        void comer(){
            cout<<"El animal come"<<endl;
        }
        virtual void emitirSonido(){
            cout<<"el animal emite sonido"<<endl;
        }
};
class Perro: public Animal{
    public:
    void emitirSonido(){
        cout<<"aauuuuuuuuu"<<endl;
    }
    void ladrar(){
        cout<<"el perro ladra"<<endl;
    }
};
class Gato: public Animal{
    public:
        void emitirSonido()override{
            cout<<"miauuuu"<<endl;
        }
};
int main() {
    //personas
   Persona Persona1("juan", 25);
   cout<<"nombre: "<<Persona1.getNombre()<<endl;
   cout<<"edad: "<<Persona1.getEdad()<<endl;
   Persona1.setEdad(16);
   cout<<"nueva edad:"<<Persona1.getEdad()<<endl;
   
   //animal
   Perro miPerro;
   miPerro.ladrar();
   //herencia
   miPerro.comer();
   //polimorfismo
   Perro firulais;
   firulais.emitirSonido();
   Gato michi;
   michi.emitirSonido();
    return 0;
}

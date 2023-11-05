document.querySelector("#enviar").addEventListener("click", recibir);
document.querySelector("#vista").addEventListener("click", mostrar);


//array y cajas de texto
let ListPersonas = [];
function recibir(){
    
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const id = document.getElementById('id').value;
    const edad = document.getElementById('edad').value;
    const res= document.getElementById('residencia').value;
    var persona1 = new Personas( nombre, apellido, id, edad, res);
    
    ListPersonas.push(persona1);
    
};

function mostrar(){
    alert(ListPersonas.length);
    
    for (let k=0; k< ListPersonas.length; k++){
        document.write("<h4>"+"Registro"+[k]+"<br>" +"nombre: "+ListPersonas[k].name+"<br>"+"Apellido: "+ListPersonas[k].lastname+"<br>" +"Identificación: "+ ListPersonas[k].id+"<br>"+"Edad: "+ ListPersonas[k].age+"<br>"+"Direccion: " +ListPersonas[k].address+"<hr>"+"</h4>");
    };
    
};
class Personas{
    constructor(nombre, apellido, id, edad, res){
        this.name = nombre;
        this.lastname = apellido;
        this.id = id;
        this.age= edad;
        this.address = res;
    }
}




 

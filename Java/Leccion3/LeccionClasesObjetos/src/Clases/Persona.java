
package Clases;


public class Persona {
    //Atributos de la clase(características)
    String nombre;
    String apellido;
    
    //Métododos de la clase (Acciones)
    //public: es para indicar que el método se puede utilizar fuera de esta clase
    //void: indica que no regresa ningún tipo de información
    //una clase es nuestra plantilla
    public void obtenerInformacion(){
        System.out.println("Nombre: "+nombre);
        System.out.println("Apellido: "+apellido);
    }
    
}

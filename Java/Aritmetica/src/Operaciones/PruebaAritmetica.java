/*
 Clase Aritmética: creamos un objeto
 */
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10; //variables locales
        int b = 7; //memoria STACK(con la que trabaja una variable local)
        miMetodo(); //llamamos el método nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        //para almacenar un objeto o los atributos se utiliza la memoria HEAP
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = "+ resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = "+aritmetica2.a);
        System.out.println("aritmetica2 = "+aritmetica2.b);
        //aritmetica1 = null; nunca utilizar esto, no es necesario
        //System.gc(); garbage colection, recolector de basura, es pesado, no utilizar
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona nombre: "+persona.apellido);
    }
    //Modularidad, creamos un nuevo método
    public static void miMetodo() { //método dentro de otro método
        int a = 10; //una variable está limitada
        System.out.println("Aqui hay otro método");
        //los atributos tienen un alcance superior a una variable local
    }
 
}
//Creamos una nueva clase
class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ //constructor
        super(); //llamada al constructor de la clase padre object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}
class Imprimir{
    public Imprimir(){
        super();//el constructor de la calse padre para reservar memoria
    }
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresión del objeto actual (this): "+this);
    }
}

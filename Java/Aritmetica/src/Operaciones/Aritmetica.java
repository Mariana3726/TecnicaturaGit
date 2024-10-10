/*
 
 */
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    //El constructor es un método especial.
    //Primero:construye un objeto.Segundo:reserva un espacio de memoria.Tercero:inicializa los atributos de la clase.
    public Aritmetica(){ //constructor 1 vacio
        System.out.println("Se esta ejecutando este constructor número uno");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){ //constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor número dos");
    }
    
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = "+ resultado);
    }
    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }
    public int sumarConArgumentos(int a, int b){
        this.a = a; //el argumento a se asigna al atributo this.a
        this.b = b;
        //return a + b;
        return this.sumarConRetorno();
    }
}
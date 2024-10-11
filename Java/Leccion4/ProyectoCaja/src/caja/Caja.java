/*
Proyecto caja:
Ejercicio 1: crear un proyecto según las especificaciones mostradas a continuación:
La fórmula es: volumen = ancho * alto * profundidad
 */
package caja;

public class Caja { //clase pública caja
    //atributos (características)
    int ancho;
    int alto;
    int profundidad;
    //Métodos y constructores (acciones)
    public Caja (){ //Constructor 1 = vacío
    }
    //Constructor con parámetros
    public Caja(int ancho, int alto, int profundidad){ //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    
    public int calcularVolumen() { //método para calcular
      return ancho * alto * profundidad;  
    }
    
}

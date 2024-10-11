/*
Proyecto caja:
Ejercicio 1: crear un proyecto según las especificaciones mostradas a continuación:
La fórmula es: volumen = ancho * alto * profundidad
 */
package caja;

public class PruebaCaja {
    public static void main(String[] args) { //método main
        //variables locales
        int medidaAncho = 3; //valores ingresados en código duro
        int medidaAlto = 2;
        int medidaProfundidad = 6;
        
        Caja caja1 = new Caja(); //instanciamos en objeto, constructor vacío
        caja1.ancho = medidaAncho; //le pasamos los valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundidad = medidaProfundidad;
        int resultado = caja1.calcularVolumen(); //llamamos al método
        //primer resultado
        System.out.println("resultado volumen de caja 1: " + resultado);
        
        Caja caja2 = new Caja(2, 4 ,6); //llamamos al constructor 2 con nuevos argumentos
        //llamamos con el nuevo objeto al método para un nuevo cálculo
        System.out.println("resultado volumen de caja 2: " + caja2.calcularVolumen());
        
    }
    
}

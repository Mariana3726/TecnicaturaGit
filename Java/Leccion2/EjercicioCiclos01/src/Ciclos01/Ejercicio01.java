/*
CICLOS
Ejercicio 1: Leer un número y mostrar su cuadrado, repetir el proceso hasta que 
se introduzca un número negativo. Trabajamos con JOptionPane
*/
package Ciclos01;

import javax.swing.JOptionPane;


public class Ejercicio01 {
    public static void main(String[] args) {
        int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0) { //mientras el número sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+" elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite  número: "));
        }
        System.out.println("El programa ha finalizado por número negativo");
    }
}

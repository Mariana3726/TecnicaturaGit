/*
Ejercicio 12: pedir un número y calcular su factorial. Hacerlo con la clase
Scanner y JOptionPane.
 */
package ciclos12;

import javax.swing.JOptionPane;

//import java.util.Scanner;


public class Ciclos12 {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        //System.out.println("Ingrese un número: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        for(int i=1; i<=numero; i++){
            factorial *= i;
        }
        //System.out.println("\nEl factorial del número ingresado es: "+factorial);
        JOptionPane.showInputDialog(null, "El factorial del número ingresado es: "+factorial);
    }
}

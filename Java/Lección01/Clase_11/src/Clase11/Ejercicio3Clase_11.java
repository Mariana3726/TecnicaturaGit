package Clase11;

import java.util.Scanner;

public class Ejercicio3Clase_11 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //se leen dos números ingresados por el usuario
        System.out.print("Ingrese el primer número: ");
        double numero1 = scanner.nextDouble();

        System.out.print("Ingrese el segundo número: ");
        double numero2 = scanner.nextDouble();

        double resultado;

        if (numero1 == numero2) {
            // Si son iguales, multiplicamos
            resultado = numero1 * numero2;
            System.out.println("El resultado de la multiplicación es: " + resultado);
        } else if (numero1 > numero2) {
            // Si el primero es mayor, restamos
            resultado = numero1 - numero2;
            System.out.println("El resultado de la resta es: " + resultado);
        } else {
            // Si no, sumamos
            resultado = numero1 + numero2;
            System.out.println("El resultado de la suma es: " + resultado);
        }
    }
}

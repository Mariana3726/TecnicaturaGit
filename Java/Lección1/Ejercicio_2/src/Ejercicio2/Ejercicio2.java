package Ejercicio2;
//Calcular área y perímetro de un rectángulo

import java.util.Scanner;

public class Ejercicio2 {

    public static void main(String[] args) {
        {
            try {
                Scanner sca = new Scanner(System.in);
                float base, altura, perimetro, area;

                System.out.print("Ingresa los metros de la base: ");
                base = sca.nextFloat();
                System.out.print("Ingresa los metros de la altura: ");
                altura = sca.nextFloat();

                perimetro = (2 * base) + (2 * altura);
                area = base * altura;

                System.out.println("El perímetro es " + perimetro + " metros");
                System.out.println("El área es " + area + " metros cuadrados");
            } catch (Exception ex) {
                System.out.println("Debes ingresar números con punto decimal (por ejemplo, 5.5).");
            }
        }
    }
}

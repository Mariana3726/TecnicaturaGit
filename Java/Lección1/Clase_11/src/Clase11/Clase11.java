package Clase11;

/*Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobará si 
su promedio de tres calificaciones es mayor o igual a 7, si es menor reprueba.*/
import java.util.Scanner;

public class Clase11 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicita las tres calificaciones al usuario
        /*System.out.print("Ingresa la primera calificación: ");
        double calificacion1 = scanner.nextDouble();

        System.out.print("Ingresa la segunda calificación: ");
        double calificacion2 = scanner.nextDouble();

        System.out.print("Ingresa la tercera calificación: ");
        double calificacion3 = scanner.nextDouble();

        // Calcula el promedio
        double promedio = (calificacion1 + calificacion2 + calificacion3) / 3;

        // Verifica si el alumno aprueba o reprueba
        if (promedio >= 7) {
            System.out.println("El alumno aprueba el curso con un promedio de " + promedio);
        } else {
            System.out.println("El alumno reprueba el curso con un promedio de " + promedio);*/
        }
    }

    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el monto de la compra: ");
        double compra = scanner.nextDouble();

        double descuento;
        if (compra > 100) {
            descuento = 0.2; // 20% de descuento
        } else {
            descuento = 0; // Sin descuento
        }

        double totalConDescuento = compra - (compra * descuento);

        System.out.println("Total de la compra: $" + compra);
        System.out.println("Descuento aplicado: " + (descuento * 100) + "%");
        System.out.println("Total a pagar: $" + totalConDescuento);

        scanner.close();
    }
}

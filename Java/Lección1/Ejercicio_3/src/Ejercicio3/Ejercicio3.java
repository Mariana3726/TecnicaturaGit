package Ejercicio3;
//Calcule e imprima la suma de tres calificaciones
import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int calificacion1, calificacion2, calificacion3;

        System.out.print("Ingrese la primera calificación: ");
        calificacion1 = leer.nextInt();

        System.out.print("Ingrese la segunda calificación: ");
        calificacion2 = leer.nextInt();

        System.out.print("Ingrese la tercera calificación: ");
        calificacion3 = leer.nextInt();

        // Calcula la suma de las calificaciones
        int suma = calificacion1 + calificacion2 + calificacion3;

        // Calcula el promedio
        double promedio = suma / 3.0; // Usamos 3.0 para obtener un resultado decimal

        System.out.println("La suma de las calificaciones es: " + suma);
        System.out.println("El promedio es: " + promedio);
    }
}
        

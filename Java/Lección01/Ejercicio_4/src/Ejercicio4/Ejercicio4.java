
package Ejercicio4;

import java.util.Scanner;
/*Guillermo tiene N dólares. Luis tiene la mitad de lo que posee Guillermo.
Juan tiene la mitad de lo que poseen Luis y Guillermo juntos. Hacer un programa 
que calcule  e imprima la cantidad de dinero que tienen entre los tres.*/



public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double guillermoDolares, luisDolares, juanDolares, totalDolares;

        System.out.print("Ingrese la cantidad de dólares de Guillermo: ");
        guillermoDolares = sc.nextDouble();

        // Calculamos los montos de Luis y Juan
        luisDolares = guillermoDolares / 2;
        juanDolares = (guillermoDolares + luisDolares) / 2;

        // Calculamos el total
        totalDolares = guillermoDolares + luisDolares + juanDolares;

        // Mostramos los resultados
        System.out.println("\nRESULTADO");
        System.out.println("----------");
        System.out.println("Dinero de Guillermo: $" + guillermoDolares);
        System.out.println("Dinero de Luis     : $" + luisDolares);
        System.out.println("Dinero de Juan     : $" + juanDolares);
        System.out.println("Total              : $" + totalDolares);
    }
    
}

package Clase11;
//en un almacén se hace un 20% de descuento a los clientes cuya compra supere los
//$100. ¿Cuál será la cantidad que pagará una persona por su compra?
import java.util.Scanner;

public class Ejercicio2Clase11 {

    public static void main(String[] args) {
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

    }
}

package Leccion2;
//Condicional

import java.util.Scanner;


public class Leccion2 {

    public static void main(String[] args) {
        /* var condicion = false;
        if(condicion) {
            System.out.println("Condición verdadera"); //condicional simple
        }
        else{
            System.out.println("Condición falsa"); //condicional doble
        }
        
        var numero = 3;
        var numeroTexto = "Número desconocido";
        if(numero == 1){
            numeroTexto = "Número uno";
        }
        else if(numero == 2){
            numeroTexto = "Número dos";
        }
        else if (numero == 3) {
            numeroTexto = "Número tres";
        }
        else if (numero == 4) {
            numeroTexto = "Número cuatro";
        }
        else{
            numeroTexto = "Número no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);*/

        //SENTENCIA DE CONTROL SWITCH
        Scanner entrada = new Scanner(System.in);
        System.out.println("Escriba un número del 1 al 4: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "Valor desconocido";
        switch (numero) {
            case 1:
                numeroTexto = "Número uno";
                break;
            case 2:
                numeroTexto = "Número dos";
                break;
            case 3:
                numeroTexto = "Número tres";
                break;
            case 4:
                numeroTexto = "Número cuatro";
                break;
            default:
                numeroTexto = "Caso no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
    }
}

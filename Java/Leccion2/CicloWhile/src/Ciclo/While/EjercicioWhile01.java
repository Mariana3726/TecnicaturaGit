package Ciclo.While;


public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0; //inferencia de tipos
        while(conteo <= 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //vamos aumentando en uno la variable
        }
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador <= 7);
        
        //Uso de las palabras break y continue junto a las etiquetas Labels
        //ejemplo: Inicio
                
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break;
            }
        }
        inicio:
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){
              continue inicio;  //vamos a la siguiente iteración             
            }
            System.out.println("contando = " + contando);
        }
   
    }
        
}

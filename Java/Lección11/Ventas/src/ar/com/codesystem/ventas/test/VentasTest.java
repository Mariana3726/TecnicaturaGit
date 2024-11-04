
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;


public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalón", 9500.00);
        Producto producto2 = new Producto("Campera", 5900.00);
        Producto producto3 = new Producto("Medias", 900.00);
        Producto producto4 = new Producto("Musculosa", 3900.00);
        Producto producto5 = new Producto("Short", 1900.00);
        Producto producto6 = new Producto("Zapatillas", 12900.00);
        Producto producto7 = new Producto("Sueter", 4500.00);
        Producto producto8 = new Producto("Camiseta", 2900.00);
        Producto producto9 = new Producto("Medias 3/4", 500.00);
        Producto producto10 = new Producto("Cardigan", 8900.00);
        Producto producto11 = new Producto("Chomba", 3900.00);
        Producto producto12 = new Producto("Guantes", 1900.00);
        
        
        Orden orden1 = new Orden();
        Orden orden2 = new Orden();
        Orden orden3 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden2.agregarProducto(producto9);
        orden2.agregarProducto(producto12);
        orden3.agregarProducto(producto5);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto7);
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        orden3.mostrarOrden();
        
        //Tarea:
        //Crear mas objetos de tipo Producto = 10
        //Crear mas objetos de tipo Orden = 2
    }
}

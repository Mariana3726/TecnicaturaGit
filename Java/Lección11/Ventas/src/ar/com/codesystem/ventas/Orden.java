
package ar.com.codesystem.ventas;

public class Orden {
    private int idOrden;
    private Producto productos[]; //declaramos el arreglo
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODCUTOS = 10;
    
    //Constructor vacío
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODCUTOS];
    }
    
    //método que combina lal clases producto y orden
    public void agregarProducto(Producto producto){
        if(this.contadorProductos < Orden.MAX_PRODCUTOS){
            this.productos[this.contadorProductos++] = producto;
        }
        else{
            System.out.println("Se ha superado el máximo de productos: "+Orden.MAX_PRODCUTOS);
        }
    }
    
    public double calcularTotal(){
        double total = 0; //variable temporal
        for (int i = 0; i < this.contadorProductos; i++) {
            //Producto producto = this.productos[i];
            //total += producto.getPrecio();
            total += this.productos[i].getPrecio();
        }
        return total;
    }
    
    public void mostrarOrden(){
        System.out.println("Id Orden: "+idOrden);
        double totalOrden = this.calcularTotal();
        System.out.println("El total de la orden es: $"+totalOrden);
        System.out.println("Productos de la orden: ");
        for (int i = 0; i < this.contadorProductos; i++) {
            System.out.println(this.productos[i]);
            
        }
    }
    
}

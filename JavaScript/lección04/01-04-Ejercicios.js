//Ampliando el uso de var,let y const
/*
Con var puedes reasignar en cualquier momento
este forma parte del ambito global
Un error es que se sobreescriba
*/

var nombre = 'Mariana';
nombre = 'Florencia';
console.log(nombre);

function saludar(){
    var nombre3 = 'Natalia';
    console.log(nombre3);
}
//console.log(nombre3); //aqui no lee el dato en la función

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //en la función funcionó bien,en la estructura if falló

/*
let: esa puede ser reasignada en cualquier momento,la diferencia
es que su ámbito es de bloque,solo disponible dentro de un 
bloque de llaves o dentro de una función
*/

function saludar2(){
    let nombre2 = 'Ariel';
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);
 /*
 const se utiliza para variables que no pueden ser reasignadas
 */

 const fechaNacimiento = 2006;
 console.log(fechaNacimiento);
 //fechaNacimiento = 2003;
 //console.log(fechaNacimiento); //solo se ejecuta el console anterior



 //Ejercicio 1: calcular estación del año//
 let mes = 11;
 let estación;
 if(mes == 1 || mes == 2 || mes == 12){
    estación = "Verano";
 }
 else if(mes == 3 || mes == 4 || mes == 5){
    estación = "Otoño";
 }
 else if(mes == 6 || mes == 7 || mes == 8){
    estación = "Invierno";
 }
 else if(mes == 9 || mes == 10 || mes == 11){
    estación = "Primavera";
 }
 else{
    estación = "Valor incorrecto"
 }
 console.log("El valor corresponde a la estación: "+estación);

 //Ejercicio 2: hora del dia//

 let horaDia = 18;
 let mensaje;
 if(horaDia >= 6 && horaDia <= 13){
    mensaje  = "Desayuno y trabajo";
 }
 else if(horaDia >= 14 && horaDia <= 16){
    mensaje = "Gym";
 }
 else if( horaDia >= 17 && horaDia <= 19){
    mensaje = "Almuerzo y estudio";
 }
 else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Clases, estudio y cena"
 }
 else{
    mensaje = "Valor incorrecto";
 }
 console.log(mensaje);

 //Estructura switch(la sintaxis es igual a Java)
 switch(mes){ //se puede utilizar números y tmb cadenas
    case 1: case 2: case 12:
        estación = "Verano";
        break;
    case 3: case 4: case 5:
        estación = "Otoño";
        break;
    case 6: case 7: case 8:
        estación = "Invierno";
        break;
    case 9: case 10: case 11:
        estación = "Primavera";
        break;
    default:
        estación = "Valor incorrecto";
 }
 console.log("Bienvenido a la estación "+estación);

 //Evitar repetir tu código
 //Dry don´t repeat yourself
 //Let days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
 let days = 8;
 
 switch(days) {
   case 1:
      console.log('hoy es Lunes');
      break;
   case 2:
      console.log('hoy es Martes');
      break;
   case 3:
      console.log('hoy es Miércoles');
      break;
   case 4:
      console.log('hoy es Jueves');
      break;
   case 5:
      console.log('hoy es Viernes');
      break;
   case 6:
      console.log('hoy es Sábado');
      break;
   case 7:
      console.log('hoy es Domingo');
      break;
   default:
      console.log('Error en el ingreso del día de la semana');
      break;
 }

 //Esta es la opción mejorada, para no repetir código
 let days2 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];

 function getDay(n){
   if(n < 1 || n > 7){
      throw new Error('out of range');
   }
   return days2[n-1];
 }
 console.log(getDay(1)); 

 //Hacer un ejercicio similar al que está hecho con la estructura switch y con la opción mejorada

 let month = 11;
 
 switch(month) {
   case 1:
      console.log('Enero');
      break;
   case 2:
      console.log('Febrero');
      break;
   case 3:
      console.log('Marzo');
      break;
   case 4:
      console.log('Abril');
      break;
   case 5:
      console.log('Mayo');
      break;
   case 6:
      console.log('Junio');
      break;
   case 7:
      console.log('Julio');
      break;
   case 8:
      console.log('Agosto');
      break;
   case 9:
      console.log('Septiembre');
      break;
   case 10:
      console.log('Octubre');
      break;
   case 11:
      console.log('Noviembre');
      break;
   case 12:
      console.log('Diciembre');
      break;
   default:
      console.log('Error en el ingreso del mes');
      break;
 }


//versión mejorada

let month1 = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

 function getMonth(n){
   if(n < 1 || n > 12){
      throw new Error('out of range');
   }
   return month1[n-1];
 }
 console.log(getMonth(12)); 
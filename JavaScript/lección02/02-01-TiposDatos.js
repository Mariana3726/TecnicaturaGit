//Tipos de datos en JavaScript
/*
La sintaxis en lo que es comentarios es muy similar
a la de Java. Realmente diríamos que es idéntica.
*/

var nombre = "Mariana"; //Tipo str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre); 

var numero = 3000; //Tipo numérico
console.log(numero);

var objeto = {
    nombre : "Mariana",
    apellido : "Aguilera",
    telefono : "2604319088"
}
console.log(objeto);

//Tipos de datos boolenanos true o false
var bandera = true;
console.log(bandera);

 //Tipos de datos funcion
 function mifuncion(){}
 console.log(typeof mifuncion);

 //Tipo de dato symbol
 var simbolo = Symbol("MI simbolo");
 console.log(typeof simbolo);

 //Tipo de dato clase
 class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
 }

 console.log(typeof Persona);

 //Tipo de dato Undefined
 var x;
 console.log(typeof x);

 x = undefined;
 console.log(typeof x);

 //null: significa ausencia de valor
 var y = null; //null no es un tipo de dato pero su origen es de tipo object
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ['Citroen','Audi','BMW','Ford'];
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z); //es una cadena vacía [empty string]
console.log(typeof z);

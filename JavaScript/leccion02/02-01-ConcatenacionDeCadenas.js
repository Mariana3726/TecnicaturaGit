var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+''+apellido; //primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'Mariana'+' '+'Aguilera';//segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izq a der siguiendo la cadena lee el num como str
console.log(juntos);
juntos = nombre + (78 + 17); //Aqui para diferenciar a través de los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; //tercera concatenación concatenamos usando el operador simplificado
console.log(nombre);

//Hoy no se va a usar var. se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//apellido2 = "Perez"; una constante no puede ser modificada
console.log(apellido2)

let x, y; //se pueden crear varias variables dentro de una misma línea
x = 17, y = 21; //se puede hacer asignacion de varias variables dentro de la misma linea
let z = x + y; //se asigna el valor de la operación
console.log(z);

let _1num = 31; //no utilizar numeros para iniciar el nombre de una variable
let rompiendo = "rompe"; //no utilizar palabras reservadas para variables

console.log(_1num);
console.log(rompiendo);


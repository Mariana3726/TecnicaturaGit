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

//Hoy ya no se va a usar var, sino let y const
let nombre2 = "Pedro";
console.log(nombre2); 

const apellido2 = "Lepes";
//apellido2 = "Perez"; una constante no puede ser modificada
console.log(apellido2)


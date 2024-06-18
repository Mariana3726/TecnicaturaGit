//Ejercicio para encontrar números pares e impares
let parImpar = 14;
if(parImpar % 2 == 0){
    console.log('El número es par');
}
else{
    console.log('El número es impar');
}

//Ejercicio: es mayor o menor de edad
let edad = 18, adulto = 18;
if( edad >= adulto ){
	console.log('Es adulto');
}
else{
	console.log('Es menor de edad') 
}

//Ejercicio: dentro de un rango
let dentroRango = 11
; //aca vamos a ir cambiando el valor
let valMIin = 0, valMax = 10;
if(dentroRango >= valMIin && dentroRango <= valMax){
    console.log('Está dentro del rango establecido')
}
else{
    console.log('Está fuera del rango establecido')
}
//Ejercicio: si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("El padre no puede asistir al juego de su hijo")
}
//Operador ternario
let resultado2 = 3 > 2 ? "verdadero" : "falso";
console.log(resultado2)
let numero = 8;
resultado2 = numero % 2 == 0 ? "Es un Par" : "Es Impar"
console.log(resultado2)

//Convertir strig a número
let miNumero = "18";
console.log(typeof miNumero);
let edad2 = Number(miNumero); //esta es una función
console.log(typeof edad2);
//Función isNaN
if(isNaN(edad2)){ //no es un número=is not a number(devuelve un resultado booleano)
    console.log("Esta variable no contiene solo números")
}
else{
    if(edad2 >= 18){
        console.log("Puede votar");
    }
else {
        console.log("No puede votar");
    }
}
let resultado3 = edad2 >= 18 ? "Puede votar" : "No puede votar";
console.log(resultado3);


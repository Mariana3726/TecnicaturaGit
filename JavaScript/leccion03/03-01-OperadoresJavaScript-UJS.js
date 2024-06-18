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

let x = 10; //variable de tipo primitivo
console.log(x.lenggth);
console.log('Tipos primitivos');

//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'es',
    get lang(){ //método get
        return this.idioma.toUpperCase(); //convierte minúsculas a mayúsculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ //método o función de JS
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){ //este es el método get
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    }
    
}
console.log(persona.nombre);
console.log(persona.email);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');

let persona2 = new Object(); //debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '2615423456';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');
console.log(persona['apellido']); //accedemos como si fuera una arreglo
console.log('Usamos el ciclo for in');

//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log('Cambiamos y eliminamos un error');
persona.apellida = 'Betancud'; //cambiamos dinámicamente un valor del objeto
delete persona.apellida; //eliminamos el error
console.log(persona);


//Distintas formas de imprimir un objeto
//Número 1: las mas sencilla, concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto: Forma 1');
console.log(persona.nombre+', '+persona.apellido);

//Número 2: a través del ciclo for in
console.log('Distintas formas de imprimir un objeto: Forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Número 3: la función Object.values()
console.log('Distintas formas de imprimir un objeto: Forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Número 4: utilizaremos el método JSON.stringify
console.log('Distintas formas de imprimir un objeto: Forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log('Comenzamos a utilizar el método get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el método get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){ //constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Leo', 'López', 'lopezleo@gmail.com');
padre.nombre = 'Luis'; //modificamos el nombre
padre.telefono = '152417888'; //una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); //utilizamos la función

let madre = new Persona3('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.telefono); //la propiedad no está definida
console.log(madre.nombreCompleto());


//Diferfentes formas de crear objetos
//Caso objeto 1
let miObjeto1 = new Object(); //esta es una opcion formal

//Caso objeto 2
let miObjeto2 = {}; //esta es una opción breve y recomendada

//Caso string 1
let miCadena1 = new String('Hola'); //sintaxis formal

//caso string 2
let miCadena2 = 'Hola'; //sintaxis simplificada y recomendada

//Caso con números 1
let miNumero1 = new Number(1); //formal no recomendable

//Caso con números 2
let miNumero2 = 1; //recomendada

//Caso Boolean 1
let miBoolean1 =  new Boolean(false); //formal

//Caso Boolean 2
let miBoolean2 = false; //recomendado

//caso arreglos 1
let miArreglo1 = new Array(); //formal

//caso arreglos 2
let miArreglo2 = []; //recomendado

//caso funcion 1
let miFuncion1 = new function(){}; //todo despues de new es considerado objeto

//caso funcion 2
let miFuncion2 = function(){}; //simplificada y recomendada

//Uso del prototype: a través de él se ingresa una propiedad para todos los objetos que formen parte de la función.
Persona3.prototype.telefono = '265788897';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '453700991800';
console.log(madre.telefono);

//Uso de call: permite llamar un método que está definido en un objeto desde otro objeto
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo,telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
       // return this.nombre+' '+this.apellido;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}
console.log(persona4.nombreCompleto2('Lic.', '684678368437'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '2615256577'));

//Método Apply: este método nos permite a un método que no se encuentra definido en cierto objeto. Apply lee el 
//arreglo y lo está asignando como argumentos.
let arreglo = ['Ing.', '6574362864789'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));
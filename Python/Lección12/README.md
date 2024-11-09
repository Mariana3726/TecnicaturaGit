# Método de Resolución de Métodos (MRO)
### _El Método de Resolución de Métodos (MRO) es un concepto en programación orientada a objetos, especialmente en lenguajes como Python. Se refiere al orden en el que se buscan los métodos (o atributos) en una jerarquía de clases cuando se llama a un método en una instancia de una clase_.
### Cómo funciona?
#### 1. _Búsqueda en la clase actual_: Primero, se busca el método en la clase de la instancia.
#### 2. _Búsqueda en las clases base_: Si no se encuentra en la clase actual, se busca en las clases base en el orden especificado por el MRO.
#### 3. _Orden de herencia_: El MRO respeta el orden de herencia de las clases, asegurando que las clases derivadas se busquen antes que las clases base.
#### > _Puedes ver el MRO de una clase en Python utilizando el atributo __mro__ o la función mro()._ <

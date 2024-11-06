## **HERENCIA MÚLTIPLE**
### _La herencia múltiple en Python permite que una clase herede atributos y métodos de más de una clase base. Esto puede ser útil para combinar funcionalidades de diferentes clases en una sola._
#### > Características Clave
#### Acceso a Múltiples Métodos: La clase derivada puede acceder a los métodos de todas las clases base.
#### Orden de Resolución de Métodos (MRO): Python utiliza un algoritmo llamado C3 Linearization para determinar el orden en que se buscan los métodos. Puedes ver el MRO usando el atributo __mro__ o la función mro().
#### > Ventajas
#### Reutilización de Código: Permite reutilizar código de múltiples clases.
#### Flexibilidad: Facilita la creación de clases con combinaciones específicas de funcionalidades.
#### > Desventajas
#### Complejidad: Puede hacer que el código sea más difícil de entender y mantener.
#### Conflictos de Nombres: Si dos clases base tienen métodos con el mismo nombre, puede haber confusión sobre cuál método se debe usar.

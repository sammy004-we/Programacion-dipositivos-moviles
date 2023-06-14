# •	Selecciona un patrón de diseño y explica su idea 

# Patrón de Diseño Observador (Observer Pattern).
Este patrón es parte de la categoría de patrones de comportamiento y se utiliza para establecer una relación de uno a muchos entre un objeto llamado sujeto y múltiples objetos observadores. El objetivo del patrón de Observador es notificar automáticamente a los observadores cuando ocurren cambios en el sujeto, de modo que puedan actualizar su estado o realizar alguna acción correspondiente.

## Estructura:

Sujeto (Subject): Es el objeto principal que mantiene una lista de observadores y proporciona métodos para agregar, eliminar y notificar a los observadores.
Observador (Observer): Es la interfaz o clase base que define los métodos que deben ser implementados por los observadores. Esto generalmente incluye un método de actualización que se invoca cuando el sujeto experimenta cambios.
Observadores Concretos (Concrete Observers): Son las clases concretas que implementan la interfaz de observador. Cada observador concreto puede tener su propio estado y definir su propia lógica de actualización.
Funcionamiento:

El sujeto mantiene una lista de observadores y proporciona métodos para agregar, eliminar y notificar a los observadores.
Los observadores se registran en el sujeto mediante el método de registro apropiado.
Cuando el sujeto experimenta cambios, notifica a todos los observadores llamando a su método de actualización.
Cada observador concreto implementa su propia lógica de actualización, que puede implicar obtener el nuevo estado del sujeto y realizar acciones basadas en ese estado.
## Beneficios:

Desacoplamiento: El patrón de Observador permite que los sujetos y los observadores sean independientes y no dependan directamente entre sí. Esto facilita la extensibilidad y el mantenimiento del código.
Notificaciones automáticas: Los observadores se actualizan automáticamente cuando se producen cambios en el sujeto, sin necesidad de que el sujeto tenga conocimiento directo de los observadores.
Escalabilidad: El patrón de Observador es escalable, ya que permite tener múltiples observadores registrados para un sujeto y se pueden agregar o eliminar observadores en cualquier momento sin afectar al sujeto o a otros observadores.
## Aplicación:
El patrón de Observador se aplica en situaciones donde hay una dependencia uno a muchos entre objetos, y cuando se desea mantener los objetos desacoplados mientras se asegura que los observadores sean notificados automáticamente de los cambios en el sujeto. Se encuentra comúnmente en aplicaciones de interfaz de usuario, eventos en tiempo real, sistemas de publicación-suscripción y sistemas basados en eventos.

El patrón de Observador permite establecer una relación de uno a muchos entre un sujeto y múltiples observadores. Cuando el sujeto experimenta cambios, notifica automáticamente a los observadores, lo que les permite actualizar su estado o realizar acciones correspondientes. Esto promueve el desacoplamiento y la escalabilidad en el diseño de software.

## **## Patrón de adaptador (Adapter Pattern):**
Este patrón se utiliza para permitir que dos interfaces incompatibles trabajen juntas. Actúa como un puente entre dos clases, convirtiendo la interfaz de una clase en otra interfaz esperada por el cliente.

## Patrón de puente (Bridge Pattern):
Este patrón separa la abstracción de su implementación, permitiendo que ambos evolucionen de manera independiente. Proporciona una estructura más flexible al permitir que una clase tenga varias implementaciones y pueda cambiarlas en tiempo de ejecución.

## Patrón de decorador (Decorator Pattern):
El patrón de decorador permite agregar funcionalidad adicional a un objeto de forma dinámica. Se envuelve el objeto original en una serie de decoradores que proporcionan características adicionales sin modificar la estructura básica del objeto.

## Patrón de fachada (Facade Pattern):
Este patrón proporciona una interfaz unificada y simplificada a un conjunto de interfaces más complejas y subsistemas. Actúa como un punto de entrada único para acceder a las funcionalidades del subsistema, ocultando su complejidad y facilitando su uso.


# •	Patrones de diseño - Hooks vs HOC

Los patrones de diseño Hooks y HOC (Higher-Order Components) son dos enfoques utilizados en React para reutilizar la lógica y la funcionalidad en los componentes. Aquí tienes una comparación entre ambos:

## Hooks:

Los Hooks son una característica introducida en React a partir de la versión 16.8.
Permiten agregar estado y otras características de React a los componentes funcionales, que originalmente solo podían ser componentes sin estado.
Los Hooks se implementan como funciones especiales que se llaman dentro de los componentes funcionales.
Algunos ejemplos de Hooks son useState para el manejo del estado local, useEffect para el manejo de efectos secundarios y useContext para acceder al contexto.
Los Hooks ofrecen una sintaxis más concisa y clara en comparación con los componentes de clase.
Permiten una mejor separación de la lógica y la presentación en los componentes, lo que facilita la reutilización y el testing.

## HOC (Higher-Order Components):

Los HOC son una técnica de composición utilizada en React desde antes de la introducción de los Hooks.
Un HOC es una función que recibe un componente y devuelve un nuevo componente con funcionalidad adicional.
Los HOC envuelven componentes existentes para agregarles características y comportamiento adicionales.
Los HOC pueden compartir lógica entre múltiples componentes, lo que permite la reutilización de esa lógica en diferentes partes de la aplicación.
Algunos ejemplos populares de HOC son withRouter para acceder a las propiedades de enrutamiento, connect para conectar componentes a un store de Redux y memo para optimizar la renderización de componentes.
En general, tanto los Hooks como los HOC tienen como objetivo principal facilitar la reutilización de la lógica y mejorar la modularidad de los componentes en React. Los Hooks se enfocan más en proporcionar una sintaxis más simple y directa para trabajar con el estado y los efectos, mientras que los HOC se basan en la composición de componentes existentes para agregar funcionalidad adicional.


# Redux y Context 
Son dos enfoques diferentes para manejar el estado en aplicaciones React. A continuación:

## Redux:
Redux es una biblioteca de administración de estado predecible para aplicaciones JavaScript, y es ampliamente utilizado en el desarrollo de aplicaciones React. Sigue el patrón de diseño Flux y se basa en tres conceptos fundamentales: el store, las acciones y los reducers.
Store: Es un objeto que almacena el estado global de la aplicación. Solo puede ser modificado mediante acciones.
Acciones: Son objetos que describen un cambio en el estado de la aplicación. Deben tener un tipo definido y pueden llevar datos adicionales.
Reducers: Son funciones puras que especifican cómo debe cambiar el estado de la aplicación en respuesta a una acción. Reciben el estado actual y una acción, y devuelven un nuevo estado.
Redux promueve la idea de un flujo unidireccional de datos, lo que facilita el seguimiento y la depuración del estado de la aplicación. Además, al mantener el estado centralizado en el store, es más fácil compartir datos entre componentes y mantener un estado consistente en toda la aplicación.

## Context:
Context es una característica de React que permite pasar datos a través del árbol de componentes sin tener que pasar explícitamente las propiedades a cada nivel. Proporciona una forma de compartir información entre componentes sin necesidad de usar una "prop drilling" (pasar props a través de múltiples niveles de componentes).
El contexto consta de dos partes principales: el Provider y el Consumer.

Provider: Es un componente que envuelve una parte del árbol de componentes y permite que los componentes secundarios accedan a los datos proporcionados a través del contexto.
Consumer: Es un componente que permite a los componentes secundarios consumir los datos proporcionados por el Provider.
El Context es útil cuando se tiene un estado compartido que necesita ser accesible desde diferentes partes de la aplicación, pero no es recomendado para compartir grandes cantidades de datos o para casos en los que el estado se actualiza con frecuencia. En esos casos, Redux suele ser una opción más adecuada debido a su capacidad para manejar de manera eficiente actualizaciones de estado complejas.

Redux es una biblioteca de administración de estado predecible que utiliza un store centralizado y sigue el patrón Flux, mientras que Context es una característica de React que permite compartir datos a través del árbol de componentes sin necesidad de pasar props manualmente. Ambos enfoques son útiles en diferentes situaciones, dependiendo de la complejidad y las necesidades de la aplicación.

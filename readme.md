# Examen de Jesús Fernando Almanza Loredo

## Problemas 1 y 2 de algoritmos
Para ejecutar el proyecto, se tiene que tener instalado Python 3 o superior en el sistema. Ya teniendo instalado 
Python, se ejecuta el siguiente comando en la raiz del proyecto:

``python3 ./main.py``

Al ejecutarse, se tiene que desplegar un menú con 2 opciones que corresponden a los problemas que aparecen en el 
apartado de algoritmos.

## Patrones de diseño

### Problema 1
Considero conveniente usar el patron Strategy y Adapter

Strategy ofrece la ventaja de poder separar las variaciones del algoritmo original que en este caso seria el adaptador.

Se pueden crear estrategias del adaptador para lograr sortear la desventaja que tiene el 
patron adapter (dupilcación de codigo) y aprovechar que ese patron permite usar multiples servicios sin tener que usar condicionales.

### Problema 2
La diferencia entre Factory Method y Abstract Factory es que Factory Method se implementa con herencia y polimorfismo
y en cuanto al Abstract Factory se implementa usando interfaces

### Ejemplo de Factory Method

```
// Clase padre
import ...

class Padre{
    private atributo
    
    constructor(Atributo atributo){
        this.atributo = atributo
    }
    
    protected Metodo(): string{
        return this.atributo
    }
}

// Clase hija
import Padre from './padre'
import ...

class Hija extends Padre{
    constructor(Atributo atributo){
        super(atributo)
    }

    protected Metodo(): string{
        this.atributo = this.atributo.toUpperCase()
        return this.atributo
    }
}
```

### Ejemplo de Abstract Method
```
//Interfaz
export interface InterfazAbstracto{
    Foo metodo1(a, b)
    Bar metodo2(c, d)
}

// Implementado en otro lado
import InterfazAbstracto from './interfaz.abstracto'

class Clase{
    InterfazAbstracto fabrica
    
    constructor(InterfazAbstracto fabrica){
        this.fabrica = fabrica
    }
    
    public prueba(): null{
        Foo metodo1 = this.fabrica.metodo1
        metodo1(2, 1)
    }
}
```
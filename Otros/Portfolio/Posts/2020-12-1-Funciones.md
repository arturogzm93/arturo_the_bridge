---
layout: article
title: Funciones
categories: articles
---

En este Notebook tienes una guía completa para orientarte en el uso de funciones en Python.

Se trata de bloques de código que encapsulan una serie de operaciones. Se usan para modular nuestro código y evitar escribir código de más.

1. [Definición, sintaxis y return](#1.-Definición,-sintaxis-y-return)
2. [Argumentos posicionales](#2.-Argumentos-posicionales)
3. [Argumentos variables](#3.-Argumentos-variables)
4. [Argumentos keyword](#4.-Argumentos-keyword)
5. [Recursividad](#5.-Recursividad)
6. [Documentar funciones](#6.-Documentar-funciones)
7. [Resumen](#7.-Resumen)

## 1. Definición, sintaxis y return
Mediante las **funciones** podemos encapsular código en formato entrada/salida. Por lo que si tienes un código repetitivo, que depende de ciertos inputs, las funciones pueden ser una buena solución.

Es una manera de agrupar conjuntos de operaciones en módulos. **¿Cuándo usarlas?** Cuando tengamos varias operaciones que ejecutamos repetidamente en distintas partes del código. En ese caso, encapsulamos las operaciones en una función, y cada vez que haya que realizar tal operativa, llamamos a la función, y en una sola línea de código tenemos ejecutada esas operaciones.

Hasta ahora hemos estado utilizando funciones *built-in*, para operaciones sencillas como `len()`, `sum()` o `max()`. En este Notebook aprenderas a crear tus propias funciones.

La sintaxis es:
> ```Python
> def nombre_funcion(input):
>    operaciones varias
>    return output
> ```

Fíjate que sigue la **sintaxis de línea** vista en Notebooks anteriores. Además, todo lo que va después del `return` es ignorado, puesto que es la salida. En el `return` acaba la función. Ahora bien, eso no quiere decir que haya un único return. Si introducimos una sentencia `if/else`, podremos poner returns diferentes dependiendo de qué condición se cumpla. Vamos a crear nuestra primera función
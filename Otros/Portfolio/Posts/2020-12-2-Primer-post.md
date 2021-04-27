---
layout: article
title: Python - Flujos de control
categories: articles
modified: 2014-08-27
image:
  teaser: code.jpg
---

Hasta ahora hemos visto cómo ejecutar un programa secuencialmente, empieza en la primera línea y acaba en la última. Pero ¿y si queremos que cambien los outputs del programa en función de ciertas condiciones, o si queremos que tome otros caminos en caso de encontrar errores?. Todo esto lo podremos hacer con los flujos de control. Sentencias que encontrarás en todos los lenguajes de programación.

1. [Sintaxis de línea](#1.-Sintaxis-de-línea)
1. [if/elif/else](#2.-if/elif/else)
2. [Bucle for](#3.-Bucle-for)
3. [Bucle while](#4.-Bucle-while)
4. [Break/continue](#5.-Break/continue)
5. [Try/except](#6.-Try/except)
10. [Resumen](#7.-Resumen)


## 1. Sintaxis de línea
La manera en la que Python encapsula todo el código que va dentro de un flujo de control como `if` o `for` es diferente a como se suele hacer en otros lenguajes, en los que se rodea de llaves `{}` o paréntesis `()` todo el contenido del flujo. Con Python no. En Python simplemente hay que añadir una tabulación a cada línea de código que vaya dentro del flujo de control.

> ```Python
> for condiciones:
>     Código dentro de este bucle
> ```


Si lo dejamos fuera, este código se ejecutará secuencialmente después de que corra el for

> ```Python
> for condiciones:
>
> Código fuera de este bucle
> ```

Veamos un ejemplo. Tenemos una lista de numeros, y queremos ver cuáles son enteros. Para ello los recorremos con un `for` (vermos más en profundiad en este notebook). Vamos iternando uno a uno cada elemento. Luego mediante un `if` comprobamos si es entero. Fíjate que todo lo que va dentro del `for` lleva una tabulación y lo que va dentro del `if` lleva dos tabulaciones, puesto que sus sentencias van tanto dentro del `if`, como dentro del `for`.


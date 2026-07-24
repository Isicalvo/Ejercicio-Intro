## Introducción
Ayuda a Odiseo a volver a casa!
Odiseo lleva muchos años intentando volver a casa, pero cada vez le pasa algo! En esta ocasión se encuentra con la hechicera Circe, a quien debe ganar con estrategia e ingenio. Para esto Hermes te a ha dado la oportunidad de crear un monstruo que pelee contra ella, el cual debe usar los ataques correctos con el poder suficiente para derrotar a circe pero solo 1 unidad más alto para no agotar tu poder. Para realizar esta hasaña, necesitarás crear la clase monstruo.

## Objetivo

La clase monstruo debe tener los siguientes requisitos:

Cualidades
Al crear al monstruo hay que entregarle un nombre.
El monstruo al crearse tiene un nivel de magia de 100, con cada ataque que se hace debe disminuir la magia en el nivel del ataque con el que respondiste.
Al preguntarle a todo mostruo de esta clase como se llama, este responderá "RAAAWR, soy {nombre}".

HABILIDADES

luchar: Al recibir un tipo de ataque (AGUA, FUEGO, PLANTA) con un número entero que indicará el nivel del ataque recibido. El monstruo deberá responder con un ataque que tenga un nivel +1 al ataque recibido y debe ser de un tipo que venza al recibido (AGUA vence a FUEGO, FUEGO vence a PLANTA y PLANTA vence a FUEGO). Responderás con un string que indique el tipo de ataque y su nivel. EJEMPLO: Si recibes "FUEGO 12" debes retornar "AGUA 13", y restar 13 a la cantidad de magia.
En el caso de quedarse sin magia suficiente para el ataque, usa toda la restante.

derrota:el monstruo retornará una frase "Nadie... lo lamento X o X"

## Ejemplo
#### Input
PLANTA 12 \n
AGUA 7 \n
FUEGO 20 \n
FUEGO 56 \n
PLANTA 9 \n
#### Output
RAAAWR, soy PEDRO \n
FUEGO 13 \n
PLANTA 8 \n
Quedan 79 puntos de magia \n
AGUA 21 \n
AGUA 57 \n
Quedan 1 puntos de magia \n
FUEGO 1 \n
Nadie... lo lamento X o X \n
Aquí Odiseo le puso PEDRO al monstruo y habló con él. Cada 2 ataques revisó el nivel de magia restante. Cuando le quedaba 1 punto de magia recibió un ataque de PLANTA 9, al cual solo pudo responder con FUEGO 1 justo antes de rendirse. 
Solo debes preocuparte de crear la clase con las cualidades y habilidades descritas, nosotros nos encargamos de la impresión.

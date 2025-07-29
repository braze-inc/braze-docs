---
nav_title: División de decisiones 
article_title: División de decisiones 
alias: /decision_split/
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo crear y utilizar divisiones de decisión en el lienzo."
tool: Canvas

---

# División de decisiones 

> El componente Decision Split de Canvas le permite ofrecer experiencias personalizadas y en tiempo real a sus usuarios.



Este componente puede utilizarse para crear ramas Canvas en función de si un usuario coincide con una consulta.

## Crea una división de decisiones 

 

### Define tu división

¿Cómo quiere dividir a sus usuarios?  Básicamente, está creando una consulta en `true` o `false` que evaluará a sus usuarios y luego los dirigirá a un paso u otro. Debe utilizar al menos un segmento o un filtro. No es necesario utilizar a la vez un segmento y un filtro.



{% alert note %}

{% endalert %} 

## Utiliza tu división

Utilizar una división por decisión puede ayudarte a distinguir las rutas de tus usuarios en función de su segmento o sus atributos, ¡incluso si utilizan determinados canales de mensajería para recibir tus mensajes!

Supongamos que está creando un flujo de incorporación. Puede empezar con un correo electrónico de bienvenida al registrarse. Luego, dos días después, quieres enviar un mensaje push, pero solo a los usuarios habilitados para push. Después, todos los usuarios reciben otro correo electrónico tres días después de haberse inscrito. También puede utilizar su división de decisiones para enviar un mensaje dentro de la aplicación a los usuarios que no tienen activada la función push para animarles a activarla.

Si no hay ningún paso siguiendo uno de los caminos, los usuarios que vayan por ese camino saldrán del Canvas. 

  

## Análisis

Consulte la tabla siguiente para ver las descripciones de los análisis de este paso:

| Métrica | Descripción |
|---|---|
|  | El número total de veces que se ha introducido el paso. Si su Canvas tiene re-elegibilidad y un usuario introduce un paso de División de Decisión dos veces, se registrarán dos entradas. |
|  | Número de entradas que cumplen los criterios especificados y han seguido el camino "sí". |
|  | El número de entradas que no cumplieron los criterios especificados y siguieron la ruta "no". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


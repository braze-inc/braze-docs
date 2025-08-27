---
nav_title: Contexto 
article_title: Contexto 
alias: /context/
page_order: 1.5
page_type: reference
description: "Este artículo de referencia explica cómo crear y utilizar pasos en Canvas."
tool: Canvas

---

# Contexto

> Utiliza los pasos de Contexto para crear o actualizar un conjunto de variables que representen el contexto de un usuario (o información sobre el comportamiento de ese usuario) a medida que se desplaza por un Canvas. Cada variable contextual incluye un nombre, un tipo de datos y un valor que puede incluir Liquid. Configurando el contexto como parte de tu recorrido de usuario, puedes hacer cosas como retrasar mensajes o filtrar usuarios en función de variables de contexto.

{% alert important %}
Los pasos del contexto están actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Cómo funciona

Cada paso en Canvas está compuesto por un nombre de variable y un tipo de datos asociado, o variables de contexto (antes denominadas propiedades de entrada en Canvas). Estas variables seguirán a un usuario a través de un Canvas y se puede acceder a ellas utilizando el Líquido `context`.

![Un paso de Contexto como primer paso de un Canvas.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Hay dos formas de establecer variables de contexto:

- **A la entrada de Canvas:** Las variables de eventos o llamadas a la API que desencadenan la entrada de un usuario en un Canvas se almacenan como variable de contexto.
- **Utilizando un paso de Contexto:** Puedes crear o actualizar variables contextuales en el editor de pasos.

Ten en cuenta que las variables incluidas en la variable de contexto no se almacenan automáticamente en el perfil de usuario.

## Crear un paso Contexto

Para crear un paso de Contexto, añade un paso a tu Canvas. A continuación, arrastra y suelta el componente desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **Contexto**.

### Definir variables de contexto

1. Dale un nombre a tu variable Contexto.
2. Selecciona un tipo de datos.
3. Introduce una expresión de Liquid o selecciona el botón **Añadir personalización**. Esto genera un fragmento de código Liquid para utilizarlo en tu expresión Liquid.
4. Selecciona **Vista previa** para ver la variable de contexto.
5. Selecciona **Hecho** para guardar el paso.

Puedes utilizar variables de Contexto en cualquier lugar donde puedas utilizar Liquid, como en los pasos de Actualización de mensajes y usuarios, con el botón **Añadir personalización**.

## Tipos de variables de contexto

Se pueden asignar tipos a las variables de contexto del Canvas que se creen o actualicen en el paso. Ten en cuenta que si la expresión Liquid en tiempo de ejecución devuelve un valor que no coincide con el tipo, la variable de contexto no se actualizará.

Por ejemplo, si el tipo de datos de la variable de contexto se establece en **Fecha**, pero el valor no es una fecha, la variable no se actualizará. Esto significa que ocurrirá lo siguiente

- El usuario avanzará al siguiente paso o saldrá del Canvas si es el último paso del Canvas.
- En tu análisis de pasos en Canvas, esto se contará como *No actualizado*.

Braze saldrá de un usuario en el paso si:

- La variable de contexto no devuelve ningún valor.
- Falla una llamada a un Contenido conectado incrustado.
- Los tipos de variables de contexto no coinciden.

### Tipos JSON y respuestas de contenido conectado

Braze evalúa las variables de contexto que se espera que sean de tipo JSON (u Objeto) de las respuestas de Contenido conectado en cadenas. Para evitar que las variables de contexto se evalúen como cadenas, introduce estos resultados en este filtro Liquid: `as_json_string`. Un ejemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Utilizar variables de contexto con pasos de Retraso

Puedes añadir [opciones de retraso personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) con la información del paso Contexto, lo que significa que puedes seleccionar la variable que retrasa a los usuarios.

[1]: {% image_buster /assets/img/context_step3.png %}

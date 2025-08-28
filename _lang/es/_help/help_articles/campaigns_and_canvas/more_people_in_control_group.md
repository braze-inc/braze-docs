---
nav_title: Manejar un gran grupo de control
article_title: Manejar un gran grupo de control
page_order: 2

page_type: solution
description: "Este artículo de ayuda describe por qué tu grupo de control puede ser mayor de lo esperado, y te guía por los pasos para solucionarlo."
tool: Canvas
---

# Manejar un gran grupo de control

Al crear tu Canvas, puede que esperases que tu audiencia se dividiera a partes iguales entre tu grupo de control y tu grupo de variantes, como en el siguiente [ejemplo](#example). Podemos explicarte por qué y cómo solucionarlo.

El grupo al que se une un usuario depende de su configuración. Puede ser el grupo de control o el grupo variante. Un usuario entrará en un Canvas cuando cumpla todos tus criterios definidos en el [Paso de entrada]({{site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-use-the-entry-wizard-to-set-up-your-canvas). Cuando configures tu Canvas, define qué porcentaje de usuarios entrará en cada variante y el grupo de control.

Si tu grupo de control es grande en comparación con tu grupo de variantes (y ésta no es tu intención), te recomendamos lo siguiente:
1. Configura tu filtro de audiencia de entrada como "Está habilitado el push".
2. Establece el filtro de audiencia de entrada en "está adherido o suscrito".

Al crear un Canvas con un grupo de control, asegúrate de que todos los usuarios de la audiencia de entrada puedan recibir mensajes dentro del Canvas (por ejemplo, que el Canvas contenga mensajes push y por correo electrónico).

## Casos de uso

Imaginemos el siguiente escenario:
- Un Canvas tiene una única variante y un grupo de control.
- El primer paso de la variante es una notificación push.
- El 90 % de los usuarios fueron seleccionados para entrar en la variante, y el 10 %, para entrar en el grupo de control.

![Ejemplo de Canvas]({% image_buster /assets/img_archive/trouble15.png %})

En este caso, el 90% de los usuarios que entren en el Canvas entrarán en la variante. 

Si repasamos los usuarios activos, podemos ver que, aunque contiene 39 800 usuarios, solo el 73 % de ellos tienen habilitación push:

![Audiencia de entrada]({% image_buster /assets/img_archive/trouble16.png %})

Esto significa que, aunque hayamos especificado que el 90% de los usuarios introduzcan la variante, no todos esos usuarios pueden recibir realmente una notificación push. Estos usuarios que no pueden recibir una notificación push seguirán entrando en la variante a pesar de todo.

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

_Última actualización el 3 de diciembre de 2020_


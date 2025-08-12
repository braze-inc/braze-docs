---
nav_title: Lógica de segmentación
article_title: Lógica de segmentación 
page_order: 3

page_type: solution
description: "Este artículo de ayuda te explica las diferencias entre los operadores Y y O, y cómo puedes utilizarlos para crear segmentos potentes."
tool: Segments
---

# Lógica de segmentación 

Los operadores `AND` y `OR` habilitan un potente filtrado al [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). Utilizando estos operadores, puedes dirigirte a tus usuarios en función de sus acciones o comportamientos en el paso **Audiencia** objetivo de la construcción de tus campañas o Lienzos.

## Comprender los operadores AND y OR

Los operadores `AND` y `OR` funcionan de forma diferente. Puedes utilizar cada operador en función de lo que quieras conseguir al segmentar tu audiencia. 

### Cuándo utilizar el operador AND

En general, utiliza `AND` si te interesa la intersección de dos o más valores de un atributo concreto.

Veamos cómo dirigir una campaña a usuarios de todos los países excepto Canadá y Estados Unidos. En este caso, utilizar el operador `AND` puede ayudar a filtrar a estos usuarios. La declaración `Country is not United States AND Country is not Canada` sólo incluirá a los usuarios que no sean de Estados Unidos ni de Canadá. Por tanto, utilizando esta lógica, tanto los usuarios de Canadá como los de Estados Unidos quedarán excluidos.

### Cuándo utilizar el operador OR

Utiliza `OR` si tu objetivo es dirigirte a usuarios que cumplan al menos una condición de un conjunto de condiciones. Si tienes tres condiciones unidas por `OR`, entonces una, dos o todas las condiciones pueden ser verdaderas para que la afirmación real sea verdadera.

Por ejemplo, imagina que quieres enviar un mensaje a todos tus usuarios de la versión 1.0 o 1.1 de tu aplicación. Para dirigirte a los usuarios que están en la versión 1.0 y en la versión 1.1, puedes utilizar los filtros `Is 1.0` y `Is 1.1` con el operador `OR` en tu segmento. Esto se dirigirá a todos los usuarios que estén en las versiones 1.0 o 1.1.

En el siguiente ejemplo, considera una promoción válida tanto para usuarios de Estados Unidos como de Canadá. Quieres asegurarte de que sólo los usuarios de las zonas donde la promoción es válida reciben la promoción. En este caso, utiliza la siguiente frase para orientar tu campaña: `Country is United States OR Country is Canada`. Con el operador `OR`, tu campaña sólo llegaría a los usuarios cuyo país sea Canadá o cuyo país sea Estados Unidos.

#### Cuándo evitar el operador OR

Puede haber situaciones de selección de usuarios en las que deba evitarse utilizar el operador `OR`. El operador `OR` crea una sentencia que se evalúa como verdadera si un usuario cumple los criterios de uno o varios de los filtros de una sentencia. Por ejemplo, si quieres crear un segmento de usuarios que pertenezcan a "amantes de la comida" pero que no pertenezcan ni a "no amantes de la comida" ni a "amantes de los dulces", en este caso funcionaría el operador `OR`.

![]({% image_buster /assets/img_archive/or_operator_segment.png %})

Sin embargo, si tu objetivo es segmentar a los usuarios que pertenecen al segmento "amantes de la comida" y no están en ninguno de los segmentos "no amantes de la comida" y "amantes de los dulces", utiliza el operador `AND`. De este modo, los usuarios que reciben la campaña o el Canvas están en el segmento previsto ("foodies") y no en los otros segmentos ("non-foodies" y "candy-lovers") al mismo tiempo. 

Los siguientes criterios negativos de selección no deben utilizarse con el operador `OR` cuando dos o más filtros hagan referencia al mismo atributo:

- `is not`
- `does not equal`
- `does not match regex`

Si `is not`, `does not equal`, o `does not match regex` se utilizan con el operador `OR` dos o más veces en una frase, se seleccionarán los usuarios con todos los valores del atributo correspondiente.

### Utilizando ambos operadores

En el siguiente ejemplo, utilizaremos los operadores `AND` y `OR`. En este caso, la audiencia objetivo incluye a los usuarios que compraron zapatillas Nike o Adidas, y optaron por recibir notificaciones por correo electrónico.

![Crear un segmento de compradores de zapatillas en el que la marca favorita del usuario sea Nike o Adidas, y éste haya optado por la adhesión voluntaria al correo electrónico]({% image_buster /assets/img_archive/NikeSneakers.png %})

Otra forma de asegurarte de que estás construyendo la lógica correcta es crear tu segmento y [tener una vista previa de los usuarios]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/) que entran en él en función de tus filtros. De este modo puedes asegurarte de que sus atributos, versión de la aplicación o cualquier otra segmentación coincide con lo que estás viendo.

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

_Última actualización: 3 de junio de 2022_


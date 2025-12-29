---
nav_title: Convenciones para nombrar eventos
article_title: Convenciones para nombrar eventos
page_order: 10
page_type: reference
description: "Este artículo de referencia cubre las convenciones de denominación de eventos adecuadas y las mejores prácticas."

---

# Convenciones para nombrar eventos

> Esta página trata de las convenciones adecuadas para nombrar los eventos y de las mejores prácticas. Al mantener la coherencia en tu taxonomía de eventos y atributos, mantendrás tus datos limpios y utilizables para los usuarios nuevos y existentes de la plataforma Braze. Esto ayuda a evitar problemas posteriores, como desencadenar una campaña a la audiencia equivocada o generar resultados erróneos tras utilizar el evento equivocado.

## Buenas prácticas

- Mantén clara tu convención de nombres.
- Usa mayúsculas y minúsculas y un formato coherente para los nombres de los eventos.
- Evita dar nombres similares a los actos.
- Evita las cadenas largas de atributos de eventos, que se truncarán o cortarán en el panel de Braze.

## Convenciones de denominación

### Utilizar grupos de eventos

Utiliza grupos para diferenciar partes de tu producto para nombrar eventos. Al categorizar tu producto en grupos, cualquier usuario puede entender claramente a qué se refiere y qué hace.

### Estructura de nombres de los eventos

La estructura de nombres más común es `group_noun_action`. Los eventos deben ir todos en minúsculas para evitar errores de instrumentación y propiedades identificadoras.

### Propiedades

Etiqueta un evento y luego identifica las diferencias utilizando las propiedades. Esto es útil para eventos que son intrínsecamente iguales pero tienen pequeñas diferencias, como los canales de una campaña. También podemos ver fácilmente cómo fluyen los usuarios a través de los eventos. Consulta el [objeto propiedades del evento]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) para ver un ejemplo y contexto adicional.

## Ejemplos

Supongamos que formas parte de una empresa de comercio electrónico y te interesa hacer un seguimiento de cuándo los clientes se han registrado en tu aplicación y cuándo se han suscrito a tu boletín de noticias. Aquí tienes ejemplos de nombres de eventos eficaces:

- `user_signup`
- `newsletter_subscribed`

Estos dos nombres de evento indican claramente el evento que están siguiendo. A medida que crees más eventos personalizados, asegúrate de que tus convenciones de nomenclatura sean comprensibles. Por ejemplo, evita utilizar nombres de eventos como `signup_event_1`, ya que carece de claridad y no transmite lo que el evento está siguiendo, en comparación con `user_signup`.

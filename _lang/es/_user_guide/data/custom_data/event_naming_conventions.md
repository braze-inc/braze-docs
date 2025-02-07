---
nav_title: Convenciones para nombrar eventos
article_title: Convenciones para nombrar eventos
page_order: 10
page_type: reference
description: "Este artículo de referencia cubre las convenciones de nomenclatura de eventos adecuadas y las mejores prácticas."

---

# Convenciones de nomenclatura de eventos

> Esta página trata de las convenciones adecuadas para nombrar los eventos y de las mejores prácticas. Al mantener la coherencia en tu taxonomía de eventos y atributos, mantendrás tus datos limpios y utilizables para los usuarios nuevos y existentes de la plataforma Braze. Esto ayuda a evitar problemas posteriores, como desencadenar una campaña a la audiencia equivocada o generar resultados erróneos tras utilizar el evento equivocado.

## Buenas prácticas

- Mantén clara tu convención de nomenclatura.
- Los nombres de los eventos deben escribirse y formatearse con coherencia.
- Evita dar nombres similares a los eventos.
- Evite las cadenas largas de atributos de eventos, que se truncarán o cortarán en el cuadro de mandos de Braze.

## Convenciones de denominación

### Utilizar grupos de eventos

Utilice grupos para diferenciar las partes de su producto para nombrar eventos. Al categorizar su producto en grupos, cualquier usuario puede entender claramente a qué se refiere el evento y qué hace.

### Estructura de nomenclatura de eventos

La estructura de nombres más común es `group_noun_action`. Los eventos deben ir todos en minúsculas para evitar errores de instrumentación e identificación de propiedades.

### Propiedades

Etiquete un evento y luego identifique las diferencias mediante el uso de propiedades. Esto es útil para eventos que son intrínsecamente iguales pero tienen pequeñas diferencias, como los canales de una campaña. También podemos ver fácilmente cómo fluyen los usuarios a través de los eventos. Consulte el [objeto de propiedades de eventos]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) para ver un ejemplo y contexto adicional.

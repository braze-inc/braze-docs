---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la administración de datos personalizados
page_order: 1
page_type: FAQ
description: "Esta página ofrece respuestas a preguntas frecuentes sobre la gestión de datos personalizados en Braze."
---

# Preguntas más frecuentes

> Esta página ofrece respuestas a algunas preguntas frecuentes sobre la administración de datos personalizados.

### ¿Por qué tu atributo personalizado se detecta como un tipo de datos diferente en producción que en desarrollo?

Braze detecta automáticamente el tipo de datos de un atributo personalizado basándose en el primer valor que recibe. Si tu entorno de desarrollo envía primero un valor `100`numérico, el atributo se almacena como un número. Si el primer valor de tu entorno de producción llega como una cadena (por ejemplo,`"100"`entre comillas), el atributo se almacena como una cadena.

Para evitarlo, asegúrate de que tu integración envíe tipos de datos coherentes en todos los entornos. Si ya se ha establecido un tipo incorrecto, puedes forzar el tipo de datos correcto en **Configuración de datos** > **Atributos personalizados** utilizando el [menú desplegable de tipos de datos]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#forcing-data-type-comparisons).

### Si fuerzas un cambio de tipo de datos en un atributo personalizado, ¿se convertirán los datos existentes?

No. Forzar un cambio en el tipo de datos solo afecta a los nuevos datos que entran en Braze. La ingesta de datos antes del cambio de tipo seguirá almacenándose como el tipo anterior y es posible que no se pueda realizar la segmentación con los filtros del nuevo tipo. Aparece una advertencia en los perfiles de usuario afectados. Para los nuevos datos entrantes, si un valor no coincide con el tipo forzado, Braze puede convertirlo al tipo forzado (por ejemplo, la cadena`"100"`  al número `100`); los valores que no se pueden convertir se ignoran y no actualizan el atributo.

Si necesitas que todos los datos de usuario existentes coincidan con el nuevo tipo, debes volver a enviar los valores de los atributos de esos usuarios a través del SDK, la API o una importación CSV. No existe una conversión automática masiva para los datos existentes.

### ¿Cómo puedes evitar problemas con los tipos de datos al utilizar la ingesta de datos de Cloud (CDI)?

Cuando utilices CDI para sincronizar datos de fuentes externas (como Databricks o Snowflake), asegúrate de que las columnas de origen utilicen los tipos de datos correctos antes de realizar la sincronización. Entre los problemas más comunes se incluyen:

- **Marcas de tiempo almacenadas como cadenas**: Asegúrate de que las columnas de fecha utilicen un tipo de marca de tiempo o fecha y hora en la base de datos de origen, y no un tipo varchar o cadena.
- **Números almacenados como cadenas**: Convierte las columnas numéricas a tipos enteros o flotantes en tu consulta de origen antes de sincronizar.
- **Tipos inconsistentes entre sincronizaciones**: Si el tipo de columna cambia entre sincronizaciones, Braze puede rechazar los nuevos datos. Verifica que tu esquema de origen siga siendo coherente.

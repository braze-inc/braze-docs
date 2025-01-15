---
nav_title: Supera a
article_title: Supera a
alias: /partners/outgrow/
description: "Este artículo proporciona una guía completa sobre la configuración de una integración nativa entre Outgrow y Braze para mejorar la sincronización de datos de usuario y las campañas personalizadas."
page_type: partner
search_tag: Partner
---

# Supera a

> [Outgrow](https://outgrow.co/) es una plataforma de contenido interactivo que te permite crear cuestionarios, calculadoras, encuestas y otros tipos de contenido atractivo para recopilar datos de usuario e información. La integración de Braze y Outgrow te permite transferir automáticamente los datos de usuario de Outgrow a Braze, habilitando campañas altamente personalizadas y dirigidas.

Cuando utilizas la integración de Braze y Outgrow para contenidos interactivos, las ventajas que obtienes incluyen:

- **Personalización mejorada**: Recopila datos de cuestionarios, encuestas y calculadoras de Outgrow que puedan mapearse a atributos personalizados en Braze. Estos datos permiten una segmentación precisa y campañas personalizadas.
- **Sincronización de datos en tiempo real**: Recibe datos de Outgrow en Braze en tiempo real, lo que te permitirá actuar de inmediato sobre la información de los usuarios. Esto permite un seguimiento puntual o mensajes personalizados basados en las interacciones más recientes de los usuarios.
- **Gestión de datos racionalizada**: Automatiza la transferencia de datos entre Outgrow y Braze, eliminando las exportaciones e importaciones manuales de datos, reduciendo las discrepancias de datos y ahorrando tiempo.
- **Mejora de la experiencia del usuario**: Aprovecha la información de los usuarios para crear experiencias más relevantes, que conduzcan a una mayor satisfacción, retención y valor de duración del ciclo de vida.
- **Orientación y segmentación flexibles**: Perfecciona la segmentación en Braze utilizando los datos de Outgrow, lo que te permite dirigirte a los usuarios en función de interacciones específicas (como las puntuaciones de los cuestionarios o las respuestas a los cuestionarios) para crear campañas que resuenen entre tus usuarios.

## Requisitos previos

Antes de configurar la integración de Outgrow y Braze, confirma que tienes lo siguiente:

| Requisito | Descripción |
|-------------|-------------|
| **Superar la cuenta** | Una cuenta Outgrow registrada para configurar y administrar la configuración del contenido interactivo y la transferencia de datos |
| **Cuenta Braze** | Una cuenta Braze con acceso a las credenciales de la API REST |
| **Clave de API** | Una clave de API de Braze con el permiso `users.track` para habilitar la transferencia de datos de usuario |
| **Atributos personalizados en Braze** | Atributos personalizados configurados en Braze para captar las respuestas de Outgrow (como puntuaciones de cuestionarios, segmentos y otros) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Sigue estos pasos para configurar la integración de Braze y Outgrow:

### Paso 1: Generar clave de API Braze

1. En tu cuenta Braze, ve a **Consola para desarrolladores** > **Configuración de API**.
2. Selecciona **Crear nueva clave de API**.
3. Pon un nombre a tu clave de API, activa el permiso `users.track` y guarda la clave de API.

### Paso 2: Configura la integración Braze en Outgrow

1. Accede a tu cuenta de Outgrow.
2. En el panel, ve a **Integraciones**.
3. En la lista de integraciones disponibles, selecciona **Braze**.
4. Introduce tu **clave de API Braze** y **la URL del punto final de la API REST**:
   - **Clave de API**: Introduce la clave de API que se generó en Braze
   - **URL del punto final REST**: Introduce el punto final de tu instancia de Braze (por ejemplo, `https://rest.iad-01.braze.com`)
5. Selecciona **Guardar** para activar la integración.

### Paso 3: Mapear datos Outgrow a atributos Braze

En Outgrow, puedes mapear respuestas de contenido interactivo (como resultados de cuestionarios, segmentos personalizados o puntuaciones de interacción) con atributos personalizados de Braze.

1. En la **configuración de integración** de Outgrow para Braze, define qué respuestas de Outgrow mapear a atributos de Braze.
2. Asegúrate de que cada respuesta seleccionada se alinea con un atributo personalizado en Braze. Por ejemplo:
   - La puntuación del cuestionario está mapeada en `outgrow_quiz_score`.
   - Mapeados de segmentos personalizados a `outgrow_custom_segment`.
3. Guarda tu configuración de mapeado.

### Paso 4: Prueba la integración

Tras configurar la integración, realiza una prueba para confirmar que los datos se transfieren correctamente de Outgrow a Braze.

1. Publica una experiencia Outgrow (como un cuestionario o una calculadora) y complétala como usuario de prueba.
2. En tu cuenta Braze, ve a la sección **Perfil de usuario** y comprueba si hay atributos actualizados (como `outgrow_quiz_score` o `outgrow_custom_segment`).
3. Comprueba que los datos se rellenan correctamente con los atributos personalizados adecuados.

## Utilización de los datos de Outgrow en Braze para la segmentación y la selección de objetivos

### Creación de segmentos en Braze con datos de Outgrow

Con la integración, puedes crear segmentos Braze basados en atributos personalizados rellenados a partir de las respuestas de Outgrow.

1. En Braze, ve a **Interacción** > **Segmentos** y selecciona **Crear nuevo segmento**.
2. Nombra tu segmento y establece filtros basados en los datos de Outgrow. Por ejemplo:
   - Filtra por `outgrow_quiz_score` para dirigirte a los usuarios que hayan superado un determinado umbral.
   - Filtrar por `outgrow_custom_segment` para dirigirte a los usuarios que pertenecen a un segmento determinado definido por Outgrow.
3. Guarda tu segmento para utilizarlo en campañas y Lienzos.

### Lanzar campañas con segmentos definidos por Outgrow

Puedes utilizar los segmentos personalizados creados a partir de los datos de Outgrow para personalizar tus campañas Braze y dirigirte a los usuarios en función de sus respuestas al contenido interactivo. Para hacerlo y crear una experiencia de usuario más personalizada, sigue estos pasos:

1. En Braze, ve a **Interacción** > **Campañas**.
2. Selecciona **Crear campaña** y elige el tipo de campaña (correo electrónico, push, mensaje dentro de la aplicación u otros).
3. En el paso de segmentación de la audiencia, selecciona el segmento creado a partir de los atributos de Outgrow (como usuarios con puntuaciones específicas en el cuestionario o segmentos).
4. Personaliza el contenido y la configuración de tu campaña, y luego lánzala.

## Solución de problemas comunes

| Problema | Solución |
|-------|----------|
| **Los datos no se transfieren a Braze** | Comprueba que la clave de API y la URL del punto final son correctas en tu configuración de integración de Outgrow. Asegúrese de que la clave API tiene el permiso `users.track` activado. |
| **Mapeado incorrecto de los datos** | Asegúrate de que cada respuesta Outgrow mapeada corresponde a un atributo personalizado Braze válido y que los nombres de los atributos coinciden exactamente. |
| **El segmento no se filtra correctamente** | Asegúrate de que los atributos personalizados en Braze están correctamente configurados y reciben datos. Vuelve a comprobar tu lógica de filtrar segmentos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Consideraciones adicionales

- **Privacidad de datos**: Cumplir la normativa sobre privacidad de datos (como el RGPD y la CCPA) al transferir datos de usuario entre plataformas.
- **Límites de velocidad**: Los datos de crecimiento se envían a Braze en tiempo real, pero pueden aplicarse límites de tasa de la API de Braze para grandes volúmenes de datos. Planifica en consecuencia las experiencias de alto tráfico.
- **Configuración personalizada de atributos**: Comprueba que los atributos personalizados de Braze utilizados en esta integración están correctamente configurados para capturar los datos enviados desde Outgrow.

Para obtener ayuda adicional, consulta [la documentación de Outgrow](https://support.outgrow.co/docs/configuring-native-integration-between-outgrow-braze) o ponte en contacto con el servicio de asistencia de Outgrow.
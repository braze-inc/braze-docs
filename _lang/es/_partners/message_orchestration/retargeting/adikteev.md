---
nav_title: Adikteev
article_title: Predicción de abandono Adikteev
description: "Este artículo de referencia describe la asociación entre Braze y Adikteev, un motor de retención de usuarios que combina la predicción del abandono con servicios integrales de reorientación de aplicaciones."
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Predicción de abandono Adikteev

> [Adikteev](https://www.adikteev.com/churn-prediction) es un motor de retención de usuarios que combina la predicción del abandono con servicios integrales de reorientación de aplicaciones.

_Esta integración está mantenida por Adikteev._

## Sobre la integración

La integración de Braze y Adikteev te permite impulsar la retención de usuarios aprovechando la tecnología de predicción del abandono de usuarios de Adikteev dentro de las campañas de CRM de Braze para dirigirte prioritariamente a los segmentos de usuarios de alto riesgo.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta Adikteev | Se necesita una cuenta Adikteev para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con el permiso `users.track`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **API e identificadores**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ejemplos

{% tabs %}
{% tab Filtrado de audiencia %}
Afina tus segmentos de audiencia en función del riesgo de abandono.<br> Los nombres y valores de los atributos personalizados enviados por Adikteev son configurables.

![Una captura de pantalla que muestra un ejemplo de cómo utilizar un atributo personalizado enviado por Adikteev como filtro de segmento de audiencia.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab Focalización de mensajes %}
Personalización de tus campañas de mensajería Braze en función del riesgo de abandono de los destinatarios.

![Una captura de pantalla que muestra un ejemplo de cómo utilizar un atributo personalizado enviado por Adikteev como filtro de segmentación de campaña.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## Integración

### Paso 1: Comparte el flujo de eventos de tu aplicación

Para empezar a ejecutar la predicción de abandono en la audiencia de tu aplicación, Adikteev necesitará que actives los postbacks de eventos desde tu plataforma de medición móvil. Sigue las instrucciones del [sitio web de soporte de Adikteev](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation) para configurarlo.

### Paso 2: Crea tu clave de API REST Braze

En Braze, ve a **Configuración** > **API e identificadores**. Selecciona **Crear nueva clave de API**, introduce el Nombre de la clave de API que elijas y asegúrate de que se añade el siguiente permiso:

- `users.track`

### Paso 3: Proporciona información al equipo Adikteev

Para completar la integración, debes proporcionar tu clave de API REST y la URL del punto final REST a tu administrador de cuentas de Adikteev. Adikteev establecerá la conexión y se pondrá en contacto contigo una vez finalizada la configuración para validar la integración.

## Dosificación y límites de velocidad

El punto final `user.track` se utiliza para actualizar los datos de tus usuarios. Consulta [la documentación de la API]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para obtener todos los detalles sobre los límites de velocidad del punto final, las solicitudes por lotes y los detalles de las solicitudes.

{% alert tip %}
Recuerda que las llamadas a la API sólo deben realizarse para actualizar datos que hayan cambiado, con el fin de reducir el número total de llamadas a la API. En otras palabras, actualiza sólo a los usuarios cuyo segmento de abandono haya cambiado.
{% endalert %}

## Identificadores de usuario y dispositivo

Los perfiles de usuario en Braze pueden asociarse a cualquier tipo de identificador de usuario o dispositivo; la lista de opciones disponibles depende de cómo hayas integrado la recopilación de datos con Braze. En el caso de Adikteev, tendrás que encontrar un identificador común entre tu MMP y tus perfiles de usuario en Braze para poder enviar correctamente la información del segmento de abandono.

## Retención y supresión de datos

Si no se realiza ninguna actualización, el atributo y su valor se conservan indefinidamente en los perfiles de usuario Braze.

Para eliminar un atributo de perfil, ponlo en `null`.

## Solicitar cargas útiles

La carga útil enviada desde Adikteev a Braze es personalizable y puede configurarse según las necesidades del cliente. Esto incluye configurar los identificadores utilizados, el nombre del atributo personalizado y si Adikteev puede crear nuevos usuarios en Braze o sólo actualizar los usuarios existentes.


## Asistencia y solución de problemas

Ponte en contacto con tu director de cuentas de Adikteev para cualquier pregunta relacionada con la integración o para obtener ayuda con tus casos de uso.


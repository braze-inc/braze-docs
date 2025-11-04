---
nav_title: Komo
article_title: Komo
description: "Este artículo de referencia describe la asociación entre Braze y Komo, una plataforma de interacción con los clientes especializada en gamificación, contenido interactivo, concursos, premios y fidelización. A través de esta integración, los datos propios y de zero-party data capturados en Komo pueden publicarse en Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo](https://komo.tech/) es una plataforma de interacción con los clientes especializada en gamificación, contenidos interactivos, concursos, premios y fidelización.

_Esta integración está mantenida por Komo._

## Sobre la integración

La integración de Braze y Komo te permite recopilar datos propios y zero-party data a través de los Komo Engagement Hubs. Estos hubs son micrositios dinámicos que ofrecen contenidos interactivos y características de gamificación. Los datos de usuario recogidos de estos centros se transmiten a la API de Braze.

- Ingesta de datos de usuario propios y de terceros desde Komo a Braze en tiempo real.
- Ingesta de datos de estudios de mercado y preferencias de los usuarios cuando responden a encuestas, cuestionarios y preguntas tipo test.
- Construir progresivamente perfiles de usuario en Braze a medida que el usuario sigue interactuando y compartiendo más datos sobre sí mismo.
- Estandarizar el aspecto de los correos electrónicos transaccionales enviados a través de Braze

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Komo | Necesitarás una cuenta activa de Komo para beneficiarte de esta asociación. Visita [Komo](https://komo.tech/) para iniciar una prueba ahora. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia.<br><br>Por ejemplo, debería ser algo así https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos prácticos

{% tabs local %}
{% tab Captura de datos - Envío de formularios %}

Cuando un usuario envía un formulario de captura de datos personalizable en Komo, los campos de Komo mapeados en la integración Braze se pasarán a Braze a través de la llamada a la API `/users/track/`.

Los formularios de captura de datos existen al principio o al final de las tarjetas.

{% endtab %}
{% tab Investigación de mercados - Próximamente %}

Próximamente, Komo añadirá la posibilidad de transmitir datos de estudios de mercado obtenidos cuando un usuario responde a una pregunta de un cuestionario, una encuesta, un test de personalidad, un swiper, etc. Estos datos te habilitarán para mejorar el perfil de un usuario más allá de los datos capturados en los envíos de formularios.

{% endtab %}
{% endtabs %}

## Integración

### Paso 1: Publica un Komo Engagement Hub y una tarjeta

Tendrás que publicar un Komo Engagement Hub con al menos una tarjeta que contenga un formulario de captura de datos. Cuando se publique, podrás probar la experiencia del usuario de extremo a extremo y verificar que la integración funciona correctamente.

![]({% image_buster /assets/img/komo/komo_hub_publish.png %})

### Paso 2: Añade la integración Braze

En Komo, ve a la pestaña **Configuración del Hub** y selecciona la sección **Integraciones**. A continuación, busca la integración Braze en la lista y selecciona el botón **Conectar** para habilitar la integración.

![]({% image_buster /assets/img/komo/komo_hub_settings_integrations.png %})

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %})

#### Configurar el mapeado de usuarios

Lo primero que tendrás que configurar es cómo mapearás los usuarios capturados en Komo a usuarios dentro de Braze. Si estás capturando el `braze_id` o `external_id` por un campo dentro de Komo, entonces puedes seleccionar la clave apropiada; de lo contrario, selecciona la opción más común será un alias de usuario de correo electrónico o teléfono.

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}){: style="max-width:65%;"}

A continuación, tendrás que definir un mapeado de los campos Komo que quieras transferir a atributos Braze. Komo captura una gran cantidad de datos, por lo que sólo se enviarán a Braze los campos mapeados en la integración Braze.

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}){: style="max-width:65%;"}

Por último, añade tu clave de API y la URL del punto final REST y haz clic en **Guardar** para habilitar la integración.

## Utilizar la integración

Una vez completada la integración, puedes utilizar los datos de Komo enviados a Braze para crear segmentos de segmentación.



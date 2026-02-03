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
{% tab Data Capture - Form Submission %}

Cuando un usuario envía un formulario de captura de datos personalizable en Komo, los campos de Komo mapeados en la integración Braze se pasarán a Braze a través de la llamada a la API `/users/track/`.

Los formularios de captura de datos existen al principio o al final de las tarjetas.

{% endtab %}
{% tab Market Research - Coming soon %}

Komo también habilita la capacidad de pasar a través de los datos de investigación de mercado capturados cuando un usuario responde a una pregunta de test, encuesta, test de personalidad, swiper y similares. Estos datos te habilitarán para mejorar el perfil de un usuario más allá de los datos capturados en los envíos de formularios.

{% endtab %}
{% endtabs %}

## Integración

### Paso 1: Publica un Komo Engagement Hub y una tarjeta

Tendrás que publicar un Komo Hub con al menos una tarjeta que contenga un formulario de captura de datos. Cuando se publique, podrás probar la experiencia del usuario de extremo a extremo y verificar que la integración funciona correctamente.

![Centro Komo.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### Paso 2: Añade la aplicación Braze Connected 

En Komo, ve a la pestaña **Configuración de la empresa** y selecciona la sección **Aplicaciones conectadas**. 

A continuación, busca la integración Braze en la lista y selecciona el botón **Conectar** para habilitar la integración.

![Conecta la integración Braze.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Conectar Integración Braze Paso 2b.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### Configura la integración mediante un Flujo de trabajo

Ahora tienes que configurar un flujo de trabajo, dentro de un espacio de trabajo, sitio o tarjeta, para sincronizar los datos con Braze. 

El alcance del flujo de trabajo en el ámbito de todo el Espacio de Trabajo, de un Sitio (que contiene muchas Tarjetas) o de una sola Tarjeta, depende de si quieres que el flujo de trabajo se desencadene en muchas Tarjetas o campañas. 

Después de crear un Flujo de trabajo, define tu desencadenante, busca Braze en el menú de pasos y añade el paso "Seguir usuario". 

![Seguimiento de la configuración del usuario.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

Desde aquí, configura los eventos, atribuciones y suscripciones que quieres sincronizar de Komo a Braze. 

![Lista de bloques de contenido.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## Utilizar la integración

Ahora tu integración está en marcha y puedes supervisar cada ejecución en la pestaña Ejecuciones del flujo de trabajo. 

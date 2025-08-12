---
nav_title: Toovio
article_title: Toovio
description: "Este artículo de referencia describe la asociación entre Braze y Toovio, una empresa de datos como servicio, que te ayuda a descubrir tus datos procesables y a utilizar los elementos más importantes para impulsar resultados incrementales basados en objetivos predefinidos."
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [Toovio](https://toovio.com/) es una empresa de datos como servicio impulsada por inteligencia artificial que te ayuda a descubrir tus datos procesables y a utilizar los elementos más críticos para impulsar resultados incrementales basados en objetivos predefinidos.

_Esta integración está mantenida por Toovio._

## Sobre la integración

La asociación entre Braze y Toovio proporciona la activación de mensajes casi en tiempo real, las herramientas para impulsar el rendimiento incremental y el acceso a las herramientas avanzadas de medición de campañas de Toovio.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Toovio | Se necesita una cuenta Toovio para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Braze Currents | Braze Currents permite a los clientes Braze transmitir datos de eventos o comportamiento a un socio de datos Braze (AWS S3, Google Cloud Storage o Microsoft Azure Blob Storage) para su procesamiento externo a la plataforma Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

La siguiente integración permite a Toovio generar desencadenantes dirigidos a clientes específicos y comunicarse casi en tiempo real. Los desencadenantes determinados por Toovio se transmitirán a Braze a través del [punto final `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze.

### Paso 1: Definir socio de datos

Debe compartirse con Toovio una ubicación para la fuente Currents; esto permite a Toovio acceder y procesar los datos de eventos y comportamiento del usuario.

### Paso 2: Configura una campaña desencadenada

Crea una [campaña desencadenada por la API de]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) Braze basada en los eventos de clientes a los que Toovio se dirigirá. Además, deben definirse los atributos del usuario objetivo y los valores que desencadenarán la campaña.

### Paso 3: Configura tu cuenta Toovio

Ponte en contacto con Toovio en [info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request) con el asunto "Solicitud de nuevo cliente" para crear una cuenta. Toovio trabajará con los clientes para desencadenar la configuración y los modelos subyacentes.



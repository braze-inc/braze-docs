---
nav_title: Página del socio

page_order: 4

#Required
description: "Esta es la descripción de la Búsqueda de Google. Los caracteres que pasan de 160 se truncan, sé breve."
page_type: partner
tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks
  
noindex: true
#ATTENTION: remove noindex and this alert from template

---

# [Nombre del socio]

> ¡Te damos la bienvenida a la plantilla de la página del socio! Aquí encontrarás todo lo que necesitas para crear tu propia página del socio. En esta primera sección, deberías describir al socio en el primer párrafo en una o dos oraciones. Incluye también un enlace al sitio principal de ese socio.

En el segundo párrafo, deberías explorar y explicar la relación entre Braze y este socio. En este párrafo se debería explicar cómo Braze y este socio trabajan juntos para estrechar el vínculo entre el usuario de Braze y su cliente. Explica la "elevación" que se produce cuando un usuario de Braze se integra o aprovecha a este socio y sus servicios.

## Requisitos o prerrequisitos

Esta sección trata de todo lo que necesitas para integrarte con el socio y empezar a utilizar sus servicios. La mejor forma de entregar esta información es con un párrafo instructivo rápido que describa cualquier detalle importante no técnico de información "que es necesario saber", como si tu integración estará sujeta o no a comprobaciones o autorizaciones de seguridad adicionales. A continuación, debes utilizar un gráfico para describir los requisitos técnicos de la integración.

{% alert important %}
Los siguientes requisitos son los típicos que puedes necesitar de Braze. Recomendamos utilizar el título, origen, enlaces y fraseología atribuidos que se indican en el siguiente cuadro. Asegúrate de ajustar la descripción para que sepas para qué sirve cada uno de estos requisitos.
{% endalert %}

| Requisito | Origin | Acceso | Descripción |
|---|---|---|---|
|Clave de API REST del espacio de trabajo Braze | Plataforma Braze | **Configuración** > página **Clave de API**  | Esta descripción debería indicarte qué hacer con la clave de API REST del espacio de trabajo. |
|Punto final de la API Braze | Plataforma Braze | Consulta nuestra [lista de puntos finales]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) o abre un [ticket de soporte]({{site.baseurl}}/braze_support/). | Descripción pendiente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## [Tipo de integración] Integración

Aquí es donde divides la integración en pasos. No te limites a escribir párrafos interminables: se trata de documentación técnica que utilizarán tanto especialistas en marketing como desarrolladores para poner en marcha la integración. Tu único objetivo en esta sección es escribir documentación descriptiva que ayude al usuario de Braze a realizar su trabajo. Con "Tipo de integración" en el título de la sección, nos referimos a indicar si se trata o no de una integración en paralelo, de servidor a servidor o "Fuera de la caja". Esto te habilita a tener múltiples secciones de integración si hay más de una forma de integrarse con este socio.

Si se trata de una integración de Currents, esta página debe estar ubicada en la sección Currents, y debe crearse una página de navegación correspondiente que redirija a esa ubicación en Currents.

### Paso 1: Esta es una breve descripción del primer paso

Desglosa esto, incluyendo cualquier código que sea necesario. Recuerda que puedes ofrecer varios conjuntos de códigos diferentes: no es necesario que sólo ofrezcas una forma de integración.

### Paso 2: Este Paso Describirá las Imágenes

Tienes la opción de poner imágenes en tu documentación, por lo que te recomendamos que lo hagas y que lo hagas con cuidado.

### Paso 3: Cuántos pasos

Esboza el uso de la integración, sobre todo si implica insertar Liquid en nuestro creador de mensajes.

## Personalización

Esta sección **es opcional**. Aquí podrías esbozar cualquier forma específica de personalizar tu integración entre los dos socios.

## Utilizar esta integración

Debe describir cómo utilizar la integración: informa a tu lector de si tiene que pulsar algunos botones o si no tiene que hacer nada en absoluto tras la integración.

### Paso 1: Esta es una breve descripción del primer paso

El típico paso a paso.

## Ejemplos

Puede ser una parte fundamental de tu documentación. Aunque esto es opcional, es un buen lugar para esbozar casos de uso típicos o incluso novedosos para la integración. Esto puede utilizarse como una forma de vender o mejorar la relación: proporciona contexto, ideas y, lo que es más importante, una forma de visualizar las capacidades de la integración.

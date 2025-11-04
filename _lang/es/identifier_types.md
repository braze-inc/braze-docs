---
nav_title: "Tipos de identificadores API"
article_title: Tipos de identificadores API
page_order: 2.2
toc_headers: h2
description: "Este artículo de referencia cubre los diferentes tipos de identificadores API que existen en el panel de Braze, dónde puedes encontrarlos y para qué se utilizan." 
page_type: reference

---

# Tipos de identificadores API

> Esta guía de referencia aborda los distintos tipos de identificadores de API que se pueden encontrar en el panel de control de Braze, su finalidad, dónde se pueden encontrar y cómo se suelen utilizar. Para obtener información sobre las claves de la API REST o las claves de la API del espacio de trabajo, consulte la [descripción general de la API]({{site.baseurl}}/api/api_key/).

Los siguientes identificadores pueden utilizarse para acceder a tu plantilla, Canvas, campaña o segmento desde la API externa de Braze. Todos los mensajes deben seguir la codificación [UTF-8](https://en.wikipedia.org/wiki/UTF-8).

## Identificador de la aplicación

El identificador de aplicación o `app_id` es un parámetro que asocia la actividad con una aplicación específica en su espacio de trabajo. Designa con qué aplicación del espacio de trabajo estás interactuando. Por ejemplo, tendrás un `app_id` para tu aplicación para iOS, un `app_id` para tu aplicación para Android y un `app_id` para tu integración web. En Braze, es posible que tenga varias aplicaciones para la misma plataforma en los distintos tipos de plataformas compatibles con Braze.

### ¿Dónde puedo encontrarlo?

Hay dos maneras de localizar tu `app_id`:

{% tabs local %}
{% tab App Identifiers %}
Ve a **Configuración** > **API e identificadores** > **Identificadores de aplicación**. Tu clave de API para cada aplicación aparece en la columna **Identificador**.
{% endtab %}

{% tab App Settings %}
Ve a **Ajustes** > **Ajustes de la aplicación**. Su clave API aparece junto al campo **Clave API** en la sección de configuración.

{% endtab %}
{% endtabs %}

### ¿Para qué sirve?

Los identificadores de aplicación en Braze se utilizan al integrar el SDK y también se utilizan para hacer referencia a una aplicación específica en las llamadas a la API REST. Con `app_id` puedes hacer muchas cosas, como extraer datos de un evento personalizado que se haya producido para una aplicación concreta, recuperar estadísticas de desinstalación, estadísticas de nuevos usuarios, estadísticas de DAU y estadísticas de inicio de sesión para una aplicación concreta.

{% alert tip %}
A veces, puede que se te pida un `app_id`, pero no estás trabajando con una aplicación, porque es un campo heredado específico de una plataforma concreta, puedes omitir este campo incluyendo cualquier cadena de caracteres como marcador de posición de este parámetro obligatorio.
{% endalert %}

### Múltiples identificadores de aplicaciones

Durante la configuración del SDK, el caso de uso más común para múltiples identificadores de aplicaciones es separar esos identificadores para las variantes de compilación de depuración y lanzamiento.

Para cambiar fácilmente entre varios identificadores de aplicación en tus compilaciones, te recomendamos que crees un archivo `braze.xml` distinto para cada [variante de compilación](https://developer.android.com/studio/build/build-variants.html) relevante. Una variante de fabricación es una combinación del tipo de fabricación y la variante de producto. Por defecto, un nuevo proyecto Android está configurado con los tipos de compilación `debug` y `release` y sin sabores de producto.

Para cada variante de compilación relevante, crea un nuevo `braze.xml` para ella en `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Cuando se compile la variante de compilación, utilizará el nuevo identificador.

## Identificador de plantilla

Un identificador de [plantilla]({{site.baseurl}}/api/endpoints/templates/) o ID de plantilla es una clave aleatoria generada por Braze para una plantilla determinada dentro del cuadro de mandos. Los ID de plantilla son únicos para cada plantilla y pueden utilizarse para hacer referencia a las plantillas a través de la API. 

Las plantillas son estupendas si tu empresa contrata tus diseños HTML para campañas. Una vez construidas las plantillas, ahora tienes una plantilla que no es específica para una campaña, sino que puede aplicarse a una serie de campañas, como un boletín de noticias.

### ¿Dónde puedo encontrarlo?

Puedes encontrar el ID de tu plantilla de dos maneras:

{% tabs local %}
{% tab Templates %}
Vaya a **Plantillas**, seleccione una página de plantilla y, a continuación, seleccione una plantilla preexistente. Si la plantilla que desea aún no existe, cree una y guárdela. En la parte inferior de la página de la plantilla individual, podrá encontrar el identificador de su plantilla.
{% endtab %}

{% tab API Keys %}
Ve a **Configuración** > **API e identificadores**. Aquí, Braze ofrece una búsqueda de **Identificadores de API adicionales** donde puede buscar identificadores específicos.

{% endtab %}
{% endtabs %}

### ¿Para qué sirve?

- Actualizar plantillas mediante la API
- Obtener información sobre una plantilla específica

## Identificador del lienzo

Un identificador de [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/) o Canvas ID es una clave aleatoria generada por Braze para un Canvas determinado dentro del panel. Los ID de lienzo son exclusivos de cada lienzo y pueden utilizarse para hacer referencia a lienzos a través de la API. 

Ten en cuenta que si tienes un Canvas con variantes, existe un ID de Canvas general, así como IDs de Canvas de variantes individuales anidados bajo el Canvas principal. 

### ¿Dónde puedo encontrarlo?

Puedes encontrar tu Canvas ID en el panel de control. Vaya a **Mensajería** > **Lienzo** y seleccione un Lienzo preexistente. Si el lienzo que desea no existe todavía, cree uno y guárdelo. En la parte inferior de una página individual de Canvas, haga clic en **Analizar variantes**. Aparecerá una ventana con el identificador de la API Canvas situado en la parte inferior.

### ¿Para qué sirve?

- Seguimiento analítico de un mensaje específico
- Obtenga estadísticas agregadas de alto nivel sobre el rendimiento de Canvas
- Obtener detalles sobre un lienzo concreto
- Con Currents para aportar datos a nivel de usuario para un enfoque más amplio de los Canvas
- Con entrega desencadenada por API para recopilar estadísticas de mensajes transaccionales

## Identificador de campaña

Un identificador de [campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) o ID de campaña es una clave aleatoria generada por Braze para una campaña determinada dentro del panel. Los ID de campaña son exclusivos de cada campaña y pueden utilizarse para hacer referencia a las campañas a través de la API. 

Ten en cuenta que, si tienes una campaña con variantes, hay tanto un ID de campaña general como ID de campaña de variantes individuales anidados bajo la campaña principal. 

### ¿Dónde puedo encontrarlo?

Puedes encontrar tu ID de campaña de dos maneras:

{% tabs local %}
{% tab Campaigns %}
Vaya a **Mensajería** > **Campañas** y seleccione una campaña preexistente. Si la campaña que desea no existe todavía, cree una y guárdela. En la parte inferior de la página de campaña individual, podrá encontrar su **Identificador API de campaña**.

{% endtab %}

{% tab API Keys %}
Ve a **Configuración** > **API e identificadores**. Aquí, Braze ofrece una búsqueda de **Identificadores de API adicionales** donde puede buscar identificadores específicos.

{% endtab %}
{% endtabs %}

### ¿Para qué sirve?

- Seguimiento analítico de un mensaje específico
- Obtén estadísticas agregadas de alto nivel sobre el rendimiento de la campaña
- Obtener detalles sobre una campaña concreta
- Con Currents para aportar datos a nivel de usuario y tener una visión más amplia de las campañas.
- Con entrega desencadenada por API para recopilar estadísticas de mensajes transaccionales
- Para [buscar una campaña específica]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/#search-syntax) en la página **Campañas** utilizando el filtro `api_id:YOUR_API_ID`

## Identificador de segmento

Un identificador de [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) o ID de segmento es una clave aleatoria generada por Braze para un segmento determinado dentro del panel. Los ID de segmento son exclusivos de cada segmento y pueden utilizarse para hacer referencia a los segmentos a través de la API. 

### ¿Dónde puedo encontrarlo?

Puedes encontrar el ID de tu segmento de dos maneras:

{% tabs local %}
{% tab Segments %}
Vaya a **Audiencia** > **Segmentos** y seleccione un segmento preexistente. Si el segmento que desea no existe todavía, cree uno y guárdelo. En la parte inferior de la página del segmento individual, podrá encontrar su identificador de segmento.

{% endtab %}

{% tab API Keys %}
Ve a **Configuración** > **API e identificadores**. Aquí, Braze ofrece una búsqueda de **Identificadores de API adicionales** donde puede buscar identificadores específicos.

{% endtab %}
{% endtabs %}

### ¿Para qué sirve?

- Obtener detalles sobre un segmento específico
- Recuperar análisis de un segmento específico
- Tira de cuántas veces se ha registrado un evento personalizado para un segmento concreto
- Especifica y envía una campaña a los miembros de un segmento desde la API

## Enviar identificador

Un identificador de envío, o ID de envío, es una clave generada por Braze o creada por usted para un envío de mensaje determinado bajo la cual debe realizarse el seguimiento de los análisis. El identificador de envío le permite recuperar los análisis de una instancia específica de una campaña enviada a través del [punto final`/sends/data_series` ]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/).

### ¿Dónde puedo encontrarlo?

Las campañas activadas por API y API que se envían como difusión generarán automáticamente un identificador de envío si no se proporciona un identificador de envío. Si deseas especificar tu propio identificador de envío, primero tendrás que crear uno a través del [punto final`/sends/id/create` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/). El identificador debe tener todos los caracteres ASCII y una longitud máxima de 64 caracteres. Puede reutilizar un identificador de envío en varios envíos de la misma campaña si desea agrupar los análisis de esos envíos.

### ¿Para qué sirve?
Envíe y siga el rendimiento de los mensajes mediante programación, sin necesidad de crear campañas para cada envío.

## Identificador del grupo de suscripción

Un identificador de grupo de suscripción, o ID de grupo de suscripción, es una clave generada por Braze para un grupo de suscripción determinado. Los ID son únicos para cada grupo de suscripción y pueden utilizarse para hacer referencia a los grupos de suscripción a través de la API.

### ¿Dónde puedo encontrarlo?

Vaya a **Audiencia** > **Suscripciones** y copie el ID que aparece junto al grupo de suscripción correspondiente.

### ¿Para qué sirve?

- Listar los grupos de suscripción de un usuario
- Obtener el estado del grupo de suscripción de un usuario
- Actualizar el estado del grupo de suscripción de un usuario

---
nav_title: Integración
article_title: Integración de tarjetas de contenido para Android y FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia cubre la integración de la tarjeta de contenido y los diferentes modelos de datos y propiedades específicos de la tarjeta disponibles para tu aplicación Android o FireOS."
channel:
  - content cards
search_rank: 1
---

# Integración de tarjetas de contenido

> Este artículo de referencia cubre la integración de la tarjeta de contenido y los diferentes modelos de datos y propiedades específicos de la tarjeta disponibles para tu aplicación Android o FireOS.

{% alert note %}
Cuando estés listo para empezar con la implementación y la personalización, consulta la [Guía de personalización de la tarjeta de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards).
{% endalert %}

En Android, la fuente de tarjetas de contenido se implementa como un [fragmento](https://developer.android.com/guide/components/fragments.html) disponible en el proyecto Braze Android UI. Consulta la documentación de [Google Fragments](https://developer.android.com/guide/fragments#Adding " Android: Fragmentos") para obtener información sobre cómo añadir un fragmento a una actividad.

La clase [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) actualizará y mostrará automáticamente el contenido de las tarjetas de contenido y registrará los análisis de uso. Las tarjetas que pueden aparecer en el `ContentCards` de un usuario se crean en el panel de Braze.

## Modelo de datos de la tarjeta de contenido {#card-types-for-android}

El modelo de datos de las tarjetas de contenido está disponible en el SDK de Android. Para una referencia completa del modelo de datos de la tarjeta de contenido, consulta la [documentación de referencia del SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

Braze tiene cuatro tipos únicos de tarjetas de contenido que comparten un modelo base: [sólo imagen](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html), [imagen subtitulada](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html), [clásico (anuncio de texto)](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) y [clásico (noticias breves)](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html). Cada tipo hereda propiedades comunes de un modelo base y tiene las siguientes propiedades adicionales.

Consulta [Análisis de]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) tarjetas para obtener información sobre cómo suscribirte a los datos de las tarjetas.

### Propiedades del modelo de tarjeta de contenido base {#base-card-for-android}

El modelo de [tarjeta base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) proporciona un comportamiento básico para todas las tarjetas.  

|Propiedad | Descripción |
|---|---|
|`getId()` | Devuelve el ID de la tarjeta configurado por Braze.|
|`getViewed()` | Devuelve un booleano que refleja si la tarjeta ha sido leída o no por el usuario.|
|`getExtras()` | Devuelve un mapeado de pares clave-valor extras para esta tarjeta.|
|`getCreated()`  | Devuelve la marca de tiempo unix de la hora de creación de la tarjeta desde Braze.|
|`getIsPinned` | Devuelve un booleano que refleja si la tarjeta está anclada.|
|`getOpenUriInWebView()`  | Devuelve un booleano que refleja si se deben abrir las URI de esta tarjeta <br> en el Braze WebView o no.|
|`getExpiredAt()` | Obtiene la fecha de caducidad de la tarjeta.|
|`getIsRemoved()` | Devuelve un booleano que refleja si el usuario final ha descartado esta tarjeta.|
|`getIsDismissible()`  | Devuelve un booleano que refleja si la tarjeta está anclada.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Sólo imagen Propiedades de la tarjeta de imagen {#banner-image-card-for-android}

[Las tarjetas de sólo imagen](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) son imágenes a tamaño completo en las que se puede hacer clic.

|Propiedad | Descripción |
|---|---|
|`getImageUrl()` | Devuelve la URL de la imagen de la tarjeta.|
|`getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo.|
|`getDomain()` | Devuelve el texto del enlace para la URL de la propiedad.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de imagen subtitulada {#captioned-image-card-for-android}

[Las tarjetas de imágenes con subtítulos](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) son imágenes de tamaño completo en las que se puede hacer clic y que van acompañadas de un texto descriptivo.

|Propiedad | Descripción |
|---|---|
|`getImageUrl()` | Devuelve la URL de la imagen de la tarjeta.|
|`getTitle()` | Devuelve el texto del título de la tarjeta.|
|`getDescription()` | Devuelve el texto del cuerpo de la tarjeta.|
|`getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo.|
|`getDomain()` | Devuelve el texto del enlace de la URL de la propiedad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta clásica {#text-Announcement-card-for-android}

Una tarjeta clásica sin imagen incluida dará como resultado una [tarjeta de anuncio de texto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Si se incluye una imagen, recibirás una [breve tarjeta de noticias](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Propiedad | Descripción |
|---|---|
|`getTitle()` | Devuelve el texto del título de la tarjeta. |
|`getDescription()` | Devuelve el texto del cuerpo de la tarjeta. |
|`getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo. | 
|`getDomain()` | Devuelve el texto del enlace de la URL de la propiedad. |
|`getImageUrl()` | Devuelve la URL de la imagen de la tarjeta, sólo se aplica a la Tarjeta de Noticias Corta clásica. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos de tarjeta

Todos los objetos del modelo de datos [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) ofrecen los siguientes métodos de análisis para registrar eventos de usuario en servidores de Braze.

|Método | Descripción |
|---|---|
|`logImpression()` | Registra manualmente una impresión en Braze para una tarjeta concreta. |
|`logClick()` | Registra manualmente un clic en Braze para una tarjeta concreta. |
|`setIsDismissed()` | Registra manualmente en Braze el descarte de una tarjeta concreta. Si una tarjeta ya está marcada como descartada, no se puede volver a marcar como descartada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


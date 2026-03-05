## Requisitos previos

Antes de poder utilizar las tarjetas de contenido Braze, tendrás que integrar el [SDK para Android de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) en tu aplicación. Sin embargo, no es necesaria ninguna configuración adicional.

## Fragmentos de Google

En Android, la fuente de tarjetas de contenido se implementa como un [fragmento](https://developer.android.com/guide/components/fragments.html) disponible en el proyecto Braze Android UI. La clase [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) actualizará y mostrará automáticamente el contenido de las tarjetas de contenido y registrará los análisis de uso. Las tarjetas que pueden aparecer en el `ContentCards` de un usuario se crean en el panel de Braze.

Para saber cómo añadir un fragmento a una actividad, consulta [la documentación de Google sobre fragmentos](https://developer.android.com/guide/fragments#Adding).

## Tipos de tarjeta y propiedades

El modelo de datos de las tarjetas de contenido está disponible en el SDK de Android y ofrece los siguientes tipos únicos de tarjetas de contenido. Cada tipo comparte un modelo base, lo que les permite heredar propiedades comunes del modelo base, además de tener sus propias propiedades únicas. Para ver la documentación de referencia completa, consulta [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Modelo de tarjeta base {#base-card-for-android}

El modelo de [tarjeta base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) proporciona un comportamiento básico para todas las tarjetas.  

|Propiedad | Descripción |
|---|---|
|`getId()` | Devuelve el ID de la tarjeta configurado por Braze.|
|`getViewed()` | Devuelve un booleano que refleja si la tarjeta ha sido leída o no por el usuario.|
|`getExtras()` | Devuelve un mapeado de extras clave-valor para esta tarjeta.|
|`getCreated()`  | Devuelve la marca de tiempo unix de la hora de creación de la tarjeta desde Braze.|
|`isPinned` | Devuelve un booleano que refleja si la tarjeta está anclada.|
|`getOpenUriInWebView()`  | Devuelve un booleano que refleja si se deben abrir las URI de esta tarjeta <br> en el Braze WebView o no.|
|`getExpiredAt()` | Obtiene la fecha de caducidad de la tarjeta.|
|`isRemoved()` | Devuelve un booleano que refleja si el usuario final ha descartado esta tarjeta.|
|`isDismissibleByUser()`  | Devuelve un booleano que refleja si el usuario puede deshabilitar la tarjeta.|
|`isClicked()` | Devuelve un booleano que refleja el estado de clic de esta tarjeta.|
|`isDismissed` | Devuelve un booleano que refleja si se ha descartado la tarjeta. Configura `true` para marcar la tarjeta como descartada. Si una tarjeta ya está marcada como descartada, no se puede volver a marcar como descartada.|
|`isControl()` | Devuelve un booleano si esta tarjeta es una tarjeta de control y no debe renderizarse.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Sólo imagen {#banner-image-card-for-android}

[Las tarjetas de sólo imagen](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) son imágenes a tamaño completo en las que se puede hacer clic.

|Propiedad | Descripción |
|---|---|
|`getImageUrl()` | Devuelve la URL de la imagen de la tarjeta.|
|`getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo.|
|`getDomain()` | Devuelve el texto del enlace para la URL de la propiedad.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagen subtitulada {#captioned-image-card-for-android}

[Las tarjetas de imágenes con subtítulos](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) son imágenes de tamaño completo en las que se puede hacer clic y que van acompañadas de un texto descriptivo.

|Propiedad | Descripción |
|---|---|
|`getImageUrl()` | Devuelve la URL de la imagen de la tarjeta.|
|`getTitle()` | Devuelve el texto del título de la tarjeta.|
|`getDescription()` | Devuelve el texto del cuerpo de la tarjeta.|
|`getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo.|
|`getDomain()` | Devuelve el texto del enlace de la URL de la propiedad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Clásico {#text-Announcement-card-for-android}

Una tarjeta clásica sin imagen incluida dará como resultado una [tarjeta de anuncio de texto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Si se incluye una imagen, recibirás una [breve tarjeta de noticias](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Propiedad | Descripción |
|---|---|
|`getTitle()` | Devuelve el texto del título de la tarjeta. |
|`getDescription()` | Devuelve el texto del cuerpo de la tarjeta. |
|`getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo. | 
|`getDomain()` | Devuelve el texto del enlace de la URL de la propiedad. |
|`getImageUrl()` | Devuelve la URL de la imagen de la tarjeta, sólo se aplica a la Tarjeta de Noticias Corta clásica. |
|`isDismissed` | Devuelve un booleano que refleja si se ha descartado la tarjeta. Configura `true` para marcar la tarjeta como descartada. Si una tarjeta ya está marcada como descartada, no se puede volver a marcar como descartada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos de tarjeta

Todos los objetos del modelo de datos [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) ofrecen los siguientes métodos de análisis para registrar eventos de usuario en servidores de Braze.

|Método | Descripción |
|---|---|
|`logImpression()` | Registra manualmente una impresión en Braze para una tarjeta concreta. |
|`logClick()` | Registra manualmente un clic en Braze para una tarjeta concreta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

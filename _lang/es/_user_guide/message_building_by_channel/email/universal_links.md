---
nav_title: Enlaces universales y enlaces de aplicaciones
article_title: Enlaces universales y enlaces de aplicaciones
page_order: 6.4
page_type: reference
description: "Este artículo de ayuda te explica cómo configurar los enlaces universales de Apple y los enlaces de aplicaciones de Android."
channel: email
---

# Enlaces universales y enlaces de aplicaciones

Los enlaces universales de Apple y los enlaces de aplicaciones de Android son mecanismos concebidos para proporcionar una transición sin problemas entre el contenido Web y las aplicaciones móviles. Mientras que los enlaces universales son específicos de iOS, los enlaces de aplicaciones de Android sirven para el mismo propósito para las aplicaciones de Android.

## Cómo funcionan los enlaces universales y los enlaces de aplicación

Los enlaces universales (iOS) y los enlaces a aplicaciones (Android) son enlaces Web estándar (`http://mydomain.com`) que apuntan tanto a una página Web como a un contenido dentro de una aplicación.

Cuando se abre un enlace universal o App Link, el sistema operativo comprueba si alguna aplicación instalada está registrada para ese dominio. Si se encuentra una aplicación, se inicia inmediatamente sin cargar la página Web. Si no se encuentra ninguna aplicación, la URL web se carga en el navegador web predeterminado del usuario, que también podría configurarse para redirigir a la App Store o a Google Play Store respectivamente.

Claramente, los enlaces universales permiten a un sitio web asociar sus páginas web con pantallas de aplicaciones específicas, de modo que cuando un usuario hace clic en un enlace a una página web que corresponde a una pantalla de aplicación, la aplicación puede abrirse directamente (si la aplicación está instalada en ese momento).

Esta tabla resume las principales diferencias entre los vínculos universales y los vínculos en profundidad tradicionales:

|                        | Enlaces universales y enlaces de aplicaciones                                  | Vínculos profundos                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Compatibilidad de plataformas | iOS (versión 9 y posteriores) y Android (versión 6.0 y posteriores)  | Utilizado en varios SO móviles    |
| Propósito                | Vincula fácilmente el contenido de la Web y de la aplicación en dispositivos iOS y Android | Enlace al contenido específico de la aplicación |
| Función               | Dirige a páginas Web o al contenido de una aplicación en función del contexto           | Abre pantallas específicas de la aplicación   |
| Instalación de la aplicación       | Abre la aplicación si la aplicación está instalada, si no, abre el contenido Web | Requiere la instalación de una aplicación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

Los enlaces universales y los enlaces a aplicaciones son los más utilizados para las campañas de correo electrónico, ya que los correos electrónicos se pueden abrir y clicar tanto desde ordenadores de sobremesa como desde dispositivos móviles.

Algunos canales no funcionan bien con estos enlaces. Por ejemplo, las notificaciones push, los mensajes dentro de la aplicación y las tarjetas de contenido deben utilizar vínculos profundos basados en esquemas (`mydomain://`).

{% alert note %}
Los enlaces de las aplicaciones Android requieren un `IBrazeDeeplinkHandler` personalizado con lógica para gestionar los enlaces de sus dominios de forma separada de otras URL de la Web. Puede ser más fácil utilizar vínculos en profundidad en su lugar y mantener uniformes las prácticas de vinculación para canales distintos del correo electrónico.
{% endalert %}

## Requisitos previos

Para utilizar enlaces universales y enlaces de aplicación:

- Tu sitio web debe ser accesible mediante HTTPS
- Tu aplicación debe estar disponible en App Store (iOS) o Google Play Store (Android)

## Configuración de enlaces universales y enlaces de aplicaciones

Para que las aplicaciones admitan enlaces universales o App Links, tanto iOS como Android requieren que se aloje un archivo de permisos especial en el dominio del enlace. Este archivo contiene definiciones de qué aplicaciones pueden abrir enlaces de ese dominio y, para iOS, qué rutas pueden abrir estas aplicaciones:

- **iOS:** Archivo de la Asociación de Sitios de Aplicaciones de Apple (AASA)
- **Android:** Archivo de enlaces de activos digitales

Además de este archivo de permisos, hay definiciones codificadas de los dominios de enlace que la aplicación puede abrir, que se configuran dentro de la aplicación:

- **iOS:** Establecer como "Dominios asociados" en Xcode
- **Android:** Definido en el archivo `AndroidManifest.xml` de la aplicación

Esta asociación dominio-app de dos partes es necesaria para que funcione un enlace universal o App Link e impide que cualquier aplicación secuestre enlaces de un dominio concreto o que cualquier dominio abra una aplicación concreta.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Estos pasos están adaptados de la documentación para desarrolladores de Apple. Para más información, consulta [Permitir que aplicaciones y sitios web enlacen a tu contenido](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Paso 1: Configura los derechos de tu aplicación

{% alert note %}
[En Xcode 13 y posteriores](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), Xcode puede gestionar el aprovisionamiento de derechos por ti automáticamente. Probablemente puedas saltar al [paso 1c](#step-1c) y volver a consultar estas instrucciones si tienes problemas.
{% endalert %}

#### Paso 1a: Registra tu aplicación {#step-1a}

1. Ve a developer.apple.com y conéctate.
2. Haz clic en **Certificados, Identificadores & Perfiles**.
3. Haz clic en **Identificadores**.
4. Si aún no tienes un identificador de aplicación registrado, haz clic en + para crearlo.
   a. Introduce un **Nombre**. Puede ser lo que tú quieras.
   b. Introduce el **ID del paquete**. Puedes encontrar tu ID de paquete en la pestaña **General** de tu proyecto de Xcode para obtener el objetivo de compilación adecuado.

#### Paso 1b: Activa los Dominios Asociados en el identificador de tu aplicación

1. En tu identificador de aplicación existente o recién creado, localiza la sección **Servicios de la aplicación**.
2. Selecciona **Dominios asociados**.
3. Haz clic en **Guardar**.

\![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Paso 1c: Activa los dominios asociados en tu proyecto Xcode {#step-1c}

Antes de continuar, asegúrate de que tu proyecto Xcode tiene seleccionado el mismo equipo en el que acabas de registrar tu identificador de aplicación. 

1. En Xcode, ve a la pestaña **Capacidades** de tu archivo de proyecto.
2. Activa **los dominios asociados**.

##### Consejo para la solución de problemas

Si aparece el error "Un ID de aplicación con el identificador 'tu-app-id' no está disponible. Introduce una cadena diferente", haz lo siguiente:

1. Comprueba que has seleccionado el equipo correcto.
2. Comprueba que el ID del paquete[(paso 1a](#step-1a)) de tu proyecto de Xcode coincide con el utilizado para registrar el identificador de la aplicación.

#### Paso 1d: Añade el derecho de dominio

En la sección de dominios, añade la etiqueta de dominio adecuada. Debes anteponer el prefijo `applinks:`. En este caso, puedes ver que hemos añadido `applinks:yourdomain.com`.

\![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Paso 1e: Confirma que el archivo de derechos está incluido en la compilación

En el navegador de proyectos, asegúrate de que tu nuevo archivo de derechos está seleccionado en **Afiliación de destino**.

Xcode debería encargarse de ello automáticamente.

### Paso 2: Configura tu sitio web para alojar el archivo AASA

Para asociar el dominio de tu sitio web con tu aplicación nativa en iOS, tienes que alojar el archivo Apple App Site Association (AASA) en tu sitio web. Este archivo sirve como forma segura de verificar la propiedad del dominio a iOS. Antes de iOS 9, los desarrolladores podían registrar cualquier esquema URI para abrir sus aplicaciones, sin ninguna verificación. Sin embargo, con AASA, este proceso es ahora mucho más seguro y fiable.

El archivo AASA contiene un objeto JSON con una lista de aplicaciones y las rutas URL en el dominio que deben incluirse o excluirse como enlaces universales. Aquí tienes un ejemplo de archivo AASA:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": “JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`: Se construye combinando el **ID de equipo** de tu aplicación (visita `https://developer.apple.com/account/#/membership/` para obtener el ID de equipo) y el **identificador de paquete**. En el ejemplo anterior, "JHGFJHHYX" es el ID del equipo, y "com.facebook.ios" es el ID del paquete.
- `paths`: Matriz de cadenas que especifican qué rutas se incluyen o excluyen de la asociación. Puedes utilizar `NOT` antes de la ruta para desactivar las rutas. En este ejemplo, todos los enlaces de esta ruta irán a la Web en lugar de abrir la aplicación. Puedes utilizar `*` como comodín para habilitar todas las rutas de un directorio y `?` para que coincida con un único carácter (como /archivos/201?/ para que coincida con todos los números de 2010-2019).

{% alert note %}
Estas cadenas distinguen entre mayúsculas y minúsculas y se ignoran las cadenas de consulta y los identificadores de fragmentos.
{% endalert %}

### Paso 3: Aloja el archivo AASA en tu dominio

Cuando tengas listo tu archivo AASA, ya puedes alojarlo en tu dominio en `https://<<yourdomain>>/apple-app-site-association` o en `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Sube el archivo `apple-app-site-association` a tu servidor Web HTTPS. Puedes colocar el archivo en la raíz de tu servidor o en el subdirectorio `.well-known`. No añadas `.json` al nombre del archivo.

{% alert important %}
iOS sólo intentará obtener el archivo AASA a través de una conexión segura (HTTPS).
{% endalert %}

Al alojar el archivo de AASA, asegúrate de que el archivo sigue estas directrices:

- Se sirve a través de HTTPS.
- Utiliza el tipo MIME `application/json`.
- No supera los 128 KB (requisito en iOS 9.3.1 y posteriores)

### Paso 4: Prepara tu aplicación para gestionar enlaces universales

Cuando un usuario pulsa un enlace universal en un dispositivo iOS, el dispositivo lanza la aplicación y le envía un objeto [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity). La aplicación puede entonces consultar el objeto NSUserActivity para determinar cómo se inició.

Para admitir enlaces universales en tu aplicación, sigue estos pasos:

1. Añade una asignación de derechos que especifique los dominios que admite tu aplicación.
2. Actualiza el delegado de tu aplicación para que responda adecuadamente cuando reciba el objeto NSUserActivity.

En Xcode, abre la sección **Dominios asociados** en la pestaña **Capacidades** y añade una entrada para cada dominio que admita tu aplicación, precedida de `applinks:`. Por ejemplo, `applinks:www.mywebsite.com`.

{% alert note %}
Apple recomienda limitar esta lista a no más de 20 ó 30 dominios.
{% endalert %}

### Paso 5: Prueba tu enlace universal

Añade el enlace universal a un correo electrónico y envíalo a un dispositivo de prueba. Si pegas un enlace universal directamente en el campo URL de Safari, la aplicación no se abrirá automáticamente. Si lo haces, tendrás que bajar manualmente el sitio web para que aparezca un aviso en la parte superior pidiéndote que abras la aplicación correspondiente.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Estos pasos están adaptados de la documentación para desarrolladores de Android. Para más información, consulta [Añadir enlaces a aplicaciones Android](https://developer.android.com/training/app-links#add-app-links) y [Crear enlaces profundos al contenido de las aplicaciones](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Los enlaces de las aplicaciones Android requieren un `IBrazeDeeplinkHandler` personalizado con lógica para gestionar los enlaces de sus dominios de forma separada de otras URL de la Web. Puede ser más fácil utilizar vínculos en profundidad en su lugar y mantener uniformes las prácticas de vinculación para canales distintos del correo electrónico.
{% endalert %}

### Paso 1: Crear vínculos profundos

En primer lugar, tienes que crear vínculos profundos para tu aplicación Android. Esto puede hacerse añadiendo [filtros de intención](https://developer.android.com/guide/components/intents-filters) en tu archivo `AndroidManifest.xml`. El filtro de intención debe incluir la acción `VIEW` y la categoría `BROWSABLE`, junto con la URL de tu sitio web en el elemento de datos.

### Paso 2: Asocia tu aplicación a tu sitio web

Tienes que asociar tu aplicación a tu sitio web. Esto puede hacerse creando un archivo de Enlaces de Activos Digitales. Este archivo debe estar en formato JSON e incluye detalles sobre las aplicaciones Android que pueden abrir enlaces a tu sitio web. Debe colocarse en el directorio `.well-known` de tu sitio web.

### Paso 3: Actualiza el archivo de manifiesto de tu aplicación

En tu archivo `AndroidManifest.xml`, añade un elemento de metadatos dentro del elemento de aplicación. El elemento de metadatos debe tener un atributo `android:name` de "asset_statements" y un atributo `android:resource` que apunte a un archivo de recursos con una cadena que incluya la URL de tu sitio web.

### Paso 4: Prepara tu aplicación para gestionar vínculos profundos

En tu aplicación Android, tienes que gestionar los vínculos profundos entrantes. Puedes hacerlo obteniendo la intención que inició tu actividad y extrayendo los datos de ella.

### Paso 5: Prueba tus vínculos profundos

Por último, puedes probar tus vínculos profundos. Enviarte un enlace a través de una aplicación de mensajería o correo electrónico y hacer clic en él. Si todo está configurado correctamente, debería abrir tu aplicación.

{% endtab %}
{% endtabs %}

## Enlaces universales, enlaces de aplicaciones y seguimiento de clics

{% alert note %}
Los enlaces de seguimiento de clics suelen configurarse como parte de tu incorporación al correo electrónico. Si esto no se completó durante la incorporación del cliente, ponte en contacto con tu director de cuentas para que te ayude.
{% endalert %}

Nuestros socios de envío por correo electrónico, SendGrid y SparkPost, utilizan dominios de seguimiento de clics para envolver todos los enlaces e incluir parámetros de URL para el seguimiento de clics en los correos electrónicos Braze.

Por ejemplo, un enlace como `https://www.example.com` se convierte en algo como `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Para permitir que los enlaces de correo electrónico con seguimiento de clics funcionen como enlaces universales o enlaces de aplicación, tendrás que realizar algunos ajustes adicionales. Asegúrate de añadir el dominio de seguimiento de clics (`links.email.example.com`) como dominio que la aplicación puede abrir. Además, el dominio de seguimiento de clics debe servir a los archivos AASA (iOS) o Enlaces de Activos Digitales (Android). Esto ayudará a garantizar que los enlaces de correo electrónico con seguimiento de clics funcionen fácilmente.

Si no quieres que todos los enlaces de seguimiento de clics sean enlaces universales o App Link, puedes especificar qué enlaces deben ser enlaces universales en función del socio de envío por correo electrónico. Consulta las secciones siguientes para más detalles.

### SendGrid

Para tratar un enlace de seguimiento de clics de SendGrid como un enlace universal:

1. Configura tus valores pathPrefix de AASA o AndroidManifest para que sólo traten los enlaces con `/uni/` en la ruta URL como enlaces universales.
2. Añade el atributo `universal="true"` a la etiqueta de anclaje de tu enlace (`<a>`). Esto cambia la ruta URL del enlace envuelto para incluir `/uni/`.

{% alert note %}
Para los correos electrónicos AMP, este atributo debe ser data-universal="true".
{% endalert %}

Por ejemplo:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\. Asegúrate de que tu aplicación está configurada para gestionar correctamente los enlaces empaquetados. Consulta el artículo de SendGrid sobre [Resolución de enlaces de seguimiento de clics de SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) y sigue los pasos correspondientes a tu sistema operativo. Este artículo contiene código de ejemplo para [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) y [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Con esta configuración, los enlaces con `/uni/` en la ruta URL funcionarán como enlaces universales, mientras que todos los demás enlaces funcionarán como enlaces Web.

### SparkPost

Para tratar un enlace de seguimiento de clics de SparkPost como un enlace universal, añade el siguiente atributo a la sección Atributos del editor de arrastrar y soltar para correo electrónico, o edita manualmente el HTML del enlace para incluir el siguiente atributo en la etiqueta de anclaje de tu enlace: `data-msys-sublink="custom_path"`.

Esta ruta personalizada te permite tratar selectivamente las URL con ese valor como un enlace universal.

Por ejemplo:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

A continuación, asegúrate de que tu aplicación está configurada para gestionar correctamente la ruta personalizada. Consulta el artículo de SparkPost sobre [Cómo utilizar el seguimiento de clics de SparkPost en los vínculos profundos](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Este artículo contiene código de ejemplo para [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) y [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

### Desactivar el seguimiento de clics enlace a enlace

Puedes desactivar el seguimiento de clics para enlaces específicos añadiendo código HTML a tu mensaje de correo electrónico para el editor HTML o a un bloque HTML para el editor de arrastrar y soltar.

#### SendGrid

Si tu proveedor de servicios de correo electrónico es SendGrid, utiliza el código HTML `clicktracking=off` de esta forma:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost 

Si tu proveedor de servicios de correo electrónico es SparkPost, utiliza el código HTML `data-msys-clicktrack="0"` así:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

Si tu proveedor de servicios de correo electrónico es Amazon SES, utiliza el código HTML `ses:no-track` de la siguiente manera:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Editor de arrastrar y soltar

Cuando utilices el editor de arrastrar y soltar de correo electrónico, introduce tu código HTML como atributo personalizado si tu enlace está unido a un texto, un botón o una imagen.

##### Atributo personalizado para un enlace de texto

#### SendGrid

Selecciona lo siguiente para el atributo personalizado:

- **Nombre:** `clicktracking`
- **Valor:** `off`

#### SparkPost

Selecciona lo siguiente para el atributo personalizado:

- **Nombre:** `data-msys-clicktrack`
- **Valor:** `0`

\![Un atributo personalizado para un enlace de texto.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Atributo personalizado para un botón o una imagen

#### SendGrid

Selecciona lo siguiente para el atributo personalizado:

- **Nombre:** `clicktracking`
- **Valor:** `off`
- **Tipo:** Enlace

#### SparkPost

Selecciona lo siguiente para el atributo personalizado:

- **Nombre:** `data-msys-clicktrack`
- **Valor:** `0`
- **Tipo:** Enlace

\![Un atributo personalizado para un botón.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Solución de problemas de enlaces universales con seguimiento de clics

Si tus enlaces universales no funcionan como esperas en tus correos electrónicos, como cuando el destinatario navega desde su aplicación de correo electrónico al navegador web antes de redirigirse finalmente a la aplicación, consulta estos consejos para solucionar problemas en la configuración de tu enlace universal.

#### Verificar la ubicación del archivo de enlace

Asegúrate de que el archivo AASA (iOS) o el archivo Enlaces a activos digitales (Android) se encuentra en la ubicación correcta:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

Es importante asegurarse de que estos archivos estén siempre accesibles públicamente. Si no puedes acceder a ellos, es posible que te hayas saltado algún paso al configurar los enlaces universales para el correo electrónico.

#### Verificar las definiciones de dominio

Asegúrate de que tienes las definiciones correctas de los dominios que tu aplicación puede abrir.

- **iOS:** Revisa los dominios asociados configurados en Xcode para tu aplicación[(paso 1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c)). Comprueba que el dominio de seguimiento de clics está incluido en esa lista.
- **Android:** Abre la página de información de la aplicación (pulsa prolongadamente el icono de la aplicación y haz clic en ⓘ). Dentro del menú de información de la aplicación, localiza **Abrir de forma predeterminada** y tócalo. Esto debería mostrar una pantalla con todos los enlaces verificados que la aplicación puede abrir. Comprueba que el dominio de seguimiento de clics está incluido en esa lista.


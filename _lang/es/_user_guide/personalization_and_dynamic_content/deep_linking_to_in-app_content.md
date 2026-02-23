---
nav_title: Vinculación en profundidad al contenido de la aplicación
article_title: Vinculación en profundidad al contenido de la aplicación
page_order: 3
description: "Este artículo de referencia explica cómo añadir enlaces profundos al contenido de los mensajes integrados en la aplicación."

---

# Vinculación en profundidad al contenido de la aplicación

## ¿Qué es la vinculación en profundidad?

La vinculación en profundidad es una forma de lanzar una aplicación nativa y proporcionar información adicional indicándole que realice una acción concreta o muestre un contenido específico.

Esto tiene tres partes:

1. Identifica qué aplicación iniciar.
2. Indica a la aplicación qué acción debe realizar.
3. Proporciona a la acción cualquier dato adicional que necesite.

Los enlaces profundos son URI personalizados que enlazan con una parte específica de la aplicación y contienen estas tres partes. La clave está en definir un esquema personalizado. `http:` es el esquema con el que casi todo el mundo está familiarizado, pero los esquemas pueden empezar por cualquier palabra. Un esquema debe empezar por una letra, pero puede contener letras, números, signos más, signos menos o puntos. En la práctica, no existe un registro central que evite los conflictos, por lo que es una buena práctica incluir su nombre de dominio en el esquema. Por ejemplo, `twitter://` es la URI de iOS para lanzar la aplicación móvil de X, antes Twitter.

Todo lo que aparece después de los dos puntos dentro de un enlace profundo es texto libre. Depende de ti definir su estructura e interpretación; sin embargo, una convención común es modelarla según las URL de `http:`, incluyendo un `//` inicial y parámetros de consulta (por ejemplo, `?foo=1&bar=2`). En el ejemplo anterior, `twitter://user?screen_name=[id]` se utilizaría para lanzar un perfil específico en la aplicación.

{% alert important %}
Braze no admite el uso de un envoltorio como Flutter para enviar vínculos profundos. Para utilizar esta característica, debes configurar los vínculos en profundidad en la capa nativa.
{% endalert %}

## Etiquetas UTM y atribución de campañas

### ¿Qué es una etiqueta UTM?

[Las etiquetas UTM (Urchin Traffic Manager)](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) le permiten incluir detalles de atribución de campañas directamente en los enlaces. Las etiquetas UTM son utilizadas por Google Analytics para recopilar datos de atribución de campañas y pueden utilizarse para realizar un seguimiento de las siguientes propiedades:

- `utm_source`: El identificador de la fuente del tráfico (por ejemplo,`my_app`)
- `utm_medium`: El medio de la campaña (por ejemplo,`newsfeed`)
- `utm_campaign`: El identificador de la campaña (por ejemplo,`spring_2016_campaign`)
- `utm_term`: Identificador de un término de búsqueda de pago que llevó al usuario a tu aplicación o sitio web (por ejemplo,`pizza`)
- `utm_content`: Un identificador del enlace o contenido específico sobre el que el usuario ha hecho clic (por ejemplo,`toplink` o `android_iam_button2`)

Las etiquetas UTM pueden incrustarse tanto en enlaces HTTP (web) normales como en enlaces profundos y rastrearse mediante Google Analytics.

### Usar etiquetas UTM con Braze

Si quieres utilizar etiquetas UTM con enlaces HTTP (Web) normales (por ejemplo, para hacer la atribución de campañas para tus campañas de correo electrónico) y tu organización ya utiliza Google Analytics, puedes utilizar [el creador de URL de Google](https://ga-dev-tools.google/ga4/campaign-url-builder/) para generar enlaces UTM. Estos enlaces pueden incrustarse fácilmente en el texto de la campaña Braze como cualquier otro enlace.

Para utilizar etiquetas UTM en los vínculos profundos de tu aplicación, ésta debe tener el [SDK de Google Analytics](https://developers.google.com/analytics/devguides/collection/) correspondiente integrado y correctamente configurado para gestionar los vínculos profundos. Consulta a tus desarrolladores si tienes dudas al respecto.

Una vez integrado y configurado el SDK de análisis, las etiquetas UTM pueden utilizarse con vínculos profundos en las campañas Braze. Para configurar etiquetas UTM para tu campaña, incluye las etiquetas UTM necesarias en la URL de destino o en los vínculos profundos. Los siguientes ejemplos muestran cómo utilizar etiquetas UTM en notificaciones push y mensajes in-app.

#### Atribución de aperturas push con etiquetas UTM

Para incluir etiquetas UTM en tus enlaces profundos para notificaciones push, configura el comportamiento al hacer clic del mensaje push para que sea un enlace profundo, luego escribe la dirección del enlace profundo e incluye las etiquetas UTM deseadas de la siguiente manera:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![]({% image_buster /assets/img_archive/push_utm_tags.png %})

#### Atribución de los clics de mensajes dentro de la aplicación con etiquetas UTM

Para incluir etiquetas UTM en los vínculos profundos de tus mensajes dentro de la aplicación, utiliza lo siguiente:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![]({% image_buster /assets/img_archive/iam_utm_tags.png %})


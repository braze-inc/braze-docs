---
nav_title: Vinculación en profundidad al contenido de la aplicación
article_title: Vinculación en profundidad al contenido de la aplicación
page_order: 3
description: "Este artículo de referencia explica cómo añadir enlaces profundos al contenido de los mensajes integrados en la aplicación."

---

# Vinculación en profundidad al contenido de la aplicación

## ¿Qué es la vinculación en profundidad?

La vinculación profunda es una forma de lanzar una aplicación nativa y proporcionar información adicional que le indique que realice una acción específica o muestre un contenido concreto.

Esto tiene tres partes:

1. Identificar qué aplicación lanzar
2. Indica a la aplicación qué acción debe realizar
3. Facilite a la acción cualquier dato adicional que necesite

Los enlaces profundos son URI personalizados que enlazan con una parte específica de la aplicación y contienen estas tres partes. La clave está en definir un esquema personalizado. `http:` es el esquema con el que casi todo el mundo está familiarizado, pero los esquemas pueden empezar por cualquier palabra. Un esquema debe empezar por una letra, pero puede contener letras, números, signos más, signos menos o puntos. En la práctica, no existe un registro central que evite los conflictos, por lo que es una buena práctica incluir su nombre de dominio en el esquema. Por ejemplo, `twitter://` es la URI de iOS para lanzar la aplicación móvil de X, antes Twitter.

Todo lo que aparece después de los dos puntos dentro de un enlace profundo es texto libre. La definición de su estructura e interpretación depende del usuario, aunque una convención común es modelarla a partir de las URL de `http:`, incluyendo un `//` inicial y parámetros de consulta (por ejemplo, `?foo=1&bar=2`). En el ejemplo anterior, `twitter://user?screen_name=[id]` se utilizaría para lanzar un perfil específico en la aplicación.

{% alert important %}
Braze no admite el uso de un envoltorio como Flutter para enviar vínculos profundos. Para utilizar esta característica, debes configurar los vínculos en profundidad en la capa nativa.
{% endalert %}


## Etiquetas UTM y atribución de campañas

### ¿Qué es una etiqueta UTM?

[Las etiquetas UTM (Urchin Traffic Manager)][4] le permiten incluir detalles de atribución de campañas directamente en los enlaces. Las etiquetas UTM son utilizadas por Google Analytics para recopilar datos de atribución de campañas y pueden utilizarse para realizar un seguimiento de las siguientes propiedades:

- `utm_source`: el identificador de la fuente del tráfico (por ejemplo,`my_app`)
- `utm_medium`el soporte de la campaña (por ejemplo,`newsfeed`)
- `utm_campaign`: el identificador de la campaña (por ejemplo,`spring_2016_campaign`)
- `utm_term`identificador de un término de búsqueda de pago que llevó al usuario a tu aplicación o sitio web (por ejemplo,`pizza`)
- `utm_content`identificador del enlace/contenido específico en el que ha hecho clic el usuario (por ejemplo,`toplink` o `android_iam_button2`)

Las etiquetas UTM pueden incrustarse tanto en enlaces HTTP (web) normales como en enlaces profundos y rastrearse mediante Google Analytics.

### Usar etiquetas UTM con Braze

Si desea utilizar etiquetas UTM con enlaces HTTP (web) normales -por ejemplo, para realizar la atribución de campañas para sus campañas de correo electrónico- y su organización ya utiliza Google Analytics, puede utilizar simplemente [el generador de URL de Google][6] para generar enlaces UTM. Estos enlaces pueden incrustarse fácilmente en el texto de la campaña Braze como cualquier otro enlace.

Para utilizar etiquetas UTM en los vínculos profundos de tu aplicación, ésta debe tener el [SDK de Google Analytics][5] correspondiente integrado y correctamente configurado para gestionar los vínculos profundos. Consulta a tus desarrolladores si tienes dudas al respecto.

Una vez integrado y configurado el SDK de análisis, las etiquetas UTM pueden utilizarse con vínculos profundos en las campañas Braze. Para configurar etiquetas UTM para tu campaña, incluye las etiquetas UTM necesarias en la URL de destino o en los vínculos profundos. Los siguientes ejemplos muestran cómo utilizar etiquetas UTM en notificaciones push y mensajes in-app.

#### Atribución de aperturas push con etiquetas UTM

Para incluir etiquetas UTM en tus enlaces profundos para notificaciones push, configura el comportamiento al hacer clic del mensaje push para que sea un enlace profundo, luego escribe la dirección del enlace profundo e incluye las etiquetas UTM deseadas de la siguiente manera:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![][8]

#### Atribución de los clics de mensajes dentro de la aplicación con etiquetas UTM

Para incluir etiquetas UTM en los vínculos profundos de tus mensajes dentro de la aplicación, utiliza lo siguiente:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![][10]

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/#Android_Deep_Advance
[4]: https://support.google.com/analytics/answer/1033863?hl=en
[5]: https://developers.google.com/analytics/devguides/collection/
[6]: https://support.google.com/analytics/answer/1033867
[8]: {% image_buster /assets/img_archive/push_utm_tags.png %}
[9]: {% image_buster /assets/img_archive/news_feed_utm_tags.png %}
[10]: {% image_buster /assets/img_archive/iam_utm_tags.png %}
[11]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/

---
nav_title: Señales
article_title: Insignias de fuente de noticias para iOS
platform: iOS
page_order: 3
description: "Este artículo de referencia explica cómo implementar el recuento de señales de fuentes de noticias en tu aplicación iOS."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Señales

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Solicitar recuentos de tarjetas de canal de noticias no leídas

![]({% image_buster /assets/img_archive/newsfeed_badges.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Las señales son una forma estupenda de llamar la atención sobre los nuevos contenidos que esperan a tus usuarios en la fuente de noticias. Si quieres añadir una señal a tu canal de noticias, el SDK de Braze proporciona métodos para consultar lo siguiente:

- Tarjetas de fuentes de noticias no leídas para el usuario actual
- Total de tarjetas de fuentes de noticias visibles para el usuario actual

Las siguientes declaraciones de métodos en [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "controlador de la fuente abk") lo describen con detalle:

```
- (NSInteger)unreadCardCountForCategories:(ABKCardCategory)categories;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)cardCountForCategories:(ABKCardCategory)categories;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once, even if they appear in multiple Content Cards views.
 */
 ```

## Mostrar el número de elementos no leídos de la fuente de noticias en el recuento de señales de la aplicación

Además de servir como recordatorios de notificaciones push para una aplicación, las señales también pueden indicar elementos no vistos en la fuente de noticias del usuario. Actualizar el recuento de señales en función de las actualizaciones de la Fuente de noticias no leídas puede ser una herramienta valiosa para atraer a los usuarios de nuevo a tu aplicación y aumentar las sesiones.

Llama a este método que registra el recuento de señales después de que se cierre la aplicación y finalice la sesión del usuario:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

{% endtab %}
{% endtabs %}

Dentro de este método, implementa el siguiente código, que actualiza activamente el recuento de señales mientras el usuario ve las tarjetas durante una sesión determinada.

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].feedController unreadCardCountForCategories:ABKCardCategoryAll];
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = Appboy.sharedInstance()?.feedController.unreadCardCount(forCategories: ABKCardCategory.all) ?? 0
```

{% endtab %}
{% endtabs %}

En cualquier momento, por ejemplo, en el método `applicationDidBecomeActive`, utiliza el código siguiente para borrar el recuento de señales:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

Para más información, consulta el `Appboy.h` [archivo de cabecera](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h Archivo de cabecera").


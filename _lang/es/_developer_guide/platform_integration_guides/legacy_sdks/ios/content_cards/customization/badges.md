---
nav_title: Señales
article_title: Señales de tarjetas de contenido para iOS
platform: iOS
page_order: 5
description: "Este artículo trata sobre cómo añadir señales a tus tarjetas de contenido en tu aplicación iOS."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Señales

## Solicitar recuentos de tarjetas de contenido no leídas

Si quieres mostrar el número de tarjetas de contenido no leídas que tiene tu usuario, te sugerimos que solicites un recuento de tarjetas y lo representes con una Señal. Las señales son una forma estupenda de llamar la atención sobre los nuevos contenidos que esperan a tus usuarios en las tarjetas de contenido. Si quieres añadir una señal a tus tarjetas de contenido, el SDK de Braze proporciona métodos para consultar lo siguiente:

- Tarjetas de contenido sin ver para el usuario actual
- Total de tarjetas de contenido visible para el usuario actual

Las siguientes declaraciones de métodos en [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html) describen esto en detalle:

```objc
- (NSInteger)unviewedContentCardCount;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)contentCardCount;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once even if they appear in multiple Content Cards views.
 */
```

## Mostrar el número de tarjetas de contenido no vistas en el recuento de señales de la aplicación

Además de servir como recordatorios de notificaciones push para una aplicación, las señales también pueden utilizarse para indicar elementos no vistos en la fuente de tarjetas de contenido del usuario. Actualizar el recuento de señales en función de las actualizaciones de las tarjetas de contenido no vistas puede ser valioso para atraer a los usuarios de nuevo a tu aplicación y aumentar las sesiones.

Este método registra el recuento de señales después de que se cierre la aplicación y finalice la sesión del usuario:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Dentro de este método, implementa el siguiente código, que actualiza activamente el recuento de señales mientras el usuario ve las tarjetas durante una sesión determinada:

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].contentCardsController unviewedContentCardCount];
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Dentro de este método, implementa el siguiente código, que actualiza activamente el recuento de señales mientras el usuario ve las tarjetas durante una sesión determinada:

```swift
UIApplication.shared.applicationIconBadgeNumber =
  Appboy.sharedInstance()?.contentCardsController.unviewedContentCardCount() ?? 0
```

{% endtab %}
{% endtabs %}

Para más información, consulta el [archivo de cabecera](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`.

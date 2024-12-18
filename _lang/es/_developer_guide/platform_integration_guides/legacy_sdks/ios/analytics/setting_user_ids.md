---
nav_title: Configuración de ID de usuario
article_title: Configuración de ID de usuario para iOS
platform: iOS
page_order: 1
description: "Este artículo de referencia muestra cómo establecer ID de usuario en tu aplicación de iOS, las convenciones de nomenclatura de ID de usuario sugeridas y algunas buenas prácticas."
 
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuración de ID de usuario para iOS

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Convención de nomenclatura de ID de usuario sugerida

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Asignar un ID de usuario

Debes realizar la siguiente llamada en cuanto se identifique el usuario (generalmente después de iniciar la sesión) para establecer el ID de usuario:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance] changeUser:@"YOUR_USER_ID_STRING"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.changeUser("YOUR_USER_ID")
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**No llames a `changeUser()` cuando un usuario cierra la sesión. `changeUser()` solo se debe llamar cuando el usuario inicia sesión en la aplicación.** Si configuras [`changeUser()`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69%20%22changeuser%22) a un valor predeterminado estático asociará TODA la actividad del usuario a ese "usuario" predeterminado hasta que el usuario vuelva a conectarse.
{% endalert %}

Asegúrate de llamar a este método en el hilo principal de tu aplicación. Llamar al método de forma asíncrona puede provocar un comportamiento indefinido.

Además, te recomendamos que no cambies el ID de usuario cuando un usuario cierra la sesión, ya que esto hace que no puedas dirigirte al usuario que había iniciado sesión anteriormente con campañas de reactivación de la interacción. Si prevés varios usuarios en el mismo dispositivo, pero sólo quieres dirigirte a uno de ellos cuando tu aplicación esté desconectada, te recomendamos que hagas un seguimiento por separado del ID de usuario al que quieres dirigirte mientras está desconectado y que vuelvas a cambiar a ese ID de usuario como parte del proceso de cierre de sesión de tu aplicación.

## Prácticas recomendadas y notas sobre la integración del ID de usuario

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Asignación de alias de usuarios

{% multi_lang_include archive/setting_user_ids/aliasing.md plataforma="iOS" %}


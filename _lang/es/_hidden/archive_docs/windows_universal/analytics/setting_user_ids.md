---
nav_title: Configuración de ID de usuario
article_title: Configuración de ID de usuario para Windows Universal
platform: Windows Universal
page_order: 1
description: "En este artículo de referencia se explica cómo configurar ID de usuario en la plataforma Universal de Windows."
hidden: true
---

# Configuración de los ID de usuario
{% multi_lang_include archive/windows_deprecation.md %}

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Debes realizar la siguiente llamada en cuanto se identifique el usuario (generalmente después de iniciar la sesión) para establecer el ID de usuario:

```csharp
Appboy.SharedInstance.ChangeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**No llames a `changeUser()` cuando un usuario cierra la sesión. `changeUser()` solo se debe llamar cuando el usuario inicia sesión en la aplicación.** Si configuras `changeUser()` con un valor predeterminado estático, se asociará TODA la actividad del usuario con ese "usuario" predeterminado hasta que vuelva a conectarse.
{% endalert %}

Además, te recomendamos que no cambies el ID de usuario cuando un usuario cierra la sesión, ya que esto hace que no puedas dirigirte al usuario que había iniciado sesión anteriormente con campañas de reactivación de la interacción. Si prevés varios usuarios en el mismo dispositivo, pero sólo quieres dirigirte a uno de ellos cuando tu aplicación esté desconectada, te recomendamos que hagas un seguimiento por separado del ID de usuario al que quieres dirigirte mientras está desconectado y que vuelvas a cambiar a ese ID de usuario como parte del proceso de cierre de sesión de tu aplicación.

## Convención de nomenclatura de ID de usuario sugerida

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Prácticas recomendadas y notas sobre la integración del ID de usuario

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/developer_guide/rest_api/messaging/
[6]: http://developer.android.com/reference/java/util/Locale.html#default_locale "Documentación para desarrolladores de Android - Localización"

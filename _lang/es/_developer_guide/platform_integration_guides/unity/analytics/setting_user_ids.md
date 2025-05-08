---
nav_title: Configuración de ID de usuario
article_title: Configuración de ID de usuario para Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 0
description: "En este artículo de referencia se explica cómo configurar los ID de usuario en la plataforma Unity, incluyendo las convenciones de nomenclatura sugeridas y las mejores prácticas."
 
---

# Configuración de los ID de usuario

> En este artículo de referencia se explica cómo configurar los ID de usuario en la plataforma Unity, incluyendo las convenciones de nomenclatura sugeridas y las mejores prácticas.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Debes realizar la siguiente llamada en cuanto se identifique el usuario (generalmente después de iniciar la sesión) para establecer el ID de usuario:

```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```

{% alert warning %}
**No llames a `ChangeUser()` cuando un usuario cierra la sesión. `ChangeUser()` solo se debe llamar cuando el usuario inicia sesión en la aplicación.** Si configuras `ChangeUser()` con un valor predeterminado estático, se asociará TODA la actividad del usuario con ese "usuario" predeterminado hasta que vuelva a conectarse.
{% endalert %}

Además, te recomendamos que no cambies el ID de usuario cuando un usuario cierra la sesión, ya que esto hace que no puedas dirigirte al usuario que había iniciado sesión anteriormente con campañas de reactivación de la interacción. Si prevés varios usuarios en el mismo dispositivo, pero sólo quieres dirigirte a uno de ellos cuando tu aplicación esté desconectada, te recomendamos que hagas un seguimiento por separado del ID de usuario al que quieres dirigirte mientras está desconectado y que vuelvas a cambiar a ese ID de usuario como parte del proceso de cierre de sesión de tu aplicación.

## Convención de nomenclatura de ID de usuario sugerida

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Prácticas recomendadas y notas sobre la integración del ID de usuario

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/

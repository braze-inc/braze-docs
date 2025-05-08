---
nav_title: Configuración de ID de usuario
article_title: Configuración de ID de usuario para la Web
platform: Web
page_order: 1
page_type: reference
description: "Este artículo describe cómo establecer ID de usuario para cada uno de tus usuarios, incluyendo las mejores prácticas y los puntos importantes a tener en cuenta antes de realizar cualquier cambio."
 
---

# Configuración de los ID de usuario

> Este artículo describe cómo establecer ID de usuario para cada uno de tus usuarios, incluyendo las mejores prácticas y los puntos importantes a tener en cuenta antes de realizar cualquier cambio.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Debes realizar la siguiente llamada en cuanto se identifique el usuario (generalmente después de iniciar la sesión) para establecer el ID de usuario:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**No llames a `changeUser()` cuando un usuario se desconecte.** Si configuras `changeUser()` con un valor predeterminado estático, se asociará TODA la actividad del usuario con ese "usuario" predeterminado hasta que vuelva a conectarse.
{% endalert %}

Te recomendamos que no cambies el ID de usuario cuando un usuario cierra la sesión, ya que esto hace que no puedas dirigirte al usuario que había iniciado sesión anteriormente con campañas de reactivación de la interacción. Si prevés varios usuarios en el mismo dispositivo, pero sólo quieres dirigirte a uno de ellos cuando tu aplicación esté desconectada, te recomendamos que hagas un seguimiento por separado del ID de usuario al que quieres dirigirte mientras está desconectado y que vuelvas a cambiar a ese ID de usuario como parte del proceso de cierre de sesión de tu aplicación.

Consulta la [documentación de`changeUser()` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser "Javadocs") para obtener más información.

## Convención de nomenclatura de ID de usuario sugerida

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Prácticas recomendadas y notas sobre la integración del ID de usuario

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Asignación de alias de usuarios

{% multi_lang_include archive/setting_user_ids/aliasing.md plataforma="Web" %}


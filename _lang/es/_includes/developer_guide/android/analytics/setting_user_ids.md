 
# Configuración de los ID de usuario
 
> Este artículo de referencia muestra cómo configurar ID de usuario en tu aplicación Android o FireOS, las convenciones sugeridas para nombrar ID de usuario y algunas buenas prácticas.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Convención de nomenclatura de ID de usuario sugerida

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### Asignar un ID de usuario

Debes realizar la siguiente llamada en cuanto se identifique el usuario (generalmente después de iniciar la sesión) para establecer el ID de usuario:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**No llames a `changeUser()` cuando un usuario cierra la sesión. `changeUser()` solo se debe llamar cuando el usuario inicia sesión en la aplicación.** Si configuras `changeUser()` con un valor predeterminado estático, se asociará TODA la actividad del usuario con ese "usuario" predeterminado hasta que vuelva a conectarse.
{% endalert %}

Además, te recomendamos **que no** cambies el ID de usuario cuando un usuario cierra la sesión, ya que esto hace que no puedas dirigirte al usuario que había iniciado sesión anteriormente con campañas de reactivación de la interacción. Si prevés varios usuarios en el mismo dispositivo, pero sólo quieres dirigirte a uno de ellos cuando tu aplicación esté desconectada, te recomendamos que hagas un seguimiento por separado del ID de usuario al que quieres dirigirte mientras está desconectado y que vuelvas a cambiar a ese ID de usuario como parte del proceso de cierre de sesión de tu aplicación.

Consulta la documentación [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) para más información.

## Prácticas recomendadas y notas sobre la integración del ID de usuario

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Asignación de alias de usuarios

{% multi_lang_include archive/setting_user_ids/aliasing.md plataforma="Android" %}


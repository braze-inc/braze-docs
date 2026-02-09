{% multi_lang_include developer_guide/prerequisites/react_native.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Habilitación de historias push

Para el SDK de React Native, **las historias push están disponibles para Android de forma predeterminada**.

Para habilitar las historias push en iOS mediante Expo, asegúrate de que tienes un grupo de aplicaciones definido para tu aplicación. Para más información, consulta [Añadir un grupo de aplicaciones]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

A continuación, configura la propiedad `enableBrazeIosPushStories` en `true` y asigna el ID de tu grupo de aplicaciones a `iosPushStoryAppGroup` en tu objeto `expo.plugins` en `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

Por último, añade el identificador de paquete de esta extensión de aplicación a la configuración de credenciales de tu proyecto: `<your-app-bundle-id>.BrazeExpoPushStories`. Para más detalles sobre este proceso, consulta [Utilizar extensiones de aplicación con los Servicios de Aplicación Expo]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions).

{% alert warning %}
Si utilizas historias push con los servicios de aplicaciones Expo, asegúrate de utilizar la bandera `EXPO_NO_CAPABILITY_SYNC=1` al ejecutar `eas build`. Hay un problema conocido en la línea de comandos que elimina la capacidad de Grupos de aplicaciones del perfil de aprovisionamiento de tu extensión.
{% endalert %}

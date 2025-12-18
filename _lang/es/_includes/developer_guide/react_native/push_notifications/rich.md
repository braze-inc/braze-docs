{% multi_lang_include developer_guide/prerequisites/react_native.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Utilizar Expo para habilitar las notificaciones push enriquecidas

Para el SDK de React Native, **las notificaciones push enriquecidas están disponibles para Android de forma predeterminada**.

Para habilitar las notificaciones push enriquecidas en iOS mediante Expo, configura la propiedad `enableBrazeIosRichPush` en `true` en tu objeto `expo.plugins` en `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

Por último, añade el identificador de paquete de esta extensión de aplicación a la configuración de credenciales de tu proyecto: `<your-app-bundle-id>.BrazeExpoRichPush`. Para más detalles sobre este proceso, consulta [Utilizar extensiones de aplicación con los Servicios de Aplicación Expo]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions).

{% multi_lang_include developer_guide/prerequisites/react_native.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Habilitando histórias por push

Para o SDK do React Native, **histórias por push estão disponíveis para Android por padrão**.

Para ativar os stories por push no iOS usando o Expo, é necessário ter um grupo de app definido para seu aplicativo. Para saber mais, veja [Adicionando um grupo de app]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

Em seguida, configure a propriedade `enableBrazeIosPushStories` para `true` e atribua o ID do grupo de app a `iosPushStoryAppGroup` em seu objeto `expo.plugins` em `app.json`:

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

Por fim, adicione o identificador de pacote para essa extensão de app à configuração de credenciais de seu projeto: `<your-app-bundle-id>.BrazeExpoPushStories`. Para obter mais detalhes sobre esse processo, consulte [Uso de extensões de app com o Expo Application Services]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions).

{% alert warning %}
Se estiver usando stories por push com o Expo Application Services, use o sinalizador `EXPO_NO_CAPABILITY_SYNC=1` ao executar `eas build`. Há um problema conhecido na linha de comando que remove o recurso Grupos de app do perfil de provisionamento de sua extensão.
{% endalert %}

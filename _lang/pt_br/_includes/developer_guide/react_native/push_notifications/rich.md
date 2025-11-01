{% multi_lang_include developer_guide/prerequisites/react_native.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Uso da Expo para ativar notificações por push avançadas

Para o React Native SDK, **as notificações por push avançadas estão disponíveis para Android por padrão**.

Para ativar notificações por push avançadas no iOS usando o Expo, configure a propriedade `enableBrazeIosRichPush` como `true` em seu objeto `expo.plugins` em `app.json`:

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

Por fim, adicione o identificador de pacote para essa extensão de app à configuração de credenciais de seu projeto: `<your-app-bundle-id>.BrazeExpoRichPush`. Para obter mais detalhes sobre esse processo, consulte [Uso de extensões de app com o Expo Application Services]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions).

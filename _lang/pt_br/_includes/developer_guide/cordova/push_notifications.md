{% multi_lang_include developer_guide/prerequisites/cordova.md %} Após integrar o SDK, a funcionalidade básica de notificação por push é ativada por padrão. Para usar [notificações por push ricas]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) e [histórias por push]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova), você precisará configurá-las individualmente. Para usar mensagens por push no iOS, você também precisa fazer upload de um certificado de push válido.

{% alert warning %}
Sempre que você adicionar, remover ou atualizar seus plugins Cordova, o Cordova irá sobrescrever o Podfile no projeto Xcode do seu app iOS. Isso significa que você precisará configurar esses recursos novamente sempre que modificar seus plugins Cordova.
{% endalert %}

## Desabilitando notificações por push básicas (apenas iOS)

Após integrar o SDK Braze Cordova para iOS, a funcionalidade básica de notificação por push é ativada por padrão. Para desabilitar essa funcionalidade no seu app iOS, adicione o seguinte ao seu `config.xml` arquivo. Para saber mais, veja [Configurações opcionais]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```

{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Ativando o deep linking por push

Por padrão, o SDK Braze Cordova não lida automaticamente com o deep linking por push a partir de notificações. Para ativar o deep linking por push, adicione as seguintes preferências ao elemento `platform` no arquivo `config.xml` do seu projeto.

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_forward_universal_links" value="YES" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
</platform>
```

Para personalizar o comportamento da pilha de retorno quando os deep links são seguidos, você também pode adicionar essas preferências opcionais:

```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="YOUR_ACTIVITY_CLASS_NAME" />
</platform>
```
{% endtab %}
{% endtabs %}

Para uma lista completa de opções de configuração de push disponíveis, veja [Configurações opcionais]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

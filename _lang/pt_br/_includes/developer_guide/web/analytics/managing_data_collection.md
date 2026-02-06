## Desativar o rastreamento de dados

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab standard implementation %}
Para desativar a atividade de rastreamento de dados no Web SDK, use o método [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). Isso sincronizará todos os dados registrados antes da chamada para `disableSDK()` e fará com que todas as chamadas subsequentes para o Braze Web SDK para essa página e para futuros carregamentos de página sejam ignoradas.
{% endtab %}

{% tab google tag manager %}
Use o tipo de tag **Disable Tracking (Desativar rastreamento** ) ou **Resume Tracking (Retomar rastreamento)** para desativar ou reativar o rastreamento da Web, respectivamente. Essas duas opções chamam [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) e [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).
{% endtab %}
{% endtabs %}

### Melhores práticas

Para oferecer aos usuários a opção de interromper o rastreamento, recomendamos a criação de uma página simples com dois links ou botões: um que chama `disableSDK()` quando clicado e outro que chama `enableSDK()` para permitir que os usuários aceitem novamente. Você pode usar esses controles para iniciar ou parar o rastreamento por meio de outros sub-processadores de dados também.

{% alert note %}
O SDK do Braze não precisa ser inicializado para chamar `disableSDK()`, o que permite desativar o rastreamento para usuários totalmente anônimos. Por outro lado, `enableSDK()` não inicializa o SDK da Braze, então você também deve chamar `initialize()` depois para ativar o rastreamento.
{% endalert %}

## Retomada do rastreamento de dados

Para retomar a coleta de dados, você pode usar o método [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) método.

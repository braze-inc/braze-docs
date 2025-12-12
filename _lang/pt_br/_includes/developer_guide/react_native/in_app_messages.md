{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Tipos de mensagens

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Modelo de dados

O modelo de mensagem no app está disponível no SDK do React Native. Braze tem quatro tipos de mensagem no app que compartilham o mesmo modelo de dados: **slideup**, **modal**, **full** e **HTML full**.

### Mensagens

O modelo de mensagem no app fornece a base para todas as mensagens no app.

|Propriedade          | Descrição                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | A representação JSON da mensagem.                                                                                |
|`message`         | O texto da mensagem.                                                                                                      |
|`header`          | O cabeçalho da mensagem.                                                                                                    |
|`uri`             | O URI associado à ação de clique do botão.                                                                       |
|`imageUrl`        | A URL da imagem da mensagem.                                                                                                 |
|`zippedAssetsUrl` | Os ativos compactados preparados para exibir conteúdo HTML.                                                                    |
|`useWebView`      | Indica se a ação de clique do botão deve redirecionar usando uma visualização da web.                                            |
|`duration`        | A duração de exibição da mensagem.                                                                                          |
|`clickAction`     | O tipo de ação de clique do botão. Os tipos são: `URI`, e `NONE`.                                     |
|`dismissType`     | O tipo de fechamento da mensagem. Os dois tipos são: `SWIPE` e `AUTO_DISMISS`.                                                 |
|`messageType`     | O tipo de mensagem no app suportado pelo SDK. Os quatro tipos são: `SLIDEUP`, `MODAL`, `FULL` e `HTML_FULL`.          |
|`extras`          | O dicionário de extras da mensagem. Valor padrão: `[:]`.                                                                   |
|`buttons`         | A lista de botões na mensagem no app.                                                                             |
|`toString()`      | A mensagem como uma string de representação.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do modelo de mensagem no app, consulte a documentação para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) e para [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

### Botões

Botões podem ser adicionados às mensagens no app para realizar ações e registrar análise de dados. O modelo de botão fornece a base para todos os botões de mensagem no app.

|Propriedade          | Descrição                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | O texto no botão.                                                                                                     |
|`uri`             | O URI associado à ação de clique do botão.                                                                            |
|`useWebView`      | Indica se a ação de clique do botão deve redirecionar usando uma visualização da web.                                                 |
|`clickAction`     | O tipo de ação de clique processada quando o usuário clica no botão. Os tipos são: `URI`, e `NONE`. |
|`id`              | O ID do botão na mensagem.                                                                                               |
|`toString()`      | A representação do botão como uma string.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do modelo de botão, consulte a documentação para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) e para [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button).

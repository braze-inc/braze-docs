---
nav_title: Cartões de conteúdo
article_title: Cartões de conteúdo para o Flutter
platform: Flutter
page_order: 3
page_type: reference
description: "Este artigo aborda como começar a usar os cartões de conteúdo para apps Flutter."
channel: content cards

---

# integração do cartão de conteúdo

> Este artigo aborda como configurar os cartões de conteúdo para seu app Flutter.

O SDK da Braze inclui um feed de cartão padrão para você começar com os Cartões de Conteúdo. Para mostrar o feed do cartão, você pode usar o método `braze.launchContentCards()`. O feed de cartão padrão incluído com o SDK da Braze lidará com toda a análise de dados, rastreamento, dispensas e renderização para os cartões de conteúdo de um usuário.

## Personalização

Você pode usar esses métodos adicionais para criar um feed de cartões de conteúdo personalizado em seu app usando os seguintes métodos disponíveis na [interface pública do plug-in](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart):

| Método                                         | Descrição                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Solicita os cartões de conteúdo mais recentes do servidor SDK da Braze.                                           |
| `braze.logContentCardClicked(contentCard)`    | Registra um clique para o objeto do cartão de conteúdo fornecido.                                                            |
| `braze.logContentCardImpression(contentCard)` | Registra uma impressão para o objeto de cartão de conteúdo fornecido.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Registra uma dispensa para o objeto do cartão de conteúdo fornecido.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Recebimento de dados do cartão de conteúdo

Para receber dados de cartões de conteúdo em seu app Flutter, o `BrazePlugin` é compatível com o envio de dados de cartões de conteúdo usando o [Dart Streams](https://dart.dev/tutorials/language/streams).

O [objeto](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) `BrazeContentCard` é compatível com um subconjunto de campos disponíveis nos objetos do modelo nativo, incluindo , `description`, `title`, `image`, `url`, `extras`, entre outros.

### Etapa 1: Ouça os dados do cartão de conteúdo na camada Dart

Para receber os dados do cartão de conteúdo na camada Dart, use o código abaixo para criar um `StreamSubscription` e chamar `braze.subscribeToContentCards()`. Lembre-se de `cancel()` a inscrição de fluxo quando ela não for mais necessária.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Para obter um exemplo, consulte [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) em nosso app de amostra.

### Etapa 2: Encaminhar dados do cartão de conteúdo da camada nativa

Para receber os dados na camada Dart da etapa 1, adicione o seguinte código para encaminhar os dados do cartão de conteúdo das camadas nativas.

{% tabs %}
{% tab Android %}

Os dados do cartão de conteúdo são encaminhados automaticamente da camada do Android.

{% endtab %}
{% tab iOS %}

1. Implemente `contentCards.subscribeToUpdates` para assinar atualizações de cartões de conteúdo, conforme descrito na documentação [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)).

2. Sua implementação de retorno de chamada `contentCards.subscribeToUpdates` deve chamar `BrazePlugin.processContentCards(contentCards)`.

Para obter um exemplo, consulte [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) em nosso app de amostra.

{% endtab %}
{% endtabs %}

#### Reprodução da chamada de retorno para cartões de conteúdo

Para armazenar quaisquer cartões de conteúdo disparados antes que o retorno de chamada esteja disponível e reproduzi-los depois que ele for definido, adicione a seguinte entrada ao mapa `customConfigs` ao inicializar o `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Teste de exibição do cartão de conteúdo de amostra

Siga estas etapas para testar um cartão de conteúdo de amostra.

1. Defina um usuário ativo no app React chamando o método `braze.changeUserId('your-user-id')`.
2. Vá para **Campaigns (Campanhas** ) e siga [este guia]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create) para criar uma nova campanha de Content Card (Cartão de conteúdo).
3. Crie sua campanha de teste do cartão de conteúdo e vá para a guia **Teste**. Adicione o mesmo `user-id` que o usuário teste e clique em **Send Test (Enviar teste**).
4. Toque na notificação por push e isso deve abrir um cartão de conteúdo em seu dispositivo. Talvez seja necessário atualizar seu feed para que ele seja exibido.

![Uma campanha do Braze Content Card mostrando que você pode adicionar seu próprio ID de usuário como destinatário de teste para testar seu Content Card.]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

Para obter mais detalhes sobre cada plataforma, siga os guias de [integração do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/) ou [integração do iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui).

## Suporte a GIFs

{% multi_lang_include wrappers/gif_support/content_cards.md %}


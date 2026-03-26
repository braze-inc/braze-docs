## Sobre os Cartões de Conteúdo do Flutter

O SDK da Braze inclui um feed de cartão padrão para você começar com os Cartões de Conteúdo. Para mostrar o feed do cartão, você pode usar o método `braze.launchContentCards()`. O feed de cartão padrão incluído com o SDK da Braze lidará com toda a análise de dados, rastreamento, dispensas e renderização dos cartões de conteúdo de um usuário.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Métodos do cartão

Você pode usar esses métodos adicionais para criar um feed de Cartões de Conteúdo personalizado no seu app usando os seguintes métodos disponíveis na [interface pública do plug-in](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart):

| Método                                         | Descrição                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Solicita os Cartões de Conteúdo mais recentes do servidor do SDK da Braze.                                           |
| `braze.logContentCardClicked(contentCard)`    | Registra um clique para o objeto do cartão de conteúdo fornecido.                                                            |
| `braze.logContentCardImpression(contentCard)` | Registra uma impressão para o objeto do cartão de conteúdo fornecido.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Registra uma dispensa para o objeto do cartão de conteúdo fornecido.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Recebimento de dados do cartão de conteúdo

Para receber dados de cartões de conteúdo no seu app Flutter, o `BrazePlugin` oferece suporte ao envio de dados de cartões de conteúdo usando [Dart Streams](https://dart.dev/tutorials/language/streams).

O [objeto](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) `BrazeContentCard` oferece suporte a um subconjunto de campos disponíveis nos objetos do modelo nativo, incluindo `description`, `title`, `image`, `url`, `extras`, entre outros.

### Ouvir dados do cartão de conteúdo na camada Dart

Para receber os dados do cartão de conteúdo na camada Dart, use o código abaixo para criar um `StreamSubscription` e chamar `braze.subscribeToContentCards()`. Lembre-se de usar `cancel()` na inscrição do stream quando ela não for mais necessária.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Para ver um exemplo, consulte [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) no app de amostra do SDK Flutter da Braze.

### Encaminhar dados do cartão de conteúdo da camada nativa do iOS

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Os dados do cartão de conteúdo são encaminhados automaticamente das camadas nativas do Android e do iOS. Nenhuma configuração adicional é necessária.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Se você estiver usando o Flutter SDK 17.1.0 ou anterior, o encaminhamento de dados do cartão de conteúdo da camada nativa do iOS requer configuração manual. Seu aplicativo provavelmente contém um retorno de chamada `contentCards.subscribeToUpdates` que chama `BrazePlugin.processContentCards(contentCards)`. Para migrar para o Flutter SDK 18.0.0, remova a chamada `BrazePlugin.processContentCards(_:)` — o encaminhamento de dados agora é feito automaticamente.

Para ver um exemplo, consulte [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) no app de amostra do SDK Flutter da Braze.

{% endtab %}
{% endtabs %}

#### Reprodução do retorno de chamada para cartões de conteúdo

Para armazenar quaisquer cartões de conteúdo disparados antes que o retorno de chamada esteja disponível e reproduzi-los depois que ele for definido, adicione a seguinte entrada ao mapa `customConfigs` ao inicializar o `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

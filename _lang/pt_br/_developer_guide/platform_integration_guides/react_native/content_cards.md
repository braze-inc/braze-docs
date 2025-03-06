---
nav_title: Cartões de conteúdo
article_title: Cartões de conteúdo para React Native
platform: React Native
page_order: 3
page_type: reference
description: "Este artigo aborda como começar a usar os cartões de conteúdo para apps React Native."
channel: content cards

---

# Integração do cartão de conteúdo

> Este artigo aborda como configurar cartões de conteúdo para o React Native.

Os SDKs da Braze incluem um feed de cartão padrão para que você comece a usar os cartões de conteúdo. Para mostrar o feed do cartão, você pode usar o método `Braze.launchContentCards()`. O feed de cartão padrão incluído com o SDK da Braze lidará com toda a análise de dados, rastreamento, dispensas e renderização para os cartões de conteúdo de um usuário.

## Personalização

Para criar sua própria interface do usuário, você pode obter uma lista de cartões disponíveis e ouvir as atualizações dos cartões:

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
Se você optar por criar sua própria interface do usuário para exibir cartões, deverá chamar `logContentCardImpression` para receber análises de dados desses cartões. Isso inclui os cartões `control`, que devem ser rastreados mesmo que não sejam exibidos ao usuário.
{% endalert %}

Você pode usar esses métodos adicionais para criar um feed de cartões de conteúdo personalizado em seu aplicativo:

| Método                                   | Descrição                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Inicia o elemento da interface do usuário dos cartões de conteúdo.                                                                 |
| `requestContentCardsRefresh()`           | Solicita os cartões de conteúdo mais recentes do servidor do SDK da Braze. A lista de cartões resultante é passada para cada um dos [ouvintes de eventos de cartão de conteúdo](#customization) registrados anteriormente. |
| `getContentCards()`                      | Recupera os cartões de conteúdo do Braze SDK. Isso retorna uma promessa que é resolvida com a lista mais recente de cartões do servidor. |
| `getCachedContentCards()`                | Retorna a matriz de cartões de conteúdo mais recente do cache.                                            |
| `logContentCardClicked(cardId)`          | Registra um clique para o ID do cartão de conteúdo fornecido. Esse método é usado apenas para análise de dados. Para executar a ação de clique, chame também `processContentCardClickAction(cardId)`.                                                        |
| `logContentCardImpression(cardId)`       | Registra uma impressão para o ID do cartão de conteúdo fornecido.                                                      |
| `logContentCardDismissed(cardId)`        | Registra um descarte de cartão para o cartão de conteúdo ID fornecido.                                                        |
| `processContentCardClickAction(cardId)`  | Executar a ação de um determinado cartão.                                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Teste de exibição do cartão de conteúdo de amostra

Siga estas etapas para testar um cartão de conteúdo de amostra.

1. Defina um usuário ativo no aplicativo React chamando o método [`Braze.changeUser('your-user-id')`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
2. Vá para **Campaigns (Campanhas** ) e siga [este guia]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create) para criar uma nova campanha de Content Card (Cartão de conteúdo).
3. Crie sua campanha de teste do cartão de conteúdo e vá para a guia **Teste**. Adicione o mesmo `user-id` que o usuário teste e clique em **Send Test (Enviar teste**). Em breve, será possível iniciar um cartão de conteúdo em seu dispositivo.

![Uma campanha de cartão de conteúdo Braze mostrando que você pode adicionar seu próprio ID de usuário como um destinatário de teste para testar seu cartão de conteúdo.]({% image_buster /assets/img/react-native/content-card-test.png %} "Teste de Campanha de Cartão de Conteúdo")

Para obter mais integrações, siga as [instruções de integração do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/) ou [as instruções de integração do iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui), dependendo de sua plataforma.

Uma implementação de exemplo disso pode ser encontrada no BrazeProject dentro do [React Native SDK](https://github.com/braze-inc/braze-react-native-sdk).

## Modelo de dados do cartão de conteúdo

O modelo de dados dos cartões de conteúdo está disponível no React Native SDK. Para uma referência completa do modelo de dados do cartão de conteúdo, consulte a documentação para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) e para [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).

O SDK React Native do Braze tem três tipos exclusivos de cartões de conteúdo que compartilham um modelo básico: **somente imagem**, **imagem com legenda** e **clássico**.

Há também um tipo de cartão **de controle** especial, que é retornado aos usuários que estão no grupo de controle de um determinado cartão.

Cada tipo herda propriedades comuns de um modelo básico e tem as seguintes propriedades adicionais.

### Propriedades do modelo do cartão de conteúdo básico

O modelo de cartão básico fornece o comportamento fundamental para todos os cartões.

|Propriedade      | Descrição                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
|`id`          | O ID do cartão definido pela Braze.                                                                                            |
|`created`     | O registro de data e hora UNIX da hora de criação do cartão na Braze.                                                             |
|`expiresAt`   | O registro de data e hora UNIX do tempo de expiração do cartão. Quando o valor é menor que 0, isso significa que o cartão nunca expira.      |
|`viewed`      | Se o cartão foi lido ou não pelo usuário. Isso não registra análise de dados.                                           |
|`clicked`     | Se o cartão foi clicado pelo usuário.                                                                         |
|`pinned`      | Se o cartão está fixado.                                                                                            |
|`dismissed`   | Se o usuário dispensou este cartão. Marcar um cartão como dispensado que já foi dispensado será uma operação nula. |
|`dismissible` | Se o cartão é descartável pelo usuário.                                                                           |
|`url`         | (Opcional) A string de URL associada à ação de clique do cartão.                                                       |
|`openURLInWebView` | Se os URLs para este cartão devem ser abertos no WebView do Braze ou não.                                            |
|`isControl`   | Se este cartão é um cartão de controle. Os cartões de controle não devem ser exibidos ao usuário.                                |
|`extras`      | O mapa de extras de chave-valor para este cartão.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do cartão base, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Propriedades do modelo de cartão de conteúdo somente de imagem

Os cartões somente de imagem são imagens clicáveis e em tamanho real.

|Propriedade           | Descrição                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | O tipo de cartão de conteúdo, `IMAGE_ONLY`.                                                                              |
|`image`            | A URL da imagem do cartão.                                                                                      |
|`imageAspectRatio` | A proporção da imagem do cartão. Destina-se a servir como uma dica antes que o carregamento da imagem seja concluído. Nota que a propriedade pode não ser fornecida em certas circunstâncias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do cartão de imagem apenas, consulte a documentação para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) e para [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct).

### Propriedades do modelo de cartão de conteúdo de imagem legendada

Cartões de imagem legendados são imagens em tamanho real clicáveis com texto descritivo acompanhante.

|Propriedade           | Descrição                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | O tipo de cartão de conteúdo, `CAPTIONED`.                                                                               |
|`image`            | A URL da imagem do cartão.                                                                                      |
|`imageAspectRatio` | A proporção da imagem do cartão. Destina-se a servir como uma dica antes que o carregamento da imagem seja concluído. Nota que a propriedade pode não ser fornecida em certas circunstâncias. |
|`title`            | O texto do título do cartão.                                                                                      |
|`cardDescription`  | O texto de descrição do cartão.                                                                                |
|`domain`           | (Opcional) O texto do link para a URL da propriedade, por exemplo, `"braze.com/resources/"`. Pode ser exibido na interface do usuário do cartão para indicar a ação/direção de clicar no cartão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do cartão de imagem legendada, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### propriedades do modelo de cartão de conteúdo clássico

Os cartões clássicos têm um título, descrição e uma imagem opcional à esquerda do texto.

|Propriedade           | Descrição                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | O tipo de cartão de conteúdo, `CLASSIC`.                                                                                 |
|`image`            | (Opcional) A URL da imagem do cartão.                                                                           |
|`title`            | O texto do título do cartão.                                                                                      |
|`cardDescription`  | O texto de descrição do cartão.                                                                                |
|`domain`           | (Opcional) O texto do link para a URL da propriedade, por exemplo, `"braze.com/resources/"`. Pode ser exibido na interface do usuário do cartão para indicar a ação/direção de clicar no cartão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do clássico (anúncio de texto) cartão de conteúdo, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Para uma referência completa do cartão de imagem clássico (notícia curta), consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

### Propriedades do modelo do cartão de conteúdo de controle

Os cartões de controle incluem todas as propriedades básicas, com algumas diferenças importantes. E o mais importante:

- A propriedade `isControl` tem a garantia de ser `true`.
- A propriedade `extras` tem a garantia de estar vazia.

Para uma referência completa do cartão de controle, consulte a documentação para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html) e para [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct).

## Suporte a GIFs

{% multi_lang_include wrappers/gif_support/content_cards.md %}


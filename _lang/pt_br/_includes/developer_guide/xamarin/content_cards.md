## Sobre os cartões de conteúdo do Xamarin

O SDK do Braze Xamarin inclui um feed de cartão padrão para que você comece a usar os cartões de conteúdo. O feed de cartão padrão incluído com o SDK da Braze lidará com toda a análise de dados, rastreamento, dispensas e renderização para os Cartões de Conteúdo de um usuário.

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Tipos e propriedades do cartão

O SDK do Braze Xamarin tem três tipos exclusivos de cartões de conteúdo que compartilham um modelo básico: [Banner](#xamarin_banner), [Imagem com legenda](#xamarin_captioned-image) e [Clássico](#xamarin_classic). Cada tipo herda propriedades comuns de um modelo base e possui as seguintes propriedades adicionais.

### Modelo de cartão básico

|Propriedade           | Descrição                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
|`idString`         | O ID do cartão definido pela Braze.                                                                                            |
|`created`          | O carimbo de data/hora UNIX do horário de criação do cartão do Braze.                                                             |
|`expiresAt`        | O carimbo de data/hora UNIX do tempo de expiração do cartão. Quando o valor é menor que 0, isso significa que o cartão nunca expira.      |
|`viewed`           | Se o cartão foi lido ou não pelo usuário. Isso não registra análise de dados.                                           |
|`clicked`          | Se o cartão foi clicado pelo usuário.                                                                         |
|`pinned`           | Se o cartão está fixado.                                                                                            |
|`dismissed`        | Se o usuário dispensou este cartão. Marcar um cartão como dispensado que já foi dispensado será uma operação nula. |
|`dismissible`      | Se o cartão pode ser descartado pelo usuário.                                                                           |
|`urlString`        | (Opcional) A string de URL associada à ação de clique do cartão.                                                       |
|`openUrlInWebView` | Se os URLs para esse cartão devem ser abertos no Braze WebView ou não.                                                 |
|`isControlCard`    | Se este cartão é um cartão de controle. Os cartões de controle não devem ser exibidos ao usuário.                                |
|`extras`           | O mapa de extras de chave-valor para este cartão.                                                                             |
|`isTest`           | Se este cartão é um cartão de teste.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do cartão base, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Banner

Os cartões de banner são imagens clicáveis e de tamanho completo.

|Propriedade           | Descrição                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | A URL da imagem do cartão.                                                                                      |
|`imageAspectRatio` | A proporção da imagem do cartão. Destina-se a servir como uma dica antes que o carregamento da imagem seja concluído. Nota que a propriedade pode não ser fornecida em certas circunstâncias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do cartão de banner, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) (agora renomeada para apenas imagem).

### Imagem legendada

Cartões de imagem legendados são imagens em tamanho real clicáveis com texto descritivo acompanhante.

|Propriedade           | Descrição                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | A URL da imagem do cartão.                                                                                      |
|`imageAspectRatio` | A proporção da imagem do cartão. Destina-se a servir como uma dica antes que o carregamento da imagem seja concluído. Nota que a propriedade pode não ser fornecida em certas circunstâncias. |
|`title`            | O texto do título do cartão.                                                                                      |
|`cardDescription`  | O texto de descrição do cartão.                                                                                |
|`domain`           | (Opcional) O texto do link para a URL da propriedade, por exemplo, `"braze.com/resources/"`. Pode ser exibido na interface do usuário do cartão para indicar a ação/direção de clicar no cartão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do cartão de imagem legendada, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### Clássico

Os cartões clássicos têm um título, descrição e uma imagem opcional à esquerda do texto.

|Propriedade           | Descrição                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | (Opcional) A URL da imagem do cartão.                                                                           |
|`title`            | O texto do título do cartão.                                                                                      |
|`cardDescription`  | O texto de descrição do cartão.                                                                                |
|`domain`           | (Opcional) O texto do link para a URL da propriedade, por exemplo, `"braze.com/resources/"`. Pode ser exibido na interface do usuário do cartão para indicar a ação/direção de clicar no cartão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do clássico (anúncio de texto) cartão de conteúdo, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Para uma referência completa do cartão de imagem clássico (notícia curta), consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

## Métodos do cartão

Você pode usar esses métodos adicionais para criar um feed de Cartões de Conteúdo personalizado dentro do seu app:

| Método                                   | Descrição                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Solicita os cartões de conteúdo mais recentes do servidor SDK da Braze.                                           |
| `getContentCards()`                      | Recupera os Cartões de Conteúdo do SDK da Braze. Isso retornará a lista mais recente de cartões do servidor. |
| `logContentCardClicked(cardId)`          | Registra um clique para o ID do cartão de conteúdo fornecido. Este método é usado apenas para análise de dados.                    |
| `logContentCardImpression(cardId)`       | Registra uma impressão para o ID do cartão de conteúdo fornecido.                                                      |
| `logContentCardDismissed(cardId)`        | Registra uma dispensa para o ID do cartão de conteúdo fornecido.                                                        |

---
nav_title: Integração
article_title: Integração do feed de notícias para Android e FireOS
page_order: 1.2
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda diferentes tipos de cartões do Feed de notícias, as diferentes propriedades específicas do cartão disponíveis e um exemplo de integração personalizada para seu aplicativo Android ou FireOS."
channel:
  - news feed
  
---

# Integração do Feed de notícias

> Este artigo de referência aborda diferentes tipos de cartões do Feed de notícias, as diferentes propriedades específicas do cartão disponíveis e um exemplo de integração personalizada para seu aplicativo Android ou FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

No Android, o feed de notícias é implementado como um [fragmento](http://developer.android.com/guide/components/fragments.html) disponível no projeto Braze Android UI. Consulte a [documentação do Google sobre fragmentos ](https://developer.android.com/guide/fragments#Adding " Documentação do Android: Fragmentos ") para obter informações sobre como adicionar um fragmento a uma atividade.

A classe `BrazeFeedFragment` será atualizada automaticamente e exibirá o conteúdo do feed de notícias e a análise de dados de uso do registro. Os cartões que podem aparecer no feed de notícias de um usuário são definidos no dashboard do Braze.

## Tipos de cartão

O Braze tem cinco tipos de cartões exclusivos: imagem de banner, imagem com legenda, anúncio de texto e notícias curtas. Cada tipo herda propriedades comuns de um modelo básico e tem as seguintes propriedades adicionais.

### Propriedades do modelo do cartão básico

O modelo de [cartão básico](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) fornece o comportamento fundamental para todos os cartões.  

|Propriedade|Descrição|
|---|---|
| `getId()` | Retorna o ID do cartão definido pelo Braze. |
| `getViewed()` | Retorna um booleano que reflete se o cartão foi lido ou não lido pelo usuário. |
| `getExtras()` | Retorna um mapa de extras de valor-chave para esse cartão. |
| `setViewed(boolean)` | Define o campo visualizado de um cartão. |
| `getCreated()` | Retorna o registro de data e hora unix do momento de criação do cartão no dashboard da Braze. |
| `getUpdated()` | Retorna o registro de data e hora unix do momento da última atualização do cartão no dashboard da Braze. |
| `getCategories()` | Retorna a lista de categorias atribuídas ao cartão; os cartões sem uma categoria serão atribuídos a `ABKCardCategoryNoCategory`. |
| `isInCategorySet(EnumSet)` | Retorna true se o cartão pertencer ao conjunto de categorias fornecido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de imagem de banner

[Os cartões de imagem de banner](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-banner-image-card/index.html) são imagens clicáveis em tamanho real.

|Propriedade|Descrição|
|---|---|
| `getImageUrl()` | Retorna o URL da imagem do cartão. |
| `getUrl()` | Retorna o URL que será aberto depois que o cartão for clicado. Pode ser um URL HTTP ou HTTPS ou um URL de protocolo. |
| `getDomain()` | Retorna o texto do link para o URL da propriedade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de imagem legendado

[Os cartões de imagem legendados](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) são imagens clicáveis em tamanho real com o texto descritivo que as acompanha.

|Propriedade|Descrição|
|---|---|
| `getImageUrl()` | Retorna o URL da imagem do cartão. |
| `getTitle()` | Retorna o texto do título do cartão. |
| `getDescription()` | Retorna o texto do corpo do cartão. |
| `getUrl()` | Retorna o URL que será aberto depois que o cartão for clicado.  Pode ser um URL HTTP ou HTTPS ou um URL de protocolo. |
| `getDomain()` | Retorna o texto do link para o URL da propriedade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de anúncio de texto (imagem legendada sem imagem)

[Os cartões de anúncio de texto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) são cartões clicáveis que contêm texto descritivo.

|Propriedade|Descrição|
|---|---|
| `getTitle()` | Retorna o texto do título do cartão. |
| `getDescription()` | Retorna o texto do corpo do cartão. |
| `getUrl()` | Retorna o URL que será aberto depois que o cartão for clicado. Pode ser um URL HTTP ou HTTPS ou um URL de protocolo. |
| `getDomain()` | Retorna o texto do link para o URL da propriedade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de notícias curtas

[Os cartões de notícias curtas](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) são cartões clicáveis com imagens e texto descritivo.

|Propriedade|Descrição|
|---|---|
| `getImageUrl()` | Retorna o URL da imagem do cartão. |
| `getTitle()` | Retorna o texto do título do cartão. |
| `getDescription()` | Retorna o texto do corpo do cartão. |
| `getUrl()` | Retorna o URL que será aberto depois que o cartão for clicado. Pode ser um URL HTTP ou HTTPS ou um URL de protocolo. |
| `getDomain()` | Retorna o texto do link para o URL da propriedade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Análise de dados da sessão

Os fragmentos da interface do usuário do Android não rastreiam automaticamente a análise de dados da sessão. Para garantir que as sessões sejam [rastreadas corretamente]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/), ligue para `IBraze.openSession()` quando o app for aberto.

## Criação de link

A vinculação ao feed de notícias a partir de uma mensagem no app deve ser ativada registrando o `BrazeFeedActivity` em seu `AndroidManifest.xml`.

## Integração de feed personalizado

Se quiser exibir o feed de forma totalmente personalizada, é possível fazê-lo usando suas próprias exibições preenchidas com dados de nossos modelos. Para obter modelos de feed de notícias, você precisará se inscrever para receber atualizações do feed de notícias e usar os dados do modelo resultante para preencher suas exibições. Também será necessário registrar análises de dados nos objetos do modelo à medida que os usuários interagem com as visualizações.

### Parte 1: Inscrição de atualizações de feed

Primeiro, declare uma variável privada em sua classe de feed personalizado para manter seu inscrito:

```java
// subscriber variable
private IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

Em seguida, adicione o seguinte código para inscrever-se para receber as atualizações do feed pela Braze, normalmente dentro de `Activity.onCreate()` da atividade do feed:

```java
// Remove the old subscription first
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
mFeedUpdatedSubscriber = new IEventSubscriber<FeedUpdatedEvent>() {
  @Override
  public void trigger(final FeedUpdatedEvent event) {
    // This list of Card objects included in the FeedUpdatedEvent should be used to populate your News Feed views.
    List<Card> cards = event.getFeedCards();
    // your logic here
  }
};
Braze.getInstance(context).subscribeToFeedUpdates(mFeedUpdatedSubscriber);

// Request a refresh of feed data
Braze.getInstance(context).requestFeedRefresh();
```

Também recomendamos cancelar a inscrição quando a atividade do feed personalizado deixar de ser vista. Adicione o seguinte código ao método de ciclo de vida `onDestroy()` de sua atividade:

```
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

### Parte 2: Análise de dados de registro

Ao usar exibições personalizadas, será necessário registrar a análise de dados manualmente, pois a análise só é tratada automaticamente quando se usa exibições da Braze.

Para registrar uma exibição do feed, chame [`Braze.logFeedDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-feed-displayed.html).

Para registrar uma impressão ou clicar em um cartão, ligue para [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) e [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) respectivamente.


---
nav_title: Integração
article_title: Integração do cartão de conteúdo para Android e FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Este artigo de referência cobre a integração do cartão de conteúdo e os diferentes modelos de dados e propriedades específicas do cartão disponíveis para seu aplicativo Android ou FireOS."
channel:
  - content cards
search_rank: 1
---

# integração de Cartões de Conteúdo

> Este artigo de referência cobre a integração do cartão de conteúdo e os diferentes modelos de dados e propriedades específicas do cartão disponíveis para seu aplicativo Android ou FireOS.

{% alert note %}
Quando estiver pronto para começar a implementação e a personalização, consulte o [Guia de personalização do cartão de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards).
{% endalert %}

No Android, o feed de Cartões de Conteúdo é implementado como um [fragmento](https://developer.android.com/guide/components/fragments.html) disponível no projeto de UI do Braze para Android. Consulte a [documentação do Fragments Android do Google](https://developer.android.com/guide/fragments#Adding ": Fragments") para obter informações sobre como adicionar um fragmento a uma atividade.

A classe [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) será atualizada automaticamente e exibirá o conteúdo dos cartões de conteúdo e a análise de dados de uso do registro. Os cartões que podem aparecer no `ContentCards` de um usuário são criados no dashboard do Braze.

## Modelo de dados do cartão de conteúdo {#card-types-for-android}

O modelo de dados dos cartões de conteúdo está disponível no SDK para Android. Para obter uma referência completa do modelo de dados do cartão de conteúdo, consulte a [documentação de referência do SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

A Braze tem quatro tipos únicos de cartões de conteúdo que compartilham um modelo base: [imagem apenas](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html), [imagem legendada](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html), [clássico (anúncio em texto)](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) e [clássico (notícia curta)](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html). Cada tipo herda propriedades comuns de um modelo base e possui as seguintes propriedades adicionais.

Para saber mais sobre a inscrição de dados dos cartões, consulte [análise de dados de registro]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics).

### Propriedades do modelo de cartão de conteúdo base {#base-card-for-android}

O modelo de [cartão base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) fornece comportamento fundamental para todos os cartões.  

|Propriedade | Descrição |
|---|---|
|`getId()` | Retorna o ID do cartão definido pelo Braze.|
|`getViewed()` | Retorna um booleano que reflete se o cartão está lido ou não lido pelo usuário.|
|`getExtras()` | Retorna um mapa de extras de valor-chave para esse cartão.|
|`getCreated()`  | Retorna o timestamp unix do horário de criação do cartão do Braze.|
|`getIsPinned` | Retorna um booleano que reflete se o cartão está fixado.|
|`getOpenUriInWebView()`  | Retorna um booleano que reflete se os Uris para este cartão devem ser abertos <br> no WebView do Braze ou não.|
|`getExpiredAt()` | Obtém a data de expiração do cartão.|
|`getIsRemoved()` | Retorna um booleano que reflete se o usuário final descartou este cartão.|
|`getIsDismissible()`  | Retorna um booleano que reflete se o cartão está fixado.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de apenas imagem {#banner-image-card-for-android}

[Cartões apenas com imagem](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) são imagens de tamanho completo clicáveis.

|Propriedade | Descrição |
|---|---|
|`getImageUrl()` | Retorna o URL da imagem do cartão.|
|`getUrl()` | Retorna a URL que será aberta após o cartão ser clicado. Pode ser um URL HTTP(s) ou um URL de protocolo.|
|`getDomain()` | Retorna o texto do link para o URL da propriedade.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de imagem legendada {#captioned-image-card-for-android}

[Cartões de imagem legendados](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) são imagens em tamanho real clicáveis com texto descritivo acompanhante.

|Propriedade | Descrição |
|---|---|
|`getImageUrl()` | Retorna o URL da imagem do cartão.|
|`getTitle()` | Retorna o texto do título do cartão.|
|`getDescription()` | Retorna o texto do corpo do cartão.|
|`getUrl()` | Retorna a URL que será aberta após o cartão ser clicado. Pode ser um URL HTTP(s) ou um URL de protocolo.|
|`getDomain()` | Retorna o texto do link para o URL da propriedade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades clássicas do cartão {#text-Announcement-card-for-android}

Um cartão de anúncio de texto clássico sem uma imagem incluída resultará em um [cartão de anúncio de texto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Se uma imagem for incluída, você receberá um [cartão de notícias curto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Propriedade | Descrição |
|---|---|
|`getTitle()` | Retorna o texto do título do cartão. |
|`getDescription()` | Retorna o texto do corpo do cartão. |
|`getUrl()` | Retorna a URL que será aberta após o cartão ser clicado. Pode ser um URL HTTP(s) ou um URL de protocolo. | 
|`getDomain()` | Retorna o texto do link para o URL da propriedade. |
|`getImageUrl()` | Retorna a URL da imagem do cartão, aplica-se apenas ao cartão de Notícias Curtas clássico. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos do cartão

Todos os [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) objetos do modelo de dados oferecem os seguintes métodos de análise de dados para registrar eventos de usuários nos servidores da Braze.

|Método | Descrição |
|---|---|
|`logImpression()` | Registre manualmente uma impressão no Braze para um determinado cartão. |
|`logClick()` | Registre manualmente um clique no Braze para um cartão específico. |
|`setIsDismissed()` | Registre manualmente uma dispensa no Braze para um cartão específico. Se um cartão já estiver marcado como descartado, não poderá ser marcado como descartado novamente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


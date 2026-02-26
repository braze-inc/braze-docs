## Pré-requisitos

Antes de poder usar os cartões de conteúdo Braze, você precisará integrar o [Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) em seu app. No entanto, não é necessária nenhuma configuração adicional.

## Fragmentos do Google

No Android, o feed de Cartões de Conteúdo é implementado como um [fragmento](https://developer.android.com/guide/components/fragments.html) disponível no projeto de UI do Braze para Android. A classe [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) será atualizada automaticamente e exibirá o conteúdo dos cartões de conteúdo e a análise de dados de uso do registro. Os cartões que podem aparecer no `ContentCards` de um usuário são criados no dashboard do Braze.

Para saber como adicionar um fragmento a uma atividade, consulte [a documentação sobre fragmentos do Google](https://developer.android.com/guide/fragments#Adding).

## Tipos e propriedades do cartão

O modelo de dados dos cartões de conteúdo está disponível no Android SDK e oferece os seguintes tipos exclusivos de cartões de conteúdo. Cada tipo compartilha um modelo básico, o que lhes permite herdar propriedades comuns do modelo básico, além de ter suas próprias propriedades exclusivas. Para obter a documentação de referência completa, consulte [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Modelo de cartão básico {#base-card-for-android}

O modelo de [cartão básico](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) fornece o comportamento fundamental para todos os cartões.  

|Propriedade | Descrição |
|---|---|
|`getId()` | Retorna o ID do cartão definido pelo Braze.|
|`getViewed()` | Retorna um booleano que reflete se o cartão está lido ou não lido pelo usuário.|
|`getExtras()` | Retorna um mapa de extras de valor-chave para esse cartão.|
|`getCreated()`  | Retorna o timestamp unix do horário de criação do cartão do Braze.|
|`isPinned` | Retorna um booleano que reflete se o cartão está fixado.|
|`getOpenUriInWebView()`  | Retorna um booleano que reflete se os Uris para este cartão devem ser abertos <br> no WebView do Braze ou não.|
|`getExpiredAt()` | Obtém a data de expiração do cartão.|
|`isRemoved()` | Retorna um booleano que reflete se o usuário final descartou este cartão.|
|`isDismissibleByUser()`  | Retorna um booleano que reflete se o cartão é descartável pelo usuário.|
|`isClicked()` | Retorna um booleano que reflete o estado clicado desse cartão.|
|`isDismissed` | Retorna um booleano que reflete se o cartão foi descartado. Defina como `true` para marcar o cartão como descartado. Se um cartão já tiver sido marcado como descartado, ele não poderá ser marcado como descartado novamente.|
|`isControl()` | Retorna um booleano se esse cartão for um cartão de controle e não deve ser renderizado.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Somente imagem {#banner-image-card-for-android}

[Cartões apenas com imagem](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) são imagens de tamanho completo clicáveis.

|Propriedade | Descrição |
|---|---|
|`getImageUrl()` | Retorna o URL da imagem do cartão.|
|`getUrl()` | Retorna a URL que será aberta após o cartão ser clicado. Pode ser um URL HTTP(s) ou um URL de protocolo.|
|`getDomain()` | Retorna o texto do link para o URL da propriedade.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagem legendada {#captioned-image-card-for-android}

[Cartões de imagem legendados](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) são imagens em tamanho real clicáveis com texto descritivo acompanhante.

|Propriedade | Descrição |
|---|---|
|`getImageUrl()` | Retorna o URL da imagem do cartão.|
|`getTitle()` | Retorna o texto do título do cartão.|
|`getDescription()` | Retorna o texto do corpo do cartão.|
|`getUrl()` | Retorna a URL que será aberta após o cartão ser clicado. Pode ser um URL HTTP(s) ou um URL de protocolo.|
|`getDomain()` | Retorna o texto do link para o URL da propriedade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Clássico {#text-Announcement-card-for-android}

Um cartão de anúncio de texto clássico sem uma imagem incluída resultará em um [cartão de anúncio de texto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Se uma imagem for incluída, você receberá um [cartão de notícias curto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Propriedade | Descrição |
|---|---|
|`getTitle()` | Retorna o texto do título do cartão. |
|`getDescription()` | Retorna o texto do corpo do cartão. |
|`getUrl()` | Retorna a URL que será aberta após o cartão ser clicado. Pode ser um URL HTTP(s) ou um URL de protocolo. | 
|`getDomain()` | Retorna o texto do link para o URL da propriedade. |
|`getImageUrl()` | Retorna a URL da imagem do cartão, aplica-se apenas ao cartão de Notícias Curtas clássico. |
|`isDismissed` | Retorna um booleano que reflete se o cartão foi descartado. Defina como `true` para marcar o cartão como descartado. Se um cartão já tiver sido marcado como descartado, ele não poderá ser marcado como descartado novamente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos do cartão

Todos os [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) objetos do modelo de dados oferecem os seguintes métodos de análise de dados para registrar eventos de usuários nos servidores da Braze.

|Método | Descrição |
|---|---|
|`logImpression()` | Registre manualmente uma impressão no Braze para um determinado cartão. |
|`logClick()` | Registre manualmente um clique no Braze para um cartão específico. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

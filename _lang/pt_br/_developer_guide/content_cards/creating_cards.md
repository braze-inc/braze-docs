---
nav_title: Criar cartões
article_title: Criar Cartões de Conteúdo
page_order: 0
description: "Este artigo aborda os componentes para criar uma interface de usuário personalizada de cartão de conteúdo."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Criar cartões de conteúdo

> Este artigo discute a abordagem básica que você usará ao implementar Cartões de conteúdo personalizados, bem como três casos de uso comuns. Ele pressupõe que você já tenha lido os outros artigos do guia de personalização de Cartões de conteúdo para entender o que pode ser feito por padrão e o que requer código personalizado. É especialmente útil entender como [registrar análises de dados]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) para seus Cartões de conteúdo personalizados. 

{% multi_lang_include banners/content_card_alert.md %}

## Criando um cartão

### Etapa 1: Criar uma interface de usuário personalizada 

{% tabs local %}
{% tab web %}

Primeiro, crie seu componente HTML personalizado que será usado para renderizar os cartões. 

{% endtab %}
{% tab android %}

Primeiro, crie seu próprio fragmento personalizado. O [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) padrão foi projetado apenas para lidar com nossos tipos de cartão de conteúdo padrão, mas é um bom ponto de partida.

{% endtab %}
{% tab swift %}

Primeiro, crie seu próprio componente personalizado de view controller. O [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) padrão foi projetado apenas para lidar com nossos tipos de cartão de conteúdo padrão, mas é um bom ponto de partida.

{% endtab %}
{% endtabs %}

### Etapa 2: Assine as atualizações do cartão

Registre uma função de retorno de chamada para se inscrever em atualizações de dados quando os cartões forem atualizados. Você pode analisar os objetos de cartão de conteúdo e extrair os dados da carga útil, como `title`, `cardDescription` e `imageUrl`, e então usar os dados do modelo resultante para preencher sua interface personalizada.

Para obter os modelos de dados do cartão de conteúdo, inscreva-se nas atualizações de Cartões de conteúdo. Preste atenção especial às seguintes propriedades:

* **`id`:** Representa a string de ID do cartão de conteúdo. Este é o identificador único usado para registrar análises de dados de Cartões de conteúdo personalizados.
* **`extras`:** Engloba todos os pares de valores-chave do dashboard da Braze. 

Todas as propriedades fora de `id` e `extras` são opcionais para análise em Cartões de conteúdo personalizados. Para saber mais sobre o modelo de dados, consulte o artigo de integração de cada plataforma: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).

{% tabs local %}
{% tab web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
Os Cartões de conteúdo só são atualizados no início da sessão se `subscribeToContentCardsUpdates()` for chamado antes de `openSession()`. Você também pode [atualizar o feed manualmente]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/) a qualquer momento.
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

#### Etapa 2a: Criar uma variável privada de assinante

Para se inscrever nas atualizações do cartão, primeiro declare uma variável privada na sua classe personalizada para armazenar seu assinante:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

#### Etapa 2b: Inscrever-se nas atualizações

Adicione o seguinte código para se inscrever nas atualizações de cartão de conteúdo da Braze, normalmente dentro do `Activity.onCreate()` da sua atividade personalizada de Cartões de conteúdo:

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

#### Etapa 2c: Cancelar inscrição

Cancele a inscrição quando sua atividade personalizada sair da visualização. Adicione o seguinte código ao método de ciclo de vida `onDestroy()` da sua atividade:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

#### Etapa 2a: Criar uma variável privada de assinante

Para se inscrever nas atualizações do cartão, primeiro declare uma variável privada na sua classe personalizada para armazenar seu assinante:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

#### Etapa 2b: Inscrever-se nas atualizações

Adicione o seguinte código para se inscrever nas atualizações de cartão de conteúdo da Braze, normalmente dentro do `Activity.onCreate()` da sua atividade personalizada de Cartões de conteúdo:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh()
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

#### Etapa 2c: Cancelar inscrição

Cancele a inscrição quando sua atividade personalizada sair da visualização. Adicione o seguinte código ao método de ciclo de vida `onDestroy()` da sua atividade:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Para acessar o modelo de dados dos Cartões de conteúdo, chame [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) na sua instância `braze`.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Além disso, você pode manter uma inscrição para observar alterações nos seus Cartões de conteúdo. Você pode fazer isso de duas maneiras: 
1. Mantendo um cancellable; ou 
2. Mantendo um `AsyncStream`.

##### Cancellable 

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

##### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Além disso, se você quiser manter uma inscrição nos seus cartões de conteúdo, pode chamar [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)):

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}


### Etapa 3: Implementar análise de dados

As impressões, os cliques e os descartes de cartão de conteúdo não são registrados automaticamente na sua visualização personalizada. É necessário [implementar cada método respectivo]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) para registrar adequadamente todas as métricas na análise de dados do dashboard da Braze.

### Etapa 4: Teste seu cartão (opcional)

Para testar seu cartão de conteúdo:

1. Defina um usuário ativo no seu app chamando o método [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
2. Na Braze, acesse **Campanhas** e [crie uma nova campanha de cartão de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create).
3. Na sua campanha, selecione **Teste** e insira o `user-id` do usuário teste. Quando estiver pronto, selecione **Enviar Teste**. Você poderá lançar um cartão de conteúdo no seu dispositivo em breve.

![Uma campanha de cartão de conteúdo da Braze mostrando que você pode adicionar seu próprio ID de usuário como destinatário de teste para testar seu cartão de conteúdo.]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

## Posicionamentos de Cartões de conteúdo

Os Cartões de conteúdo podem ser usados de muitas maneiras diferentes. Três implementações comuns são usá-los como centro de mensagens, anúncio de imagem dinâmico ou carrossel de imagens. Para cada um desses posicionamentos, você atribuirá [pares de valores-chave]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (a propriedade `extras` no modelo de dados) aos seus Cartões de conteúdo e, com base nos valores, ajustará dinamicamente o comportamento, a aparência ou a funcionalidade do cartão durante o tempo de execução. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Caixa de entrada de mensagens

Os Cartões de conteúdo podem ser usados para simular um centro de mensagens. Nesse formato, cada mensagem é seu próprio cartão que contém [pares de valores-chave]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) que acionam eventos de clique. Esses pares de valores-chave são os identificadores-chave que o app analisa ao decidir para onde ir quando o usuário clica em uma mensagem da caixa de entrada. Os valores dos pares de valores-chave são arbitrários. 

#### Exemplo

Por exemplo, você pode querer criar dois cartões de mensagem: um chamado à ação para os usuários ativarem recomendações de leitura e um código de cupom dado ao seu novo segmento de assinantes.

Chaves como `body`, `title` e `buttonText` podem ter valores simples de string que seus profissionais de marketing podem definir. Chaves como `terms` podem ter valores que fornecem uma pequena coleção de frases aprovadas pelo seu departamento jurídico. Chaves como `style` e `class_type` têm valores de string que você pode definir para determinar como seu cartão é exibido no seu app ou site.

{% tabs local %}
{% tab Reading recommendations %}
Pares de valores-chave para o cartão de recomendação de leitura:

| Chave         | Valor                                                                |
|------------|----------------------------------------------------------------------|
| `body`       | Adicione seus interesses ao seu perfil do Politer Weekly para obter recomendações pessoais de leitura. |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab New subscriber coupon %}
Pares de valores-chave para um novo cupom de assinante:

| Chave         | Valor                                                            |
|------------|------------------------------------------------------------------|
| `title`      | Assine para obter jogos ilimitados                                    |
| `body`       | Especial de Despedida do Verão - 10% de desconto nos jogos Politer              |
| `buttonText` | Assine agora                                                    |
| `style`      | promo                                                            |
| `class_type` | notification_center                                              |
| `card_priority` | 2                                                              |
| `terms`      | new_subscribers_only                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

{% details Informações adicionais para Android %}

No SDK do Android e do FireOS, a lógica do centro de mensagens é orientada pelo valor `class_type`, que é fornecido pelos pares de valores-chave da Braze. Usando o método [`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards/), você pode filtrar e identificar esses tipos de classe.

{% tabs local %}
{% tab Kotlin %}
**Usando `class_type` para comportamento ao clicar**<br>
Quando inflamos os dados do cartão de conteúdo em nossas classes personalizadas, usamos a propriedade `ContentCardClass` dos dados para determinar qual subclasse concreta deve ser usada para armazenar os dados.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

Então, ao lidar com a interação do usuário com a lista de mensagens, podemos usar o tipo de mensagem para determinar qual visualização será exibida ao usuário.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**Usando `class_type` para comportamento ao clicar**<br>
Quando inflamos os dados do cartão de conteúdo em nossas classes personalizadas, usamos a propriedade `ContentCardClass` dos dados para determinar qual subclasse concreta deve ser usada para armazenar os dados.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

Então, ao lidar com a interação do usuário com a lista de mensagens, podemos usar o tipo de mensagem para determinar qual visualização será exibida ao usuário.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### Carrossel

É possível definir Cartões de conteúdo em seu feed de carrossel totalmente personalizado, permitindo que os usuários deslizem e visualizem cartões adicionais em destaque. Por padrão, os Cartões de conteúdo são classificados por data de criação (o mais recente primeiro), e seus usuários verão todos os cartões para os quais são elegíveis.

Para implementar um carrossel de Cartões de conteúdo:

1. Crie uma lógica personalizada que observe as [alterações nos seus Cartões de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) e lide com a chegada de Cartões de conteúdo.
2. Crie uma lógica personalizada no lado do cliente para exibir um número específico de cartões no carrossel em um determinado momento. Por exemplo, você pode selecionar os cinco primeiros objetos de cartão de conteúdo do array ou introduzir pares de valores-chave para criar uma lógica condicional.

{% alert tip %}
Se estiver implementando um carrossel como um feed secundário de Cartões de conteúdo, certifique-se de [classificar os cartões no feed correto usando pares de valores-chave]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
{% endalert %}

### Apenas imagem

Os Cartões de conteúdo não precisam se parecer com "cartões". Por exemplo, os Cartões de conteúdo podem aparecer como uma imagem dinâmica que é exibida persistentemente na sua página inicial ou no topo de páginas designadas.

Para isso, seus profissionais de marketing criarão uma campanha ou etapa do canva com um tipo de cartão de conteúdo **Apenas Imagem**. Em seguida, defina os pares de valores-chave apropriados para usar [os Cartões de conteúdo como conteúdo suplementar]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content).
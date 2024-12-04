---
nav_title: Criação de cartões de conteúdo personalizados
article_title: Criação de cartões de conteúdo personalizados
page_order: 5
description: "Este artigo aborda os componentes da criação de uma interface do usuário de cartão de conteúdo personalizado"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Criação de cartões de conteúdo personalizados

> Este artigo discute a abordagem básica que você usará ao implementar cartões de conteúdo personalizados, bem como três casos de uso comuns: imagens de banner, uma caixa de entrada de mensagens e um carrossel de imagens. Ele pressupõe que você já tenha lido os outros artigos do guia de personalização do Content Card para entender o que pode ser feito por padrão e o que requer código personalizado. É especialmente importante entender como [registrar a análise de dados]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) dos seus cartões de conteúdo personalizados. 

O Braze oferece diferentes [tipos de cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details): `imageOnly`, `captionedImage`, `classic`, `classicImage`, e `control`. Eles podem ser usados como ponto de partida para suas implementações, ajustando sua aparência e comportamento. 

Você também pode exibir os cartões de conteúdo de uma maneira totalmente personalizada, criando sua própria interface de apresentação preenchida com dados dos modelos Braze. Analisar os objetos do cartão de conteúdo e extrair seus dados de carga útil. Em seguida, use os dados do modelo resultante para preencher sua interface de usuário personalizada - a fase de "execução" da [abordagem crawl, walk, run]({{site.baseurl}}/developer_guide/customization_guides/customization_overview).

{% alert note %}
Cada tipo de cartão de conteúdo padrão é uma subclasse que herda propriedades diferentes da classe genérica do modelo de cartão de conteúdo. A compreensão dessas propriedades herdadas será útil durante a personalização. Consulte a documentação da classe do cartão para obter detalhes completos[(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard), [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)).
{% endalert %}


## Visão geral da personalização

Dependendo do seu caso de uso, a implementação exata do seu cartão de conteúdo personalizado poderá variar um pouco, mas você deverá seguir esta fórmula básica:

1. Crie sua própria interface de usuário
2. Ouça as atualizações de dados
3. Análise de dados com registro manual

### Etapa 1: Criar uma interface de usuário personalizada 

{% tabs %}
{% tab Android %}

Primeiro, crie seu próprio fragmento personalizado. O padrão [`ContentCardFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) foi projetado apenas para lidar com nossos tipos de cartão de conteúdo padrão, mas é um bom ponto de partida.

{% endtab %}
{% tab iOS %}

Primeiro, crie seu próprio componente personalizado de view controller. O padrão [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) foi projetado apenas para lidar com nossos tipos de cartão de conteúdo padrão, mas é um bom ponto de partida.

{% endtab %}
{% tab Web %}

Primeiro, crie seu componente HTML personalizado que será usado para renderizar os cartões. 

{% endtab %}
{% endtabs %}

### Etapa 2: Assine as atualizações do cartão

Em seguida, registre uma função de retorno de chamada para [se inscrever para atualizações de dados]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates) quando os cartões forem atualizados. 

### Etapa 3: Implementar análise de dados

As impressões, os cliques e os descartes de cartão de conteúdo não são registrados automaticamente na sua visualização personalizada. É necessário [implementar cada método respectivo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events) para registrar adequadamente todas as métricas na análise de dados do dashboard do Braze.

## Posicionamento de cartões de conteúdo

Os cartões de conteúdo podem ser usados de muitas maneiras diferentes. Três implementações comuns são usá-los como um centro de mensagens, um anúncio em banner ou um carrossel de imagens. Para cada um desses posicionamentos, você atribuirá [pares de valores-chave]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (a propriedade `extras` no modelo de dados) aos seus cartões de conteúdo e, com base nos valores, ajustará dinamicamente o comportamento, a aparência ou a funcionalidade do cartão durante o tempo de execução. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Caixa de entrada de mensagens

Os cartões de conteúdo podem ser usados para simular um centro de mensagens. Nesse formato, cada mensagem é seu próprio cartão que contém [pares de chave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) que acionam eventos de clique. Esses pares chave-valor são os identificadores de chave que o aplicativo analisa ao decidir para onde ir quando o usuário clica em uma mensagem da caixa de entrada. Os valores dos pares de valores-chave são arbitrários. 

Veja um exemplo de configuração do dashboard que pode ser usado para criar dois cartões de mensagem: uma mensagem é uma chamada à ação para que um usuário adicione suas preferências para receber recomendações de leitura direcionadas, e outra fornece um código de cupom para um segmento de novos assinantes. 

![]({% image_buster /assets/img/content_cards/content-card-message-inbox-with-kvps.png %}){: style="max-width:20%;float:right;margin-left:15px;border:0px;"}

Exemplos de pares de valores-chave para o cartão de recomendação de leitura podem ser:

- body: Adicione seus interesses ao seu perfil do Politer Weekly para obter recomendações pessoais de leitura.
- style: info
- class_type: notification_center
- card_priority: 1

Exemplos de pares de valores-chave para um novo cupom de assinante podem ser:

- title: Assine para obter jogos ilimitados
- body: Especial de Despedida do Verão - 10% de desconto nos jogos Politer
- buttonText: Assine agora
- estilo: promocional
- class_type: notification_center
- card_priority: 2
- terms: new_subscribers_only

Seus profissionais de marketing poderiam disponibilizar esse cartão de conteúdo apenas para um segmento de novos usuários. 

Você trataria cada um dos valores. Chaves como `body`, `title` e `buttonText` podem ter valores simples de string que seus profissionais de marketing podem definir. Chaves como `terms` podem ter valores que fornecem uma pequena coleção de frases aprovadas por seu departamento jurídico. Você decidiria como renderizar `style` e `class_type` em seu app ou site. 

{% details Explicação adicional para Android %}

No SDK do Android e do FireOS, a lógica do centro de mensagens é orientada pelo valor `class_type`, que é fornecido pelos pares de chave/valor da Braze. Usando o método [`createContentCardable`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide) você pode filtrar e identificar esses tipos de classe.

{% tabs %}
{% tab Kotlin %}
**Usando `class_type` para comportamento ao clicar**<br>
Quando inflamos os dados do Content Card em nossas classes personalizadas, usamos a propriedade `ContentCardClass` dos dados para determinar qual subclasse concreta deve ser usada para armazenar os dados.

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

Então, ao enviar de mensagens para a interação do usuário com a lista de mensagens, podemos usar o tipo de mensagem para determinar qual visualização será exibida ao usuário.

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
Quando inflamos os dados do Content Card em nossas classes personalizadas, usamos a propriedade `ContentCardClass` dos dados para determinar qual subclasse concreta deve ser usada para armazenar os dados.

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

Então, ao enviar de mensagens para a interação do usuário com a lista de mensagens, podemos usar o tipo de mensagem para determinar qual visualização será exibida ao usuário.

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

Os cartões de conteúdo podem ser definidos em um feed de carrossel em que o usuário pode deslizar horizontalmente para visualizar cartões adicionais em destaque. 

Para criar um carrossel de cartões de conteúdo, implemente uma lógica que observe as [alterações em seus cartões de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) e lide com a chegada de cartões de conteúdo. Por padrão, os cartões de conteúdo são classificados por data de criação (o mais recente primeiro), e o usuário vê todos os cartões para os quais é elegível. Implemente a lógica do lado do cliente para exibir um número específico de cartões no carrossel em um determinado momento.

Dito isso, você pode solicitar e aplicar a lógica de exibição adicional de várias maneiras. Por exemplo, você pode selecionar os cinco primeiros objetos do cartão de conteúdo do vetor ou introduzir pares de valores-chave para criar uma lógica condicional.

Se estiver implementando um carrossel como um feed secundário de cartões de conteúdo, consulte [Personalização do feed padrão de cartões de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) para saber como classificar os cartões no feed correto com base em pares de valores-chave.

### Banner

Os cartões de conteúdo não precisam se parecer com "cartões". Por exemplo, os cartões de conteúdo de banner podem aparecer como um banner dinâmico que é exibido persistentemente em sua página inicial ou na parte superior de páginas designadas.

Para conseguir isso, seus profissionais de marketing criarão uma campanha ou etapa do Canva com um cartão de conteúdo do tipo **Somente imagem**. Em seguida, defina os pares de valores-chave apropriados para usar [os cartões de conteúdo como conteúdo suplementar]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content).



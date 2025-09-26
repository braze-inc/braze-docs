---
nav_title: Criação de cartões
article_title: Criação de cartões de conteúdo
page_order: 0
description: "Este artigo aborda os componentes da criação de uma interface de usuário de cartão de conteúdo personalizado."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Criação de cartões de conteúdo

> Este artigo discute a abordagem básica que você usará ao implementar cartões de conteúdo personalizados, bem como três casos de uso comuns. Ele pressupõe que você já tenha lido os outros artigos do guia de personalização do Content Card para entender o que pode ser feito por padrão e o que requer código personalizado. É especialmente útil entender como [registrar a análise]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) de dados dos seus cartões de conteúdo personalizados. 

## Criação de um cartão

### Etapa 1: Criar uma interface de usuário personalizada 

{% tabs local %}
{% tab Android %}

Primeiro, crie seu próprio fragmento personalizado. O padrão [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) foi projetado apenas para lidar com nossos tipos de cartão de conteúdo padrão, mas é um bom ponto de partida.

{% endtab %}
{% tab swift %}

Primeiro, crie seu próprio componente personalizado de view controller. O padrão [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) foi projetado apenas para lidar com nossos tipos de cartão de conteúdo padrão, mas é um bom ponto de partida.

{% endtab %}
{% tab web %}

Primeiro, crie seu componente HTML personalizado que será usado para renderizar os cartões. 

{% endtab %}
{% endtabs %}

### Etapa 2: Assine as atualizações do cartão

Em seguida, registre uma função de retorno de chamada para [se inscrever para atualizações de dados]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates) quando os cartões forem atualizados. 

### Etapa 3: Implementar análise de dados

As impressões, os cliques e os descartes de cartão de conteúdo não são registrados automaticamente na sua visualização personalizada. É necessário [implementar cada método respectivo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events) para registrar adequadamente todas as métricas na análise de dados do dashboard do Braze.

### Etapa 4: Teste seu cartão (opcional)

Para testar seu cartão de conteúdo:

1. Defina um usuário ativo em seu aplicativo chamando o método [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) método.
2. No Braze, acesse **Campaigns (Campanhas**) e [crie uma nova campanha de cartão de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create).
3. Em sua campanha, selecione **Test (Teste**) e insira o usuário teste `user-id`. Quando estiver pronto, selecione **Send Test (Enviar teste**). Em breve, será possível iniciar um cartão de conteúdo em seu dispositivo.

![Uma campanha de cartão de conteúdo Braze mostrando que você pode adicionar seu próprio ID de usuário como um destinatário de teste para testar seu cartão de conteúdo.]({% image_buster /assets/img/react-native/content-card-test.png %} "Teste de Campanha de Cartão de Conteúdo")

## posicionamentos de cartão de conteúdo

Os cartões de conteúdo podem ser usados de muitas maneiras diferentes. Três implementações comuns são usá-las como um centro de mensagens, um anúncio de imagem dinâmico ou um carrossel de imagens. Para cada um desses posicionamentos, você atribuirá [pares de valores-chave]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (a propriedade `extras` no modelo de dados) aos seus cartões de conteúdo e, com base nos valores, ajustará dinamicamente o comportamento, a aparência ou a funcionalidade do cartão durante o tempo de execução. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Caixa de entrada de mensagens

Os cartões de conteúdo podem ser usados para simular um centro de mensagens. Nesse formato, cada mensagem é seu próprio cartão que contém [pares de chave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) que acionam eventos de clique. Esses pares chave-valor são os identificadores de chave que o aplicativo analisa ao decidir para onde ir quando o usuário clica em uma mensagem da caixa de entrada. Os valores dos pares de valores-chave são arbitrários. 

#### Exemplo

Por exemplo, talvez queira criar dois cartões de mensagens: uma chamada para ação para que os usuários ativem as recomendações de leitura e um código de cupom dado ao seu novo segmento de assinantes.

Chaves como `body`, `title` e `buttonText` podem ter valores simples de string que seus profissionais de marketing podem definir. Chaves como `terms` podem ter valores que fornecem uma pequena coleção de frases aprovadas por seu departamento jurídico. Chaves como `style` e `class_type` têm valores de string que podem ser definidos para determinar como o cartão será renderizado no app ou site.

{% tabs local %}
{% tab Recomendações de leitura %}
Pares de valores-chave para o cartão de recomendação de leitura:

| Chave         | Valor                                                                |
|------------|----------------------------------------------------------------------|
| `body`       | Adicione seus interesses ao seu perfil do Politer Weekly para obter recomendações pessoais de leitura. |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab Cupom para novos assinantes %}
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

No SDK do Android e do FireOS, a lógica do centro de mensagens é orientada pelo valor `class_type`, que é fornecido pelos pares de chave/valor da Braze. Usando o método [`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards/) você pode filtrar e identificar esses tipos de classe.

{% tabs local %}
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

É possível definir cartões de conteúdo em seu feed de carrossel totalmente personalizado, permitindo que os usuários deslizem e visualizem cartões adicionais em destaque. Por padrão, os cartões de conteúdo são classificados por data de criação (o mais recente primeiro), e seus usuários verão todos os cartões para os quais são elegíveis.

Para implementar um carrossel de cartões de conteúdo:

1. Crie uma lógica personalizada que observe as [alterações em seus cartões de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) e lide com a chegada de cartões de conteúdo.
2. Crie uma lógica personalizada no lado do cliente para exibir um número específico de cartões no carrossel em um determinado momento. Por exemplo, você pode selecionar os cinco primeiros objetos do cartão de conteúdo do vetor ou introduzir pares de valores-chave para criar uma lógica condicional.

{% alert tip %}
Se estiver implementando um carrossel como um feed secundário de cartões de conteúdo, certifique-se de [classificar os cartões no feed correto usando pares de valores-chave]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
{% endalert %}

### Somente imagem

Os cartões de conteúdo não precisam se parecer com "cartões". Por exemplo, os cartões de conteúdo podem aparecer como uma imagem dinâmica que é exibida persistentemente em sua página inicial ou na parte superior de páginas designadas.

Para conseguir isso, seus profissionais de marketing criarão uma campanha ou etapa do Canva com um cartão de conteúdo do tipo **Somente imagem**. Em seguida, defina os pares de valores-chave apropriados para usar [os cartões de conteúdo como conteúdo suplementar]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content).

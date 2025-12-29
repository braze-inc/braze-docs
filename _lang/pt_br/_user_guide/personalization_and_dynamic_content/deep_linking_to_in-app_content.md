---
nav_title: Links diretos para conteúdo no aplicativo
article_title: Deep Linking para conteúdo no aplicativo
page_order: 3
description: "Este artigo de referência aborda orientações sobre como adicionar links diretos ao conteúdo de suas mensagens in-app."

---

# Links diretos para conteúdo no aplicativo

## O que é deep linking?

O deep linking é uma forma de iniciar um aplicativo nativo e fornecer informações adicionais que o instruem a realizar uma ação específica ou mostrar um conteúdo específico.

Há três partes para isso:

1. Identifique o aplicativo a ser iniciado.
2. Instrua o aplicativo sobre a ação a ser executada.
3. Forneça à ação todos os dados adicionais necessários.

Deep links são URIs personalizados que vinculam a uma parte específica do aplicativo e contêm todas essas três partes. O segredo é definir um esquema personalizado. `http:` é o esquema com o qual quase todo mundo está familiarizado, mas os esquemas podem começar com qualquer palavra. Um esquema deve começar com uma letra, mas pode conter letras, números, sinais de adição, sinais de subtração ou pontos. Na prática, não existe um registro central para evitar conflitos, portanto, é uma prática recomendada incluir seu nome de domínio no esquema. Por exemplo, `twitter://` é o URI do iOS para iniciar o aplicativo móvel do X, antigo Twitter.

Tudo o que vem depois dos dois pontos em um deep link é texto de forma livre. Cabe a você definir sua estrutura e interpretação; no entanto, uma convenção comum é modelá-la de acordo com os URLs `http:`, incluindo um `//` inicial e parâmetros de consulta (por exemplo, `?foo=1&bar=2`). No exemplo anterior, `twitter://user?screen_name=[id]` seria usado para iniciar um perfil específico no aplicativo.

{% alert important %}
O Braze não oferece suporte ao uso de um wrapper como o Flutter para enviar links diretos. Para usar esse recurso, você deve configurar links diretos na camada nativa.
{% endalert %}

## Tags UTM e atribuição de campanhas

### O que é uma tag UTM?

[As tags UTM (Urchin Traffic Manager)](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) permitem que você inclua detalhes de atribuição de campanha diretamente nos links. As tags UTM são usadas pelo Google Analytics para coletar dados de atribuição de campanha e podem ser usadas para rastrear as seguintes propriedades:

- `utm_source`: O identificador da origem do tráfego (por exemplo,`my_app`)
- `utm_medium`: A mídia da campanha (por exemplo,`newsfeed`)
- `utm_campaign`: O identificador da campanha (por exemplo,`spring_2016_campaign`)
- `utm_term`: Identificador de um termo de pesquisa paga que levou o usuário ao seu aplicativo ou site (por exemplo,`pizza`)
- `utm_content`: Um identificador do link ou conteúdo específico em que o usuário clicou (por exemplo,`toplink` ou `android_iam_button2`)

As tags UTM podem ser incorporadas em links HTTP (web) regulares e links diretos e rastreadas usando o Google Analytics.

### Uso de tags UTM com o Braze

Se você quiser usar tags UTM com links HTTP (web) regulares (por exemplo, para fazer atribuição de campanha para suas campanhas de e-mail) e sua organização já usa o Google Analytics, você pode usar [o construtor de URL do Google](https://ga-dev-tools.google/ga4/campaign-url-builder/) para gerar links UTM. Esses links podem ser prontamente incorporados ao texto da campanha do Braze, como qualquer outro link.

Para usar tags UTM em links diretos para seu aplicativo, ele deve ter o [SDK do Google Analytics](https://developers.google.com/analytics/devguides/collection/) relevante integrado e configurado corretamente para lidar com links diretos. Consulte seus desenvolvedores se não tiver certeza sobre isso.

Depois que o SDK do Analytics for integrado e configurado, as tags UTM poderão ser usadas com deep links nas campanhas do Braze. Para configurar as tags UTM para sua campanha, inclua as tags UTM necessárias no URL de destino ou nos links diretos. Os exemplos a seguir mostram como usar tags UTM em notificações push e mensagens no aplicativo.

#### Atribuição de aberturas push com tags UTM

Para incluir tags UTM em seus deep links para notificações push, defina o comportamento ao clicar na mensagem push como um deep link e, em seguida, escreva o endereço do deep link e inclua as tags UTM desejadas da seguinte maneira:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

\![]({% image_buster /assets/img_archive/push_utm_tags.png %})

#### Atribuição de cliques em mensagens in-app com tags UTM

Para incluir tags UTM nos deep links em suas mensagens in-app, use o seguinte:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

\![]({% image_buster /assets/img_archive/iam_utm_tags.png %})


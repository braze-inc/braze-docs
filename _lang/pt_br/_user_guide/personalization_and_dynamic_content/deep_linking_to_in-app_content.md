---
nav_title: Deep linking para conteúdo no aplicativo
article_title: Deep linking para conteúdo no aplicativo
page_order: 3
description: "Este artigo de referência aborda orientações sobre como adicionar deep linking ao conteúdo de suas mensagens no app."

---

# Deep linking para conteúdo no app

## O que é deep linking?

O deep linking é uma forma de iniciar um app nativo e fornecer informações adicionais, dizendo a ele para realizar uma ação específica ou mostrar um conteúdo específico.

Há três partes nesse processo:

1. Identifique o aplicativo a ser iniciado.
2. Instrua o app sobre qual ação deve ser executada.
3. Forneça à ação todos os dados adicionais necessários.

Os deep links são URIs personalizados que vinculam a uma parte específica do app e contêm todas essas três partes. O segredo é definir um esquema personalizado. `http:` é o esquema com o qual quase todo mundo está familiarizado, mas os esquemas podem começar com qualquer palavra. Um esquema deve começar com uma letra, mas pode conter letras, números, sinais de adição, sinais de subtração ou pontos. Na prática, não há um registro central para evitar conflitos, portanto, é uma prática recomendada incluir seu nome de domínio no esquema. Por exemplo, `twitter://` é o URI do iOS para iniciar o app móvel do X, antigo Twitter.

Tudo após os dois pontos em um deep linking é texto livre. Cabe a você definir sua estrutura e interpretação; no entanto, uma convenção comum é modelá-la de acordo com os URLs `http:`, incluindo um `//` inicial e parâmetros de consulta (por exemplo, `?foo=1&bar=2`). No exemplo anterior, `twitter://user?screen_name=[id]` seria usado para iniciar um perfil específico no app.

{% alert important %}
O Braze não oferece suporte ao uso de um wrapper como o Flutter para enviar deep linkings. Para usar esse recurso, você deve configurar os deep links na camada nativa.
{% endalert %}

## Tags UTM e atribuição de campanhas

### O que é uma tag UTM?

 As tags UTM são usadas pelo Google Analytics para coletar dados de atribuição de campanha e podem ser usadas para rastrear as seguintes propriedades:

- `utm_source`: O identificador da origem do tráfego (por exemplo, `my_app`)
- `utm_medium`: A mídia da campanha (por exemplo, `newsfeed`)
- `utm_campaign`: O identificador da campanha (por exemplo, `spring_2016_campaign`)
- `utm_term`: Identificador de um termo de pesquisa paga que levou o usuário ao seu app ou site (por exemplo, `pizza`)
- `utm_content`: Um identificador do link ou conteúdo específico em que o usuário clicou (por exemplo, `toplink` ou `android_iam_button2`)

As tags UTM podem ser incorporadas em links HTTP (web) regulares e deep links e rastreadas usando o Google Analytics.

### Uso de tags UTM com a Braze

 Esses links podem ser prontamente incorporados ao texto da campanha do Braze, como qualquer outro link.

 Consulte seus desenvolvedores se não tiver certeza sobre isso.

Depois que o SDK do Analytics for integrado e configurado, as tags UTM poderão ser usadas com deep links nas campanhas do Braze. Para configurar tags UTM para sua campanha, inclua as tags UTM necessárias no URL de destino ou nos deep linkings. Os exemplos a seguir mostram como usar tags UTM em notificações por push e mensagens no app.

#### Atribuição de aberturas push com tags UTM

Para incluir tags UTM em seus deep links para notificações por push, defina o comportamento ao clicar na mensagem push para ser um deep link e, em seguida, escreva o endereço do deep link e inclua as tags UTM desejadas da seguinte maneira:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```



#### Atribuição de cliques em mensagens no app com tags UTM

Para incluir tags UTM nos deep links em suas mensagens no app, use o seguinte:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```




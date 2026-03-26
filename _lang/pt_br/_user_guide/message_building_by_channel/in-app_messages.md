---
nav_title: "Mensagem no app"
article_title: Mensagens no app
page_order: 2
alias: /in-app_messages/
description: "Essa landing page é o lar de todos os assuntos relacionados à mensagem no app. Aqui, você pode encontrar artigos sobre como criar mensagens no app, o editor de arrastar e soltar, como personalizar suas mensagens, relatórios e muito mais."
channel:
  - in-app messages
search_rank: 5
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} Mensagens no app

> Mensagens no app ajudam você a enviar conteúdo para o seu usuário sem interromper seu dia com uma notificação por push, já que essas mensagens não são entregues fora do app do usuário e não invadem a tela inicial dele. 

Mensagens no app personalizadas e sob medida aprimoram a experiência do usuário e ajudam o público a obter o máximo valor do seu app. Com uma variedade de layouts e ferramentas de personalização para escolher, as mensagens no app engajam seus usuários mais do que nunca. Elas vêm com contexto, têm menor urgência e são entregues quando o usuário está ativo dentro do seu app. Para exemplos de mensagens no app, confira nossas [histórias de clientes](https://www.braze.com/customers/).

## Casos de uso

Com o rico nível de conteúdo oferecido pelas mensagens no app, você pode aproveitar esse canal para uma variedade de casos de uso:

| Caso de uso | Explicação |
| --- | --- |
| Push primer | Execute uma campanha de [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) usando uma mensagem no app rich para mostrar aos seus clientes o benefício da aceitação do push para seu app ou site e apresente a eles um pedido de aceitação da permissão de push.
| Vendas e promoções | Use mensagens modais no app com código personalizado para cumprimentar os clientes com mídias chamativas, com códigos de promoção estáticos ou ofertas. Incentive-os a fazer compras ou conversões quando, de outra forma, não o fariam. |
| Incentivar a adoção de recursos | Incentive os clientes a usar outras partes do seu app ou a aproveitar um serviço. |
| Campanhas altamente personalizadas | Coloque as mensagens no app como a primeira coisa que seus clientes veem quando entram em seu aplicativo ou site. Acrescente alguns recursos de personalização da Braze, como [conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), para motivar os usuários a agir e, portanto, tornar seu alcance mais eficaz.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Outros casos de uso a serem considerados incluem o seguinte:

- Novos recursos do app
- Gerenciamento de aplicativos
- Avaliações
- Fazer upgrades ou atualizações de aplicativos
- Brindes e sorteios

## Tipos de mensagens padrão

As guias a seguir mostram como é para seus usuários abrir um dos nossos tipos de mensagem no app padrão - mensagens no app deslizantes, modais e em tela cheia.

{% tabs %}
{% tab Slideup %}

As mensagens deslizantes geralmente aparecem na parte superior e inferior da tela do app (é possível definir isso ao criar a mensagem). Eles são ótimos para alertar seus usuários sobre novos termos de serviço, cookies e outros trechos de informações.

![Mensagem no app em slideup que aparece na parte inferior da tela do aplicativo. O slide para cima inclui uma imagem de ícone e uma mensagem breve.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Os modais aparecem no centro da tela do dispositivo com uma sobreposição de tela que os ajuda a se destacar do seu app em segundo plano. Eles são perfeitos para sugerir, de forma não tão sutil, que o usuário aproveite uma venda ou um brinde.

![Mensagem modal no app que aparece no centro de um aplicativo e site como uma caixa de diálogo. O modal inclui uma imagem, cabeçalho, corpo da mensagem e dois botões.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fullscreen %}

As mensagens em tela cheia são exatamente o que se espera - elas ocupam a tela inteira do dispositivo! Esse tipo de mensagem é ótimo quando você realmente precisa da atenção do usuário, como nas atualizações obrigatórias do app.

![Mensagem no app em tela cheia ocupando a tela do aplicativo. A mensagem em tela cheia inclui uma imagem grande, cabeçalho, corpo da mensagem e dois botões.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Além desses modelos de mensagem padrão, você também pode personalizar ainda mais sua comunicação usando mensagens no app em HTML personalizado, modais web com CSS ou formulários de captura de e-mail na web. Para saber mais, consulte [Personalização]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Mensagens no app com modelo

Mensagens no app são entregues como mensagens no app com modelo quando **Reavaliar a elegibilidade da campanha antes de exibir** é selecionado ou se qualquer uma das seguintes tags Liquid existir na mensagem:

- `canvas_entry_properties`
- `connected_content`
- Variáveis de SMS, como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Isso significa que durante o início da sessão, o dispositivo receberá o disparo daquela mensagem no app em vez da mensagem inteira. Quando o usuário dispara a mensagem no app, o dispositivo do usuário faz uma solicitação de rede para buscar a mensagem real.

{% alert note %}
A mensagem não será entregue se o dispositivo não tiver acesso à internet. A mensagem pode não ser entregue se a lógica Liquid demorar muito para ser resolvida.
{% endalert %}

## Comportamento de abortar

No Braze, um aborto ocorre quando um usuário realiza uma ação que o torna elegível para receber uma mensagem, mas ele não recebe a mensagem porque sua lógica Liquid o marca como inelegível. Por exemplo:

1. Sam realiza uma ação que deve disparar uma campanha de e-mail.
2. O corpo do e-mail contém lógica Liquid que diz que se a pontuação de um atributo personalizado for menor que 50, não envie este e-mail.
3. A pontuação do atributo personalizado de Sam é 20.
4. O Braze reconhece que Sam não deve receber este e-mail, e o e-mail é abortado.
5. Um evento de aborto é registrado.

No entanto, como as mensagens no app são um canal de pull, os abortos funcionam de maneira um pouco diferente para elas.

### Comportamento de aborto de mensagem no app

As mensagens no app são puxadas pelo dispositivo no início da sessão e armazenadas em cache no dispositivo, então, independentemente da qualidade da conexão com a Internet, a mensagem pode ser entregue instantaneamente ao usuário. Por exemplo, se um usuário receber cinco mensagens no app durante sua sessão, ele receberá todas as cinco no início da sessão. As mensagens serão armazenadas localmente e aparecerão quando seus eventos de gatilho definidos ocorrerem (início da sessão, o usuário clica em um botão que registra um evento personalizado, ou outros).

Em outras palavras, a lógica que determina se devemos abortar uma mensagem no app ocorre **antes** do gatilho ter ocorrido. Para demonstrar isso, digamos que Sam, do exemplo de e-mail, está inscrito em notificações por push.

1. Sam inicia uma sessão lançando um app da Braze em seu telefone.
2. Com base nos critérios de público das campanhas ativas no espaço de trabalho, Sam pode ser elegível para cinco campanhas diferentes. Todas as cinco são puxadas para seu telefone e armazenadas em cache.
3. Sam **não** realizou nenhuma ação que acionaria essas mensagens, mas ele poderia receber essas mensagens na sessão.
4. O Liquid em duas das mensagens no app tem regras que excluem Sam de receber a mensagem (como seu atributo personalizado de pontuação não ser alto o suficiente).
5. Sam não recebe as duas mensagens no app que o excluem, mas ele recebe as outras três mensagens.
6. Nenhum evento de aborto é registrado.

A Braze não registra nenhum evento de aborto no caso de Sam porque isso não atende à nossa definição de aborto; Sam **não** realizou nenhuma ação que acionaria as mensagens. Para mensagens no app, os usuários nunca realmente realizam o gatilho antes que a Braze determine que eles não deveriam ver a mensagem.

#### Comportamento de aborto de mensagem no app com template

[Mensagens no app com template](#templated-in-app-messages) forçam o SDK a reavaliar se uma mensagem deve ser exibida quando o evento de gatilho ocorre. Isso tem um comportamento de aborto diferente. Para demonstrar, vamos considerar este exemplo:

1. Sam inicia uma sessão do Braze ao abrir um app com tecnologia Braze em seu telefone.
2. Os critérios de público das campanhas ativas dizem que Sam pode ser elegível para uma mensagem no app com modelo, então as informações do gatilho são enviadas para seu dispositivo sem a carga útil da mensagem.
3. Sam seleciona um botão que registra um evento personalizado, disparando a mensagem no app com modelo.
4. O dispositivo de Sam faz uma solicitação de rede para buscar a mensagem no app.
5. A lógica Liquid da mensagem leva a um abort, então o Braze registra isso como um abort; Sam realizou a ação-gatilho antes dessa avaliação.

##### Comparando o comportamento de aborto de mensagens no app

Esta tabela compara os fluxos de mensagens no app que Sam experimentou:

| Mensagem no app | Comportamento de abortar |
| --- | --- |
| Padrão | Um evento de aborto não foi registrado porque Sam não realizou nenhuma ação que dispararia uma mensagem.<br><br>Mensagens no app padrão não registram abortos porque a definição de um aborto é “não viu a mensagem apesar de realizar a ação-gatilho.” Como as mensagens no app são entregues ao dispositivo antes que as ações-gatilho ocorram, não faz sentido considerar mensagens no app omitidas por causa da lógica Liquid. |
| Modelado | Um evento de abort foi registrado porque Sam realizou a ação-gatilho para disparar a mensagem no app com modelo, mas recebeu um abort na modelagem Liquid. <br><br>Mensagens no app com modelo registram abortos porque a avaliação Liquid ocorre após a ação-gatilho ter sido realizada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mais recursos

Antes de começar a criar suas próprias campanhas de mensagens no app - ou usar mensagens no app em uma campanha multicanais -, recomendamos que consulte nosso [guia de preparação de mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). Este guia aborda questões de direcionamento, conteúdo e conversão que você deve considerar ao criar mensagens no app.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

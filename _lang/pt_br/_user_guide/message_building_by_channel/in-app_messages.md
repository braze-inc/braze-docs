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

> As mensagens no app ajudam a levar o conteúdo ao usuário sem interromper o dia dele com uma notificação por push, pois essas mensagens não são enviadas para fora do app do usuário e não interferem na tela inicial dele. 

Mensagens no app personalizadas e sob medida aprimoram a experiência do usuário e ajudam o público a obter o máximo valor do seu app. Com uma variedade de layouts e ferramentas de personalização para escolher, as mensagens no app engajam seus usuários mais do que nunca. Eles vêm com contexto, têm menor urgência e são entregues quando o usuário está ativo em seu app. Para ver exemplos de mensagens no app, confira [as histórias de](https://www.braze.com/customers/) nossos [clientes](https://www.braze.com/customers/).

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

![Mensagem no app em slideup que aparece na parte inferior da tela do aplicativo. O slide-up inclui uma imagem de ícone e uma breve mensagem.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Os modais aparecem no centro da tela do dispositivo com uma sobreposição de tela que os ajuda a se destacar do seu app em segundo plano. Eles são perfeitos para sugerir, de forma não tão sutil, que o usuário aproveite uma venda ou um brinde.

![Mensagem modal no app que aparece no centro de um aplicativo e site como uma caixa de diálogo. O modal inclui uma imagem, um cabeçalho, um corpo de mensagem e dois botões.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fullscreen %}

As mensagens em tela cheia são exatamente o que se espera - elas ocupam a tela inteira do dispositivo! Esse tipo de mensagem é ótimo quando você realmente precisa da atenção do usuário, como nas atualizações obrigatórias do app.

![Mensagem no app em tela cheia ocupando a tela do aplicativo. A mensagem em tela cheia inclui uma imagem grande, cabeçalho, corpo da mensagem e dois botões.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Além desses modelos de mensagem padrão, você também pode personalizar ainda mais seu envio de mensagens usando mensagens no app em HTML personalizado, modais da Web com CSS ou formulários de captura de e-mail da Web. Para saber mais, consulte [Personalização]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Mensagens no app modeladas

As mensagens no app são entregues como modelos de mensagens no app quando a opção **Reavaliar elegibilidade da campanha antes de exibir** estiver selecionada ou se qualquer uma das seguintes Liquid tags existir na mensagem:

- `canvas_entry_properties`
- `connected_content`
- Variáveis de SMS, como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Isso significa que, durante o início da sessão, o dispositivo receberá o disparo dessa mensagem no app, em vez da mensagem inteira. Quando o usuário dispara a mensagem no app, o dispositivo do usuário faz uma solicitação de rede para buscar a mensagem real.

{% alert note %}
A mensagem não será entregue se o dispositivo não tiver acesso à Internet. A mensagem pode não ser entregue se a lógica do Liquid demorar muito para ser resolvida.
{% endalert %}

## Comportamento de abortar

No Braze, um aborto ocorre quando um usuário realiza uma ação que o torna elegível para receber uma mensagem, mas ele não recebe a mensagem porque a lógica Liquid o marca como inelegível. Por exemplo:

1. Sam executa uma ação que deve disparar uma campanha de e-mail.
2. O corpo do e-mail contém a lógica Liquid que diz que se a pontuação de um atributo personalizado for menor que 50, não envie esse e-mail.
3. A pontuação do atributo personalizado de Sam é 20.
4. O Braze reconhece que Sam não deveria receber esse e-mail, e o e-mail é abortado.
5. Um evento de aborto é registrado.

No entanto, como as mensagens no app são um canal de envio de mensagens, a interrupção funciona de forma um pouco diferente para elas.

### Comportamento de abortar mensagens no app

As mensagens no app são recebidas pelo dispositivo no início da sessão e armazenadas em cache no dispositivo, portanto, independentemente da qualidade da conexão com a Internet, a mensagem pode ser entregue instantaneamente ao usuário. Por exemplo, se um usuário receber cinco mensagens no app em sua sessão, ele receberá todas as cinco no início da sessão. As mensagens serão armazenadas em cache localmente e aparecerão quando ocorrerem os eventos de gatilho definidos (início da sessão, o usuário clica em um botão que registra um evento personalizado ou outro).

Em outras palavras, a lógica que determina se devemos abortar uma mensagem no app ocorre **antes da** ocorrência do disparo. Para demonstrar isso, digamos que o Sam do exemplo de e-mail esteja inscrito em notificações por push.

1. Sam inicia uma sessão abrindo um app do Braze em seu telefone.
2. Com base nos critérios de público das campanhas ativas no espaço de trabalho, Sam poderia ser elegível para cinco campanhas diferentes. Todos os cinco são colocados em seu telefone e armazenados em cache.
3. Sam **não** executou nenhuma ação que pudesse disparar essas mensagens, mas eles poderiam receber essas mensagens na sessão.
4. O Liquid em duas das mensagens no app tem regras que excluem Sam de receber a mensagem (como o fato de o atributo personalizado de pontuação não ser alto o suficiente).
5. Sam não recebe as duas mensagens no app que os excluem, mas recebe as outras três mensagens.
6. Nenhum evento de aborto é registrado.

O Braze não registra nenhum evento de abortamento no caso de Sam porque isso não atende à nossa definição de abortamento; Sam **não executou** nenhuma ação que disparasse as mensagens. Para mensagens no app, os usuários nunca realmente disparam antes que o Braze determine que eles não devem ver a mensagem.

#### Comportamento de abortamento de mensagem no app modelado

[As mensagens no app modeladas](#templated-in-app-messages) forçam o SDK a reavaliar se uma mensagem deve ser exibida quando o evento de gatilho ocorrer. Isso tem um comportamento diferente de abortar. Para demonstrar, vamos considerar este exemplo:

1. Sam inicia uma sessão do Braze ao iniciar um app habilitado para o Braze em seu telefone.
2. Os critérios de público das campanhas ativas dizem que Sam pode ser elegível para uma mensagem no app modelada, portanto, as informações do disparo são enviadas para o dispositivo dele sem a carga útil da mensagem.
3. Sam seleciona um botão que registra um evento personalizado, disparando a mensagem no app modelada.
4. O dispositivo de Sam faz uma solicitação de rede para buscar a mensagem no app.
5. A lógica Liquid da mensagem leva a um aborto, portanto o Braze registra isso como um aborto; Sam executou a ação-gatilho antes dessa avaliação.

##### Comparação do comportamento de abortar mensagens no app

Esta tabela compara os fluxos de mensagens no app que Sam experimentou:

| Mensagem no app | Comportamento de abortar |
| --- | --- |
| Padrão | Um evento de abortamento não foi registrado porque Sam não executou nenhuma ação que disparasse uma mensagem.<br><br>As mensagens no app padrão não registram abortos porque a definição de um aborto é "não viu a mensagem apesar de ter executado a ação-gatilho". Como as mensagens no app são entregues ao dispositivo antes que as ações-gatilho ocorram, não faz sentido considerar as mensagens no app omitidas por causa da lógica Liquid. |
| Modelo | Foi registrado um evento de aborto porque Sam executou a ação-gatilho para disparar a mensagem no app, mas recebeu um aborto no modelo Liquid. <br><br>Mensagens no app com modelos registram abortos porque a avaliação do Liquid ocorre após a ação-gatilho ter sido executada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mais recursos

Antes de começar a criar suas próprias campanhas de mensagens no app - ou usar mensagens no app em uma campanha multicanais -, recomendamos que consulte nosso [guia de preparação de mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). Este guia aborda questões de direcionamento, conteúdo e conversão que você deve considerar ao criar mensagens no app.

---
nav_title: Aliasing de links
article_title: Aliasing de links
alias: /link_aliasing/
page_order: 3
description: "Este artigo descreve como funciona o aliasing de links e fornece exemplos da aparência de seus links."
channel:
  - email

---

# [![Curso de aprendizado do Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"} Aliasing de link
 
> Use o aliasing de links para criar nomes reconhecíveis e gerados pelo usuário para identificar links enviados em mensagens de e-mail da Braze. Esses links estão disponíveis para redirecionamento de segmentação, acionamento baseado em ações e análise de links.

## Sobre o aliasing de links

Com o aliasing de links, é possível criar nomes gerados pelo usuário para identificar e rastrear links enviados em e-mails. Dessa forma, você pode usar com eficiência esses aliases de links reconhecíveis em seus e-mails para rastrear o envolvimento e analisar o desempenho da campanha, sem precisar fazer referência ao link completo.

Com o aliasing de links, você pode:

- **Redirecione os usuários que clicaram em links específicos:** Identifique e direcione os usuários que clicaram em um link.
- **Crie acionadores baseados em ações:** Envie um e-mail quando um usuário clicar em um link.
- **Analise as métricas:** Compare o número de usuários que clicaram no Link A em relação ao Link B.

### Como funciona

O Braze identifica exclusivamente os links nos e-mails anexando um parâmetro extra chamado `lid` (também conhecido como identificador de link) a cada URL de link. Esse valor `lid` permite que o Braze rastreie, monitore e agregue as interações do usuário com o link, mesmo que o restante dos parâmetros do URL seja diferente. Isso ajuda a fornecer insights sobre como os usuários se envolvem com o conteúdo das suas campanhas de e-mail.

Os identificadores de link também serão atualizados se uma campanha de e-mail, um Canvas com uma mensagem de e-mail ou um bloco de conteúdo for duplicado.

## Criação de um alias de link

Para criar um alias de link, siga estas etapas: 

1. Em sua campanha ou componente do Canvas, vá para o corpo do e-mail.
2. Selecione a guia **Gerenciamento de links**.
3. O Braze gera automaticamente aliases de link padrão exclusivos para cada um de seus links.
4. Dê um nome ao alias. Os aliases devem ser nomeados exclusivamente por variante de campanha de e-mail ou componente do Canvas. 

Você também pode definir um alias que será usado para fazer referência a um link específico ao lidar com relatórios ou segmentação. 

Página de gerenciamento de links com quatro aliases de links.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
O aliasing de links só é suportado nos atributos `href` dentro de tags de âncora HTML, onde é seguro anexar um parâmetro de consulta. É uma prática recomendada incluir um ponto de interrogação (?) no final do seu link para que o Braze possa anexar facilmente o valor `lid`. Sem anexar o valor `lid`, o Braze não reconhecerá o URL para aliasing de link.
{% endalert %}

## Gerenciamento de aliases de links

Para visualizar todos os seus aliases de links rastreados, faça o seguinte:

1. Vá para **Configurações** > **Preferências de e-mail** em **Configurações do espaço de trabalho**.
2. Selecione a guia **Link Aliasing Settings (Configurações de aliasing de link** ).

{% alert important %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), essas configurações estão em **Manage Settings (Gerenciar configurações**).
{% endalert %}

Aqui, você pode classificar, pesquisar e desativar o rastreamento de aliases de links.

Página de aliases de links rastreados que mostra dois aliases de links denominados "TechPartners" e "Help" que estão associados a uma campanha denominada "Email_Survey".]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Use os pontos de extremidade [List link alias for campaign]({{site.baseurl}}/get_campaign_link_alias/) e [List link alias for Canvas]({{site.baseurl}}/get_canvas_link_alias/) para extrair o conjunto `alias` em cada variante de mensagem em uma campanha ou em um componente Canvas específico de e-mail.
{% endalert %}

A Braze recomenda avaliar os links dentro do e-mail, adicionar modelos de links e fornecer uma convenção de nomenclatura que funcione para fins de segmentação e relatórios. Isso ajuda a manter o controle de todos os links.

Quando o aliasing de links está ativado, as mensagens, os blocos de conteúdo e os modelos de links não são modificados. Todas as mensagens existentes que usam modelos de links ou blocos de conteúdo serão as mesmas. No entanto, quando você atualizar uma mensagem, a marcação de alias de link será aplicada a todos os links, portanto, será necessário reaplicar os modelos de link para que os links fiquem visíveis.

## Como os links são atualizados com o aliasing de links

As tabelas a seguir fornecem exemplos de links em um corpo de e-mail, resultados de aliasing de links e explicações sobre como o link original é atualizado com o aliasing de links.

### Link permanente

**Lógica:** O Braze insere um ponto de interrogação (?) e adiciona o primeiro parâmetro de consulta ao URL.

| Link no corpo do e-mail    | Link com aliasing                     |
|-----------------------|----------------------------------------|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link com mais parâmetros de consulta

**Lógica:** O Braze detecta outros parâmetros de consulta e anexa `lid=` ao final do URL.

| Link no corpo do e-mail                                            | Link com aliasing                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link HTML

**Lógica:** O Braze reconhece que um link é um URL e já tem um ponto de interrogação (?) presente, portanto, o parâmetro de consulta `lid` é anexado após o ponto de interrogação.

| Link no corpo do e-mail                                                | Link com aliasing                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link com âncora

**Lógica:** O Braze espera que o URL use uma estrutura padrão em que as âncoras (#) estejam presentes após um ponto de interrogação (?). Como o Braze lê da esquerda para a direita, o ponto de interrogação e o valor `lid` são anexados antes da âncora.

| Link no corpo do e-mail                               | Link com aliasing                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link com âncora e tag de captura

**Lógica:** Ao usar o aliasing de link com URLs que contêm âncoras (#), o Braze espera que a âncora seja colocada após os parâmetros de consulta. Isso significa que o valor `lid` deve ser anexado antes da âncora para o rastreamento adequado e, como o Braze lê o URL da esquerda para a direita, o ponto de interrogação (?) e `lid` devem vir antes da âncora.

| Link no corpo do e-mail                                                                        | Link com aliasing                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions#special-offer?lid={{link_alias}}">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Aliases de links de rastreamento

Na guia **Link Management (Gerenciamento de links** ), selecione quais aliases você gostaria que fossem "rastreados" para fins de segmentação e que estivessem presentes nos filtros de segmentação. Observe que os aliases rastreados são apenas para fins de segmentação e não terão impacto sobre o rastreamento do seu link para fins de relatório.

{% alert tip %}
Para acompanhar as métricas de engajamento do link, certifique-se de que seu link seja precedido por HTTP ou HTTPS. Para desativar o rastreamento de cliques para links específicos, consulte [Links universais e Links de aplicativos]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

O Braze permite que você selecione um número ilimitado de links para rastrear, embora você só possa redirecionar os usuários para os links mais recentes que eles abriram. Os perfis de usuário incluem os 100 links clicados mais recentemente. Por exemplo, se você rastrear 500 links e um usuário clicar em todos eles, poderá redirecionar ou criar segmentos com base nos 100 links clicados mais recentemente.

{% tabs local %}
{% tab Drag-And-Drop Editor %}

\![Guia Gerenciamento de links do editor de e-mail do tipo arrastar e soltar.]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab HTML editor %}

\![Guia Gerenciamento de links do editor de e-mail HTML.]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
O Braze só rastreia até os últimos 100 aliases de links clicados no nível do perfil.
{% endalert %}

### Filtros baseados em ações
 
Você pode criar mensagens baseadas em ações direcionadas a qualquer link (rastreado ou não) ou redirecionar usuários com base no fato de terem clicado em um alias em qualquer campanha de e-mail ou componente do Canvas.

Opções baseadas em ação para segmentar usuários que clicaram em um alias em um componente do Canvas ou interagiram com uma campanha.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### Filtros de segmentação

No Braze, se você tiver um alias de link em seu e-mail e um usuário clicar nele, o evento será registrado no perfil do usuário com o alias.

Se você usar o filtro de segmentação "Clicked Alias in Any Campaign or Canvas Step" (Alias clicado em qualquer campanha ou etapa do Canvas) e depois decidir renomear esse alias de link, os dados de cliques anteriores no perfil do usuário **não serão** atualizados, o que significa que ele ainda será exibido como o alias de link anterior. Portanto, se você segmentar usuários com base no novo alias de link, ele não incluirá os dados do alias de link anterior.

Se você usar o filtro de segmentação "Clicked Alias in Campaign" (Alias clicado na campanha) ou "Clicked Alias in Canvas" (Alias clicado no Canvas), isso filtrará seus usuários pelo fato de terem clicado em um alias específico em uma campanha ou Canvas específico. Se vários usuários compartilharem o mesmo endereço de e-mail e o alias do link for clicado, todos os outros usuários que compartilham o endereço de e-mail terão seus perfis de usuário atualizados. 

Os seguintes filtros de segmentação se aplicam a eventos de clique que são rastreados no momento em que o evento é processado. Isso significa que os links não rastreados não removerão os dados existentes e o rastreamento de um link não preencherá novamente os dados. Para obter mais detalhes, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

#### Desbloqueio de links

O cancelamento do rastreamento de um link não realocará os segmentos existentes com o filtro para o alias não rastreado. Os dados antigos permanecerão nos perfis de usuário até serem substituídos por dados mais recentes. 

Os links em mensagens arquivadas são automaticamente desmarcados. No entanto, se as mensagens arquivadas forem desarquivadas, os links precisarão ser rastreados novamente. Quando os aliases de links são rastreados, os relatórios de links são indexados pelo alias em vez de domínios de nível superior ou URLs completos.

Aba Campaign Analytics que exibe três aliases de link e seu total de cliques.]({% image_buster /assets/img/link_aliasing_click_table.png %})

### Evento de cliques em e-mails

Se você exportar seus dados de envolvimento com o Currents, um evento de clique de e-mail será ligeiramente diferente se você tiver o alias de link ativado. Ele terá dois campos adicionais para o [evento de cliques em e-mails]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/) quando o aliasing de links estiver ativado: `link_id` e `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
O comportamento do `dispatch_id` difere entre o Canvas e as campanhas porque o Braze trata as etapas do Canvas (exceto as etapas de entrada, que podem ser programadas) como eventos acionados, mesmo quando são "programadas". Saiba mais sobre o [comportamento do`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/) no Canvas e nas campanhas.

_Atualização registrada em agosto de 2019._
{% endalert %}

## Aliasing de links em blocos de conteúdo

Os novos blocos de conteúdo terão seus links modificados e o Braze acrescentará um `lid={{placeholder}}` a cada link, quando aplicável. Esse valor de espaço reservado é resolvido quando inserido em uma variante de mensagem de e-mail.

Para modificar os links nos blocos de conteúdo existentes que foram criados antes de o Braze ativar o alias de links, duplique os blocos de conteúdo existentes e, em seguida, modifique os links nos blocos de conteúdo duplicados.

Quando um bloco de conteúdo sem um valor `lid` é inserido em uma nova mensagem, os links desse bloco de conteúdo não são rastreados com um alias. Quando um novo Content Block for inserido em uma variante de mensagem "antiga", os links dessa variante de mensagem serão reconhecidos por aliasing de links. Os links do Content Block também são reconhecidos. No entanto, os blocos de conteúdo "antigos" não podem aninhar blocos de conteúdo "novos".

{% alert tip %}
Para blocos de conteúdo, a Braze recomenda criar cópias de blocos de conteúdo existentes para usar em novas mensagens. Isso pode ser feito por meio de duplicação em massa para evitar cenários em que você possa fazer referência a um Content Block que não tenha sido ativado para aliasing de links em uma nova mensagem.
{% endalert %}

## Aliasing de links para URLs gerados pelo Liquid

Para URLs gerados pelo Liquid, como declarações `assign` no HTML ou de um bloco de conteúdo, você deve adicionar um ponto de interrogação (`?`) à tag Liquid. Isso permite que o Braze acrescente parâmetros de consulta (`lid = somevalue`) para que o link aliasing possa funcionar corretamente. Sem identificar onde anexar os parâmetros de consulta, o aliasing de links não reconhecerá esses URLs e os modelos de links não serão aplicados.

### Exemplo

Confira este exemplo de aliasing de link para ver a formatação recomendada do link:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

Se o link tiver parâmetros dentro dele que contenham um ponto de interrogação (`?`), você poderá substituí-lo na tag de âncora por um E comercial (`&`), como neste exemplo:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}



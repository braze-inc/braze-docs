---
nav_title: Aliasing de links
article_title: Aliasing de links
alias: /link_aliasing/
page_order: 3
description: "Este artigo descreve como funciona o aliasing de links e fornece exemplos de como seus links ficarão."
channel:
  - email

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %}](https://learning.braze.com/link-aliasing) ){: style="float:right;width:120px;border:0;" class="noimgborder"}Aliasing de links
 
> Use o aliasing de usuário para criar nomes reconhecíveis e gerados pelo usuário para identificar links enviados em mensagens de e-mail do Braze. Esses links estão disponíveis para redirecionamento de segmentação, disparo baseado em ação e análise de dados de links.

## Sobre o aliasing de links

Com a aliasação de links, você pode criar nomes gerados pelo usuário para identificar e rastrear links enviados em e-mails. Dessa forma, você pode usar eficientemente esses aliases de link reconhecíveis em seus e-mails para rastrear engajamento e analisar performance da campanha, sem precisar referenciar o link completo.

Com o aliasing de link, você pode:

- **Redirecionar usuários que clicaram em links específicos:** Identificar e direcionar usuários que clicaram em um link.
- **Criar gatilhos baseados em ações:** Envie um e-mail quando um usuário clicar em um link.
- **Analise métricas:** Compare quantos usuários clicaram no Link A em comparação com o Link B.

### Como funciona?

O Braze identifica de forma única os links dentro dos emails ao anexar um parâmetro extra chamado `lid` (também conhecido como identificador de link) a cada URL de link. Este valor `lid` permite que Braze rastreie, monitore e agregue interações do usuário com o link, mesmo que o restante dos parâmetros da URL possa diferir. Isso ajuda a fornecer insights sobre como os usuários interagem com o conteúdo em suas campanhas de e-mail.

## Criação de um alias de link

Para criar um alias de link, siga estas etapas: 

1. Na sua campanha ou componente canva, Acessar o corpo do seu e-mail.
2. Selecione a guia **Link Management**.
3. O Braze gera automaticamente aliases de link padrão exclusivos para cada um de seus links.
4. Dê um nome ao alias. Os aliases devem ser nomeados exclusivamente por variante de campanha de e-mail ou componente do Canva. 

Você também pode definir um alias que será usado para fazer referência a um link específico ao lidar com relatórios ou segmentação. 

![Página de gerenciamento de links com quatro aliases de links.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
O aliasing de links só é compatível com as atribuições `href` dentro de tags de âncora HTML, onde é seguro anexar um parâmetro de consulta. É uma boa prática incluir um ponto de interrogação (?) no final do seu link para que o Braze possa facilmente anexar o `lid` valor. Sem anexar o valor `lid`, a Braze não reconhecerá o URL para aliasing de link.
{% endalert %}

## Gerenciamento de aliases de links

Para ver todos os seus aliases de link rastreados, faça o seguinte:

1. Acesse **Configurações** > **Preferências de envio de e-mail** em **Configurações do espaço de trabalho**.
2. Selecione a guia **Link Aliasing Settings (Configurações de aliasing de link)**.

{% alert important %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), essas configurações estão em **Manage Settings (Gerenciar configurações**).
{% endalert %}

Aqui, você pode classificar, pesquisar e desativar o rastreamento para aliases de link.

![Página de aliases de links rastreados que mostra dois aliases de links chamados "TechPartners" e "Help" que estão associados a uma campanha chamada "Email_Survey".]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Use os endpoints [List link alias for campaign]({{site.baseurl}}/get_campaign_link_alias/) e [List link alias for Canvas]({{site.baseurl}}/get_canvas_link_alias/) para extrair o conjunto `alias` em cada variante de mensagem em uma campanha ou um componente Canvas específico de e-mail.
{% endalert %}

Braze recomenda avaliar os links dentro do e-mail, adicionar modelos de links e fornecer uma convenção de nomes que funcione para fins de segmentação e relatórios. Isso o ajuda a manter o rastreamento de todos os links.

Quando o aliasing de links está ativado, mensagens, Blocos de Conteúdo e modelos de links não são modificados. Todas as mensagens existentes que usam modelos de links ou blocos de conteúdo serão as mesmas. No entanto, quando você atualizar uma mensagem, a marcação do alias do link será aplicada a todos os links, portanto, será necessário reaplicar os modelos de link para que os links fiquem visíveis.

## Como os links são atualizados com alias de link

As tabelas a seguir fornecem exemplos de links em um e-mail, resultados de aliasing de links e explicações sobre como o link original é atualizado com o aliasing de links.

### Link permanente

**Lógica:** O Braze insere um ponto de interrogação (?) e adiciona o primeiro parâmetro de consulta ao URL.

| Link no corpo do e-mail    | Link com aliasing                     |
|-----------------------|----------------------------------------|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link com mais consulta parâmetros

**Lógica:** A Braze detecta outros parâmetros de consulta e anexa o endereço `lid=` ao final do URL.

| Link no corpo do e-mail                                            | Link com aliasing                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### link HTML

**Lógica:** Braze reconhece que um link é uma URL e já possui um ponto de interrogação (?) presente, então o parâmetro de consulta `lid` é anexado após o ponto de interrogação.

| Link no corpo do e-mail                                                | Link com aliasing                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link com âncora

**Lógica:** O Braze espera que o URL use uma estrutura padrão em que as âncoras (#) estejam presentes após um ponto de interrogação (?). Porque Braze lê da esquerda para a direita, o ponto de interrogação e o valor `lid` são anexados antes do âncora.

| Link no corpo do e-mail                               | Link com aliasing                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link com âncora e captura de tag

**Lógica:** Ao usar alias de link com URLs que contêm âncoras (#), Braze espera que a âncora seja colocada após os parâmetros de consulta. Isso significa que o valor `lid` deve ser anexado antes do âncora para um rastreamento adequado, e como o Braze lê a URL da esquerda para a direita, o ponto de interrogação (?) e `lid` devem vir antes do âncora.

| Link no corpo do e-mail                                                                        | Link com aliasing                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions#special-offer?lid={{link_alias}}">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Rastreamento link aliases

Na guia **Link Management (Gerenciamento de links)**, selecione quais aliases você gostaria que fossem "rastreados" para fins de segmentação e que estivessem presentes nos filtros de segmentação. Note que os aliases rastreados são apenas para fins de segmentação e não terão impacto sobre o rastreamento de seu link para fins de relatório.

{% alert tip %}
Para rastrear as métricas de engajamento do link, seu link precisa ser precedido por HTTP ou HTTPS. Para desativar o rastreamento de cliques para links específicos, consulte [Links universais e App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

O Braze permite selecionar um número ilimitado de links para rastreamento, embora você só possa redirecionar os usuários para os links mais recentes que eles abriram. Os perfis de usuário incluem os 100 links clicados mais recentemente. Por exemplo, se você rastrear 500 links e um usuário clicar em todos os 500, poderá redirecionar ou criar segmentos com base nos 100 links clicados mais recentemente.

{% tabs local %}
{% tab editor de arrastar e soltar %}

![Guia Gerenciamento de links do editor de arrastar e soltar de e-mail.]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab editor de HTML %}

![Guia Gerenciamento de links do editor de e-mail HTML.]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
O Braze só rastreia até os últimos 100 aliases de links clicados no nível do perfil.
{% endalert %}

### Filtros baseados em ações
 
É possível criar mensagens baseadas em ações direcionadas a qualquer link (rastreado ou não) ou redirecionar usuários com base no fato de terem clicado em um alias em qualquer campanha de e-mail ou componente do Canvas.

![Opções baseadas em ações para direcionamento a usuários que clicaram em um alias em um componente do Canva ou interagiram com uma campanha.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### Filtros de segmentação

No Braze, se você tiver um alias de link no seu e-mail e um usuário clicar nele, o evento é registrado no perfil do usuário com o alias.

Se você usar o filtro de segmentação "Clique no Alias em Qualquer Campanha ou Etapa do Canva" e depois decidir renomear este alias de link, os dados de clique anteriores no perfil do usuário **não serão** atualizados, o que significa que ainda aparecerão como o alias de link anterior. Portanto, se você direcionar os usuários com base no novo alias de link, ele não incluirá os dados do alias de link anterior.

Se você usar o filtro de segmentação "Alias Clicado na Campanha" ou "Alias Clicado no Canva", isso filtrará seus usuários com base em se eles clicaram em um alias específico em uma campanha ou Canva específica. Se vários usuários compartilharem o mesmo e-mail e o alias do link for clicado, todos os outros usuários que compartilham o e-mail terão seus perfis de usuário atualizados. 

Os seguintes filtros de segmentação se aplicam a eventos de clique que são rastreados no momento em que o evento é processado. Isso significa que os links não rastreados não removerão os dados existentes e o rastreamento de um link não preencherá os dados novamente. Para mais detalhes, veja [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

#### Deixando de rastrear links

Desvincular um link não realocará os segmentos existentes com o filtro para o alias não rastreado. Os dados antigos permanecerão nos perfis dos usuários até serem substituídos por dados mais novos. 

Os links em mensagens arquivadas são automaticamente desmarcados. No entanto, se as mensagens arquivadas forem desarquivadas, os links precisarão ser rastreados novamente. Quando os aliases de links são rastreados, os relatórios de links são indexados pelo alias em vez de domínios de nível superior ou URLs completos.

![Guia Análise de dados da campanha que exibe três aliases de links e seus cliques totais.]({% image_buster /assets/img/link_aliasing_click_table.png %})

### Evento de cliques de e-mail

Se você exportar seus dados de engajamento com Currents, um evento de clique em e-mail será ligeiramente diferente se você tiver o aliasing de link ativado. Terá dois campos adicionais para o [evento de cliques de e-mail]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/) quando o alias de link estiver ativado: `link_id` e `link_alias`.

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
O comportamento do site `dispatch_id` difere entre o Canvas e as campanhas porque o Braze trata as etapas do Canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando são "programadas". Saiba mais sobre o [comportamento do`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/) no Canva e nas campanhas.

_Atualização notada em agosto de 2019._
{% endalert %}

## Aliasing de links em blocos de conteúdo

Os novos blocos de conteúdo terão seus links modificados e o Braze acrescentará um `lid={{placeholder}}` a cada link, quando aplicável. Esse valor de espaço reservado é resolvido quando inserido em uma variante de mensagem de e-mail.

Para modificar os links nos blocos de conteúdo existentes que foram criados antes de o Braze ativar o alias de links, duplique os blocos de conteúdo existentes e, em seguida, modifique os links nos blocos de conteúdo duplicados.

Quando um bloco de conteúdo sem um valor de `lid` é inserido em uma nova mensagem, os links desse bloco de conteúdo não são rastreados com um alias. Quando um novo bloco de conteúdo for inserido em uma variante de mensagem "antiga", os links dessa variante de mensagem serão reconhecidos pelo aliasing de links. Os links do bloco de conteúdo também são reconhecidos. No entanto, os blocos de conteúdo "antigos" não podem aninhar blocos de conteúdo "novos".

{% alert tip %}
Para blocos de conteúdo, o Braze recomenda a criação de cópias de blocos de conteúdo existentes para uso em novas mensagens. Isso pode ser feito por meio da duplicação em massa para evitar cenários em que você possa fazer referência a um bloco de conteúdo que não tenha sido ativado para aliasing de links em uma nova mensagem.
{% endalert %}

## Aliasing de links para URLs gerados pelo Liquid

Para URLs gerados pelo Liquid, como declarações `assign` no HTML ou em um bloco de conteúdo, você deve adicionar um ponto de interrogação (`?`) à tag Liquid. Isso permite que o Braze acrescente parâmetros de consulta (`lid = somevalue`) para que o link aliasing possa funcionar corretamente. Sem identificar onde anexar os parâmetros de consulta, o aliasing de links não reconhecerá esses URLs e os modelos de links não serão aplicados.

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



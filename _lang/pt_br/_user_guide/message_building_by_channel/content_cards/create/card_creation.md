---
nav_title: Criação de cartões
article_title: Criação de cartões
alias: /card_creation/
description: "Este artigo descreve as diferenças entre a criação do Content Card no lançamento da campanha ou na entrada da etapa do Canvas e na primeira impressão."
page_order: 0
tool: Campaigns
channel:
  - content cards
---

# Criação de cartões

> Você pode escolher quando o Braze avalia a elegibilidade e a personalização do público-alvo para novas campanhas de Content Card e etapas do Canvas, especificando quando o cartão é criado.

## Pré-requisitos

Para aproveitar esse recurso, você deve atualizar para as seguintes versões mínimas do SDK:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Depois de atualizar o SDK, seus usuários móveis devem atualizar o aplicativo. Você pode filtrar sua campanha ou público-alvo do Canvas para segmentar apenas [usuários nessas versões mínimas do aplicativo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Visão geral

{% tabs %}
{% tab Campaign %}

Você pode escolher quando o Braze cria um cartão na etapa de **entrega** ao criar uma nova [campanha de Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) com entrega programada.

Seção Controles do cartão de conteúdo ao editar a entrega de um cartão de conteúdo programado.]({% image_buster /assets/img_archive/card_creation.png %})

As seguintes opções estão disponíveis:

- **No lançamento da campanha:** O comportamento padrão anterior para Content Cards. O Braze calcula a elegibilidade e a personalização do público-alvo quando a campanha é lançada e, em seguida, cria o cartão e o armazena até que o usuário abra seu aplicativo. 
- **Na primeira impressão (recomendado):** Quando o usuário abre seu aplicativo (ou seja, inicia uma nova [sessão](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), o Braze determina para quais Content Cards o usuário está qualificado, modela qualquer personalização como Liquid ou Connected Content e, em seguida, cria o card. Essa opção geralmente apresenta melhor desempenho nas entregas de cartões.

Independentemente da opção selecionada, a contagem regressiva da data de expiração do Content Card começará quando a campanha for lançada.

{% endtab %}
{% tab Canvas %}

Você pode escolher quando o Braze cria um cartão na guia **Canais de mensagens de** uma [etapa de Mensagem de]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) cartão de conteúdo.

Seção Controles do cartão de conteúdo ao editar a entrega de um cartão de conteúdo programado.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

As seguintes opções estão disponíveis:

- **Na entrada da etapa:** O comportamento padrão anterior para Content Cards. O Braze calcula a elegibilidade do público quando o usuário entra na etapa do Canvas e, em seguida, cria o cartão e o armazena até que o usuário abra seu aplicativo.
- **Na primeira impressão (recomendado):** O Braze calcula a elegibilidade do público-alvo quando o usuário entra na etapa do Canvas. Quando o usuário abre seu aplicativo (ou seja, inicia uma nova [sessão](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), o Braze modela qualquer personalização, como Liquid ou Connected Content, e cria o cartão. Essa opção proporcionará melhor desempenho nas entregas de cartões e personalização mais atualizada.

Independentemente da opção selecionada, a contagem regressiva da data de expiração do Content Card começará quando o usuário entrar na etapa do Canvas.

{% alert tip %}
Se quiser que usuários anônimos vejam um Content Card logo na primeira sessão, use uma campanha em vez de um Canvas. Isso ocorre porque, quando um usuário anônimo entra em um Canvas, sua sessão já foi iniciada, portanto, ele não receberá o Content Card até que inicie uma nova sessão.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Em ambas as opções, depois que um cartão é criado, o Braze não recalcula a elegibilidade ou a personalização do público.
{% endalert %}

### Diferenças entre criar cartões no lançamento ou na entrada e na primeira impressão

Esta seção descreve as principais diferenças entre a criação de cartões no lançamento da campanha ou na entrada da etapa e na primeira impressão.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Quando a campanha é lançada / Na entrada da etapa do Canvas</th>
    <th class="tg-0pky">Na primeira impressão</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Quando usar isso</td>
    <td class="tg-0pky">Se você precisar que o conteúdo seja instantâneo em um momento específico (o momento do lançamento).</td>
    <td class="tg-0pky"><ul><li>Se for necessário exibir cartões para usuários novos ou anônimos que possam entrar no segmento após o lançamento<a href="#campaign_note">(somente campanhas*</a>).</li><li>Se você estiver usando a personalização e quiser que o conteúdo mais recente esteja disponível no cartão.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Público</td>
    <td class="tg-0pky">O Braze avalia a associação do público-alvo quando a campanha é enviada.<br><br>Usuários novos ou anônimos não serão avaliados quanto à elegibilidade se tentarem visualizar o cartão após o envio da campanha. Para campanhas recorrentes, isso ocorrerá no próximo intervalo de recorrência.</td>
    <td class="tg-0pky">O Braze avalia a associação quando o usuário abre seu aplicativo da próxima vez (inicia uma sessão, <a href="#campaign_note">somente campanhas*</a>).<br><br> Essa configuração terá um alcance de público mais amplo porque todos os usuários novos ou anônimos sempre serão avaliados quanto à elegibilidade quando tentarem visualizar o cartão. <br><br>Além disso, a limitação de taxa (limitar o número de pessoas que receberão o cartão) não é aplicável quando definida como na primeira impressão.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalização</td>
    <td class="tg-0pky">O Braze avalia o Liquid, o Connected Content e os blocos de conteúdo no momento em que a campanha é lançada ou quando um usuário entra na etapa do Canvas. Para campanhas recorrentes, isso ocorrerá no próximo intervalo de recorrência.</td>
    <td class="tg-0pky">O Braze avalia Liquid, Connected Content e Content Blocks no momento da primeira impressão ou após o próximo intervalo de recorrência.</td>
  </tr>
  <tr>
    <td class="leftHeader">Análises</td>
    <td class="tg-0pky"><em>Mensagens enviadas</em> refere-se ao número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.</td>
    <td class="tg-0pky"><em>Messages Sent (Mensagens enviadas</em> ) refere-se ao número de cartões enviados a um usuário após o início de uma sessão. No Canvas, os usuários que entrarem na etapa sem iniciar uma sessão não terão um cartão enviado, e é por isso que essa métrica pode não estar alinhada com o número de usuários que entram em uma etapa.<br><br>Embora seus usuários e impressões alcançáveis não mudem, você pode esperar uma redução no volume de envio<em>(Mensagens enviadas</em>) quando um cartão é criado na primeira impressão, em comparação com se o mesmo cartão fosse criado no lançamento da campanha ou na entrada da etapa do Canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Tempo de processamento</td>
    <td class="tg-0pky">Os cartões são criados para todos os usuários qualificados do segmento no momento do lançamento. Para grandes públicos, recomendamos selecionar <b>At First Impression (Na primeira impressão</b>), pois os cartões estarão disponíveis mais rapidamente após o lançamento.</td>
    <td class="tg-0pky">Os cartões são criados na primeira vez que um usuário tenta visualizá-lo, portanto, pode levar de 1 a 2 segundos para serem exibidos na primeira impressão.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Esse cenário só se aplica a campanhas, pois o público do Canvas é avaliado na entrada do Canvas, não no nível da etapa.</sup></p>

## Considerações

### Alteração da criação do cartão após o lançamento

A Braze recomenda não alterar a forma como os cartões são criados após o lançamento de uma campanha. Devido às diferenças na forma como as mensagens enviadas são calculadas entre os dois tipos de criação de cartão, alterar a forma como os cartões são criados após o lançamento da campanha pode afetar a precisão do volume de envio.

### Tempo de processamento potencial

Recomendamos que as campanhas com grandes públicos selecionem a opção de criar cartões na primeira impressão, pois os cartões estarão disponíveis muito mais rapidamente após o lançamento da campanha. As campanhas que são acionadas no início da sessão também podem considerar a mudança para a criação do cartão na primeira impressão (disponível por meio da entrega programada) para obter melhorias no desempenho.

Quando os cartões são criados na primeira impressão, pode levar de 1 a 2 segundos para serem processados. A duração desse tempo de processamento depende de vários fatores, como o tamanho do cartão e a complexidade das opções de modelo de mensagem. Por exemplo, o tempo de processamento dos cartões que usam o Connected Content será pelo menos tão longo quanto o tempo de resposta do Connected Content.

### Versões anteriores do SDK

Se o aplicativo de um usuário estiver executando uma versão anterior do SDK, ele ainda receberá os Content Cards enviados com uma criação de cartão especificada. No entanto, os cartões levarão mais tempo para aparecer para esses usuários e poderão não aparecer até a próxima sincronização do Content Card.


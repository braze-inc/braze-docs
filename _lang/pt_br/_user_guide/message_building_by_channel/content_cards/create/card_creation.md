---
nav_title: Criação de cartões
article_title: Criação de cartões
alias: /card_creation/
description: "Este artigo descreve as diferenças entre a criação do cartão de conteúdo no lançamento da campanha ou na entrada da etapa do Canva e na primeira impressão."
page_order: 0
tool: Campaigns
channel:
  - content cards
---

# Criação de cartões

> Você pode escolher quando o Braze avalia a elegibilidade e a personalização do público para novas campanhas de cartão de conteúdo e etapas do canva, especificando quando o cartão é criado.

## Pré-requisitos

Para aproveitar esse recurso, você deve fazer upgrade para as seguintes versões mínimas do SDK:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Depois de fazer upgrade do SDK, seus usuários móveis devem atualizar o app. É possível filtrar a campanha ou o público do Canva para [direcionamento apenas aos usuários dessas versões mínimas do app]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Visão geral

{% tabs %}
{% tab Campanha %}

Você pode escolher quando o Braze cria um cartão na etapa **de entrega** ao criar uma nova [campanha de cartão de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) com entrega programada.

![Seção controles do cartão de conteúdo ao editar a entrega de um cartão de conteúdo programado.]({% image_buster /assets/img_archive/card_creation.png %})

As seguintes opções estão disponíveis:

- **No lançamento da campanha:** O comportamento padrão anterior para os cartões de conteúdo. O Braze calcula a elegibilidade do público e a personalização quando a campanha é lançada e, em seguida, cria o cartão e o armazena até que o usuário abra seu app. 
- **Na primeira impressão (recomendado):** Quando o usuário abre seu app (ou seja, inicia uma nova [sessão](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), a Braze determina para quais cartões de conteúdo o usuário é elegível, modela qualquer personalização como Liquid ou conteúdo conectado e, em seguida, cria o cartão. Essa opção geralmente apresenta melhor performance nas entregas de cartões.

Independentemente da opção selecionada, a contagem regressiva da data de expiração do cartão de conteúdo começará quando a campanha for lançada.

{% endtab %}
{% tab Canvas %}

Você pode escolher quando o Braze cria um cartão na guia **Canais de envio de mensagens de** uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) do cartão de conteúdo.

![Seção controles do cartão de conteúdo ao editar a entrega de um cartão de conteúdo programado.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

As seguintes opções estão disponíveis:

- **Na entrada da etapa:** O comportamento padrão anterior para os cartões de conteúdo. O Braze calcula a elegibilidade do público quando o usuário entra na etapa do canva e, em seguida, cria o cartão e o armazena até que o usuário abra seu app.
- **Na primeira impressão (recomendado):** O Braze calcula a elegibilidade do público quando o usuário entra na etapa do canva. Quando o usuário abrir seu app da próxima vez (ou seja, iniciar uma nova [sessão](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), a Braze modela qualquer personalização, como Liquid ou conteúdo conectado, e cria o cartão. Com essa opção, você terá melhor performance nas entregas de cartões e uma personalização mais atualizada.

Independentemente da opção selecionada, a contagem regressiva da data de expiração do Content Card começará quando o usuário entrar na etapa do canva.

{% alert tip %}
Se quiser que usuários anônimos vejam um cartão de conteúdo logo na primeira sessão, use uma campanha em vez de um Canva. Isso ocorre porque, quando um usuário anônimo entra em uma tela, sua sessão já começou, portanto, ele não receberá o cartão de conteúdo até que inicie uma nova sessão.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Em ambas as opções, depois que um cartão é criado, a Braze não recalcula a elegibilidade ou a personalização do público.
{% endalert %}

### Diferenças entre a criação de cartões no lançamento ou na entrada e na primeira impressão

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
    <th class="tg-0pky">Quando a campanha é lançada / Na entrada da etapa do canva</th>
    <th class="tg-0pky">Na primeira impressão</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Quando usar isso</td>
    <td class="tg-0pky">Se você precisar que o conteúdo seja instantâneo em um momento específico (o momento do lançamento).</td>
    <td class="tg-0pky"><ul><li>Se for necessário exibir cartões para usuários novos ou anônimos que possam entrar no segmento após o lançamento<a href="#campaign_note">(somente campanhas*</a>).</li><li>Se estiver usando a personalização e quiser que o conteúdo mais recente esteja disponível no cartão.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Público</td>
    <td class="tg-0pky">O Braze avalia o número de membros do público quando a campanha é enviada.<br><br>Usuários novos ou anônimos não serão avaliados quanto à elegibilidade se tentarem visualizar o cartão após o envio da campanha. Para campanhas recorrentes, isso ocorrerá no próximo intervalo de recorrência.</td>
    <td class="tg-0pky">A Braze avalia a associação quando o usuário abre seu app da próxima vez (inicia uma sessão, <a href="#campaign_note">somente campanhas*</a>).<br><br> Essa configuração terá um alcance de público mais amplo, pois qualquer usuário novo ou anônimo sempre será avaliado quanto à elegibilidade quando tentar visualizar o cartão. <br><br>Além disso, o limite de taxa (limitar o número de pessoas que receberão a campanha) não é aplicável quando definido como na primeira impressão<a href="#campaign_note">(somente campanhas*</a>).</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalização</td>
    <td class="tg-0pky">O Braze avalia o Liquid, o Connected Content e os blocos de conteúdo no momento em que a campanha é lançada ou quando um usuário entra na etapa do canva. Para campanhas recorrentes, isso ocorrerá no próximo intervalo de recorrência.</td>
    <td class="tg-0pky">A Braze avalia o Liquid, o conteúdo conectado e os blocos de conteúdo no momento da primeira impressão ou após o próximo intervalo de recorrência.</td>
  </tr>
  <tr>
    <td class="leftHeader">Análise de dados</td>
    <td class="tg-0pky">O <em>envio de mensagens</em> refere-se ao número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.</td>
    <td class="tg-0pky">O <em>envio de mensagens</em> refere-se ao número de cartões enviados a um usuário após o início de uma sessão. No Canva, os usuários que entrarem na etapa sem iniciar uma sessão não terão um cartão enviado, e é por isso que essa métrica pode não estar alinhada com o número de usuários que entram em uma etapa.<br><br>Embora os usuários alcançáveis e as impressões não mudem, é de se esperar uma diminuição no volume de envio<em>(mensagens enviadas</em>) quando um cartão é criado na primeira impressão, em comparação com se o mesmo cartão fosse criado no lançamento da campanha ou na etapa do Canva.</td>
  </tr>
  <tr>
    <td class="leftHeader">Tempo de processamento</td>
    <td class="tg-0pky">Os cartões são criados para todos os usuários elegíveis do segmento no momento do lançamento. Para públicos grandes, recomendamos selecionar <b>At First Impression (Na primeira impressão</b>), pois os cartões estarão disponíveis mais rapidamente após o lançamento.</td>
    <td class="tg-0pky">Os cartões são criados na primeira vez que o usuário tenta visualizar o cartão, portanto, pode levar de 1 a 2 segundos para serem exibidos na primeira impressão.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Esse cenário só se aplica a campanhas, pois o público do canva é avaliado na entrada do canva, não no nível da etapa.</sup></p>

## Considerações

### Alteração da criação do cartão após o lançamento

A Braze recomenda não alterar a forma como os cartões são criados após o lançamento de uma campanha. Devido às diferenças na forma como as mensagens enviadas são calculadas entre os dois tipos de criação de cartão, alterar a forma como os cartões são criados após o lançamento da campanha pode afetar a precisão do volume de envio.

### Tempo de processamento potencial

Recomendamos que as campanhas com grandes públicos selecionem a opção de criar cartões na primeira impressão, pois os cartões estarão disponíveis muito mais rapidamente após o lançamento da campanha. As campanhas que são disparadas no início da sessão também podem considerar a mudança para a criação do cartão na primeira impressão (disponível por meio da entrega programada) para obter melhorias na performance.

Quando os cartões são criados na primeira impressão, pode levar de 1 a 2 segundos para que eles sejam processados. A duração desse tempo de processamento depende de vários fatores, como o tamanho do cartão e a complexidade das opções de modelo de mensagem. Por exemplo, o tempo de processamento dos cartões que usam o conteúdo conectado será pelo menos tão longo quanto o tempo de resposta do conteúdo conectado.

### Versões anteriores do SDK

Se o app de um usuário estiver executando uma versão anterior do SDK, ele ainda receberá os cartões de conteúdo enviados com uma criação de cartão especificada. No entanto, os cartões levarão mais tempo para aparecer para esses usuários e poderão não aparecer até a próxima sincronização do cartão de conteúdo.


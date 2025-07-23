---
nav_title: Tags
article_title: Tags
page_order: 12
page_type: reference
description: "Este artigo de referência aborda as tags no dashboard do Braze, que você pode usar para organizar e classificar ainda mais seu engajamento."

---
# Tags

> O Braze rastreia informações de autor, editor, data e status sobre segmentos, campanhas e Canvas, e permite criar tags para organizar e classificar ainda mais o seu engajamento.

## Tags de campanhas, telas e segmentos

Você pode adicionar tags ao criar ou editar uma campanha, uma tela ou um segmento. Clique em <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** sob o nome do engajamento e selecione uma tag existente ou comece a digitar para adicionar uma nova tag.

![Adição de tags durante a criação da campanha][2]

Você também pode adicionar tags a várias campanhas, Canvas ou segmentos selecionando vários engajamentos e clicando em <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As**.

![Adição de tags a várias campanhas ao mesmo tempo][5]

As tags definidas em uma campanha, Canva ou segmento são visíveis na página de detalhes, perto do nome do engajamento.

![Tags exibidas na página Detalhes da campanha][3]

Elas também são visíveis na lista de campanhas, telas ou segmentos, juntamente com tags adicionais para rótulos de status, como **Arquivado** e **Rascunho**.

![Tags na lista de campanhas][4]{: style ="max-width:70%;" }

Para filtrar por uma tag, selecione o nome da tag na lista de tags ou pesquise a tag no painel de pesquisa usando o seletor `tag:`. Por exemplo, para pesquisar a tag `Onboarding`, digite "tag:Onboarding".

![Pesquisa de todas as campanhas marcadas como Envio de e-mail de boas-vindas][6]

{% alert important %}
Você pode adicionar até 175 tags a uma campanha, Canva ou segmento.
{% endalert %}

## Tags de dados personalizados

As tags também podem ser adicionadas aos dados personalizados durante o gerenciamento de [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) e [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events). 

{% alert important %}
Esse recurso está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse acesso antecipado.
{% endalert %}

## Práticas recomendadas {#tags-best-practices}

Os rastreamentos podem ser uma ferramenta organizacional útil para manter o controle das táticas de engajamento. Você pode vincular segmentos e campanhas a objetivos de negócios, estágios de funil e similares.

O seguinte é um exemplo de tags que um aplicativo de eCommerce pode achar útil:

<style>
table td {
    word-break: break-word;
}
</style>


<table>
<thead>
  <tr>
    <th>Funil</th>
    <th>Objetivos de negócios</th>
    <th>Regional</th>
    <th>Campanhas</th>
    <th>Férias</th>
    <th>Transações</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Onboarding<br>Reengajamento<br>Fiel<br>PowerUser<br>Churn<br>Perdido</td>
    <td>GastoAlto<br>Usuário ativo<br>Novos usuários<br>AtribuiçãoFacebook<br>PrimeiraAção</td>
    <td>Estados Unidos<br>Nordeste<br>Centro-Oeste<br>Sul<br>Oeste<br>LATAM<br>AP<br>Europa Ocidental<br>Oriente Médio</td>
    <td>Venda<br>Cupons<br>Eventos</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>Dia de São Patrício<br>MarchMadness<br>Páscoa<br>Páscoa<br>Dia das Mães<br>MemorialDay<br>Dia dos Pais<br>QuatrodeJulho<br>DiadoTrabalho<br>Dia dos Veteranos<br>DiadeColombo<br>Dia do Presidente<br>Dia das Bruxas<br>RoshHashanah<br>Dia de Ação de Graças<br>Natal<br>Hanukkah<br>AnoNovo</td>
    <td>Transacional<br>Notificação<br>ConnectedActionTaken</td>
  </tr>
</tbody>
</table>

Você pode usar as mesmas tags em campanhas, Canvas e segmentos. Para renomear, remover ou adicionar tags com eficiência em seu dashboard, acesse **Configurações** > **Gerenciamento de tags**.

![Guia Tags na página Gerenciar configurações][8]

Para organizar ainda mais suas tags, aninhe-as em uma tag principal. Por exemplo, você pode manter todas as tags de feriados aninhadas em uma tag principal `Holidays`, ou todas as tags relacionadas a um estágio do seu funil de marketing em uma tag principal `Funnel`. 

Para fazer isso, crie uma nova tag, selecione **Aninhar tag em** e escolha em qual tag existente aninhar sua nova tag. Você também pode aninhar as tags existentes na página **Gerenciamento de tags**. Nessa página, passe o mouse sobre uma linha com sua tag e clique em **<i class="fas fa-pencil-alt"></i>Edit**. Em seguida, siga as mesmas etapas anteriores.

![Criar uma tag aninhada][1]{: style ="max-width:70%;" }

## Casos de uso

Está procurando inspiração sobre como aproveitar as tags para gerenciar o ciclo de vida do envio de mensagens? Aqui estão alguns casos de uso comuns:

### Throttling

Limite a frequência com que seus clientes recebem campanhas de um determinado tipo. Por exemplo, você pode definir os seguintes filtros para limitar a frequência das campanhas promocionais:

`Last received campaign` com a tag `Promo` há mais de 5 dias
<br>`OR`<br>
`Has not received campaign` com tag `Promo`

### Relatórios

Configure um relatório de engajamento para ficar de olho no volume de todas as campanhas com uma determinada tag. Por exemplo, se quiser monitorar todas as suas campanhas push, você pode adicionar uma tag como `Push Reporting` a essas campanhas e, em seguida, configurar um [relatório de engajamento]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) para enviar um relatório dessas campanhas marcadas todos os dias.



[1]: {% image_buster /assets/img_archive/tag_nested.png %}
[2]: {% image_buster /assets/img_archive/tags_add_tag.png %}
[3]: {% image_buster /assets/img_archive/tag_details_page.png %}
[4]: {% image_buster /assets/img_archive/tags_grid.png %}
[5]: {% image_buster /assets/img_archive/tags_apply_multiple.png %}
[6]: {% image_buster /assets/img_archive/tags_filtering.png %}
[7]: {% image_buster /assets/img_archive/Tags-Potential_Tags.png %}
[8]: {% image_buster /assets/img_archive/tags_view.png %}

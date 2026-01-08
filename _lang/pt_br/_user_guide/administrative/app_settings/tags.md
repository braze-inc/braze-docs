---
nav_title: Tags
article_title: Tags
page_order: 12
page_type: reference
description: "Este artigo de referência aborda as tags no painel do Braze, que você pode usar para organizar e classificar ainda mais seu engajamento."

---
# Tags

> O Braze rastreia informações de autor, editor, data e status sobre segmentos, campanhas e Canvases, e permite que você crie tags para organizar e classificar ainda mais seu envolvimento.

## Tags de campanha, tela e segmento

Você pode adicionar tags ao criar ou editar uma campanha, um Canvas ou um segmento. Clique em <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** abaixo do nome do compromisso e selecione uma tag existente ou comece a digitar para adicionar uma nova tag.

\![Adicionando tags durante a criação da campanha.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
Você pode adicionar até 175 tags a uma campanha, Canvas ou segmento.
{% endalert %}

### Marcação em massa

Você também pode adicionar tags a várias campanhas, Canvases ou segmentos selecionando vários envolvimentos e selecionando <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As**.

\![Adição de tags a várias campanhas ao mesmo tempo.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
Quando você usa a marcação em massa para aplicar uma nova tag a várias campanhas que já têm tags diferentes, cada campanha selecionada receberá a nova tag, e todas as tags presentes em uma campanha serão aplicadas a todas as outras campanhas selecionadas, mesmo que essas tags não tenham sido originalmente associadas a elas.
{% endalert %}

### Visualização de tags

As tags definidas em uma campanha, Canvas ou segmento ficam visíveis na página de detalhes, perto do nome do envolvimento. Eles também aparecem na análise da campanha.

Tags mostradas na página do Campaign Analytics.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### Filtragem por tag

As tags são visíveis na lista de campanhas, Canvases ou segmentos, juntamente com tags adicionais para rótulos de status, como **Arquivado** e **Rascunho**. Para filtrar por uma tag, selecione o nome da tag na lista de tags.

\![Tags na lista de campanhas.]({% image_buster /assets/img_archive/tags_grid.png %})

## Tags de dados personalizados

As tags também podem ser adicionadas aos dados personalizados ao gerenciar [atributos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) e [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events). 

{% alert important %}
Esse recurso está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Gerenciamento de tags

Você pode usar as mesmas tags em campanhas, Canvases e segmentos. Para renomear, remover ou adicionar tags com eficiência em seu painel, vá para **Configurações** > **Gerenciamento de tags**.

\![Guia Tags na página Manage Settings (Gerenciar configurações).]({% image_buster /assets/img_archive/tags_view.png %})

Para organizar ainda mais suas tags, aninhe-as em uma tag principal. Por exemplo, você pode manter todas as tags de feriados aninhadas em uma tag principal `Holidays`, ou todas as tags relacionadas a um estágio do seu funil de marketing em uma tag principal `Funnel`. 

Para fazer isso, crie uma nova tag, selecione **Aninhar tag em** e escolha em qual tag existente aninhar a nova tag. Você também pode aninhar as tags existentes na página **Gerenciamento de tags**. Nessa página, passe o mouse sobre uma linha com sua tag e clique em **<i class="fas fa-pencil-alt"></i>Edit**. Em seguida, siga as mesmas etapas anteriores.

\![Criar uma tag aninhada.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## Práticas recomendadas {#tags-best-practices}

As tags podem ser uma ferramenta organizacional útil para manter o controle das táticas de engajamento. Você pode vincular segmentos e campanhas a objetivos de negócios, estágios de funil e similares.

Veja a seguir um exemplo de tags que podem ser úteis para um aplicativo de comércio eletrônico:

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
    <td>Integração<br>Reengajamento<br>Fiel<br>PowerUser<br>Agitação<br>Perdido</td>
    <td>HighSpender<br>Usuário ativo<br>Novos usuários<br>FacebookAtribuição<br>Primeira ação</td>
    <td>Estados Unidos<br>Nordeste<br>Centro-Oeste<br>Sul<br>Oeste<br>LATAM<br>AP<br>Europa Ocidental<br>Oriente Médio</td>
    <td>Vendas<br>Cupons<br>Eventos</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>Dia de São Patrício<br>MarchMadness<br>Páscoa<br>Páscoa<br>Dia das Mães<br>MemorialDay<br>Dia dos Pais<br>Quatro de julho<br>Dia do Trabalho<br>Dia dos Veteranos<br>Dia de Colombo<br>Dia do Presidente<br>Dia das Bruxas<br>RoshHashanah<br>Dia de Ação de Graças<br>Natal<br>Hanukkah<br>Novos anos</td>
    <td>Transacional<br>Notificação<br>ConnectedActionTaken</td>
  </tr>
</tbody>
</table>

## Casos de uso

Está procurando inspiração sobre como usar tags para gerenciar o ciclo de vida de suas mensagens? Aqui estão alguns casos de uso comuns.

{% tabs %}
{% tab Throttling %}

### Estrangulamento

Limite a frequência com que seus clientes recebem campanhas de um determinado tipo. Por exemplo, você pode definir os seguintes filtros para limitar a frequência das campanhas promocionais:

`Last received campaign` com a tag `Promo` há mais de 5 dias
<br>`OR`<br>
`Has not received campaign` com etiqueta `Promo`

{% endtab %}
{% tab Reporting %}

### Relatórios

Configure um Relatório de Engajamento para ficar de olho no volume de todas as campanhas com uma determinada tag. Por exemplo, se quiser monitorar todas as suas campanhas push, você pode adicionar uma tag como `Push Reporting` a essas campanhas e, em seguida, configurar um [Relatório de Engajamento]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) para enviar a você um relatório diário dessas campanhas marcadas.

{% endtab %}
{% endtabs %}
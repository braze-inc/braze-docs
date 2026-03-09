---
nav_title: Encurtamento de links
article_title: Encurtamento de link
page_order: 3
description: "Este artigo de referência aborda como ativar o encurtamento de links em suas mensagens SMS e algumas perguntas frequentes."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Encurtamento de links

> Esta página cobre como ativar o encurtamento de links em suas mensagens SMS e RCS, testar links encurtados, usar seu domínio personalizado em links encurtados e mais.

O encurtamento de links e o rastreamento de cliques permitem que você encurte automaticamente URLs contidas em mensagens SMS ou RCS e colete análises da taxa de cliques, fornecendo métricas adicionais de engajamento para ajudar a entender como seus usuários estão interagindo com suas campanhas.

O encurtamento de links e o rastreamento de cliques podem ser ativados no [nível da variante de mensagens]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) em campanhas e Canvas. 

O comprimento do URL é determinado pelo tipo de rastreamento que está ativado:
- **O rastreamento básico** ativa o rastreamento de cliques no nível da campanha. URLs estáticas terão um comprimento de 20 caracteres, e URLs personalizadas terão um comprimento de 25 caracteres.
- **Rastreamento avançado** permite rastreamento de cliques em nível de campanha e de usuário, e possibilita o uso de segmentação e capacidades de redirecionamento que dependem de cliques. Os cliques também gerarão um [evento de clique por SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) enviado pelo Currents. URLs estáticas com rastreamento avançado terão um comprimento de 27-28 caracteres, permitindo que você crie segmentos de usuários que clicaram em URLs. URLs personalizadas terão um comprimento de 32-33 caracteres.

Os links são encurtados usando nosso domínio curto compartilhado (`brz.ai`). Um exemplo de URL pode parecer algo como: `https://brz.ai/8jshX` (básico, estático) ou `https://brz.ai/p/8jshX/2dj8d` (avançado, personalizado). Para saber mais, consulte [Testes](#testing).

Quaisquer URLs estáticas que começam com `http://` ou `https://` são encurtadas. URLs estáticas encurtadas são válidas por um ano a partir da data em que foram criadas. URLs encurtadas que contêm personalização Liquid são válidas por dois meses.

{% alert note %}
Se você planeja usar o BrazeAI<sup>TM</sup> [Filtro de Canal Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) e deseja que os canais SMS e RCS sejam selecionáveis, ative o encurtamento de links com rastreamento avançado.
{% endalert %}

## Uso de encurtamento de links

Para usar o encurtamento de links, certifique-se de que a opção de encurtamento de links no criador de mensagens esteja ativada. Em seguida, opte por usar o rastreamento básico ou avançado.

![Criador de mensagens com um botão para encurtar links.]({% image_buster /assets/img/link_shortening/shortening1.png %})

O Braze reconhece apenas URLs que começam com `http://` ou `https://`. Quando um URL é reconhecido, a seção **Prévia** é atualizada com um URL de espaço reservado. O Braze estima o comprimento da URL após o encurtamento, mas um aviso solicita que você selecione um usuário teste e salve a mensagem como um rascunho para uma estimativa mais precisa.

![Criador de mensagens com um URL longo na caixa "Mensagem" e um link encurtado gerado na prévia.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Adição de parâmetros UTM

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personalização Liquid em URLs

Você pode construir dinamicamente seu URL diretamente no criador do Braze, o que lhe permite adicionar parâmetros UTM dinâmicos aos seus URLs ou enviar aos usuários links exclusivos (como direcionar os usuários para o carrinho abandonado ou para um produto específico que está de volta ao estoque).

### Criar um URL com tags de personalização Liquid compatíveis

Os URLs podem ser gerados dinamicamente com o uso de qualquer [tag de personalização Liquid compatível]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Também é possível fazer a redução de variáveis Liquid definidas de forma personalizada. Vários exemplos são mostrados abaixo:

### Criar um URL usando variáveis Liquid

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Encurtar URLs renderizados por variáveis Liquid

Encurtamos os URLs que são renderizados pelo Liquid, mesmo aqueles incluídos nas propriedades do API-trigger. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa uma URL válida, encurtamos e rastreamos essa URL antes de enviar a mensagem. 

### Encurtar URLs no endpoint `/messages/send`

O encurtamento de links também está ativado para mensagens somente da API por meio do [endpoint `/messages/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Para também ativar o rastreamento básico ou avançado, use os parâmetros de solicitação `link_shortening_enabled` ou `user_click_tracking_enabled`.

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Opcional | Booleano | Defina `link_shortening_enabled` como `true` para ativar o encurtamento de links e o rastreamento de cliques em nível de campanha. Para usar o rastreamento, um `campaign_id` e um `message_variation_id` devem estar presentes.|
|`user_click_tracking_enabled`| Opcional | Booleano | Defina `user_click_tracking_enabled` como `true` para ativar o encurtamento de links e o rastreamento de cliques no nível da campanha e do usuário. É possível usar os dados de rastreamento para criar segmentos de usuários que clicaram em URLs.<br><br> Para usar esse parâmetro, `link_shortening_enabled` deve ser `true`, e um `campaign_id` e `message_variation_id` devem estar presentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Para obter uma lista completa dos parâmetros de solicitação, acesse [parâmetros de solicitação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Testes

Antes de lançar sua campanha ou Canva, é uma prática recomendada fazer uma prévia e testar sua mensagem primeiro. Para fazer isso, acesse a guia **Teste** para visualizar e enviar uma mensagem SMS ou RCS para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou um usuário individual. 

Esta prévia é atualizada com personalização relevante e a URL encurtada. O número de caracteres e [segmentos faturáveis]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) também é atualizado para refletir a personalização renderizada e a URL encurtada.

Certifique-se de salvar a campanha ou o Canva antes de enviar uma mensagem de teste para receber uma representação da URL encurtada que é enviada em sua mensagem. Se a campanha ou o canva não for salva antes de um envio de teste, o envio de teste inclui uma URL de espaço reservado.

Para que os canvases apareçam no filtro "Clique no link SMS encurtado", a etapa do canva que contém o link curto também deve estar habilitada com rastreamento avançado, que permite o rastreamento de cliques em nível de usuário. Se o link curto estiver configurado com rastreamento básico, a opção de filtrar eventos de cliques no link curto SMS não estará disponível.

{% alert important %}
Se um rascunho for criado em um Canva ativo, não será gerado um URL encurtado. A URL encurtada real é gerada quando o rascunho do canva é ativado.
{% endalert %}

![Guia "Teste" de mensagens com campos para selecionar os destinatários do teste.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
A personalização Liquid e os URLs encurtados são modelos na guia **Teste** depois que um usuário é selecionado. Certifique-se de que um usuário esteja selecionado para receber uma contagem precisa de caracteres.
{% endalert %}

## Rastreamento de cliques

Quando o encurtamento de link está ativado, a tabela **Desempenho de SMS/MMS/RCS** inclui uma coluna intitulada **Total de Cliques** que mostra uma contagem de eventos de cliques por variante e uma taxa de cliques associada. Para mais detalhes sobre métricas, veja [Desempenho da mensagem]({{site.baseurl}}/sms_mms_rcs_reporting/).

![Tabela de métricas de performance de SMS e MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

As tabelas **Desempenho Histórico** e **Desempenho de SMS/MMS/RCS** também incluem uma opção para **Total de Cliques** e mostram uma série temporal diária de eventos de cliques. Os cliques são incrementados no redirecionamento (por exemplo, quando um usuário visita um link) e podem ser incrementados mais de uma vez por usuário.

## Redirecionamento de usuários

Para orientações sobre redirecionamento, visite [Redirecionamento]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Eu sei quais usuários individuais estão clicando em um URL?

Sim. Quando o **rastreamento avançado** está ativado, é possível redirecionar os usuários que clicaram em URLs, aproveitando os [filtros de redirecionamento de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) ou os eventos de clique de SMS (`users.messages.sms.ShortLinkClick`) enviados via Currents.

### O encurtamento de links funciona com deep links ou links universais?

O encurtamento de links não funciona com deep links. Alternativamente, você pode encurtar links universais de provedores de terceiros, como Branch ou Appsflyer, mas os usuários podem experimentar um breve redirecionamento ou efeito de "piscar". Isso ocorre porque o link encurtado passa primeiro pela web antes de resolver para o link universal que suporta a abertura do app. Além disso, a Braze não consegue solucionar problemas que possam surgir ao encurtar links universais, como quebrar a atribuição ou causar redirecionamentos inesperados.

{% alert note %}
Teste a experiência do usuário antes de implementar o encurtamento de links com links universais para confirmar que atende às suas expectativas.
{% endalert %}

### Estão `send_ids` associados a eventos de cliques SMS?

Não. No entanto, se você tiver o rastreamento avançado habilitado, você pode geralmente atribuir `send_ids` a eventos de cliques usando [Construtor de Consultas]({{site.baseurl}}/query_builder/) para consultar dados de Currents com esta consulta:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```

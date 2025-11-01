---
nav_title: Encurtamento de links
article_title: Encurtamento de links
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

> Esta página aborda como ativar o encurtamento de links em suas mensagens SMS e RCS, testar links encurtados, usar seu domínio personalizado em links encurtados e muito mais.

O encurtamento de links e o rastreamento de cliques permitem encurtar automaticamente os URLs contidos em mensagens SMS ou RCS e coletar análises de taxa de cliques, fornecendo métricas adicionais de envolvimento para ajudar a entender como os usuários estão se envolvendo com suas campanhas.

O encurtamento de links e o rastreamento de cliques podem ser ativados no [nível da variante da mensagem]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) em campanhas e Canvases. 

O comprimento do URL é determinado pelo tipo de rastreamento que está ativado:
- **O rastreamento básico** permite o rastreamento de cliques no nível da campanha. Os URLs estáticos terão um comprimento de 20 caracteres e os URLs personalizados terão um comprimento de 25 caracteres.
- **O rastreamento avançado** permite o rastreamento de cliques no nível da campanha e do usuário, além de permitir o uso de recursos de segmentação e redirecionamento que dependem de cliques. Os cliques também gerarão um [evento de clique por SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) enviado pelo Currents. Os URLs estáticos com rastreamento avançado terão um comprimento de 27 a 28 caracteres, o que permite criar segmentos de usuários que clicaram nos URLs. Para URLs personalizados, eles terão um comprimento de 32 a 33 caracteres.

Os links serão encurtados usando nosso domínio curto compartilhado (`brz.ai`). Um exemplo de URL pode ter a seguinte aparência: `https://brz.ai/8jshX` (básico, estático) ou `https://brz.ai/p/8jshX/2dj8d` (avançado, personalizado). Consulte [Testes](#testing) para obter mais informações.

Todos os URLs estáticos que começam com `http://` ou `https://` serão encurtados. Os URLs estáticos encurtados serão válidos por um ano a partir da data em que foram criados. Os URLs encurtados que contêm personalização do Liquid serão válidos por dois meses.

{% alert note %}
Se você planeja usar o [filtro de canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) <sup>BrazeAITM</sup> e deseja que os canais SMS e RCS sejam selecionáveis, ative o encurtamento de links com rastreamento avançado.
{% endalert %}

## Uso de encurtamento de links

Para usar o encurtamento de links, verifique se a opção de encurtamento de links no compositor de mensagens está ativada. Em seguida, opte por usar o rastreamento básico ou avançado.

\![Compositor de mensagens com uma opção para encurtar links.]({% image_buster /assets/img/link_shortening/shortening1.png %})

O Braze só reconhecerá URLs que comecem com `http://` ou `https://`. Quando um URL é reconhecido, a seção **Preview** é atualizada com um URL de espaço reservado. O Braze estimará o tamanho do URL após o encurtamento, mas um aviso solicitará que você selecione um usuário de teste e salve a mensagem como rascunho para obter uma estimativa mais precisa.

Compositor de mensagem com um URL longo na caixa "Mensagem" e um link encurtado gerado na visualização.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Adição de parâmetros UTM

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personalização líquida em URLs

Você pode construir dinamicamente seu URL diretamente no compositor do Braze, o que lhe permite adicionar parâmetros UTM dinâmicos aos seus URLs ou enviar links exclusivos aos usuários (como direcionar os usuários para o carrinho abandonado ou para um produto específico que está de volta ao estoque).

### Criar um URL com tags de personalização do Liquid compatíveis

Os URLs podem ser gerados dinamicamente por meio do uso de qualquer [tag de personalização do Liquid compatível]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Também oferecemos suporte à redução de variáveis Liquid definidas de forma personalizada. Vários exemplos são mostrados abaixo:

### Criar um URL usando variáveis do Liquid

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Encurtar URLs renderizados por variáveis do Liquid

Encurtamos os URLs que são renderizados pelo Liquid, mesmo aqueles incluídos nas propriedades de acionamento de API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representar um URL válido, encurtaremos e rastrearemos esse URL antes de enviar a mensagem. 

### Encurtar URLs no ponto de extremidade /messages/send

O encurtamento de links também está ativado para mensagens somente de API por meio do [ponto de extremidade`/messages/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Para ativar também o rastreamento básico ou avançado, use os parâmetros de solicitação `link_shortening_enabled` ou `user_click_tracking_enabled`.

| Parâmetro | Necessário | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Opcional | Booleano | Defina `link_shortening_enabled` como `true` para ativar o encurtamento de links e o rastreamento de cliques em nível de campanha. Para usar o rastreamento, um `campaign_id` e um `message_variation_id` devem estar presentes.|
|`user_click_tracking_enabled`| Opcional | Booleano | Defina `user_click_tracking_enabled` como `true` para ativar o encurtamento de links e o rastreamento de cliques no nível da campanha e do usuário. Você pode usar os dados rastreados para criar segmentos de usuários que clicaram em URLs.<br><br> Para usar esse parâmetro, `link_shortening_enabled` deve ser `true`, e um `campaign_id` e `message_variation_id` devem estar presentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Para obter uma lista completa dos parâmetros de solicitação, acesse [parâmetros de solicitação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Testes

Antes de lançar sua campanha ou Canvas, a melhor prática é visualizar e testar sua mensagem primeiro. Para isso, vá para a guia **Teste** para visualizar e enviar uma mensagem SMS ou RCS para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou para um usuário individual. 

Essa visualização será atualizada com a personalização relevante e o URL encurtado. O número de caracteres e [os segmentos faturáveis]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) também serão atualizados para refletir a personalização renderizada e o URL encurtado. 

Certifique-se de salvar a campanha ou o Canvas antes de enviar uma mensagem de teste para receber uma representação do URL encurtado que será enviado em sua mensagem. Se a campanha ou o Canvas não for salvo antes de um envio de teste, o envio de teste incluirá uma URL de espaço reservado.

{% alert important %}
Se um rascunho for criado em um Canvas ativo, não será gerado um URL abreviado. O URL encurtado real é gerado quando o rascunho do Canvas é ativado.
{% endalert %}

Aba "Teste" da mensagem com campos para selecionar os destinatários do teste.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
A personalização líquida e os URLs encurtados são modelados na guia **Teste** depois que um usuário é selecionado. Certifique-se de que um usuário esteja selecionado para receber uma contagem precisa de caracteres.
{% endalert %}

## Rastreamento de cliques

Quando o encurtamento de links está ativado, a tabela **SMS/MMS/RCS Performance** inclui uma coluna intitulada **Total Clicks (Total de cliques** ) que mostra uma contagem de eventos de cliques por variante e uma taxa de cliques associada. Para obter mais detalhes sobre as métricas, consulte [Desempenho da mensagem]({{site.baseurl}}/sms_mms_rcs_reporting/).

Tabela de métricas de desempenho de SMS e MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

As tabelas **Historical Performance (Desempenho histórico** ) e **SMS/MMS/RCS Performance (Desempenho de SMS/MMS/RCS** ) também incluem uma opção para **Total Clicks (Total de cliques** ) e mostram uma série temporal diária de eventos de cliques. Os cliques são incrementados no redirecionamento (por exemplo, quando um usuário visita um link) e podem ser incrementados mais de uma vez por usuário.

## Redirecionamento de usuários

Para obter orientação sobre retargeting, visite [Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Eu sei quais usuários individuais estão clicando em um URL?

Sim. Quando **o Advanced Tracking** está ativado, você pode redirecionar os usuários que clicaram em URLs, aproveitando os [filtros de redirecionamento de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) ou os eventos de clique de SMS (`users.messages.sms.ShortLinkClick`) enviados pelo Currents.

{% alert note %}
No momento, os eventos RCS Click não estão disponíveis no Currents.
{% endalert %}

### O encurtamento de links funciona com deep links ou links universais?

O encurtamento de links não funciona com links diretos. Como alternativa, você pode encurtar links universais de provedores de terceiros, como Branch ou Appsflyer, mas os usuários podem experimentar um breve redirecionamento ou efeito de "cintilação". Isso ocorre porque o link encurtado é roteado primeiro pela Web antes de ser resolvido para o link universal que suporta a abertura do aplicativo. Além disso, o Braze não consegue solucionar problemas que possam surgir ao encurtar links universais, como quebrar a atribuição ou causar redirecionamentos inesperados.

{% alert note %}
Teste a experiência do usuário antes de implementar o encurtamento de links com links universais para confirmar se ele atende às suas expectativas.
{% endalert %}

### O site `send_ids` está associado aos eventos de clique do SMS?

No entanto, se você tiver o rastreamento avançado ativado, poderá atribuir `send_ids` com eventos de clique usando o [Query Builder]({{site.baseurl}}/query_builder/) para consultar os dados do Currents com essa consulta:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```
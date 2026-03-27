O encurtamento de links e o rastreamento de cliques permitem que você encurte automaticamente URLs contidos em mensagens SMS ou RCS e colete análise de dados de taxa de cliques, fornecendo métricas de engajamento adicionais para ajudar a entender como os usuários estão interagindo com suas campanhas.

O encurtamento de links e o rastreamento de cliques podem ser ativados no [nível da variante de mensagem]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) tanto em campanhas quanto em canvas.

O comprimento da URL é determinado pelo tipo de rastreamento que está ativado:
- **Rastreamento básico** ativa o rastreamento de cliques no nível da campanha. URLs estáticas terão um comprimento de 20 caracteres, e URLs personalizadas terão um comprimento de 25 caracteres.
- **Rastreamento avançado** ativa o rastreamento de cliques no nível da campanha e no nível do usuário, e permite o uso de recursos de segmentação e redirecionamento que dependem de cliques. Os cliques também gerarão um [evento de clique de SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) enviado pelo Currents. URLs estáticas com rastreamento avançado terão um comprimento de 27-28 caracteres, permitindo que você crie segmentos de usuários que clicaram em URLs. URLs personalizadas terão um comprimento de 32-33 caracteres.

Os links são encurtados usando nosso domínio curto compartilhado (`brz.ai`) ou seu domínio personalizado de encurtamento de links. Um exemplo de URL pode ser algo como: `https://brz.ai/8jshX` (básico, estático) ou `https://brz.ai/p/8jshX/2dj8d` (avançado, personalizado). Consulte [Testes](#testing) para mais informações.

Quaisquer URLs estáticas que comecem com `http://` ou `https://` são encurtadas. URLs estáticas encurtadas são válidas por um ano a partir da data em que foram criadas. URLs encurtadas que contêm personalização com Liquid são válidas por dois meses.

{% alert note %}
Se você planeja usar o [filtro de Canal Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) da BrazeAI<sup>TM</sup> e deseja que os canais SMS e RCS sejam selecionáveis, ative o encurtamento de links com rastreamento avançado.
{% endalert %}

## Usando o encurtamento de links

Para usar o encurtamento de links, certifique-se de que o botão de encurtamento de links no criador de mensagens esteja ativado. Em seguida, escolha usar o rastreamento básico ou avançado.

![Criador de mensagens com um botão para encurtamento de links.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening1.png %})

A Braze reconhece apenas URLs que começam com `http://` ou `https://`. Quando uma URL é reconhecida, a seção **Prévia** é atualizada com uma URL de espaço reservado. A Braze estima o comprimento da URL após o encurtamento, mas um aviso solicita que você selecione um usuário teste e salve a mensagem como rascunho para uma estimativa mais precisa.

![Criador de mensagens com uma URL longa na caixa "Mensagem" e um link encurtado gerado na prévia.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening3.png %})

### Adicionando parâmetros UTM

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personalização com Liquid em URLs

Você pode construir dinamicamente sua URL diretamente no criador da Braze, permitindo adicionar parâmetros UTM dinâmicos às suas URLs ou enviar links exclusivos aos usuários (como direcionar usuários ao carrinho abandonado ou a um produto específico que voltou ao estoque).

### Criar uma URL com tags de personalização Liquid compatíveis

URLs podem ser geradas dinamicamente por meio do uso de quaisquer [tags de personalização Liquid compatíveis]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Também oferecemos suporte ao encurtamento de variáveis Liquid definidas de forma personalizada. Vários exemplos são mostrados abaixo:

### Criar uma URL usando variáveis Liquid

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Encurtar URLs renderizadas por variáveis Liquid

Encurtamos URLs que são renderizadas por Liquid, mesmo aquelas incluídas em propriedades de gatilho de API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa uma URL válida, encurtamos e rastreamos essa URL antes de enviar a mensagem.

### Encurtar URLs no endpoint `/messages/send`

O encurtamento de links também é ativado para mensagens somente via API por meio do [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Para também ativar o rastreamento básico ou avançado, use os parâmetros de solicitação `link_shortening_enabled` ou `user_click_tracking_enabled`.

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Opcional | booleano | Defina `link_shortening_enabled` como `true` para ativar o encurtamento de links e o rastreamento de cliques no nível da campanha. Para usar o rastreamento, um `campaign_id` e `message_variation_id` devem estar presentes.|
|`user_click_tracking_enabled`| Opcional | booleano | Defina `user_click_tracking_enabled` como `true` para ativar o encurtamento de links e o rastreamento de cliques no nível da campanha e do usuário. Você pode usar os dados rastreados para criar segmentos de usuários que clicaram em URLs.<br><br> Para usar este parâmetro, `link_shortening_enabled` deve ser `true`, e um `campaign_id` e `message_variation_id` devem estar presentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Para uma lista completa de parâmetros de solicitação, acesse [parâmetros de solicitação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Testes

Antes de lançar sua campanha ou canva, é uma prática recomendada visualizar e testar sua mensagem primeiro. Para isso, acesse a guia **Teste** para visualizar e enviar uma mensagem SMS ou RCS para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou um usuário individual.

Esta prévia é atualizada com a personalização relevante e a URL encurtada. O número de caracteres e os [segmentos faturáveis]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) também são atualizados para refletir a personalização renderizada e a URL encurtada.

Certifique-se de salvar a campanha ou canva antes de enviar uma mensagem de teste para receber uma representação da URL encurtada que é enviada na sua mensagem. Se a campanha ou canva não for salva antes de um envio de teste, o envio de teste incluirá uma URL de espaço reservado.

Para que os canvas apareçam no filtro "Clicou no link encurtado de SMS", a etapa do canva que contém o link encurtado também deve estar ativada com rastreamento avançado, que permite o rastreamento de cliques no nível do usuário. Se o link encurtado estiver configurado com rastreamento básico, a opção de filtrar eventos de clique em links encurtados de SMS não estará disponível.

{% alert important %}
Se um rascunho for criado dentro de um canva ativo, uma URL encurtada não será gerada. A URL encurtada real é gerada quando o rascunho do canva é ativado.
{% endalert %}

![Guia "Teste" da mensagem com campos para selecionar destinatários de teste.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening2.png %})

{% alert note %}
A personalização com Liquid e as URLs encurtadas são processadas na guia **Teste** após um usuário ter sido selecionado. Certifique-se de que um usuário esteja selecionado para receber uma contagem precisa de caracteres.
{% endalert %}

## Rastreamento de cliques

Quando o encurtamento de links está ativado, a tabela **Performance de SMS/MMS/RCS** inclui uma coluna intitulada **Total de Cliques** que mostra uma contagem de eventos de clique por variante e uma taxa de cliques associada. Para saber mais sobre métricas, consulte [Performance da mensagem]({{site.baseurl}}/sms_mms_rcs_reporting/).

![Tabela de métricas de performance de SMS e MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

As tabelas **Performance Histórica** e **Performance de SMS/MMS/RCS** também incluem uma opção para **Total de Cliques** e mostram uma série temporal diária de eventos de clique. Os cliques são incrementados no redirecionamento (como quando um usuário visita um link) e podem ser incrementados mais de uma vez por usuário.

## Redirecionamento de usuários

Para orientações sobre redirecionamento, visite [Redirecionamento]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Eu sei quais usuários individuais estão clicando em uma URL?

Sim. Quando o **Rastreamento Avançado** está ativado, você pode redirecionar usuários que clicaram em URLs aproveitando os [filtros de redirecionamento de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) ou os eventos de clique de SMS (`users.messages.sms.ShortLinkClick`) enviados pelo Currents.

### O encurtamento de links funciona com deep links ou links universais?

O encurtamento de links não funciona com deep links. Alternativamente, você pode encurtar links universais de provedores terceiros como Branch ou Appsflyer, mas os usuários podem experimentar um breve redirecionamento ou efeito de "cintilação". Isso ocorre porque o link encurtado passa pela web primeiro antes de resolver para o link universal que suporta a abertura do app. Além disso, a Braze não consegue solucionar problemas que possam surgir ao encurtar links universais, como quebrar a atribuição ou causar redirecionamentos inesperados.

{% alert note %}
Teste a experiência do usuário antes de implementar o encurtamento de links com links universais para confirmar que atende às suas expectativas.
{% endalert %}

### Os `send_ids` estão associados a eventos de clique de SMS?

Não. No entanto, se você tiver o rastreamento avançado ativado, geralmente pode atribuir `send_ids` a eventos de clique usando o [Query Builder]({{site.baseurl}}/query_builder/) para consultar dados do Currents com esta consulta:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```
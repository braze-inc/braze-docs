Link shortening permite encurtar automaticamente URLs contidas em mensagens SMS ou RCS e coletar análise de dados de taxa de cliques, fornecendo métricas de engajamento adicionais para ajudar a entender como os usuários estão interagindo com suas campanhas.

O link shortening pode ser ativado no [nível da variante de mensagem]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) tanto em campanhas quanto em canvas. Quando o link shortening está ativado, os cliques geram um [evento de clique de SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) enviado pelo Currents.

Os links são encurtados usando nosso domínio curto compartilhado (`brz.ai`) ou seu domínio personalizado de encurtamento de links, e são válidos por 9 semanas a partir da data em que foram criados. Um exemplo de URL pode ser algo como `https://brz.ai/8jshX2dj`. 

## Usando o link shortening

Para usar o link shortening, certifique-se de que a caixa de seleção de link shortening no criador de mensagens esteja selecionada.

{% tabs %}
{% tab SMS composer %}

![Criador de mensagens SMS com uma caixa de seleção marcada para link shortening.]({% image_buster /assets/img/link_shortening/shortening1.png %})

{% endtab %}
{% tab RCS composer %}

![Criador de mensagens RCS com uma caixa de seleção marcada para link shortening.]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %})

{% endtab %}
{% endtabs %}

A Braze reconhece apenas URLs que começam com `http://` ou `https://`. Quando uma URL é reconhecida, a seção **Prévia** é atualizada com uma URL de espaço reservado. A Braze estima o comprimento da mensagem após o encurtamento, mas um aviso solicita que você selecione um usuário teste e salve a mensagem como rascunho para uma estimativa mais precisa.

![Criador de mensagens com uma URL longa no campo "Mensagem" e um link encurtado gerado na prévia.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Adicionando parâmetros UTM

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personalização com Liquid em URLs

Você pode construir dinamicamente sua URL diretamente no criador da Braze, permitindo adicionar parâmetros UTM dinâmicos às suas URLs ou enviar links exclusivos aos usuários (como direcionar usuários ao carrinho abandonado ou a um produto específico que voltou ao estoque).

### Criar uma URL com tags de personalização Liquid compatíveis

URLs podem ser geradas dinamicamente por meio do uso de qualquer [tag de personalização Liquid compatível]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

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

O link shortening também é ativado para mensagens somente via API por meio do [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Para uma lista completa de parâmetros de solicitação, acesse [parâmetros de solicitação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Sim | booleano | Defina `link_shortening_enabled` como `true` para ativar o link shortening. Para usar o rastreamento, um `campaign_id` e `message_variation_id` devem estar presentes.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Testes

Antes de lançar sua campanha ou canva, a prática recomendada é visualizar e testar sua mensagem primeiro. Para isso, acesse a guia **Teste** para visualizar e enviar uma mensagem SMS ou RCS para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou um usuário individual. 

Essa prévia é atualizada com a personalização relevante e a URL encurtada. O número de caracteres e os [segmentos faturáveis]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) também são atualizados para refletir a personalização renderizada e a URL encurtada.

Certifique-se de salvar a campanha ou canva antes de enviar uma mensagem de teste para receber uma representação da URL encurtada que é enviada na sua mensagem. Se a campanha ou canva não for salva antes de um envio de teste, o envio de teste incluirá uma URL de espaço reservado.

{% alert important %}
Se um rascunho for criado dentro de uma canva ativa, uma URL encurtada não será gerada. A URL encurtada real é gerada quando o rascunho da canva é ativado.
{% endalert %}

![Guia "Teste" da mensagem com campos para selecionar destinatários de teste.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
A personalização com Liquid e as URLs encurtadas são modeladas na guia **Teste** após um usuário ter sido selecionado. Certifique-se de que um usuário esteja selecionado para receber uma contagem precisa de caracteres.
{% endalert %}

## Rastreamento de cliques

Quando o link shortening está ativado, a tabela **Performance de SMS/MMS/RCS** inclui uma coluna intitulada **Total de Cliques** que mostra uma contagem de eventos de clique por variante e uma taxa de cliques associada. Para mais informações sobre métricas, consulte [Performance de mensagens]({{site.baseurl}}/sms_mms_rcs_reporting/).

![Tabela de métricas de performance de SMS e MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

As tabelas **Performance Histórica** e **Performance de SMS/MMS/RCS** também incluem uma opção para **Total de Cliques** e mostram uma série temporal diária de eventos de clique. Os cliques são incrementados no redirecionamento (como quando um usuário visita um link) e podem ser incrementados mais de uma vez por usuário.

## Redirecionamento de usuários

Para orientações sobre redirecionamento, visite [Redirecionamento]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Eu sei quais usuários individuais estão clicando em uma URL?

Sim. Você pode redirecionar usuários que clicaram em URLs usando os [filtros de redirecionamento de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) ou os eventos de clique de SMS (`users.messages.sms.ShortLinkClick`) enviados pelo Currents.

### O link shortening funciona com deep links ou links universais?

O link shortening não funciona com deep links. Alternativamente, você pode encurtar links universais de provedores terceiros como Branch ou Appsflyer, mas os usuários podem experimentar um breve redirecionamento ou efeito de "flickering". Isso ocorre porque o link encurtado passa pela web primeiro antes de resolver para o link universal que suporta a abertura do app. Além disso, a Braze não consegue solucionar problemas que possam surgir ao encurtar links universais, como quebrar a atribuição ou causar redirecionamentos inesperados.

{% alert note %}
Teste a experiência do usuário antes de implementar o link shortening com links universais para confirmar que atende às suas expectativas.
{% endalert %}

### Os `send_ids` estão associados a eventos de clique de SMS?

Não. No entanto, você geralmente pode atribuir `send_ids` a eventos de clique usando o [Query Builder]({{site.baseurl}}/query_builder/) para consultar dados do Currents com esta consulta:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```
---
nav_title: Encurtamento de link
article_title: Encurtamento de link
page_order: 5
description: "Este artigo de referência aborda como ativar o encurtamento de links em suas mensagens SMS e algumas perguntas frequentes."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
---

# Encurtamento de links

> O encurtamento de links e o rastreamento de cliques permitem encurtar automaticamente os URLs contidos nas mensagens SMS e coletar análises de dados da taxa de engajamento, fornecendo métricas de engajamento adicionais para ajudar a entender como os usuários estão se envolvendo com suas campanhas de mensagens SMS. 

## Visão geral

O encurtamento de links e o rastreamento de cliques podem ser ativados no [nível da variante de mensagens]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) em campanhas e Canvas. 

O comprimento da URL será determinado pelo tipo de rastreamento que está ativado:
- **O rastreamento básico** ativa o rastreamento de cliques no nível da campanha. Os URLs estáticos terão um comprimento de 20 caracteres e os URLs dinâmicos terão um comprimento de 25 caracteres.
- **O rastreamento avançado ativa** o rastreamento de cliques no nível da campanha e do usuário. Os cliques também gerarão um [evento de clique por SMS]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) enviado pelo Currents. Os URLs estáticos com rastreamento avançado terão um comprimento de 27 a 28 caracteres, o que permite criar segmentos de usuários que clicaram nos URLs. Para URLs dinâmicos, eles terão um comprimento de 32 a 33 caracteres.

Os links serão encurtados usando nosso domínio curto compartilhado (`brz.ai`). Um exemplo de URL pode ter a seguinte aparência: `https://brz.ai/8jshX` (básico, estático) ou `https://brz.ai/8jshX/2dj8d` (avançado, dinâmico). Para saber mais, consulte [Testes](#testing).

Os URLs estáticos encurtados serão válidos por um ano a partir da data em que foram criados. Os URLs encurtados que contêm a personalização Liquid serão válidos por dois meses.

{% alert note %}
Se você planeja usar o [filtro BrazeAITM [Intelligent Channel]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) e deseja que o canal SMS seja selecionável, ative o encurtamento de links SMS com rastreamento avançado e [rastreamento de cliques]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#click-tracking).
{% endalert %}

### Uso de encurtamento de links

Para usar o encurtamento de links, certifique-se de que a opção de encurtamento de links no criador de mensagens esteja ativada. Em seguida, opte por usar o rastreamento básico ou avançado.

![][1]

O Braze só reconhecerá URLs que comecem com `http://` ou `https://`. Quando um URL é reconhecido, a seção **Prévia** é atualizada com um URL de espaço reservado. O Braze estimará o comprimento do URL após o encurtamento, mas um aviso solicitará que você selecione um usuário teste e salve a mensagem como rascunho para obter uma estimativa mais precisa.

![][3]

#### Adição de parâmetros UTM

Embora o encurtamento de links permita rastrear seus URLs automaticamente, também é possível adicionar parâmetros UTM aos URLs para rastrear a performance das campanhas em ferramentas de análise de dados de terceiros, como o Google Analytics.

Para adicionar parâmetros UTM ao seu URL, faça o seguinte:

1. Comece com seu URL de base. Esse é o URL da página que você deseja rastrear (como `https://www.example.com`).
2. Adicione um ponto de interrogação (?) após o URL da base.
3. Adicione cada parâmetro UTM separado por um E comercial (&).

Um exemplo é `https://www.example.com?utm_source=newsletter&utm_medium=sms`.

### Personalização Liquid em URLs

Você pode construir dinamicamente seu URL diretamente no criador do Braze, o que lhe permite adicionar parâmetros UTM dinâmicos aos seus URLs ou enviar aos usuários links exclusivos (como direcionar os usuários para o carrinho abandonado ou para um produto específico que está de volta ao estoque).

#### Criar um URL com tags de personalização Liquid compatíveis

Os URLs podem ser gerados dinamicamente com o uso de qualquer [tag de personalização Liquid compatível]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Também é possível fazer a redução de variáveis Liquid definidas de forma personalizada. Vários exemplos são mostrados abaixo:

#### Criar um URL usando variáveis Liquid

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

#### Encurtar URLs renderizados por variáveis Liquid

Encurtamos os URLs que são renderizados pelo Liquid, mesmo aqueles incluídos nas propriedades do API-trigger. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representar um URL válido, encurtaremos e rastrearemos esse URL antes de enviar a mensagem SMS. 

#### Encurtar URLs no ponto de extremidade /messages/send

O encurtamento de links também está ativado para mensagens somente da API por meio do [endpoint`/messages/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Para também ativar o rastreamento básico ou avançado, use os parâmetros de solicitação `link_shortening_enabled` ou `user_click_tracking_enabled`.

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Opcional | Booleano | Defina `link_shortening_enabled` como `true` para ativar o encurtamento de links e o rastreamento de cliques em nível de campanha. Para usar o rastreamento, um `campaign_id` e um `message_variation_id` devem estar presentes.|
|`user_click_tracking_enabled`| Opcional | Booleano | Defina `user_click_tracking_enabled` como `true` para ativar o encurtamento de links e o rastreamento de cliques no nível da campanha e do usuário. É possível usar os dados de rastreamento para criar segmentos de usuários que clicaram em URLs. Para usar o rastreamento, um `campaign_id` e um `message_variation_id` devem estar presentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Para obter uma lista completa dos parâmetros de solicitação, acesse [parâmetros de solicitação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Testes

Antes de lançar sua campanha ou Canva, é uma prática recomendada fazer uma prévia e testar sua mensagem primeiro. Para isso, acesse a guia **Teste** para fazer a prévia e enviar um SMS para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou para um usuário individual. 

Essa prévia será atualizada com a personalização relevante e o URL encurtado. O número de caracteres e [os segmentos faturáveis]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) também serão atualizados para refletir a personalização renderizada e o URL encurtado. 

Certifique-se de salvar a campanha ou o Canva antes de enviar uma mensagem de teste para receber uma representação do URL encurtado que será enviado em sua mensagem. Se a campanha ou o Canva não for salvo antes de um envio de teste, o envio de teste incluirá uma URL de espaço reservado.

{% alert important %}
Se um rascunho for criado em um Canva ativo, não será gerado um URL encurtado. O URL encurtado real é gerado quando o rascunho do Canva é ativado.
{% endalert %}

![][2]

{% alert note %}
A personalização Liquid e os URLs encurtados são modelos na guia **Teste** depois que um usuário é selecionado. Certifique-se de que um usuário esteja selecionado para receber uma contagem precisa de caracteres.
{% endalert %}

## Rastreamento de cliques

Quando a capacitação de links está ativada, a tabela de performance de SMS e MMS inclui uma coluna intitulada **Total Clicks (Total de cliques** ) que mostra uma contagem de eventos de cliques por variante e uma taxa de cliques associada. Para obter mais detalhes sobre as métricas de SMS, consulte [Performance de mensagens SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance).

![][4]

Os gráficos **Historical Performance** e **SMS/MMS Performance** também incluem uma opção para **Total Clicks** e mostram uma série temporal diária de eventos de cliques. Os cliques são incrementados no redirecionamento (por exemplo, quando um usuário visita um link) e podem ser incrementados mais de uma vez por usuário.

## Redirecionamento de usuários

Para obter orientação sobre redirecionamento, visite [SMS retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

## Domínios personalizados

O encurtamento de links também permite que você use seu próprio domínio para personalizar a aparência de seus URLs encurtados, o que ajuda a retratar uma imagem de marca consistente.

{% alert note %}
Entre em contato com seu gerente de conta Braze se estiver interessado em começar a usar domínios personalizados.
{% endalert %}

### Requisitos de domínio

- Os domínios devem ser adquiridos, pertencentes e gerenciados por você.
- O domínio usado para esse recurso deve ser exclusivo (ou seja, diferente do domínio do seu site) e não pode ser usado para hospedar nenhum conteúdo da Web.
  - Você também pode usar subdomínios exclusivos, como `sms.braze.com`.
- Recomendamos escolher um domínio com o menor número possível de caracteres para minimizar o comprimento de seus URLs.

#### Delegação de seu domínio personalizado

Quando você delega seu domínio à Braze, nós tratamos automaticamente da renovação do certificado para evitar um lapso no serviço. 

Para delegar seu domínio ao Braze, faça o seguinte: 

1. Apresente um domínio que atenda aos requisitos acima ao seu gerente de sucesso do cliente. A Braze verificará a configuração de DNS existente para o domínio e confirmará isso:

- Não existem registros de CAA OU
- **Existem** registros do CAA, mas há um registro para {% raw %}`<any number> issue "letsencrypt.org"`{% endraw %} ou {% raw %}`<anynumber> issuewild "letsencrypt.org"`{% endraw %}

2. Crie quatro novos registros A, um para cada IP, e confirme que esses são os únicos registros A existentes para o host do link de domínio:
- `151.101.130.133`
- `151.101.194.133`
- `151.101.2.133`
- `151.101.66.133`

### Uso de domínios personalizados

Uma vez configurados, os domínios personalizados podem ser atribuídos a um ou vários grupos de inscrições de SMS. 

![Configurações de grupos de inscrições que permitem selecionar um domínio de encurtamento de links.][7]

As campanhas enviadas com a capacitação de encurtamento de links ativada usarão o domínio atribuído associado ao seu grupo de inscrições de SMS.

![][8]

## Perguntas frequentes

### Encurtamento de links

#### Os links que recebo ao testar o envio de URLs são reais?

Se a campanha tiver sido salva como rascunho antes do envio do teste, sim. Caso contrário, é um link de espaço reservado. Note que a URL exata enviada em uma campanha lançada pode ser diferente daquela enviada por meio de um envio de teste.

#### O SDK da Braze precisa ser instalado para encurtar links?

Não. O encurtamento de links funciona sem integração de SDK.

#### Eu sei quais usuários individuais estão clicando em um URL?

Sim. Quando **o rastreamento avançado** está ativado, é possível redirecionar os usuários que clicaram em URLs, aproveitando os [filtros de redirecionamento de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) ou os eventos de clique de SMS (`users.messages.sms.ShortLinkClick`) enviados via Currents.

#### Posso adicionar parâmetros UTM a um URL antes de ele ser encurtado?

Sim. Podem ser adicionados parâmetros estáticos e dinâmicos. 

#### Por quanto tempo os URLs encurtados permanecem válidos?

Os URLs estáticos são válidos por um ano a partir do momento do registro do URL, como o primeiro envio. Os URLs dinâmicos são válidos por dois meses a partir do momento do registro do URL.

#### O encurtamento de links funciona com deep links ou links universais?

O encurtamento de links encurta todos os URLs estáticos que começam com `http://` ou `https://`. Evite encurtar ainda mais os links universais gerados por provedores como Branch ou Appsflyer, pois isso pode quebrar a atribuição ou o redirecionamento.

### Domínios personalizados

#### Os domínios delegados podem ser compartilhados entre vários grupos de inscrições?

Sim. Um único domínio pode ser usado com vários grupos de inscrições. Para fazer isso, selecione o domínio para cada grupo de inscrições ao qual ele deve ser associado.

#### Os domínios delegados podem ser compartilhados em vários espaços de trabalho?

Sim. Os domínios podem ser associados a grupos de inscrições em vários espaços de trabalho, desde que os espaços de trabalho estejam contidos na mesma empresa.

[1]: {% image_buster /assets/img/link_shortening/shortening1.png %}
[2]: {% image_buster /assets/img/link_shortening/shortening2.png %}
[3]: {% image_buster /assets/img/link_shortening/shortening3.png %}
[4]: {% image_buster /assets/img/link_shortening/shortening4.png %}
[5]: {% image_buster /assets/img/sms/retargeting5.png %}
[6]: {% image_buster /assets/img/sms/retargeting4.png %}
[7]: {% image_buster /assets/img/custom_domain.png %}
[8]: {% image_buster /assets/img/custom_domain2.png %}
[11]: {% image_buster /assets/img/sms/link_shortening10.png %}
[13]: {% image_buster /assets/img/link_shortening/shortening3.png %}   


---
nav_title: "Provisionamento de dados históricos da Shopify"
article_title: "Provisionamento de dados históricos da Shopify"
alias: "/shopify_historical_backfill_legacy/"
description: "Este artigo de referência descreve como configurar o provisionamento de dados históricos da Shopify, incluindo riscos e dados suportados."
page_type: partner
search_tag: Partner
page_order: 1
---

# Provisionamento de dados históricos da Shopify 

> O recurso de Preenchimento Histórico do Shopify permite que as marcas sincronizem clientes e dados de compras de maneira automatizada e contínua, para que você possa começar a interagir imediatamente com um dos seus segmentos mais valiosos – os compradores. 

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

Como parte deste preenchimento retroativo, a Braze importará todos os clientes, pedidos e eventos de compra dos últimos 90 dias antes da conexão de integração com o Shopify. Observe que esse recurso é ideal para novos clientes sem mensagens ativas em execução, dadas as implicações explicadas na próxima seção. O recurso também conta para o uso dos seus pontos de dados.

## Riscos

Esse recurso importará dados históricos e eventos que podem resultar em consequências indesejadas, como usuários recebendo mensagens irrelevantes e inoportunas para quaisquer campanhas ou canvas afetados. Campanhas e canvas usando os seguintes eventos de disparo podem ser impactados se estiverem usando qualquer um dos dados do Shopify que este recurso está sincronizando:
- Alterar valor de atributo personalizado
- Realizar evento de conversão
- Executar Evento de Exceção para Campanha
- Atualizar status de inscrição
- Atualizar status do grupo de inscrições
- Adicionar um endereço de e-mail
- Fazer compra*
- Realizar evento personalizado*

{% alert important %}
Recomendamos que você audite suas campanhas e canvas ativos atuais em busca de mensagens que possam disparar os eventos acima usando dados do nosso provisionamento de dados históricos da Shopify. 

- Para "Fazer Compra" e "Executar evento personalizado", você pode atualizar a [duração do tempo de início]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration) para qualquer data e hora após a sua loja Shopify ter sido conectada no Braze. Os eventos passados criados antes deste novo horário de início não dispararão mensagens. 
- Para todos os outros eventos acima, você pode [interrompê-los temporariamente]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign) antes de ativar o provisionamento para garantir que nenhuma mensagem seja enviada.
{% endalert %}

## Configuração do provisionamento histórico da Shopify

### Pré-requisitos

Os seguintes eventos precisam ser habilitados antes de ativar o provisionamento, senão os dados deles não serão importados:

- `shopify_created_order`
- Evento de compra da Braze 

Os eventos acima podem ser ativados durante a configuração do Shopify durante a [seleção de eventos]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection).

{% alert important %}
Você pode ativar o recurso de provisionamento apenas uma vez na sua integração.
{% endalert %}

### Etapa 1: Inicie o processo de preenchimento retroativo do Shopify

Na página de parceiro da Shopify, selecione **Start Data Backfill** (Iniciar provisionamento de dados históricos). Para os clientes existentes da Shopify, será necessário reautorizar o acesso para a Braze coletar todos os eventos de pedidos anteriores antes de iniciar o preenchimento de dados retroativos.

![]({% image_buster /assets/img/Shopify/backfill3.png %}){: style="max-width:75%;"}

### Etapa 2: ative o provisionamento de dados históricos da Shopify

Em seguida, o criador de configuração aparecerá, e você terá a opção de ativar o provisionamento de dados históricos da Shopify. Como parte desse provisionamento, a Braze sincronizará apenas os seguintes dados da Shopify dos últimos 90 dias antes da sua integração com a Shopify por padrão:
- Evento de pedido criado
- Evento de compra da Braze
- Dados de cliente

Para ver quais dados específicos de cliente estão sendo provisionados, visite a seção de [dados de cliente da Shopify suportados](#supported-shopify-customer-data).

{% alert note %}
Este recurso sincronizará apenas os estados de inscrição de e-mail e SMS para novos usuários criados durante o preenchimento retroativo. Isso não sincronizará os estados de inscrição para usuários existentes no Braze para evitar substituir os status atuais dos seus usuários.<br><br>Se você tiver feedback sobre o comportamento atual, envie-o através do portal do produto, listado no **dashboard** em **Recursos** como **Roteiro do Produto** (Se você estiver usando nossa [navegação atualizada]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), selecione **Comunidade** > **Roteiro do Produto**).
{% endalert %}

Depois que você clicar em **Avançar**, o preenchimento retroativo será ativado e começará a sincronizar os dados anteriores. Observe que o provisionamento histórico só pode ser concluído **uma vez**, ou seja, não é possível executar essa importação de novo após a sincronização dos dados.

![]({% image_buster /assets/img/Shopify/backfill1.jpg %}){: style="max-width:75%;"}

### Etapa 3: provisionamento em andamento

Você receberá uma notificação do dashboard, e seu status será exibido como "Em progresso" para indicar que o provisionamento foi iniciado. Note que o tempo necessário para a conclusão do provisionamento depende do número de clientes e pedidos que a Braze precisa sincronizar da Shopify. Durante esse tempo, você pode sair desta página e esperar por uma notificação do dashboard ou um e-mail para notificá-lo quando o preenchimento estiver completo.

![]({% image_buster /assets/img/Shopify/backfill2.png %}){: style="max-width:75%;"}

### Etapa 4: Preenchimento retroativo concluído
Você receberá uma notificação no dashboard e um e-mail após a conclusão do provisionamento da Shopify. A página de parceiros da Shopify também atualizará o status do provisionamento histórico para "Complete" (Concluído).

## Dados de cliente da Shopify suportados

### Atributos personalizados da Shopify

| Nome do atributo | Descrição |
| --- | --- |
| `shopify_order_count` | Este atributo personalizado corresponde ao total de pedidos que este cliente concluiu no Shopify. Está disponível apenas para usuários que foram provisionados como parte deste processo. |
| `shopify_total_spent` | Este atributo personalizado corresponde ao valor total gasto por este cliente no Shopify. Está disponível apenas para usuários que foram provisionados como parte deste processo. |
| `shopify_tags` | Este atributo corresponde às [tags de cliente](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) definidas pelos administradores do Shopify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Atributos padrão do Shopify
- E-mail
- Nome
- Sobrenome
- Telefone
- Cidade
- País


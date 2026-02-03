---
nav_title: Swym
article_title: Swym
description: "Este artigo de referência descreve a parceria entre o Braze e a Swym, que permite que os compradores salvem produtos e continuem sua jornada sem problemas em sites, apps móveis e lojas de varejo."
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# Swym

> [A Swym](https://getswym.com/) ajuda as marcas de comércio eletrônico a capturar a intenção de compra com alertas de Wishlists, Save for Later, Gift Registry e Back-in-Stock. Usando dados avançados e baseados em permissões, você pode criar campanhas hiperdirecionadas e oferecer experiências de compras personalizadas que impulsionam o engajamento, aumentam as conversões e a fidelidade.

*Essa integração é mantida pela Swym.*

## Sobre a integração

A integração da Swym e da Braze permite que você forneça campanhas de marketing personalizadas e orientadas por eventos que convertem a intenção do comprador em vendas. Use a integração para que os compradores possam continuar de onde pararam, colaborar com outras pessoas durante toda a jornada de compras e receber campanhas de redirecionamento de alto desempenho.

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito          | Descrição                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym  | Os apps Swym Wishlist Plus, Back in Stock ou ambos devem estar instalados em sua plataforma de comércio eletrônico (Shopify ou BigCommerce), e você deve estar no plano Enterprise.       |
| Uma chave da API REST da Braze  | Uma chave da API REST da Braze com `users.track` permissões. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Um endpoint Braze REST | [Seu URL do ponto de extremidade REST]({{site.baseurl}}/api/basics/#endpoints). Seu endpoint dependerá do URL do Braze para sua instância.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Casos de uso

Ao conectar os apps Wishlist Plus e Back in Stock Alerts da Swym com o Braze, você pode enviar automaticamente eventos de atividade do comprador, como adições à lista de desejos, inscrições em estoque, alertas de queda de preço e lembretes, para o Braze como eventos personalizados. Esses eventos podem então ser usados para disparar mensagens automatizadas no Braze, facilitando uma comunicação oportuna, relevante e engajada que leve os compradores a voltar para fazer uma compra.

## Integração do Swym

### Etapa 1: Conecte seu app Swym ao Braze

Atualmente, a integração do Braze com o Swym é uma integração gerenciada e não é de autoatendimento. Para começar, entre em contato com a equipe de suporte da Swym em [support@getswym.com](mailto:support@getswym.com) e forneça as seguintes informações para que a Swym possa configurar a integração em seu nome:

1. Gere uma [chave de API REST]({{site.baseurl}}/api/basics/#about-rest-api-keys) em seu dashboard do Braze com a permissão `users.track`.

![Geração de uma chave de API no Braze.]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
Para proteger suas chaves de API, o Swym recomenda que você compartilhe credenciais com segurança usando uma ferramenta de link único e autodestrutivo (por exemplo, [OneTimeSecret](https://onetimesecret.com/)).
{% endalert %}

{: start="2"}
2\. O Braze gerencia várias instâncias de seu dashboard e pontos de extremidade REST. Forneça o [ponto de extremidade REST]({{site.baseurl}}/api/basics/#endpoints) para a instância que está sendo provisionada.

3. Depois que a chave de API e o URL da instância forem compartilhados com a equipe de suporte do Swym, eles configurarão a integração para você e responderão com uma confirmação.

4. Após a conclusão da configuração, os eventos personalizados do Swym serão registrados automaticamente no Braze. Você pode visualizar a lista de eventos Swym registrados no dashboard do Braze acessando **Data Settings** > Custom Events. 

5. Visualize as propriedades de cada evento Swym selecionando **Manage Properties (Gerenciar propriedades** ) para o evento personalizado correspondente. Essas propriedades contêm os valores de eventos que podem ser usados para personalizar suas mensagens.

![Propriedades personalizadas no Braze.]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### Etapa 2: Assine os eventos que você deseja enviar para o Braze

No app do Wishlist Plus, acesse a guia **Marketing** e encontre a seção **Automações**. Aqui, você pode selecionar os eventos que deseja assinar. 

![Eventos a serem assinados.]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Eventos do app Swym Wishlist Plus

| Nome do evento | Quando esse evento é disparado |  
|------------|------------------------------|  
| Compartilhar lista de desejos | Quando um comprador compartilha uma lista de desejos com outra pessoa |  
| Adicionar à lista de desejos | Quando um comprador adiciona um item à sua lista de desejos |  
| Lembrete de lista de desejos | Lembrete sobre itens na lista de desejos de um comprador|   
| Lembrete de salvamento para mais tarde | Lembrete sobre os itens salvos para depois de um comprador |  
| Alerta de queda de preço | O produto em uma lista de desejos é colocado à venda |  
| Alerta de estoque baixo | O produto em uma lista de desejos está ficando sem estoque |  
| Alerta de volta ao estoque | O produto em uma lista de desejos é reabastecido |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Eventos do app Swym Back in Stock Alerts

| Nome do evento | Quando esse evento é disparado |  
|------------|------------------------------|  
| Reconhecimento de volta ao estoque | O cliente se inscreve para ser notificado quando um produto estiver novamente em estoque |  
| Alerta de reabastecimento | O produto para o qual um comprador solicitou um alerta de falta de estoque é reabastecido |  
| Lembrete de reabastecimento | Alerta de acompanhamento (geralmente cerca de 24 horas após o primeiro alerta de reabastecimento, configurável)|   
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Etapa 3: Criar uma campanha ou uma tela do Braze

Para automatizar o envio de mensagens personalizadas para seus compradores, é necessário criar uma campanha ou Canvas separado no Braze para cada evento em que você se inscreveu. Cada campanha ou Canva deve ser configurada para disparar com base em um evento específico e usar as propriedades do evento correspondente para preencher o conteúdo dinâmico em suas mensagens. Para obter orientações passo a passo, consulte [Getting Started: Campanhas e telas]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

![Um evento baseado em ações.]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

Para obter detalhes adicionais, consulte a [central de ajuda da Swym](https://help.getswym.com/en/articles/12344153-braze-integration) ou entre em contato com a equipe de suporte da Swym em [support@getswym.com](mailto:support@getswym.com). 
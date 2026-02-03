---
nav_title: Eventos de conversão
article_title: Eventos de conversão
page_order: 3
page_type: reference
description: "Este artigo de referência define eventos de conversão, como usá-los para definir suas métricas de sucesso no Braze e como usar esses eventos para ver quão engajados seus usuários estão."
tool:
    - Campaigns
    - Canvas
---

# Eventos de conversão

> Um evento de conversão é um tipo de métrica de sucesso que rastreia se um destinatário do seu envio de mensagens realiza uma ação de alto valor em um determinado período de tempo após receber seu engajamento. Use esses eventos para garantir que você está coletando informações relevantes e úteis que pode usar posteriormente para obter insights para sua campanha ou Canvas.

## Como funciona?

Para uma campanha de férias personalizada direcionada a usuários ativos, um evento de conversão de **Iniciar uma Sessão** dentro de dois ou três dias pode ser apropriado, pois permite que você tenha uma noção do engajamento do usuário ao receber sua mensagem. Você também pode selecionar eventos adicionais como **Faz Pedido**, **Fazer Upgrade do App**, ou qualquer um dos seus eventos personalizados como eventos de conversão.

{% alert tip %}
Para mais informações sobre conversões, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de campanhas.
{% endalert %}

### Regras de rastreamento de conversões

Eventos de conversão atribuem ações do usuário a um ponto de engajamento. Observe o seguinte sobre como o Braze lida com múltiplas conversões:

- **Campanhas de canal único**: As conversões ocorrem por usuário, não por dispositivo. Dentro de um único canal, um usuário converte apenas uma vez por evento de conversão, mesmo que uma mensagem seja enviada para vários dispositivos. Por exemplo, se uma campanha tem apenas um evento de conversão definido como "Faz qualquer compra" e um usuário faz duas compras separadas dentro do prazo de conversão, o Braze conta apenas uma conversão.
- **Campanhas multicanal**: Para campanhas multicanal, cada canal tem sua própria oportunidade de conversão. Um usuário pode converter uma vez por canal após receber uma mensagem nesse canal. Isso significa que se um usuário recebe mensagens em vários canais (por exemplo, tanto e-mail quanto push) e realiza a ação de conversão, o Braze conta uma conversão para cada canal, o que pode resultar em taxas de conversão superiores a 100%.
- Se um usuário realizar um evento de conversão dentro dos prazos de conversão de duas campanhas ou Canvases separadas que recebeu, a conversão é registrada em ambas.
- Um usuário conta como convertido se realizou o evento de conversão específico na janela, mesmo que não tenha aberto ou clicado na mensagem.
- Para Canvases, o rastreamento de conversão funciona com base no prazo final de conversão que começa quando um usuário entra no Canvas, não no tempo de mensagens individuais. O Braze conta conversões mesmo durante períodos de atraso entre mensagens no Canvas.

### Evento de conversão primária

O evento de conversão primário é o primeiro evento que você adiciona durante a criação da campanha ou Canvas. Esse evento é o que mais influencia seu engajamento e seus relatórios. O Braze usa seu evento de conversão primária para:

- Calcular a variação de mensagem vencedora em campanhas ou Canvases [multivariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing).
- Determine a janela em que a receita é calculada para a campanha ou o Canva.
- Ajustar distribuições de mensagens para campanhas e Canvases usando [Seleção Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

A contagem de eventos de conversão primária é o número de eventos de conversão que ocorreram. Para campanhas multicanal, o Braze conta conversões por canal (conforme descrito em [regras de rastreamento de conversão](#conversion-tracking-rules)), o que significa que a contagem de conversões pode exceder o número de usuários únicos e resultar em taxas de conversão superiores a 100%. O Braze calcula a taxa de evento de conversão primária dividindo essa contagem pelo número de destinatários únicos. O Braze considera um usuário um destinatário quando a mensagem é enviada ou exibida, dependendo do canal. Por exemplo, em push ou e-mail, um usuário se torna um destinatário após o Braze enviar a mensagem. Para mensagens no aplicativo ou Cartões de Conteúdo, o usuário deve visualizar a mensagem para ser considerado um destinatário.

{% alert note %}
Se você abortar mensagens usando a tag Liquid `abort`, o Braze aborta mensagens apenas para usuários que passam por variantes. Mensagens para usuários no grupo de controle não são abortadas, o que pode levar a porcentagens de conversão distorcidas entre variantes e grupos de controle. Como solução alternativa, use [a segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) para direcionar seus usuários na entrada da campanha e do Canva.
{% endalert %}

## Criando uma campanha com rastreamento de conversão

### Etapa 1: Configure sua campanha

[Crie uma campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) para seu canal de envio de mensagens desejado. Após configurar as mensagens e o cronograma da sua campanha, você pode adicionar até quatro eventos de conversão para rastreamento.

Use quantos eventos de conversão forem necessários. Adicionar um segundo ou terceiro evento de conversão enriquece significativamente seu relatório. Por exemplo, para uma campanha direcionada a usuários que estão se afastando, adicionar um evento de conversão secundário junto com o evento de conversão primária **Inicia Sessão** ajuda você a entender quão eficaz sua campanha é em trazer os usuários de volta ao seu aplicativo. 

### Etapa 2: Adicione os eventos de conversão

Primeiro, selecione o tipo geral de evento que você gostaria de usar:

| Tipo de Evento de Conversão   | Descrição                |
|-------------------------|----------------------------|
| **Inicia sessão**      | Um usuário é contado como convertido quando abre qualquer um dos apps que você especificar (o padrão é todos os apps no espaço de trabalho).|
| **Faz compra**      | Um usuário é contado como tendo convertido quando registra um [A evento de Compra]({{site.baseurl}}/api/objects_filters/purchase_object/). Isso rastreia qualquer compra por padrão, ou você pode especificar um produto específico.|
| **Ordem dos locais**        | Um usuário é contado como tendo convertido quando dispara o [A evento recomendado de Pedido Realizado de eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events?tab=ecommerce.order_placed#ecommerce-recommended-events). Isso rastreia qualquer pedido por padrão, ou você pode filtrar por um produto específico.|
| **Realiza evento personalizado**| Um usuário é contado como convertido quando realiza um de seus eventos personalizados existentes (não há padrão, é necessário especificar o evento).|
| **Faz upgrade de app**         | Um usuário é contado como convertido quando faz upgrade da versão do aplicativo em qualquer um dos aplicativos que você especificar (o padrão é todos os aplicativos no espaço de trabalho). A Braze realiza uma comparação numérica de melhores esforços para determinar se a mudança foi um upgrade. Versões não numéricas são contadas como conversões se a versão mudar.|
| **Abre e-mail**         | Um usuário é contado como convertido quando abre o e-mail (somente para campanhas de e-mail).|
| **Clica no e-mail**        | Um usuário é contado como convertido quando clica em um link dentro do e-mail (somente para campanhas de e-mail).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
**Propriedades aninhadas não são suportadas em eventos de conversão**. Você não pode usar propriedades aninhadas em eventos de conversão. Por exemplo, se `product_code` ou `product_name` são propriedades aninhadas dentro de um array `products` (como `products[].product_code`), você não pode usá-las para verificar se uma compra de produto específica foi feita em um evento de conversão.
{% endalert %}

Defina seu prazo de conversão. Este é o tempo máximo que pode passar antes que a Braze considere uma conversão. Você pode definir uma janela de até 30 dias durante a qual a Braze conta a conversão se o usuário realizar a ação especificada.

![O tipo de evento de conversão "Makes Purchase" como exemplo para registrar conversões para usuários que fazem qualquer compra. Esse prazo de conversão é de 12 horas.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Depois de selecionar seus eventos de conversão, continue o processo de criação da campanha e comece a enviar sua campanha.

### Etapa 3: Veja seus resultados

Acesse a página **Detalhes** para ver os detalhes de cada evento de conversão associado à campanha que você criou. Independentemente dos eventos de conversão selecionados, você também pode ver a receita total atribuída a esta campanha específica, bem como variantes específicas, durante a janela do evento de conversão primária.

{% alert note %}
Se você não selecionar nenhum evento de conversão durante a criação da campanha, o tempo padrão é de três dias.
{% endalert %}

Além disso, para mensagens multivariantes, é possível ver o número de conversões e as porcentagens de conversão do grupo de controle e de cada variante.

![Quatro eventos de conversão que rastreiam conversões com base em quando uma compra foi feita dentro de três horas, fez uma compra dentro de duas horas, iniciou uma sessão dentro de 30 minutos e iniciou uma sessão dentro de 25 minutos.]({% image_buster /assets/img_archive/conversion_event_details.png %})
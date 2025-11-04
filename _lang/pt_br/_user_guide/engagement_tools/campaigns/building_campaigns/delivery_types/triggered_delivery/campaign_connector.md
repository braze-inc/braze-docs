---
nav_title: Conector de campanha
article_title: Conector de campanha
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Este artigo de instruções explica o que é o Campaign Connector e como usá-lo para fornecer conteúdo direcionado e relevante no momento certo."

---
# Conector de campanha

> O Campaign Connector permite que você crie campanhas que são acionadas quando os usuários interagem com campanhas ativas. Você pode fornecer conteúdo direcionado e relevante no momento certo.

## Como funciona

Esse recurso permite segmentar usuários que concluem as seguintes interações com campanhas ativas:

- Exibir mensagem no aplicativo
- Clique na mensagem no aplicativo
- Clique nos botões de mensagem no aplicativo
- Clique no e-mail
- Clique no alias no e-mail
- Abrir e-mail
- Abrir diretamente a notificação por push
- Clique no botão de notificação por push
- Clique em empurrar a página da história
- Realizar evento de conversão
- Receber e-mail
- Receber SMS
- Clique no link encurtado do SMS
- Receber notificação por push
- Receber webhook
- Estão inscritos em um grupo de controle
- Exibir cartão de conteúdo
- Clique no cartão de conteúdo
- Dispensar cartão de conteúdo

### Regras de entrega

Observe que não é possível usar o Campaign Connector para enviar uma mensagem a um usuário depois que ele tiver concluído uma interação com uma campanha. Por exemplo, se você estiver executando uma campanha de marketing por nove semanas e configurar uma campanha de acompanhamento que use o Campaign Connector no início da quarta semana, a campanha de acompanhamento só entregará mensagens aos usuários que interagiram com a campanha de marketing depois que a campanha de acompanhamento foi publicada (semanas 4 a 9). Portanto, para garantir que suas campanhas de acompanhamento alcancem todos os usuários que você tem como alvo, você deve:

- Configure sua campanha original como um rascunho
- Configure e publique sua campanha de acompanhamento
- Publicar a campanha original

Essas regras de entrega são particularmente pertinentes se você estiver segmentando usuários inscritos em um grupo de controle, que recebem um e-mail ou uma notificação push. Como os usuários serão inscritos no grupo de controle assim que você publicar a campanha original, você deve publicar a campanha de acompanhamento antes de publicar a campanha original. Da mesma forma, se você publicar a campanha original antes da campanha subsequente, muitos usuários poderão receber seu e-mail e/ou notificação por push antes da publicação da campanha subsequente.

## Uso do Campaign Connector em suas campanhas

### Etapa 1: Criar uma nova campanha

Escreva as mensagens que deseja enviar aos seus usuários. Você pode selecionar uma campanha de canal único ou multicanal, dependendo do seu caso de uso.

### Etapa 2: Selecione a interação e a campanha de destino

1. Selecione [Action-Based Delivery (Entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) ) e adicione o acionador "Interact with Campaign" (Interagir com a campanha) para direcionar os usuários que interagem com uma campanha ativa. 
2. Escolha a interação do acionador. 
3. Em seguida, você selecionará a campanha ativa que deseja segmentar.

\![]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### Etapa 3: Defina o atraso da programação e adicione exceções (opcional)

Se você optar por definir um atraso de programação, poderá adicionar uma exceção à ação de acionamento. Por exemplo, talvez você queira reenviar uma campanha de e-mail para usuários que não abriram o e-mail original.  Nesse cenário, você pode escolher "E-mail recebido" como o acionador e definir um atraso de programação de uma semana. Em seguida, você pode adicionar "Abrir e-mail" como uma exceção. Agora, você reenviará o e-mail aos usuários que não abriram o e-mail original dentro de uma semana após o recebimento.

\![]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

Os eventos de exceção só serão acionados enquanto um usuário estiver esperando para receber a mensagem à qual está associado. Se um usuário executar a ação antes de aguardar a mensagem, o evento de exceção não será acionado.

### Etapa 4: Prossiga com a criação da campanha

Continue criando sua campanha como faria normalmente. Observe que, se você quiser garantir que enviará uma mensagem a todos os usuários que interagirão com uma campanha específica, seria melhor segmentar um segmento que contenha todos os usuários do seu aplicativo.

## Casos de uso

Você pode usar o Campaign Connector para direcionar usuários que se envolvem ou não com campanhas ativas.

Por exemplo, você pode optar por segmentar os usuários que clicaram em uma mensagem push promocional que anunciava frete grátis para que você possa enviar a eles uma mensagem push promocional anunciando 15% de desconto em uma compra.

Ou então, você pode acompanhar os usuários que clicaram em um link profundo em uma mensagem in-app de integração, enviando-lhes outra mensagem in-app que destaque recursos adicionais.  Dessa forma, você pode direcionar os usuários que demonstraram interesse em saber mais sobre os recursos do seu aplicativo e evitar incomodar os usuários que preferem descobrir esses recursos por conta própria.

O Campaign Connector também pode direcionar os usuários que recebem uma notificação push lembrando-os de que abandonaram o carrinho. Por exemplo, talvez você queira reenviar a notificação aos usuários que não a abriram diretamente. No entanto, é provável que você queira excluir os usuários que fizeram uma compra desde que você enviou a notificação original, mesmo que eles não a tenham aberto diretamente. Você pode obter esse caso de uso adicionando um acionador "Recebeu notificação por push" para a campanha "Carrinho abandonado", definindo um atraso de programação e adicionando "Faz compra" e "Notificações por push abertas diretamente" como exceções.


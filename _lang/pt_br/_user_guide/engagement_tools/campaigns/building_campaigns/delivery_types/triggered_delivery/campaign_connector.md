---
nav_title: Conector de campanha
article_title: Conector de campanha
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Este artigo de instruções explica o que é o Campaign Connector e como usá-lo para fornecer conteúdo direcionado e relevante no momento certo."

---
# Conector de campanha

> O Campaign Connector permite criar campanhas que são disparadas quando os usuários interagem com campanhas ativas ou cartões do Feed de notícias. Esse recurso é útil porque o capacita a fornecer conteúdo direcionado e relevante no momento certo. 

{% alert note %}
Este artigo inclui informações sobre o Feed de notícias, que está sendo descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Confira o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) para saber mais.
{% endalert %}

Esse recurso permite o direcionamento de usuários que concluem as seguintes interações com campanhas ativas:

- Ver mensagem no app
- Clique na mensagem no app
- Clique nos botões de mensagem no app
- Clique no e-mail
- Clique no alias no e-mail
- Abrir e-mail
- Abra diretamente a notificação por push
- Clique no botão de notificação por push
- Clique na página da story por push
- Realizar evento de conversão
- Receber e-mail
- Receber SMS
- Clique no link encurtado do SMS
- Receba notificações por push
- Receber webhook
- Estão inscritos em um grupo de controle
- Exibir cartão de conteúdo
- Clique no cartão de conteúdo
- Descarte de cartão de conteúdo

Assim como os usuários que concluírem as seguintes interações com cartões ativos do feed de notícias:

- Visualização
- Clique

## Regras de entrega

O recurso conector de campanha só funciona com campanhas ativas. Além disso, não é possível usar o Campaign Connector para enviar uma mensagem a um usuário depois que ele tiver concluído uma interação com uma campanha. Por exemplo, se você estiver executando uma campanha de marketing por nove semanas e configurar uma campanha de acompanhamento que utilize o Campaign Connector no início da quarta semana, a campanha de acompanhamento só enviará mensagens aos usuários que interagiram com a campanha de marketing após a publicação da campanha de acompanhamento (semanas 4 a 9). Portanto, para garantir que suas campanhas de acompanhamento alcancem todos os usuários que você está direcionando, você deve:

- Configure sua campanha original como um rascunho
- Configurar e publicar sua campanha de acompanhamento
- Publicar a campanha original

Essas regras de entrega são particularmente pertinentes se o direcionamento for para usuários inscritos em um grupo de controle, que recebem um e-mail ou uma notificação por push. Como os usuários serão inscritos no grupo de controle assim que você publicar a campanha original, é necessário publicar a campanha de acompanhamento antes de publicar a campanha original. Da mesma forma, se a campanha original for publicada antes da campanha subsequente, muitos usuários poderão receber o e-mail e/ou a notificação por push antes da publicação da campanha subsequente.

## Como usar o recurso Campaign Connector

### Etapa 1: Criar uma nova campanha

Crie as mensagens que deseja enviar aos seus usuários. Você pode selecionar uma campanha clássica ou uma campanha de canal único, dependendo do seu caso de uso.

### Etapa 2: Selecione a interação e a campanha de direcionamento

É possível direcionar usuários que interagem com uma campanha ativa ou usuários que interagem com um cartão ativo do feed de notícias.

#### Direcionamento de usuários que interagem com uma campanha

Selecione [Entrega baseada em ação][7] e adicione o disparo "Interact with Campaign" (Interagir com a campanha). Em seguida, escolha a interação do disparador. Em seguida, você selecionará a campanha ativa que deseja direcionar.

![][4]

#### Direcionamento de usuários que interagem com um cartão do Feed de notícias (obsoleto)

Selecione **Entrega baseada em ação** e adicione o disparador "Interagir com o cartão". Em seguida, escolha se deseja direcionar os usuários que visualizam um cartão do feed de notícias ou os usuários que clicam em um cartão do feed de notícias. Selecione o cartão ativo do feed de notícias que você gostaria de direcionar.

![][5]

### Etapa 3: Defina a postergação da programação e adicione exceções, se necessário

Se optar por definir uma postergação de programação, você poderá adicionar uma exceção à ação-gatilho. Por exemplo, talvez queira reenviar uma campanha de e-mail para usuários que não abriram o e-mail original.  Nesse cenário, você pode escolher "Envio de e-mail recebido" como disparador e definir uma postergação de agendamento de uma semana. Em seguida, você pode adicionar "Abrir e-mail" como uma exceção. Agora, você reenviará o e-mail aos usuários que não abriram o e-mail original dentro de uma semana após o recebimento.

![][6]

Os eventos de gatilho só serão disparados enquanto um usuário estiver esperando para receber a mensagem à qual está associado. Se um usuário executar a ação antes de aguardar a mensagem, o evento de exceção não será disparado.

### Etapa 4: Prossiga com a criação da campanha

Continue criando sua campanha como faria normalmente. Note que, se quiser garantir o envio de uma mensagem a todos os usuários que vão interagir com uma campanha específica, seria melhor direcionar um segmento de mensagem que contenha todos os usuários do seu app.

## Casos de uso

É possível usar o conector d campanha para direcionar usuários que se engajam ou não com campanhas ativas.

Por exemplo, você pode optar por direcionar os usuários que clicaram em uma mensagem push promocional que anunciava frete grátis para que você possa enviar a eles uma mensagem push promocional anunciando 15% de desconto em uma compra.

Ou então, você pode acompanhar os usuários que clicaram em um deep linking em uma mensagem no app de integração, enviando-lhes outra mensagem no app que destaque recursos adicionais.  Dessa forma, é possível direcionar os usuários que demonstraram interesse em aprender mais sobre os recursos do seu aplicativo e evitar incomodar os usuários que preferem descobrir esses recursos por conta própria.

O Campaign Connector também pode direcionar os usuários que recebem uma notificação por push, lembrando-os de que abandonaram o carrinho. Por exemplo, talvez seja interessante reenviar a notificação aos usuários que não a abriram diretamente. No entanto, é provável que você queira excluir os usuários que fizeram uma compra desde o envio da notificação original, mesmo que eles não a tenham aberto diretamente. Você pode obter esse caso de uso adicionando um disparador "Recebeu notificação por push" para a campanha "Abandono de carrinho", definindo uma postergação de programação e adicionando "Faz compra" e "Notificações por push abertas diretamente" como exceções.

[4]: {% image_buster /assets/img_archive/Campaign_Connector1.png %}
[5]: {% image_buster /assets/img_archive/Campaign_Connector2.png %}
[6]: {% image_buster /assets/img_archive/Campaign_Connector3.png %}
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
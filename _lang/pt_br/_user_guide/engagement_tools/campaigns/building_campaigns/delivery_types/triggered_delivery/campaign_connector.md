---
nav_title: Conector de campanha
article_title: Conector de campanha
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Este artigo de instruções explica o que é o Campaign Connector e como usá-lo para fornecer conteúdo direcionado e relevante no momento certo."

---
# Conector de campanha

>  

## 

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

### Regras de entrega

  Portanto, para garantir que suas campanhas de acompanhamento alcancem todos os usuários que você está direcionando, você deve:

- Configure sua campanha original como um rascunho
- Configurar e publicar sua campanha de acompanhamento
- Publicar a campanha original

Essas regras de entrega são particularmente pertinentes se o direcionamento for para usuários inscritos em um grupo de controle, que recebem um e-mail ou uma notificação por push. Como os usuários serão inscritos no grupo de controle assim que você publicar a campanha original, é necessário publicar a campanha de acompanhamento antes de publicar a campanha original. Da mesma forma, se a campanha original for publicada antes da campanha subsequente, muitos usuários poderão receber o e-mail e/ou a notificação por push antes da publicação da campanha subsequente.

## 

### Etapa 1: Criar uma nova campanha

Crie as mensagens que deseja enviar aos seus usuários. 

### Etapa 2: Selecione a interação e a campanha de direcionamento

1.  
2.  
3. Em seguida, você selecionará a campanha ativa que deseja direcionar.



### Etapa 3: 

Se optar por definir uma postergação de programação, você poderá adicionar uma exceção à ação-gatilho. Por exemplo, talvez queira reenviar uma campanha de e-mail para usuários que não abriram o e-mail original.  Nesse cenário, você pode escolher "Envio de e-mail recebido" como disparador e definir uma postergação de agendamento de uma semana. Em seguida, você pode adicionar "Abrir e-mail" como uma exceção. Agora, você reenviará o e-mail aos usuários que não abriram o e-mail original dentro de uma semana após o recebimento.



Os eventos de gatilho só serão disparados enquanto um usuário estiver esperando para receber a mensagem à qual está associado. Se um usuário executar a ação antes de aguardar a mensagem, o evento de exceção não será disparado.

### Etapa 4: Prossiga com a criação da campanha

Continue criando sua campanha como faria normalmente. Note que, se quiser garantir o envio de uma mensagem a todos os usuários que vão interagir com uma campanha específica, seria melhor direcionar um segmento de mensagem que contenha todos os usuários do seu app.

## Casos de uso

É possível usar o conector d campanha para direcionar usuários que se engajam ou não com campanhas ativas.

Por exemplo, você pode optar por direcionar os usuários que clicaram em uma mensagem push promocional que anunciava frete grátis para que você possa enviar a eles uma mensagem push promocional anunciando 15% de desconto em uma compra.

Ou então, você pode acompanhar os usuários que clicaram em um deep linking em uma mensagem no app de integração, enviando-lhes outra mensagem no app que destaque recursos adicionais.  Dessa forma, é possível direcionar os usuários que demonstraram interesse em aprender mais sobre os recursos do seu aplicativo e evitar incomodar os usuários que preferem descobrir esses recursos por conta própria.

O Campaign Connector também pode direcionar os usuários que recebem uma notificação por push, lembrando-os de que abandonaram o carrinho. Por exemplo, talvez seja interessante reenviar a notificação aos usuários que não a abriram diretamente. No entanto, é provável que você queira excluir os usuários que fizeram uma compra desde o envio da notificação original, mesmo que eles não a tenham aberto diretamente. Você pode obter esse caso de uso adicionando um disparador "Recebeu notificação por push" para a campanha "Abandono de carrinho", definindo uma postergação de programação e adicionando "Faz compra" e "Notificações por push abertas diretamente" como exceções.


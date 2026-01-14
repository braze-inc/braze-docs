---
nav_title: Consentimento e coleta de endereços
article_title: Consentimento e coleta de endereços
page_order: 6
page_type: reference
description: "Este artigo de referência aborda as práticas recomendadas para coletar consentimento e endereços de e-mail de usuários e define os diferentes estados possíveis de assinantes de usuários."
channel: email

---

# Consentimento e coleta de endereços

> Antes de enviar seus e-mails iniciais, é importante obter a permissão de seus clientes. É uma cortesia comum e faz maravilhas para suas taxas de abertura!

## Estados do assinante

Há três estados de assinatura de e-mail para um usuário: **optado**, **inscrito** e **cancelado**. Para alterar o estado da assinatura de um usuário, consulte nosso artigo sobre [alteração de assinaturas]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-subscriptions) ou use nossas [APIs de assinatura]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

| Estado do assinante | Descrição |
|---|---|
| Ativado | Esses clientes clicaram no link em um e-mail de confirmação e optaram ativamente por receber suas mensagens. |
| Assinatura | Por padrão, os usuários são inscritos no e-mail desde que tenham um endereço de e-mail válido armazenado em seu perfil. Os usuários permanecem inscritos até que cancelem a inscrição ou optem por participar. |
| Cancelamento da inscrição | Para ser marcado como cancelado, o cliente deve cancelar explicitamente a assinatura de seus e-mails ou marcar um e-mail como spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos de coleta de endereços

Além de obter a permissão dos usuários antes de enviar mensagens, há vários métodos para coletar esses endereços de e-mail que podem afetar sua capacidade de entrega. 

### Listas de endereços adquiridas

O envio de e-mails para listas compradas ou alugadas é uma violação do seu contrato com o Braze! Se você estiver comprando e-mails, estará enviando mensagens totalmente não solicitadas e se colocando em risco de problemas de entregabilidade.

### Co-registro

O co-registro refere-se a um acordo entre empresas para coletar informações do usuário. Esse é um método arriscado de cobrança. Ele permite que os usuários recebam e-mails de terceiros, às vezes sem o conhecimento ou a permissão do cliente. Se você optar por esse caminho, certifique-se de ter divulgações claras e a possibilidade de cancelar a assinatura no ponto de coleta.

### Opt-in pré-selecionado ou forçado

O opt-in pré-selecionado é um método de registro de e-mail no qual a caixa de inscrição de e-mail já está marcada para que os assinantes recebam seu e-mail. Ao deixar a caixa marcada, os assinantes estão optando e dando seu consentimento para receber seu e-mail. Esse método tende a incomodar as pessoas (também é ilegal para correspondências enviadas para ou dentro do Canadá). Você pode acabar com uma lista de e-mails de tamanho razoável, mas não pode ter certeza de que esses usuários desejam seus e-mails de marketing.

### Opção única

O single opt-in ocorre quando os assinantes se inscrevem por meio de um formulário de inscrição e são imediatamente adicionados à sua lista de e-mails. Com esse método, os usuários realizam uma única etapa para se inscrever, como digitar o endereço de e-mail em um campo de coleta ou selecionar uma caixa como parte de uma transação.

### Opção confirmada

Um opt-in confirmado ocorre quando um usuário marca uma caixa solicitando comunicação por e-mail, e uma mensagem de confirmação é enviada em retorno. Esse método permite que os usuários escolham o tipo e a frequência do conteúdo, o que melhora o envolvimento. 

Para confirmar que está direcionando apenas os usuários mais engajados, você também pode usar o método de opt-in duplo confirmado. Essa abordagem adiciona uma etapa extra na qual o usuário deve clicar em um botão ou link no e-mail de confirmação para ser colocado na lista de e-mails. 

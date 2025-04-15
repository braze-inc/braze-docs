---
nav_title: Consentimento e coleta de endereços
article_title: Consentimento e coleta de endereços
page_order: 6
page_type: reference
description: "Este artigo de referência aborda as práticas recomendadas para a coleta de consentimento e endereços de e-mail de usuários e define os diferentes estados possíveis de assinantes de usuários."
channel: email

---

# Consentimento e coleta de endereços

> Antes de enviar seus e-mails iniciais, é importante obter primeiro a permissão de seus clientes. É uma cortesia comum e faz maravilhas para suas taxas de abertura!

## Estados do assinante

Há três estados de inscrição de e-mail para um usuário: **aceitação**, **inscrição** e **cancelamento da inscrição**. Para alterar o estado da inscrição de um usuário, consulte nosso artigo sobre [alteração de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-subscriptions) ou use nossas [APIs de inscrição]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

| Estado do assinante | Descrição |
|---|---|
| Aceitou | Esses clientes clicaram no link em um e-mail de confirmação e aceitaram ativamente receber suas mensagens. |
| Inscreveu-se | Por padrão, os usuários são inscritos para receber e-mails desde que tenham um endereço de e-mail válido armazenado em seu perfil. Os usuários permanecem inscritos até que cancelem a inscrição ou aceitem. |
| Cancelou inscrição | Para ser marcado como cancelado, o cliente deve ter cancelado explicitamente a inscrição em seus e-mails ou marcado um e-mail como spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos de coleta de endereços

Além de obter a permissão dos usuários antes do envio de mensagens, há vários métodos para coletar esses endereços de e-mail que podem afetar a entregabilidade. 

### Listas de endereços adquiridas

O envio de e-mails para listas compradas ou alugadas é uma violação de seu contrato com o Braze! Se estiver comprando e-mails, estará enviando mensagens totalmente não solicitadas e se colocando em risco de problemas de entregabilidade.

### Co-registro

O co-registro refere-se a um acordo entre empresas para coletar informações do usuário. Esse é um método arriscado de cobrança. Ele aceita que os usuários recebam e-mails de terceiros, às vezes sem o conhecimento ou a permissão do cliente. Se acessar esse caminho, certifique-se de que haja divulgações claras e a possibilidade de cancelar inscrição no ponto de coleta.

### Aceitação pré-selecionada ou forçada

A aceitação pré-selecionada é um método de registro de e-mail no qual a caixa de inscrição de e-mail já está marcada para que os assinantes recebam seu e-mail. Ao deixar a caixa marcada, os assinantes estão aceitando e dando seu consentimento para receber seu e-mail. Esse método tende a incomodar as pessoas (também é ilegal para correspondências enviadas para ou dentro do Canadá). Você pode acabar com uma lista de e-mails de tamanho decente, mas não pode ter certeza de que esses usuários querem mesmo seus e-mails de marketing.

### Aceitação única

A aceitação única ocorre quando os assinantes inscrevem-se por meio de um formulário de inscrição e são imediatamente adicionados à sua lista de e-mails. Com esse método, os usuários realizam uma única etapa para se inscrever, como digitar seu endereço de e-mail em um campo de coleta ou selecionar uma caixa como parte de uma transação.

### Aceitação confirmada

Uma aceitação confirmada ocorre quando um usuário marca uma caixa solicitando o envio de mensagens por e-mail, e uma mensagem de confirmação é enviada em troca. Esse método permite que os usuários escolham o tipo e a frequência do conteúdo, o que melhora o engajamento. 

Para confirmar que está direcionando apenas os usuários mais engajados, você também pode usar o método de aceitação com confirmação dupla. Essa abordagem adiciona uma etapa extra na qual o usuário deve clicar em um botão ou link no e-mail de confirmação para ser colocado na lista de e-mails. 

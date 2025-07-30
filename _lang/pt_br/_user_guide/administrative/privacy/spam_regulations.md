---
nav_title: Regulamentações de spam
article_title: Regulamentações de spam
page_order: 4.2
page_type: reference
description: "Este artigo fornece resumos e recursos sobre vários regulamentos sobre spam que podem afetar você ou seus usuários."
channel:
- email
- push
- SMS

---

# Regulamentações de spam

> Há várias leis que regulam os remetentes de comunicações eletrônicas, incluindo e-mail, notificações por push e SMS. Você deve estar sempre ciente das [regulamentações locais](https://en.wikipedia.org/wiki/Email_spam_legislation_by_country) que podem afetar você ou seus usuários. 

A Braze está fornecendo informações relevantes com base em nossa própria pesquisa, mas você também deve consultar o texto completo dessas leis para obter detalhes completos e atualizados.

- [CAN-SPAM](#can-spam)
- [Lei anti-spam canadense](#casl)

## CAN-SPAM

A Lei CAN-SPAM de 2003 regulamenta os remetentes de e-mail no site U.S. enviando "qualquer mensagem de e-mail cujo objetivo principal seja o anúncio comercial ou a promoção de um produto ou serviço comercial". Você pode ler mais detalhes no site oficial [da Federal Trade Commission](http://www.business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business).

Há sete requisitos principais para a CAN-SPAM:

1. Não use informações de cabeçalho falsas ou enganosas (como "From", "To" e "Reply-To")
2. Não use linhas de assunto enganosas
3. Identificar a mensagem como um anúncio
4. Informe aos destinatários onde você está localizado (como endereço físico)
5. Informe aos destinatários como podem optar por não receber seus futuros e-mails
6. Atender prontamente aos pedidos de cancelamento de inscrição
7. Monitore o que os outros estão fazendo em seu nome

Os e-mails de transação estão isentos dessas regras, com exceção do item 1.

## Lei Anti-Spam Canadense (CASL) {#casl}

Em 1º de julho de 2014, a Lei Anti-Spam do Canadá (CASL) entra em vigor para os e-mails enviados a residentes canadenses. Você pode ler o texto completo da lei no [site de Leis de Justiça](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) do Governo do Canadá. Basicamente, a lei diz que os destinatários canadenses de notificações por e-mail e push precisam fornecer consentimento "expresso ou implícito" para a sua comunicação com eles.

### CASL versus CAN-SPAM

Há algumas diferenças importantes entre a CASL e a CAN-SPAM, principalmente:

- A CASL se aplica ao local onde a mensagem é recebida, portanto, os remetentes fora do Canadá são afetados
- Os destinatários das mensagens devem fazer a aceitação, em vez do cancelamento de inscrição

### Responsabilidade civil

Embora a CASL tenha um período de transição de três anos, de ponta a ponta, em 1º de julho de 2017, a Comissão Canadense de Rádio-Televisão e Telecomunicações (CRTC), o Competition Bureau e o Office of the Privacy Commissioner of Canada podem iniciar investigações e litígios durante esse período. Ao final do período de transição, os indivíduos também podem processar entidades que acreditam estar enviando spam.

### Envio de mensagens isentas

Os seguintes tipos de mensagens estão isentos dos requisitos da CASL:

- Envio de mensagens abertas fora do Canadá
- Envio de mensagens para membros da família ou outras relações pessoais
- Envio de mensagens para indivíduos associados à sua empresa, incluindo colaboradores ou contratados
- Envio de mensagens com informações sobre garantia, recall de produtos ou informações de segurança sobre um produto ou serviço que o destinatário tenha usado ou comprado
- Envio de mensagens com notificações de informações factuais sobre inscrição, associação ou conta
- Envio de mensagens que fornecem um produto ou serviço, incluindo atualizações ou upgrades de produtos

>  Essa não é a lista completa de isenções. Veja o [texto completo da lei](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) para obter mais detalhes.

### Consentimento de mensagens

A Braze exige consentimento explícito para todos os envios de e-mail e mensagens SMS/MMS.

#### Consentimento implícito

O consentimento implícito pode ser legalmente permitido em algumas jurisdições, mas não é suficiente para o envio de e-mails pelo Braze. Nossa Política de Uso Aceitável vai além dos requisitos legais.

#### Consentimento expresso

O consentimento expresso é uma confirmação escrita ou oral do destinatário da mensagem e só é válido se a mensagem incluir uma descrição clara e simples:

- Por que o consentimento está sendo solicitado
- A pessoa ou organização que está buscando o consentimento

## Filtros de spam

O fato de seus e-mails terem sido enviados com sucesso não significa que eles tenham sido necessariamente vistos. Não existe uma solução definitiva para evitar todos os filtros de spam porque cada filtro é único na forma como avalia a "pontuação de spam" de um e-mail. No entanto, aqui estão algumas dicas para evitar que seus e-mails sejam marcados como "spam".

### Obter permissão

Um processo de dupla aceitação consiste no envio de um e-mail de acompanhamento com um link de confirmação após a aceitação inicial. O uso desse recurso fornece a validação de que os destinatários desejam receber seu conteúdo. Você também pode dar uma etapa a mais, pedindo aos usuários que o adicionem ao catálogo de endereços deles. Além disso, é importante aumentar suas listas de e-mail de forma orgânica. As listas compradas tendem a ficar obsoletas!


### Construa sua reputação

Certifique-se de definir as expectativas quando as pessoas estiverem inscrevendo-se para receber seus e-mails. Seja explícito sobre o que você enviará e a frequência com que o fará. Em seguida, incentive os usuários a interagir com suas campanhas de e-mail, fornecendo conteúdo de valor. Ter conteúdo personalizado e relevante diminui a probabilidade de seus destinatários marcarem as mensagens como spam.

### Mantenha sua reputação

Esteja em contato constante com seus usuários para evitar que suas listas de e-mail fiquem obsoletas. Esperar muito tempo para enviar uma mensagem pode fazer com que o destinatário se esqueça de você e o marque como spam. Mantenha suas listas de e-mail atualizadas implementando uma política de sunsetting para remover os endereços de e-mail que forem devolvidos. As taxas de bounce são um fator-chave usado pelos provedores de acesso à internet para avaliar a reputação de um remetente.

### Verificação e teste

Certifique-se de que sua mensagem não contenha nada que possa disparar filtros de spam. Isso inclui tags supérfluas de editores de texto externos, como o Microsoft Word, formatação anormal de texto, uso excessivo de pontos de exclamação (!) e pontos de interrogação (?) como pontuação, escrita em MAIÚSCULAS e palavras disparadoras de spam. Envie e-mails com conteúdo variado usando os recursos de testes multivariantes para garantir que seus e-mails não sejam enviados para spam.

## Canal de envio de mensagens

### Envio de e-mail {#spam-email}

A qualidade de sua lista de e-mails é especialmente importante.  Um punhado de e-mails ruins em sua lista pode arruinar a entrega para um milhão de bons usuários. A coleta de uma lista de e-mails ruins gera bounces, listas de bloqueio, acessos a armadilhas de spam e diminui suas taxas de resposta. O primeiro passo é o envio de e-mails sem atividade regular e a remoção de bounces óbvios. Independentemente de você implementar um opt-in (marcar a caixa), opt-out (desmarcar a caixa), confirm opt-in (um e-mail que agradece por inscrever-se e fornece um link de cancelamento de inscrição) ou double opt-in (um e-mail que exige um clique para confirmar), o importante é pensar na qualidade da lista.

### iOS {#spam-ios-windows}

No iOS, seus usuários sempre foram solicitados a aceitar as notificações por push. A caixa de diálogo do iOS simplesmente aparece ao entrar no aplicativo e pede que o usuário aceite as notificações do seu app. O usuário do aplicativo vê a mesma mensagem pop-up no momento em que abre um aplicativo pela primeira vez, portanto, todos que estão na sua lista do iOS para notificações por push têm, por definição, aceitação.

### Android {#spam-android}

No Android, seus usuários podem presumir a aceitação pela aceitação implícita declarada na sua política de privacidade ou no contrato de licença do usuário final. Talvez você queira implementar um processo de aceitação expressa, talvez em uma tela inicial, assim que o usuário iniciar o app pela primeira vez. Acesse o artigo de [práticas recomendadas do Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) para obter mais detalhes. Também é possível orientar o usuário quanto aos tipos de notificações por push que ele receberá, aumentando assim a taxa de aceitação.


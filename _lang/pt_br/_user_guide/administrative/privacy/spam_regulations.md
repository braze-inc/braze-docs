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

> Há várias leis que regulamentam os remetentes de comunicações eletrônicas, incluindo e-mail, notificações push e SMS. Você deve estar sempre ciente das [regulamentações locais](https://en.wikipedia.org/wiki/Email_spam_legislation_by_country) que podem afetar você ou seus usuários. 

A Braze está fornecendo informações relevantes com base em nossa própria pesquisa, mas você também deve consultar o texto completo dessas leis para obter detalhes completos e atualizados.

- [CAN-SPAM](#can-spam)
- [Lei anti-spam canadense](#casl)

## CAN-SPAM

A Lei CAN-SPAM de 2003 regulamenta os remetentes de e-mail no site U.S. enviando "qualquer mensagem de correio eletrônico cujo objetivo principal seja o anúncio comercial ou a promoção de um produto ou serviço comercial". Você pode ler mais detalhes no site oficial [da Federal Trade Commission](http://www.business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business).

Há sete requisitos principais para a CAN-SPAM:

1. Não use informações de cabeçalho falsas ou enganosas (como "From", "To" e "Reply-To")
2. Não use linhas de assunto enganosas
3. Identificar a mensagem como um anúncio
4. Informe aos destinatários onde você está localizado (por exemplo, endereço físico)
5. Informe aos destinatários como podem optar por não receber seus futuros e-mails
6. Atender prontamente às solicitações de cancelamento
7. Monitorar o que os outros estão fazendo em seu nome

Os e-mails transacionais estão isentos dessas regras, com exceção do item 1.

## Lei Anti-Spam Canadense (CASL) {#casl}

Em 1º de julho de 2014, a Lei Anti-Spam do Canadá (CASL) entra em vigor para e-mails enviados a residentes canadenses. Você pode ler o texto completo da lei no [site de Leis de Justiça](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) do Governo do Canadá. Basicamente, a lei diz que os destinatários canadenses de notificações por e-mail e push precisam fornecer consentimento "expresso ou implícito" para a sua comunicação com eles.

### CASL versus CAN-SPAM

Há algumas diferenças importantes entre a CASL e a CAN-SPAM, principalmente:

- A CASL se aplica ao local onde a mensagem é recebida, portanto, os remetentes fora do Canadá são afetados
- Os destinatários da mensagem devem optar por aceitar, em vez de recusar

### Responsabilidade civil

Embora a CASL tenha um período de transição de três anos, que termina em 1º de julho de 2017, a Comissão Canadense de Rádio-Televisão e Telecomunicações (CRTC), o Competition Bureau e o Office of the Privacy Commissioner of Canada podem iniciar investigações e litígios durante esse período. Ao final do período de transição, os indivíduos também podem entrar em litígio contra entidades que acreditam estar enviando spam.

### Mensagens isentas

Os seguintes tipos de mensagens estão isentos das exigências da CASL:

- Mensagens abertas fora do Canadá
- Mensagens para membros da família ou outras relações pessoais
- Mensagens para pessoas associadas à sua empresa, incluindo funcionários ou prestadores de serviços
- Mensagens que fornecem informações de garantia, informações sobre recall de produtos ou informações de segurança ou proteção sobre um produto ou serviço que o destinatário tenha usado ou comprado
- Mensagens que fornecem notificação de informações factuais sobre assinatura, associação ou conta
- Mensagens que fornecem um produto ou serviço, incluindo atualizações ou upgrades de produtos

>  Essa não é a lista completa de isenções. Veja o [texto completo da lei](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) para obter mais detalhes.

### Consentimento de mensagem

A Braze exige consentimento explícito para todas as mensagens de e-mail e SMS/MMS.

#### Consentimento implícito

O consentimento implícito pode ser legalmente permitido em algumas jurisdições, mas não é suficiente para o envio de e-mails por meio da Braze. Nossa Política de Uso Aceitável vai além dos requisitos legais.

#### Consentimento expresso

O consentimento expresso é uma confirmação escrita ou oral do destinatário da mensagem e só é válido se a mensagem incluir uma descrição clara e simples:

- Por que o consentimento está sendo solicitado
- A pessoa ou organização que está buscando o consentimento

## Filtros de spam

O fato de seus e-mails terem sido enviados com sucesso não significa que eles tenham sido necessariamente vistos. Não existe uma solução definitiva para evitar todos os filtros de spam porque cada filtro é único na forma como avalia a "pontuação de spam" de um e-mail. No entanto, aqui estão algumas dicas para evitar que seus e-mails sejam rotulados como "spam".

### Obter permissão

Um processo de opt-in duplo consiste em enviar um e-mail de acompanhamento com um link de confirmação após um opt-in inicial. O uso desse recurso fornece a validação de que os destinatários desejam receber seu conteúdo. Você também pode dar um passo adiante, solicitando aos usuários que o adicionem ao catálogo de endereços deles. Além disso, certifique-se de aumentar suas listas de e-mail organicamente - as listas compradas tendem a ficar obsoletas!


### Construa sua reputação

Certifique-se de definir as expectativas quando as pessoas se inscreverem para receber seus e-mails. Seja explícito sobre o que você enviará e a frequência com que o fará. Em seguida, incentive os usuários a interagir com suas campanhas de e-mail fornecendo conteúdo valioso. Ter conteúdo personalizado e relevante diminui a probabilidade de seus destinatários marcarem as mensagens como spam.

### Mantenha sua reputação

Mantenha contato constante com seus usuários para evitar que suas listas de e-mail se tornem obsoletas. Esperar muito tempo para enviar uma mensagem pode fazer com que o destinatário se esqueça de você e o marque como spam. Mantenha suas listas de e-mail atualizadas, implementando uma política de descontinuidade para remover os endereços de e-mail que forem devolvidos. As taxas de rejeição são um fator importante usado pelos ISPs para avaliar a reputação de um remetente.

### Verificação e teste

Certifique-se de que sua mensagem não contenha nada que possa acionar filtros de spam. Isso inclui tags supérfluas de editores de texto externos, como o Microsoft Word, formatação anormal de texto, uso excessivo de pontos de exclamação (!) e pontos de interrogação (?) como pontuação, escrita em LETRAS MAIÚSCULAS e palavras de gatilho de spam. Envie e-mails com conteúdo variado usando recursos de teste multivariados para garantir que seus e-mails não sejam enviados para spam.

## Canal de mensagens

### E-mail {#spam-email}

A qualidade de sua lista de e-mails é especialmente importante.  Um punhado de e-mails ruins em sua lista pode arruinar sua entrega para um milhão de bons usuários. A coleta de uma lista de e-mails ruins gera devoluções, listas de bloqueio, acessos a armadilhas de spam e diminui suas taxas de resposta. A primeira etapa é eliminar os e-mails que não têm atividade regularmente e remover as devoluções óbvias. Independentemente de você implementar um opt-in (marcar a caixa), opt-out (desmarcar a caixa), confirm opt-in (um e-mail que agradece a inscrição e fornece um link para cancelar a inscrição) ou double opt-in (um e-mail que exige um clique para confirmar), o que você deve considerar é a qualidade da lista.

### iOS {#spam-ios-windows}

No iOS, seus usuários sempre foram solicitados a optar por receber notificações por push. A caixa de diálogo do iOS é simplesmente exibida ao entrar no aplicativo e solicita que o usuário opte por receber notificações do seu aplicativo. O usuário do aplicativo vê a mesma mensagem pop-up no momento em que abre um aplicativo pela primeira vez, portanto, todos os que estão na sua lista do iOS para notificações por push, por definição, optaram por participar.

### Android {#spam-android}

No Android, seus usuários podem presumir que optaram pelo opt-in implícito que está declarado na sua política de privacidade ou no contrato de licença do usuário final. Talvez você queira implementar um processo de opt-in expresso, talvez em uma tela inicial, assim que o usuário iniciar o aplicativo pela primeira vez. Acesse o artigo de [práticas recomendadas do Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) para obter mais detalhes. Você também pode orientar o usuário quanto aos tipos de notificações push que ele receberá, aumentando assim a taxa de adesão.


---
nav_title: "Sobre a SMS"
article_title: Sobre a SMS
page_order: 1
description: "Este artigo de referência aborda os casos de uso geral do canal SMS e os requisitos necessários para colocar o SMS em funcionamento."
page_type: reference
alias: /about_sms/
channel:
  - SMS
search_rank: 2
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}Sobre SMS

> Este artigo compartilha alguns casos de uso comuns, requisitos e termos a serem conhecidos que ajudarão na integração do SMS e permitirão que você se comunique de forma eficaz e estratégica com seus clientes.![Mensagem SMS com o texto "Welcome to Braze! Estamos muito feliz em ter você aqui. Dê uma olhada em nossa documentação para começar. https://www.braze.com/docs/ Text HELP para obter ajuda e STOP para parar."]({% image_buster /assets/img/sms/sms_about.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
O SMS, também conhecido como Short Message Service, é usado para enviar mensagens de texto para telefones celulares. Atualmente, há mais de 23 bilhões de mensagens de texto enviadas todos os dias em todo o mundo, sendo o SMS a forma mais direta de alcançar usuários e clientes. Esse uso generalizado e o valor comprovado tornaram o SMS uma ferramenta de marketing eficaz para empresas de todos os tamanhos. 
<br><br>
## Casos de uso em potencial

| Caso de uso | Explicação |
|---|---|
| Profissionais de marketing em geral | As mensagens SMS são uma maneira direta, flexível e eficiente de comunicar aos seus clientes as próximas ofertas, vendas favoráveis e produtos atuais ou previstos. |
| Lembretes | As mensagens SMS podem ser eficazes para notificar os usuários que marcaram um horário para um serviço. Por exemplo, o envio de uma mensagem SMS lembrando um cliente no dia anterior a uma consulta médica ajudará a minimizar a perda de consultas, economizando tempo e dinheiro para você e seus clientes. |
| Envio de mensagens transacionais | As mensagens SMS são uma maneira eficiente de enviar notificações transacionais, como confirmações de pedidos e informações de remessa, fornecendo a eles todas as informações de que precisam em um local conveniente. Observe que existem diretrizes legais que devem ser observadas no envio de mensagens transacionais. Se não tiver certeza dessas diretrizes, entre em contato com sua equipe jurídica interna.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solicitações

Antes de começar a enviar SMS, você precisa de alguns itens. Consulte a tabela a seguir para saber mais.

|Requisito | Descrição | Aquisição |
|---|---|---|
| Um número de telefone dedicado (código curto ou código longo) | Um número de telefone dedicado fornecido exclusivamente para uma única marca ou host. | A Braze cuida da aquisição desses números para você. Saiba mais sobre [códigos curtos e longos]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).|
| Lista de usuários com números de telefone | Antes de começar a enviar mensagens, é necessário adicionar usuários à sua conta. Além disso, você precisa saber o tamanho aproximado de seu público.  | Os usuários são inicialmente adicionados ao Braze por meio de nosso backend. Você deve passar essa lista para que façamos o upload para você. Os números de telefone devem ser formatados como um número de 10 dígitos, bem como um código de área do país. Saiba mais sobre [números de telefone de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). |
| [Palavras-chave e respostas de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/) | Todas as palavras-chave básicas devem ter respostas atribuídas a elas antes que você possa iniciar o envio de mensagens. | Você deve listá-las e enviá-las ao seu representante Braze ou gerente de integração durante o processo de integração. Exibir [modelos de palavras-chave de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Termos a conhecer

Para obter uma lista completa de termos, visite nossa seção [Termos de SMS para conhecer]({{site.baseurl}}/sms_terms_to_know/).


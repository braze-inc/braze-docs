---
nav_title: "Sobre a SMS"
article_title: Sobre a SMS
page_order: 1
description: "Este artigo de referência aborda os casos de uso geral do canal SMS e os requisitos necessários para colocar o SMS em funcionamento."
page_type: reference
channel:
  - SMS
search_rank: 2
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}Sobre SMS

> Este artigo compartilha alguns casos de uso comuns, requisitos e termos a serem conhecidos que ajudarão na integração do SMS e permitirão que você se comunique de forma eficaz e estratégica com seus clientes.![Mensagem SMS com o texto "Welcome to Braze! Estamos muito feliz em ter você aqui. Dê uma olhada em nossa documentação para começar. https://www.braze.com/docs/ Envie HELP para obter ajuda e STOP para parar."][picture]{: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

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
| Um número de telefone dedicado (código curto ou código longo) | Um número de telefone dedicado fornecido exclusivamente para uma única marca ou host. | A Braze cuida da aquisição desses números para você. Saiba mais sobre [códigos curtos e longos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/).|
| Lista de usuários com números de telefone | Antes de começar a enviar mensagens, é necessário adicionar usuários à sua conta. Além disso, você precisa saber o tamanho aproximado de seu público.  | Os usuários são inicialmente adicionados ao Braze por meio de nosso backend. Você deve passar essa lista para que façamos o upload para você. Os números de telefone devem ser formatados como um número de 10 dígitos, bem como um código de área do país. Saiba mais sobre [números de telefone de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/). |
| [Palavras-chave e respostas de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) | Todas as palavras-chave básicas devem ter respostas atribuídas a elas antes que você possa iniciar o envio de mensagens. | Você deve listá-las e enviá-las ao seu representante Braze ou gerente de integração durante o processo de integração. Exibir [modelos de palavras-chave de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Termos a conhecer

- **Código curto:** Um código de 5 a 6 dígitos, que é mais curto do que um número de telefone completo. Esse código é usado para endereçar e enviar mensagens SMS.<br><br>
- **Códigos longos:** Um código de 10 dígitos usado para endereçar mensagens SMS. A maioria dos números de telefone comuns são considerados códigos longos (e.g 123-456-7891). Esses códigos são usados para endereçar e enviar mensagens SMS.<br><br>
- **Grupo de inscrições:** Uma coleção de números de telefone de envio (como códigos curtos, códigos longos e/ou IDs alfanuméricos de remetente) que são usados para um tipo específico de finalidade de envio de mensagens. Por exemplo, se uma marca planeja enviar mensagens SMS transacionais e promocionais, dois grupos de inscrições com pools separados de números de telefone para envio precisarão ser configurados no dashboard do Braze.<br><br>
- **Segmento de mensagens e limites de caracteres:** Um segmento de mensagens refere-se ao número de segmentos em que sua mensagem SMS inicial será dividida. Cada mensagem tem um limite de caracteres que, se excedido, fará com que a mensagem seja dividida em segmentos. Com base nos padrões de codificação que você usa (UTF-2 ou GSM-7), há limites de caracteres variados. Consulte nosso [message copy limits][2] para saber mais sobre segmentação de envio de mensagens e limites de caracteres de mensagens.<br><br>
- **Métricas comuns de campanhas de SMS:** <br>*Enviados*, *Enviados à operadora*, *Falha na entrega*, *Entrega confirmada*, *Rejeições*, *Aceitação* e *Ajuda*. <br>Para informações sobre essas e outras métricas de SMS, consulte [relatório de SMS][1]. Note que o *envio para a operadora* está obsoleto, mas continuará a ser permitido pelos usuários que já o possuem.

<br><br>

Para obter uma lista completa de termos, visite nossa seção [Termos de SMS para conhecer]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/terms/).

[picture]: {% image_buster /assets/img/sms/sms_about.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy

---
nav_title: Registro de atividade de mensagens
article_title: Registro de Atividade de Mensagens
page_order: 5
page_type: reference
description: "Este artigo de referência descreve o Registro de Atividade de Mensagens e mostra as mensagens associadas às suas campanhas e envios. Aqui, você também pode encontrar informações sobre como entender as mensagens do log."

---

# Registro de Atividade de Mensagens {#dev-console-troubleshooting}

> O **Registro de Atividade de Mensagens** oferece a oportunidade de ver quaisquer mensagens (especialmente mensagens de erro) associadas às suas campanhas e envios.

Você pode ver transações de campanha da API, detalhes de solução de problemas sobre mensagens falhadas e reunir informações sobre como melhorar a entrega de notificações ou resolver problemas técnicos existentes.

Para acessar o log, vá para **Configurações** > **Registro de Atividade de Mensagens**.

\![Registro de Atividade de Mensagens]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Além deste artigo, também recomendamos conferir nosso curso de Aprendizado Braze sobre [Garantia de Qualidade e Ferramentas de Depuração](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que cobre como usar o Registro de Atividade de Mensagens para realizar sua própria solução de problemas e depuração.
{% endalert %}

Você pode filtrar pelo seguinte conteúdo registrado no **Registro de Atividade de Mensagens**:

- Erros de notificação push
- Erros de mensagens abortadas
- Erros de webhook
- Erros de e-mail
- Registros de mensagens da API
- Erros de Conteúdo Conectado
- Erros de audiência conectada da API REST
- Erros de aliasing de usuário
- Erros de teste A/B
- Erros de SMS/MMS
- Erros do WhatsApp
- Erros de Atividade ao Vivo
- Erros de gatilho de usuário ruim

Essas mensagens podem vir do nosso próprio sistema, seus aplicativos ou plataformas, ou de nossos parceiros de terceiros. Isso pode resultar em um número infinito de mensagens que podem aparecer neste log.

## Entendendo mensagens de log

Para determinar o que suas mensagens significam, preste atenção à redação de cada mensagem e às colunas que correspondem a ela, pois isso pode ajudá-lo a solucionar problemas usando pistas de contexto. 

Por exemplo, se você tiver uma entrada de log cuja mensagem afirma "empty-cart_app" e você não tiver certeza do que isso significa, olhe para a esquerda na coluna **Tipo**. Se você ver "Erro de Mensagem Abortada", pode assumir com segurança que a mensagem era o que foi escrito como [mensagem de abortar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) usando Liquid, e que a mensagem foi abortada porque o destinatário pretendido da mensagem tinha um carrinho vazio em seu aplicativo.

### Mensagens comuns

Existem alguns tipos de mensagens comuns que você pode ver, e algumas podem até fornecer links de solução de problemas para ajudá-lo a diagnosticar e corrigir problemas.

As seguintes mensagens listadas são para fins de exemplo e podem não corresponder exatamente ao que é exibido na coluna **Mensagem** do seu log.

| Tipo de Mensagem | Mensagem Potencial | Descrição |
|---|---|---|
| Soft Bounce | O endereço de e-mail same@example.com teve um soft bounce. | O endereço de e-mail era válido e a mensagem de e-mail chegou ao servidor de e-mail do destinatário, mas foi rejeitada por um problema "temporário". <br><br>As razões comuns para um soft bounce incluem: {::nomarkdown} <ul> <li> A caixa de entrada estava cheia (o usuário ultrapassou sua cota) </li> <li> O servidor estava fora do ar </li> <li> A mensagem era muito grande para a caixa de entrada do destinatário </li>  </ul> {:/} Se um e-mail recebeu um soft bounce, geralmente tentaremos novamente dentro de um período de 72 horas, mas o número de tentativas de reenvio varia de receptor para receptor. |
| Hard Bounce | A conta de e-mail que você tentou alcançar não existe. Tente verificar novamente o endereço de e-mail do destinatário em busca de erros de digitação ou espaços desnecessários. | Sua mensagem nunca chegou à caixa de entrada dessa pessoa porque não havia caixa de entrada para alcançar. Se você quiser investigar mais, mensagens como esta podem às vezes ter links na coluna **Ver Detalhes** que permitirão que você veja o perfil do destinatário pretendido.|
| Bloquear | Mensagem de spam é rejeitada devido à política anti-spam. | Sua mensagem foi categorizada como spam. Este erro de e-mail é registrado para um usuário se recebemos um evento do ESP indicando que o e-mail foi descartado. Pode ser que seja para aquele destinatário pretendido, mas se você está vendo esta mensagem com frequência, pode querer reavaliar seus hábitos de envio ou o conteúdo da sua mensagem. Além disso, pense de volta—você [esquentou seu IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? Se não, entre em contato com a Braze para obter conselhos sobre como fazer isso.|
| Erro de Mensagem Abortada | empty-cart_web | Se você tem um aplicativo com um carrinho ou cria um envio com uma mensagem de abortar no Liquid, você pode personalizar qual mensagem é retornada a você se o envio for abortado. Neste caso, a mensagem retornada é empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Por que minha mensagem não está listada aqui?

As mensagens no Registro de Atividade de Mensagens podem vir de uma variedade de fontes: Braze, seus aplicativos ou plataformas, ou nossos parceiros de terceiros. Isso significa que há um número infinito de mensagens que poderiam aparecer neste registro—como você pode imaginar, não podemos listar todas!

Por exemplo, algumas mensagens potenciais de "Bloqueio", além da listada na tabela anterior, poderiam ser:

- Infelizmente, mensagens de [_IP_ADDRESS_] não foram enviadas. Por favor, entre em contato com seu provedor de serviços de Internet, pois parte da rede deles está na nossa lista de bloqueio.
- Mensagem rejeitada devido à política local.
- A mensagem foi bloqueada pelo receptor como spam.
- Serviço indisponível, Cliente host [_IP_ADDRESS_] bloqueado usando Spamhaus.

## Período de retenção de armazenamento

Erros das últimas 60 horas estão disponíveis nos Registros de Atividade de Mensagens. Registros com mais de 60 horas são limpos e não estão mais acessíveis.

### Número de registros de erro armazenados

O número de registros salvos é influenciado por várias condições. Por exemplo, se uma campanha agendada for enviada para milhares de usuários, poderíamos potencialmente ver uma amostra dos erros no Registro de Atividade de Mensagens em vez de todos os erros. A seguir, uma visão geral das condições que afetam quantos registros serão salvos:
- Até 20 registros de erro do mesmo tipo de erro serão salvos para a mesma campanha ou etapa do Canvas dentro de uma hora fixa do relógio para os seguintes tipos de erro:
    - Erros de Conteúdo Conectado
    - Erros de Mensagem Abortada
    - Erros de webhook
    - Erros de rejeição de SMS
    - Erros de falha na entrega de SMS
    - Erros de falha no WhatsApp
    - Erros de teste A/B
- Até 20 logs de erro de notificação push do mesmo tipo de erro serão salvos para a mesma campanha ou combinação de etapa do Canvas e aplicativo para os seguintes tipos de erro:
    - Credencial de push inválida
    - Token de push inválido
    - Sem credencial de push
    - Erros de token
    - Cota excedida
    - Tentativas esgotadas
    - Carga útil inválida
    - Erro inesperado
- Até 100 logs de erro do mesmo tipo de erro serão salvos para o mesmo aplicativo dentro de uma hora fixa para os seguintes tipos de erro:
    - Erro de Atividade Ao Vivo (Sem credencial de push)
    - Erro de Atividade Ao Vivo (Credencial de push inválida)
    - Outros erros de Atividade Ao Vivo
    - Erros de token removido do feedback APNS
- Até 100 logs de erro do mesmo tipo de erro serão salvos para a mesma campanha ou etapa do Canvas dentro de uma hora fixa para os seguintes tipos de erro:
    - Erros de Soft Bounce de Email
    - Erros de Hard Bounce de Email
    - Erros de Bloqueio de Email
- Até 100 logs de erro de aliasing de usuário serão salvos para o mesmo espaço de trabalho dentro de uma hora fixa.


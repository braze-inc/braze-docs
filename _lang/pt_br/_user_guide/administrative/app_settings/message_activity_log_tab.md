---
nav_title: Registro de atividades de envio de mensagem
article_title: Registro de atividades de envio de mensagem
page_order: 5
page_type: reference
description: "Este artigo de referência descreve que o Message Activity Log mostra as mensagens associadas às suas campanhas e envios. Aqui, você também pode encontrar informações sobre como entender as mensagens de registro."

---

# Registro de atividade de mensagens {#dev-console-troubleshooting}

> O **Registro de atividades de envio de mensagem** oferece a oportunidade de ver todas as mensagens (especialmente mensagens de erro) associadas às suas campanhas e envios, inclusive erros de notificação por push.

Você pode ver as transações da campanha de mensagens API, solucionar problemas com detalhes sobre mensagens com falha e obter insights sobre como melhorar a entrega de notificações ou resolver problemas técnicos existentes.

Para acessar o registro, acesse **Configurações** > **Registro de atividade de mensagens**.

![Envio de mensagens do registro de atividade]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Além deste artigo, também recomendamos conferir nosso curso do Braze Learning sobre [Ferramentas de garantia de qualidade e depuração](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que aborda como usar o Message Activity Log para conduzir sua própria solução de problemas e depuração.
{% endalert %}

É possível filtrar pelo seguinte conteúdo registrado no **Message Activity Log**:

- Erros de notificação por push
- Erros de mensagens abortadas
- Erros de webhook
- Erros de correio eletrônico
- Registros de mensagens da API
- Erros de conteúdo conectado
- Erros de público conectado à API REST
- Erros de aliasing de usuário
- Erros nos Testes A/B
- Erros de SMS/MMS
- Erros do WhatsApp
- Erros de atividade ao vivo
- Erros de disparo de usuário ruim

Essas mensagens podem vir de nosso próprio sistema, de seus apps ou plataformas, ou de nossos parceiros terceirizados. Isso pode resultar em um número infinito de mensagens que podem aparecer nesse registro.

## Compreensão das mensagens de registro

Para determinar o significado de suas mensagens, preste atenção ao texto de cada mensagem e às colunas que correspondem a ela, pois isso pode ajudá-lo a solucionar problemas usando dicas de contexto. 

Por exemplo, se houver um registro cuja mensagem indique "empty-cart_app" e você não tiver certeza do que isso significa, olhe à esquerda na coluna **Type (Tipo** ). Se você vir "Erro de mensagem abortada", poderá presumir com segurança que a mensagem era o que foi escrito como [mensagem de abortamento]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) usando o Liquid e que a mensagem foi abortada porque o destinatário pretendido da mensagem tinha um carrinho vazio em seu app.

### Envio de mensagens comuns

Há alguns tipos de mensagens comuns que você pode ver, e algumas podem até fornecer links para envio de mensagens de solução de problemas para ajudá-lo a diagnosticar e corrigir problemas.

As mensagens listadas a seguir são para fins de exemplo e podem não corresponder exatamente ao que é exibido na coluna **Mensagem** do seu registro.

| Tipo de mensagem | Mensagens em potencial | Descrição |
|---|---|---|
| Soft bounce | O endereço de e-mail same@example.com é um soft bounce. | O endereço de e-mail era válido e a mensagem de e-mail chegou ao servidor de e-mail do destinatário, mas foi rejeitada por um problema "temporário". <br><br>Os motivos comuns do soft bounce incluem: {::nomarkdown} <ul> <li> A caixa de correio estava cheia (o usuário ultrapassou sua cota) </li> <li> O servidor estava fora do ar </li> <li> A mensagem era muito grande para a caixa de entrada do destinatário </li>  </ul> {:/} Se um e-mail tiver recebido um soft bounce, geralmente tentaremos novamente em um período de 72 horas, mas o número de tentativas de nova tentativa varia de acordo com o destinatário. |
| Hard bounce | A conta de e-mail que você tentou acessar não existe. Tente verificar novamente o endereço de e-mail do destinatário quanto a erros de digitação ou espaços desnecessários. | Sua mensagem nunca chegou à caixa de entrada dessa pessoa porque não havia uma caixa de entrada para ser acessada. Se quiser se aprofundar mais, mensagens como essa podem, às vezes, ter links na coluna **Exibir detalhes** que lhe permitirão visualizar o perfil do destinatário pretendido.|
| Bloquear | A mensagem de spam é rejeitada devido à política anti-spam. | Sua mensagem foi categorizada como spam. Esse erro de e-mail é registrado para um usuário se tivermos recebido um evento do ESP indicando que o e-mail foi descartado. Pode ser que seja apenas para o destinatário pretendido, mas se estiver vendo essa mensagem com frequência, talvez queira reavaliar seus hábitos de envio ou o conteúdo da sua mensagem. Além disso, pense no passado - você aqueceu [seu IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? Caso contrário, entre em contato com o Braze para obter conselhos sobre como fazer isso.|
| Erro de mensagem abortado | empty-cart_web | Se você tiver um app com um carrinho ou criar um envio com uma mensagem de abortar no app, poderá personalizar a mensagem que será retornada se o envio for abortado. Nesse caso, a mensagem retornada é empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Por que minha mensagem não está listada aqui?

As mensagens no Registro de atividades de envio de mensagem podem ser provenientes de várias fontes: Braze, seus apps ou plataformas, ou nossos parceiros terceirizados. Isso significa que há um número infinito de mensagens que podem aparecer nesse registro - como você pode imaginar, não podemos listar todas elas!

Por exemplo, algumas mensagens de "Bloqueio" em potencial, além das listadas na tabela anterior, poderiam ser:

- Infelizmente, as mensagens de [_IP_ADDRESS_] não foram enviadas. Entre em contato com seu prestador de serviço de Internet, pois parte da rede dele está em nossa lista de bloqueio.
- Mensagem rejeitada devido à política local.
- A mensagem foi bloqueada pelo destinatário como spam.
- Serviço indisponível, host do cliente [_IP_ADDRESS_] bloqueado usando Spamhaus.

## Período de retenção de armazenamento

Os erros das últimas 60 horas estão disponíveis nos registros de atividades de mensagens. Os registros com mais de 60 horas são limpos e não podem mais ser acessados. 

### Número de registros de erros armazenados

O número de registros salvos é influenciado por várias condições. Por exemplo, se uma campanha programada for enviada a milhares de usuários, é possível que vejamos uma amostra dos erros no registro de atividades de mensagens em vez de todos os erros.

Aqui está uma visão geral das condições que afetam o número de registros que serão salvos:
- Até 20 registros de erros da Connected Content serão salvos para a mesma campanha dentro de uma hora fixa.
- Até 100 registros de erro do mesmo tipo serão salvos em uma hora fixa por espaço de trabalho para os seguintes tipos de erro:
    - Erros de mensagens abortadas
    - Erros de webhook
    - Erros de notificação por push
    - Erros de atividade ao vivo
    - Erros de disparo de usuário ruim


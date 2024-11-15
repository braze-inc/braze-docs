---
article_title: Limitação de Taxa para Campanhas e canvas
permalink: /rate_limiting/
page_type: reference
description: "Este artigo de referência descreve o comportamento de limitação de taxa de velocidade de entrega do Braze anterior."
---

# Limite de taxa

> Este artigo descreve o comportamento anterior de limitação de taxa de velocidade de entrega do Braze. O comportamento atualizado de limitação de taxa é descrito [aqui]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#rate-limiting).

Braze permite que você controle a pressão de marketing limitando a taxa de suas campanhas e Canvases, regulando a quantidade de tráfego de saída de sua plataforma. Você pode implementar dois tipos diferentes de limitação de taxa para suas campanhas:

1. **O limite de taxa de velocidade de entrega** leva em consideração a largura de banda dos seus servidores.
2. **Limitação de taxa centrada no usuário** foca em proporcionar a melhor experiência para o usuário. 

Para saber mais, consulte [Sobre limitação de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-rate-limiting).

## Sobre a limitação da taxa de velocidade de entrega

Se você antecipa grandes campanhas que geram um aumento na atividade do usuário e sobrecarregam seus servidores, você pode especificar um limite de frequência por minuto para o envio de mensagens—isso significa que a Braze não enviará mais do que o seu limite de frequência definido dentro de um minuto. 

Ao direcionar usuários durante a criação da campanha, você pode navegar para **Públicos-Alvo** (para campanhas) ou **Configurações de Envio** (para canva) para selecionar um limite de frequência de entrega de mensagens (em vários incrementos, de tão baixo quanto 10 a tão alto quanto 500.000 mensagens por minuto). Observe que as campanhas sem limite de frequência podem exceder esses limites de entrega.

Por exemplo, se você estiver tentando enviar 75.000 mensagens com um limite de frequência de 10.000 por minuto, a entrega será distribuída ao longo de oito minutos. Sua campanha não enviará mais de 10.000 mensagens durante os primeiros sete minutos e 5.000 mensagens no último minuto. 

### Considerações

Mensagens enviadas usando um limite de frequência não terão a configuração de limite de frequência (como 10.000 por minuto) enviadas uniformemente ao longo de 60 segundos. Em vez disso, Braze garante que não mais de 10.000 mensagens sejam enviadas por minuto (isso pode significar uma porcentagem maior das 10.000 mensagens sendo enviadas na primeira metade do minuto em comparação com a última metade do minuto). 

Tenha cuidado com a postergação de mensagens sensíveis ao tempo com essa forma de limite de frequência. Se o  público da mensagem contiver 30 milhões de usuários, mas definirmos o limite de frequência para 10.000 por minuto, uma grande parte da sua base de usuários não receberá a mensagem até o dia seguinte. 

Esteja ciente de que as mensagens serão abortadas se forem atrasadas por 72 horas ou mais devido a um limite de frequência baixo. O usuário que criou a campanha receberá alertas no dashboard e por e-mail se o limite de frequência for muito baixo.

## Limitação de taxa de velocidade de entrega de campanhas

### Campanhas de canal único

Ao enviar uma campanha de canal único com um limite de frequência de velocidade de entrega, o limite de frequência é aplicado a todas as mensagens juntas. Por exemplo, uma campanha de e-mail com um limite de frequência de 10.000 mensagens por minuto enviará um máximo de 10.000 mensagens totais por minuto.


| Máximo de e-mails enviados por minuto | Máximo total de mensagens enviadas por minuto |
|--------------------------------|----------------------------------------|
| 10.000                         | 10.000                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Campanhas multicanal

Ao enviar uma campanha multicanais com um limite de frequência de velocidade, cada canal é enviado independentemente dos outros. Como consequência disso, o seguinte pode ocorrer:

- O número total de mensagens enviadas por minuto pode ser maior do que o limite de frequência. Por exemplo, se sua campanha tem um limite de frequência de 10.000 por minuto e utiliza e-mail e SMS, Braze pode enviar um máximo de 20.000 mensagens totais a cada minuto (10.000 e-mails e 10.000 webhooks).

| Máximo de e-mails enviados por minuto | Máximo de mensagens SMS enviadas por minuto | Máximo total de mensagens enviadas por minuto |
|--------------------------------|--------------------------------------|----------------------------------------|
| 10.000                         | 10.000                               | 20.000                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- Os usuários poderiam receber os diferentes canais em momentos diferentes, e não é necessariamente previsível qual canal eles receberão primeiro. 

Por exemplo, se você enviar uma campanha que contém e-mail e SMS, pode ter 10.000 usuários com números de telefone válidos, mas 50.000 usuários com endereços de e-mail válidos. Se você definir a campanha para enviar 100 mensagens por minuto (um limite de frequência lento para o tamanho da campanha), um usuário pode receber o SMS no primeiro lote de envios e o e-mail no último lote de envios, quase nove horas depois.

### Campanhas push multiplataforma

Para campanhas push veiculadas em várias plataformas, o limite de frequência selecionado será distribuído igualmente entre as plataformas. Uma campanha de mensagens push que aproveite o Android e o iOS com um limite de frequência de 10.000 por minuto distribuirá igualmente as 10.000 mensagens nas duas plataformas.

| Máximo de notificações do Android enviadas por minuto | Máximo de notificações por push do iOS enviadas por minuto | Máximo total de notificações por push enviadas por minuto |
|--------------------------------|--------------------------------------|----------------------------------------|
| 10.000                         | 10.000                               | 10.000                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Limitação da taxa de velocidade de entrega do canva

Ao enviar um canva com um limite de frequência de velocidade, cada canal é enviado independentemente dos outros. Como consequência disso, o seguinte pode ocorrer:

- O número total de mensagens enviadas por minuto pode ser maior do que o limite de frequência. 
    - Por exemplo, se o seu canva tiver um limite de frequência de 10.000 por minuto e utilizar e-mail e mensagens no app, a Braze pode enviar até 20.000 mensagens totais a cada minuto (10.000 e-mails e 10.000 mensagens no app).

- Os limites de taxa podem impactar a ordem em que os usuários recebem mensagens em um canva. 
    - Por exemplo, se você enviar um canva que contém e-mails e notificações por push para 50.000 usuários, pode ser que todos os 50.000 tenham endereços de e-mail válidos, mas apenas 10.000 usuários tenham tokens de push válidos. Neste caso, se você configurar o canva para enviar 1.000 mensagens por minuto e houver uma etapa do canva multicanal que contenha tanto e-mail quanto push, é possível que um usuário avance para a próxima etapa do canva (e seja elegível para receber esta próxima etapa) após receber apenas a notificação por push, mas ainda não o e-mail. 

## Visão geral do comportamento anterior e novo de limitação de taxa

Sua conta Braze está atualmente usando o comportamento anterior de limitação de taxa de velocidade de entrega. As informações abaixo detalham a diferença geral entre o comportamento de limitação de taxa de velocidade de entrega anterior e nova:

- **Campanhas de canal único e canvas:** Os limites de taxa sempre serão aplicados a todas as mensagens juntas.
- **Campanhas multicanal e Canvas (incluindo push multiplataforma):**


<style>
table td {
    word-break: normal;
}
</style>

<table>
  <tr>
    <th></th>
    <th><b>Campanhas</b></th>
    <th><b>Canva</b></th>
  </tr>
  <tr>
    <td><b>Voltar</b></td>
    <td>Aplicado para cada canal separadamente, com plataformas de push* compartilhando o limite coletivamente</td>
    <td>Aplicado para cada canal separadamente, com plataformas de push* compartilhando o limite coletivamente</td>
  </tr>
  <tr>
    <td><b>Novo</b></td>
    <td>Aplicado separadamente por canal e plataforma de push</td>
    <td>Compartilhado coletivamente</td>
  </tr>
</table>

_\*Push plataformas incluem: Android, iOS, web push, e Kindle._
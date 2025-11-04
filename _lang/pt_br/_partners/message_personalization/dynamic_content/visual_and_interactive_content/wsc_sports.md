---
nav_title: WSC Sports
article_title: WSC Sports
description: "Este artigo de referência descreve a parceria entre o Braze e a WSC Sports, uma plataforma de vídeo esportivo que permite incluir mídia esportiva rica e robusta em suas notificações por push do Braze."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> A plataforma [WSC Sports](https://wsc-sports.com/) gera vídeos esportivos personalizados para cada plataforma digital e cada fã de esportes - automaticamente e em tempo real. 

_Essa integração é mantida pela WSC Sports._

## Sobre a integração

A integração entre o Braze e a WSC Sports permite incluir mídia esportiva rica e robusta nas notificações por push do Braze. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da WSC | É necessário ter uma conta na WSC para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com permissões de **Mensagens**, **Segmentos**, **Campanhas** e **Canvas**. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

O aplicativo WSC Sports lida com o processo de ponta a ponta, desde a seleção do vídeo até a chegada da notificação por push no dispositivo do usuário final. 

### Etapa 1: selecionar configurações de envio

![]({% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"){: style="float:right;max-width:25%;margin-bottom:15px;"}

Antes de iniciar a integração, certifique-se de ter a campanha desejada e os segmentos de usuários criados no Braze. Quando concluído, na plataforma WSC Sports, selecione o vídeo desejado e, nas configurações de envio, selecione o segmento de usuário Braze e o ID da campanha que deseja usar. Por fim, escolha o horário em que deseja que a mensagem push seja enviada. 

#### Chamada da API

Depois de enviada, a WSC Sports entregará a notificação por push aos segmentos de usuários escolhidos, usando os seguintes endpoints do Braze, com base nas opções selecionadas:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#sending-messages-immediately-via-api-only)

O corpo da mensagem resultante é o seguinte: 
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### Etapa 2: fazer envio de teste

Nesse ponto, sua campanha deve estar pronta para ser testada e enviada. Verifique os registros de mensagens de erro da Braze se encontrar erros. 



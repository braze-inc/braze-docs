---
nav_title: Notify
article_title: Notify
description: "Este artigo de referência descreve a parceria entre o Braze e a Notify, uma solução de personalização omnicanal em tempo real que oferece personalização em todo o ciclo de vida do cliente."
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Notify

> [Notify](https://fr.notify-group.com/) é uma solução de software impulsionada por IA que se integra perfeitamente com ferramentas de gestão de relacionamento com o cliente para aprimorar estratégias de marketing e facilitar o engajamento em múltiplos canais.

A integração do Braze e do Notify permite que os profissionais de marketing promovam efetivamente o engajamento em várias plataformas. Em vez de depender de métodos tradicionais de marketing, uma campanha disparada pela API do Braze pode aproveitar os recursos do Notify para fornecer envio de mensagens personalizadas por meio de vários canais, incluindo e-mail, SMS, notificações por push e muito mais.

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Requisito          | Descrição                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|  Chave da API REST do Braze  | Uma chave da API REST da Braze com as permissões `users.export.segment` e `campaigns.trigger.send`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Configuração de CNAME | Um subdomínio deve ser criado para o rastreamento do pixel usado no e-mail para o Notify rastrear o engajamento do usuário com o envio de mensagens para informar melhor o modelo. Compartilhe a URL do subdomínio com o Notify após sua criação. |
| Exportação de aceitação de banco de dados | Envie os dados da campanha e de compras do ano passado (12 meses) para o Notify. ​Esta exportação será usada para treinar o modelo preditivo Notify. <br><br> **Campos:** <br><br> **Envio de e-mail:** Um hash SHA256 do e-mail, convertido para minúsculas e com quaisquer espaços em branco no início ou no final removidos.<br><br>**Segmento:** As informações do segmento que definem o nível de atividade (ativo ou inativo).<br><br>**Sub-segmento:** Qualquer outra informação relevante sobre atividades, como nível de atividade de compra.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Crie sua campanha

Crie uma [campanha acionada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery) no Braze. Então, compartilhe a campanha `api_identifier` com o Notify.

### Etapa 2: Crie seu segmento no Braze

Em seguida, crie o segmento de usuários que eles gostariam de segmentar com a campanha criada na [Etapa 1](#step-1-create-your-campaign). Em seguida, compartilhe o ID do segmento com o Notify.

### Etapa 3: Busque seu segmento

Em seguida, o Notify exportará os usuários no segmento anexado à campanha.

### Etapa 4: Notificar aciona a campanha

Usando o `/campaigns/trigger/send` endpoint, a IA da Notify aciona a campanha Braze criada na [Etapa 1](#step-1-create-your-campaign) para enviar aos usuários no momento que eles consideram mais provável de engajar.

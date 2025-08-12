---
nav_title: Worthy
article_title: Worthy
description: "Este artigo de referência descreve a parceria entre o Braze e a Worthy, uma plataforma de personalização de mensagens que permite criar experiências ricas e personalizadas no app e fornecê-las por meio do Braze."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> A integração entre a [Worthy](https://worthy.ai/) e o Braze permite que você crie facilmente experiências ricas e personalizadas no app usando o editor de arrastar e soltar da Worthy e as forneça por meio do Braze. Além disso, a Worthy fará automaticamente o seguinte:

Esta integração é mantida pela Worthy.

## Sobre a integração

- Criar um servidor de conteúdo conectado e uma API segura para seu envio de mensagens.
- Construa suas mensagens no app com análise de dados e rastreamento de cliques que aparecerão diretamente no Braze.
- Exporte automaticamente o HTML por meio do editor de arrastar e soltar da Worthy para usar em campanhas de mensagens no app com **código personalizado** no Braze, com as conexões API necessárias e o conteúdo dinâmico que você configurar.

## Casos de uso

- Experiências de boas-vindas personalizadas com base nas seleções de integração do usuário
- Experiências no app para eventos e promoções especiais
- Coleta de feedback e classificações dos clientes com base no comportamento do app
- Testar rapidamente possíveis ideias de produtos de app
- Avisos ricos, notícias e atualizações da comunidade

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta da [Worthy](https://worthy.ai/) | É necessário ter uma conta Worthy para aproveitar essa parceria. |
| SDK do Braze | Você precisará configurar o SDK do Braze no seu aplicativo móvel para enviar mensagens avançadas no app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integração

### Etapa 1: Crie envios de mensagens personalizados no Worthy

Navegue até seu app no dashboard da Worthy, selecione o **Message Creator** e crie uma mensagem personalizada que deseja usar para engajamento com seus usuários.

### Etapa 2: Criar uma campanha no Braze

Crie uma [campanha de mensagens]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) no app com código personalizado no Braze e defina o **Tipo de mensagem** como **Código personalizado**.

### Etapa 3: Copie sua mensagem personalizada no Braze

No criador de mensagens Worthy, clique em **Exportar** e selecione **Braze** para exportar sua mensagem personalizada para uso em campanhas do Braze. Copie o conteúdo exportado para a caixa de texto HTML em **HTML + Asset Zip** no editor de campanhas do Braze.

É isso aí! Você pode testar imediatamente sua mensagem personalizada usando a guia **Testar** no editor de campanha do Braze. 


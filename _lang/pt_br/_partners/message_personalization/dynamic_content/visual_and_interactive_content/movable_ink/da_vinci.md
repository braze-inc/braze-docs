---
title: "Movable Ink Da Vinci"
article_title: Movable Ink Da Vinci
alias: "/partners/movable_ink_da_vinci/"
description: "A integração entre o Braze e a Movable Ink Da Vinci permite que as marcas forneçam envios de mensagens altamente personalizadas, aproveitando o mecanismo de decisão de conteúdo orientado por IA da Da Vinci. A Da Vinci faz a curadoria do conteúdo mais relevante para cada usuário e implementa as mensagens por meio do Braze."
page_type: partner
search_tag: Partner

---

# Movable Ink Da Vinci

> A integração entre o Braze e a Movable Ink [Da Vinci](https://movableink.com/da-vinci) permite que as marcas forneçam envios de mensagens altamente personalizadas, aproveitando o mecanismo de decisão de conteúdo orientado por IA da Da Vinci. A Da Vinci faz a curadoria do conteúdo mais relevante para cada usuário e implementa as mensagens por meio do Braze.

## Pré-requisitos

| Requisito | Descrição |
|------------|-------------|
| Movable Ink Da Vinci | É necessário ter uma conta Movable Ink Da Vinci para aproveitar essa parceria. |
| Braze Currents - Eventos de engajamento com mensagens | Uma exportação Braze Currents personalizada é necessária para enviar dados de eventos de engajamento com mensagem para o Movable Ink. |
| Chave da API REST do Braze | É necessária uma chave da API REST do Braze com as permissões `messages.send`, `sends.id.create` e `campaigns.details`. Isso pode ser criado no dashboard do Braze em **Configurações***> **Chaves de API**. <br><br>A equipe da sua conta Movable Ink fornecerá mais instruções de configuração diretamente. Consulte a seção [Integração](#integration).|
| Instância do app Da Vinci no Braze | Crie uma instância dedicada do app Da Vinci no Braze. Um novo aplicativo pode ser criado no dashboard do Braze acessando **Configurações** > **Configurações do aplicativo** > **\+ Adicionar aplicativo**. Nomeie o app como "**Movable Ink - Da Vinci**" e selecione qualquer plataforma (é necessário selecionar uma plataforma, mas o tipo não afeta a funcionalidade). Saiba mais sobre [como adicionar um novo app]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Para começar a usar a integração, entre em contato com a equipe da sua conta Movable Ink para obter assistência. A Movable Ink fornecerá acesso e instruções de configuração de acordo. Você precisará fornecer ao Movable Ink um conjunto de credenciais da API do Braze para ativar o Da Vinci para enviar implantações de e-mail por meio da API de envio de mensagens do Braze.

Quando conectado, o Movable Ink o fará:

- Trabalhar com o cliente e com o Braze para configurar a conta Da Vinci da marca para que ela seja implantada com sucesso no Braze.
- Capture configurações específicas da marca para alinhar-se aos seus casos de uso de envio de mensagens.
- Realizar testes abrangentes e garantia de qualidade para validar se os e-mails são entregues conforme o esperado e se atendem a todos os padrões operacionais e de performance.

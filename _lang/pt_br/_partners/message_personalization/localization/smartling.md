---
nav_title: Smartling
article_title: Smartling
description: "Este artigo de referência descreve a parceria entre a Braze e o Smartling, um software baseado em nuvem para localização. Essa integração permite traduzir modelos de e-mail e blocos de conteúdo na Braze."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [O Smartling][2] é um software de gerenciamento de tradução em nuvem de ponta a ponta para clientes que buscam automatizar a tradução de sites, aplicativos e experiências do cliente.

A integração da Braze com o Smartling permite que você traduza modelos de e-mail e blocos de conteúdo. O Smartling oferece aos linguistas o benefício do contexto visual durante a tradução, o que reduz os erros e mantém a qualidade.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Smartling | É necessário ter uma [conta Smartling][2] para aproveitar essa parceria. |
| Projeto de tradução Smartling | Para conectar sua conta da Braze com o Smartling, primeiro você deve se inscrever [criar um projeto de tradução][3]. |
| chave da API REST Braze | Uma chave da API REST do Braze com todas as permissões de modelos e blocos de conteúdo. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Seu URL do ponto de extremidade REST][1]. Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

A integração entre o Smartling e a Braze permite traduzir modelos de e-mail e blocos de conteúdo. 

Modelos de e-mail: 
* Somente os e-mails do editor de HTML são suportados. 
* Cada tradução será armazenada como seu próprio modelo de e-mail. 

Blocos de conteúdo: 
* Todos os blocos de conteúdo são suportados. 
* Os blocos de conteúdo contêm as versões original e traduzida.
* O script Liquid determina o idioma correto para exibição com base na preferência de idioma do destinatário.

### Etapa 1: Configurar o projeto Braze no Smartling TMS

#### Como conectar a Braze ao Smartling

1. No [Smartling][2], crie um tipo de projeto [Braze Connector][6] em sua conta do Smartling. 
  - Confirmar se todos os idiomas-alvo necessários foram adicionados ao projeto.
2. Nesse projeto, clique em **Settings** (Configurações) > **Braze Settings** (Configurações da Braze) > **Connect to Braze** (Conectar à Braze).
3. Insira seu URL da API da Braze e a chave da API da Braze.
4. Clique em **Salvar**.

#### Configuração completa do conector Braze

Consulte a [documentação][3] do Smartling para obter detalhes sobre a configuração do conector.

Selecione como você deseja automatizar as solicitações anteriores de tradução.

Configure os idiomas de origem e de alvo em **Language Configuration** (Configuração de idiomas). Ele será usado pelo conector para ingerir conteúdo no Smartling TMS e fornecer traduções de volta ao Braze.

![][8]

### Etapa 2: Enviar conteúdo para Smartling

Depois que o conector Braze tiver sido conectado e configurado, você encontrará o conteúdo do Braze na guia **Braze** em seu projeto Smartling. Consulte a [documentação][7] do Smartling para saber mais.

O Smartling oferece recursos avançados para pesquisar e selecionar conteúdo por:
* Pesquisa de palavras-chave
* Tipo de conteúdo de Braze
* Tags da Braze

![][9]

### Etapa 3: Adicionar traduções ao Braze

À medida que as traduções são concluídas na plataforma Smartling, elas são enviadas automaticamente para o Braze, sem a necessidade de sincronizar manualmente o conteúdo entre o Smartling e o Braze.

[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://help.smartling.com/hc/article_attachments/13946813331739
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}
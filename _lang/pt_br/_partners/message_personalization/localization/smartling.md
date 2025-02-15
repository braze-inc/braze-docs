---
nav_title: Smartling
article_title: Smartling
description: "Este artigo de referência descreve a parceria entre a Braze e o Smartling, um software baseado em nuvem para localização. O Braze Connector oferece suporte à tradução de modelos de e-mail HTML, blocos de conteúdo, canvas e mensagens de campanha de e-mail."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> o [Smartling][5] é um software de gerenciamento de tradução em nuvem de ponta a ponta para clientes que buscam automatizar a tradução de sites, aplicativos e experiências do cliente.

O Braze Connector oferece suporte à tradução de modelos de e-mail HTML, blocos de conteúdo, canvas e mensagens de campanha de e-mail. As traduções são solicitadas pela Smartling, e o conteúdo traduzido é enviado automaticamente para o Braze.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Smartling | É necessário ter uma [conta Smartling][2] para aproveitar essa parceria. |
| Projeto de tradução Smartling | Para conectar sua conta da Braze com o Smartling, primeiro você deve se inscrever [criar um projeto de tradução][6]. |
| chave da API REST Braze | Uma chave da API REST do Braze com todas as permissões de modelos e blocos de conteúdo. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.][1] Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A integração do Smartling Braze permite que você traduza modelos de e-mail em HTML, blocos de conteúdo, canvas e mensagens de e-mail de campanha. Note os seguintes detalhes, dependendo do que estiver traduzindo:

**Modelos de e-mail**
* Somente modelos de e-mail em HTML são suportados.
* Você precisará decidir como os e-mails traduzidos serão entregues ao Braze pelo conector:
  * **Um envio de e-mail para todos os idiomas:** O conector fornece todos os idiomas no mesmo e-mail que a fonte.
  * **Um envio de e-mail por idioma:** O conector cria um novo e-mail para cada idioma no Braze.

**Blocos de conteúdo**
* Todos os blocos de conteúdo são suportados.
* Os blocos de conteúdo contêm as versões original e traduzida.
* O script Liquid determina o idioma correto para exibição com base na preferência de idioma do destinatário.

**Campanhas e canvas**
* Certifique-se de ter adicionado seus idiomas de direcionamento nas **configurações de suporte multilíngue** do Braze.
* Consulte a [documentação do Smartling][3] para obter detalhes sobre a configuração do conector.

## Integração

### Etapa 1: Configurar o projeto Braze no Smartling TMS

#### Como conectar a Braze ao Smartling

1. No [Smartling][2], crie um tipo de projeto [Braze Connector][6] em sua conta do Smartling.
  - Confirme se todos os idiomas-alvo necessários foram adicionados ao projeto.
2. Nesse projeto, selecione **Configurações** > **Configurações do Braze** > **Conectar ao Braze**.
3. Insira seu URL da API da Braze e a chave da API da Braze.
4. Selecione **Salvar**.

#### Configuração completa do conector Braze

Consulte a [documentação][3] do Smartling para obter detalhes sobre a configuração do conector.

1. Selecione como você deseja automatizar as solicitações anteriores de tradução.
2. Configure os idiomas de origem e de alvo em **Language Configuration** (Configuração de idiomas). O conector o usará para ingerir conteúdo no Smartling TMS e fornecer traduções de volta ao Braze.

![Configuração do idioma do conector.][8]

### Etapa 2: Enviar conteúdo para Smartling

Depois que o conector Braze tiver sido conectado e configurado, você encontrará o conteúdo do Braze na guia **Braze** em seu projeto Smartling. Consulte a [documentação][7] do Smartling para saber mais.

O Smartling oferece recursos avançados para pesquisar e selecionar conteúdo por:

* Pesquisa de palavras-chave
* Tipo de conteúdo de Braze
* Tags da Braze

![Lista de blocos de conteúdo.][9]

### Etapa 3: Adicionar traduções ao Braze

À medida que as traduções são concluídas na plataforma Smartling, elas são enviadas automaticamente para o Braze, sem a necessidade de sincronizar manualmente o conteúdo entre o Smartling e o Braze.

[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://www.smartling.com/
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}
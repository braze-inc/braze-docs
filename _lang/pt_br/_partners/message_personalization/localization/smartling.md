---
nav_title: Smartling
article_title: Smartling
description: "Este artigo de referência descreve a parceria entre a Braze e o Smartling, um software baseado em nuvem para localização. "
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> 

 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Smartling | É necessário ter uma [conta Smartling][2] para aproveitar essa parceria. |
| Projeto de tradução Smartling |  |
| chave da API REST Braze | Uma chave da API REST do Braze com todas as permissões de modelos e blocos de conteúdo. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Seu URL do ponto de extremidade REST][1]. Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

 


* 
* 
  *  
  *  


* Todos os blocos de conteúdo são suportados.
* Os blocos de conteúdo contêm as versões original e traduzida.
* O script Liquid determina o idioma correto para exibição com base na preferência de idioma do destinatário.


* 
* 

## Integração

### Etapa 1: Configurar o projeto Braze no Smartling TMS

#### Como conectar a Braze ao Smartling

1. No [Smartling][2], crie um tipo de projeto [Braze Connector][6] em sua conta do Smartling.
  - 
2. 
3. Insira seu URL da API da Braze e a chave da API da Braze.
4. 

#### Configuração completa do conector Braze

Consulte a [documentação][3] do Smartling para obter detalhes sobre a configuração do conector.

1. Selecione como você deseja automatizar as solicitações anteriores de tradução.
2. Configure os idiomas de origem e de alvo em **Language Configuration** (Configuração de idiomas). 



### Etapa 2: Enviar conteúdo para Smartling

Depois que o conector Braze tiver sido conectado e configurado, você encontrará o conteúdo do Braze na guia **Braze** em seu projeto Smartling. Consulte a [documentação][7] do Smartling para saber mais.

O Smartling oferece recursos avançados para pesquisar e selecionar conteúdo por:

* Pesquisa de palavras-chave
* Tipo de conteúdo de Braze
* Tags da Braze



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
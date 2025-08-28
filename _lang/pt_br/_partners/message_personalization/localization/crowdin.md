---
nav_title: Crowdin
article_title: Crowdin
description: "Este artigo de referência descreve a parceria entre a Braze e o Crowdin, uma plataforma de software em nuvem que permite automatizar a tradução dos seus modelos de e-mail e blocos de conteúdo na Braze."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> O Crowdin é um software baseado em nuvem para gerenciamento de localização. Usando o Crowdin, você pode traduzir seus apps para Android e iOS, site, capturas de tela de lojas e outros tipos de conteúdo. A tradução pode ser feita por sua equipe interna, por uma agência de tradução ou usando máquinas de tradução automática.



## Sobre a integração

A integração entre a Braze e o Crowdin permite traduzir modelos de e-mail e blocos de conteúdo. Você também pode sincronizar o conteúdo da sua conta da Braze com um projeto do Crowdin e redirecionar as traduções para a Braze.

## Pré-requisitos

| Requisito| Descrição|
| ---| ---|
| Conta do Crowdin | É necessário ter uma [conta no Crowdin](https://accounts.crowdin.com/register) para aproveitar essa parceria. |
| Projeto de tradução do Crowdin | Para conectar sua conta da Braze ao Crowdin ou ao Crowdin Enterprise, primeiro será necessário se cadastrar e criar um projeto de tradução. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com todas as permissões de modelos e blocos de conteúdo. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint do SDK do Braze | Seu URL do endpoint do SDK dependerá do URL do Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integração

### Etapa 1: configure o app da Braze no Crowdin/Crowdin Enterprise

#### Crowdin
Para configurar o app da Braze no Crowdin, siga estas etapas:

1. Acesse o [app da Braze no marketplace](https://store.crowdin.com/braze-app).
2. Clique em **Install (Instalar** ) para adicioná-lo à sua conta.
3. Abra o projeto que você criou para a localização do conteúdo da Braze.
4. Acesse a guia **Configurações > Integrações**.
5. Na seção **Applications** (Aplicativos), clique no app da Braze.
6. Na caixa de diálogo, informe suas credenciais da Braze (chave da API REST da Braze e endpoint do SDK da Braze).
7. Clique em **Registrar-se com o Braze Connector**. 

#### Crowdin Enterprise
Para configurar o app da Braze no Crowdin Enterprise, siga estas etapas:

1. Acesse a página inicial do **Espaço de trabalho** > **Marketplace**.
2. Clique em **Install (Instalar** ) no app Braze para adicioná-lo à sua organização.
3. Abra o projeto que você criou para a localização do conteúdo da Braze.
4. Acesse **Aplicativos > Personalizado**.
5. Clique no app Braze.
6. Na caixa de diálogo, informe suas credenciais da Braze (chave da API REST da Braze e endpoint do SDK da Braze).
7. Clique em **Registrar-se com o Braze Connector**.

### Etapa 2: adicione seu conteúdo ao Crowdin/Crowdin Enterprise

Depois de fornecer suas credenciais da Braze, você verá dois painéis. Selecione o conteúdo desejado para sincronizar os arquivos para tradução da sua conta da Braze e clique em **Sync to Crowdin** (Sincronizar com Crowdin).

No modo Editor do Crowdin, o conteúdo sincronizado de sua conta Braze pode ser exibido para seus tradutores como uma lista de strings ou como uma prévia do arquivo.



### Etapa 3: Adicionar traduções ao Braze

Assim que as traduções forem concluídas, abra o app Braze no Crowdin, selecione os arquivos traduzidos (para cada arquivo, você pode escolher todos os idiomas de direcionamento ou apenas alguns específicos) no painel esquerdo e clique em **Sync to Braze**.





---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "Esse artigo de referência descreve a parceria entre o Braze e a Jacquard Dynamic Optimisation que utiliza o Braze Currents e o Connected Content para coletar informações de rastreamento de cliques de seus assinantes por meio de webhooks. Em seguida, a Jacquard vincula esses eventos às suas variantes de idioma para otimização do idioma em tempo real."
page_type: partner
search_tag: Partner
---

# Otimização dinâmica de jacquard

> [A Jacquard](https://www.jacquard.com/) reúne inteligência artificial, linguística computacional e um espírito de centralização no cliente para ajudar a implementar a linguagem da marca, em escala, em canais personalizados de acordo com a voz da sua marca.

A otimização dinâmica, com tecnologia Jacquard X, aproveita o Braze Currents e o Connected Content para coletar informações de rastreamento de cliques de seus assinantes por meio de webhooks. Em seguida, a Jacquard vincula esses eventos às suas variantes de idioma para otimização do idioma em tempo real. 

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Jacquard | É necessário ter uma [conta Jacquard](https://www.jacquard.com/) para aproveitar essa parceria. |
| Token do servidor de conexão da Jacquard | Uma longa string de caracteres que servirá como senha da sua campanha da Braze para acessar sua linguagem Jacquard.<br><br>Você pode solicitá-lo ao seu gerente de sucesso do cliente da Jacquard, caso ainda não o tenha recebido. |
| Currents | Para exportar dados para o Currents, é necessário que [o Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) esteja configurado em sua conta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Solicitar credenciais do Jacquard Amazon S3

Você precisará do Jacquard para configurar um bucket S3 dedicado da Amazon para receber os eventos de rastreamento de cliques do Braze. Entre em contato com seu gerente de sucesso do cliente da Jacquard para iniciar o processo. Quando o bucket for criado, você receberá credenciais exclusivas para criar seu Current. 

### Etapa 2: crie um Current

1. Na Braze, selecione **Currents > Criar nova integração com o Currents > Exportação de dados do Amazon S3**. 
2. Em seguida, dê um nome ao seu Current e insira um e-mail de contato.
3. Adicione seu ID da chave de acesso do Jacquard AWS e a chave de acesso secreta na caixa de credenciais. Depois adicione "phrasee-braze-currents-exports" como o nome do bucket S3 da AWS. 
4. Por fim, adicione a pasta do bucket S3 da AWS que você recebeu do gerente de sucesso do cliente da Jacquard. Provavelmente será o nome de sua empresa.
5. Em **General Settings (Configurações gerais**), marque a caixa "Include events from anonymous users" (Incluir eventos de usuários anônimos) e, em **Manage Engagement Events (Gerenciar eventos de engajamento** ), marque "Email Click" (Envio de e-mail).
6. Quando terminar, selecione **Abrir Current**.

### Etapa 3: Solicitação de remoção de informações de identificação pessoal (IPI).

Em seguida, entre em contato com a equipe da sua conta da Braze para garantir que nenhuma informação pessoal identificável seja transmitida à Jacquard.

Por padrão, o Current incluirá determinadas atribuições de IPI, como e-mail e endereço. A Jacquard não pode e não receberá IPI, portanto, é fundamental que você solicite à equipe da sua conta Braze que desative essa opção para todos os dados de eventos transmitidos à Jacquard.

### Etapa 4: snippets de código do Jacquard X 

Entre em contato com a equipe da sua conta da Jacquard para obter os snippets de código necessários.

Esses snippets usam o [conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) e, depois de serem colocados nos seus e-mails, extrairão dinamicamente o idioma e um pixel de rastreamento para que a Jacquard possa otimizar sua linguagem em tempo real usando o Jacquard X.



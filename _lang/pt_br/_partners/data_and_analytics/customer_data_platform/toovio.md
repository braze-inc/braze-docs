---
nav_title: Toovio
article_title: Toovio
description: "Este artigo de referência descreve a parceria entre o Braze e a Toovio, uma empresa de dados como serviço, que o ajuda a descobrir seus dados acionáveis e a usar os elementos mais importantes para gerar resultados incrementais com base em objetivos predefinidos."
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [A Toovio](https://toovio.com/) é uma empresa de dados como serviço alimentada por inteligência artificial que o ajuda a descobrir seus dados acionáveis e a usar os elementos mais importantes para gerar resultados incrementais com base em objetivos predefinidos.

_Essa integração é mantida pelo Toovio._

## Sobre a integração

A parceria entre a Braze e a Toovio proporciona o envio de mensagens quase em tempo real, as ferramentas para impulsionar o desempenho incremental e o acesso às ferramentas avançadas de medição de campanhas da Toovio.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Toovio | É necessário ter uma conta Toovio para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Braze Currents | O Braze Currents permite que os clientes da Braze enviem dados para um parceiro de dados da Braze (AWS S3, Google Cloud Storage ou Microsoft Azure Blob Storage) para processamento externo à plataforma Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

A integração a seguir permite que o Toovio gere disparos direcionados a clientes específicos e se comunique quase em tempo real. Os disparos determinados pela Toovio serão transmitidos à Braze pelo [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) da Braze.

### Etapa 1: definir parceiro de dados

Um local de entrega para o feed do Currents deve ser compartilhado com o Toovio; isso permite que o Toovio obtenha acesso e processe os dados de eventos e comportamento dos usuários.

### Etapa 2: configurar uma campanha disparada

Crie uma [campanha disparada pela API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) do Braze com base nos eventos do cliente que o Toovio direcionará. Além disso, devem ser definidos os valores e as atribuições do usuário-alvo que dispararão a campanha.

### Etapa 3: Configure sua conta Toovio

Entre em contato com a Toovio pelo e-mail [info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request) com o assunto "New Customer Request" para configurar uma conta. A Toovio trabalhará com os clientes para configurar disparadores e modelos subjacentes.



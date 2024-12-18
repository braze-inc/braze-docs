---
nav_title: Zeotap para Currents
article_title: Zeotap para Currents
description: "Este artigo de referência descreve a parceria entre Braze Currents e Zeotap, uma plataforma de dados do cliente de próxima geração que ajuda você a descobrir e entender seu público móvel, fornecendo resolução de identidade, insights e enriquecimento de dados."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap para Currents

> A [Zeotap](https://zeotap.com/) é uma plataforma de dados do cliente de última geração que ajuda você a descobrir e entender seu público móvel, fornecendo resolução de identidade, insights e enriquecimento de dados.

A integração Braze e Zeotap permite que você amplie a escala e o alcance de suas campanhas sincronizando os segmentos de clientes da Zeotap com os perfis de usuários da Braze. Com [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), você também pode conectar dados ao Zeotap para torná-los acionáveis em toda a growth stack.

{% alert important %}
O conector HTTP personalizado está atualmente em beta. Se você estiver interessado em configurar essa integração, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
|Conta Zeotap | É necessário ter uma [conta da Zeotap](https://zeotap.com/) para usar a parceria. |
| Currents | Para exportar dados de volta para Zeotap, você precisa ter [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) configurado para sua conta. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Implementação

### Etapa 1: Crie uma Currents fonte

1. No Zeotap, acessar **Fontes** em **Integrar**.
2. Selecione **Crie Fonte**.
3. Selecione **Canais de Engajamento do Cliente** como a categoria.<br><br>![Uma janela "Criar Fonte" listando diferentes categorias, incluindo "Canais de Engajamento do Cliente".][1]{: style="max-width:70%;"}<br><br>
4. Selecione **Braze** como a fonte de dados.
5. Digite um nome de fonte.
6. Selecione sua região.<br><br>![Janela com opções para selecionar sua região e entidade de dados.][6]{: style="max-width:70%;"}<br><br>
7. Selecione **Crie Fonte**.
8. Acessar a guia **Implementation Details** e anote a **API URL** e a **Write Key**.<br><br>![Detalhes de implementação para Braze Currents que contém a URL da API e a Chave de Escrita.][2]

### Etapa 2: Configure a transmissão de dados no Currents

1. No Braze, acesse **Integrações de Parceiros** > **Exportação de Dados**.
2. Selecione **Criar Novo Corrente** e **Exportar Correntes Personalizadas**.<br><br>![O botão "Criar Novo Corrente" com um menu suspenso que contém "Exportação de Correntes Personalizadas".][3]{: style="max-width:60%;"}<br><br>
3. Insira um nome de integração e e-mail para ser contatado se ocorrerem erros com a integração.
4. Sob **Credenciais**, insira as seguintes informações que você anotou de [etapa 1](#step-1-create-a-currents-source):
- A URL da API como o **Endpoint**
- A Chave de Escrita como o **Token de Portador**<br><br>![Seções para inserir detalhes de integração e credenciais.][4]<br><br>
5. Selecione os eventos de engajamento de mensagem que você deseja enviar para Zeotap.<br><br>![A guia "Configurações Gerais" com uma seção para selecionar eventos de engajamento com mensagem.][5]
6. Selecione **Iniciar Atual** para salvar as alterações e começar a enviar eventos para Zeotap.

{% alert important %}
O conector Currents não suporta usuários anônimos (usuários sem um `external_id`).
{% endalert %}

[1]: {% image_buster /assets/img/zeotap/cec.png %}
[2]: {% image_buster /assets/img/zeotap/implementation_details.png %}
[3]: {% image_buster /assets/img/zeotap/custom_currents_export.png %}
[4]: {% image_buster /assets/img/zeotap/credentials.png %}
[5]: {% image_buster /assets/img/zeotap/message_engagement_events.png %}
[6]: {% image_buster /assets/img/zeotap/select_region.png %}
---
nav_title: Contentful
article_title: Contentful
description: "Este artigo de referência descreve a parceria entre Braze e Contentful, um sistema de gerenciamento de conteúdo que permite usar dinamicamente o Conteúdo Conectado para extrair conteúdo do Contentful para suas campanhas Braze."
alias: /partners/contentful/
page_type: partner
search_tag: Partner
---

# Contentful

>[Contentful](https://www.contentful.com/) é um sistema de gerenciamento de conteúdo sem cabeça que permite criar, gerenciar e distribuir conteúdo para qualquer plataforma. Ao contrário de um sistema de gerenciamento de conteúdo (CMS), o Contentful permite que você crie seu modelo de conteúdo para que você possa decidir qual conteúdo deseja gerenciar.<br><br>Esta página fornece um guia passo a passo para configurar o Braze Connected Content para buscar dados da API de Entrega de Conteúdo do Contentful. 

Depois de estar integrado, você pode usar as APIs RESTful do Contentful para entregar seu conteúdo em vários canais, como sites, aplicativos móveis (iOS, Android e Windows) ou muitas outras plataformas. Você também pode puxar dinamicamente conteúdo do Contentful para usar em suas campanhas do Braze.

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito          | Descrição                        |
|-----------------------|------------------------------------|
| Uma conta Contentful | Você precisa de uma conta Contentful com acesso à API de Entrega de Conteúdo. |
| Uma conta Braze | Você precisa de uma conta Braze com acesso ao recurso de Conteúdo Conectado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Obtenha suas credenciais da API Contentful

1. [Registro em Contentful](https://app.contentful.com/login) com suas credenciais.
2. Crie ou recupere tokens de acesso da API no painel do Contentful acessando **Configurações** > **Chaves da API**. Se você ainda não tiver uma chave de API, crie uma nova:<br>2.1 Selecione **Adicionar chave de API**.<br>2.2 Insira os detalhes necessários e selecione o ambiente apropriado.<br>2.3 Selecione **Salvar** e anote o **ID do Espaço** e **token de acesso da API de Entrega de Conteúdo**.
3. Identifique o modelo de conteúdo que você deseja acessar através da API Contentful.

### Etapa 2: Configurar Braze Connected Content

1. [Registro em Braze](https://dashboard.braze.com/sign_in) com suas credenciais.
2. No painel do Braze, acesse **Modelos** > **Blocos de conteúdo** > **Criar bloco de conteúdo** > **Bloco de conteúdo HTML**.
3. Crie uma solicitação de Conteúdo Conectado para a URL da [API de Entrega de Conteúdo do Contentful](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links). Um exemplo de URL da API de Entrega de Conteúdo do Contentful é ```https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries```.<br><br> A recuperação de diferentes ativos requer a inclusão de variáveis específicas. A solicitação de URL de Conteúdo Conectado do exemplo tem como alvo o endpoint [Entry](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console) do Contentful. Este endpoint precisa de variáveis como `{space_id}` e `{environment_id}`, ou `{entry_id}` e `{access_token}`. Esses podem ser retirados da sua instância do Contentful. Neste exemplo de bloco de conteúdo, as variáveis devem ser substituídas pelo seu ID de Espaço Contentful e ID de Ambiente.<br><br>A URL de API de Entrega de Conteúdo de exemplo usa apenas um dos endpoints disponíveis do Contentful. Casos de uso diferentes podem ser alcançados aproveitando diferentes URLs. Por exemplo, a [Image API](https://www.contentful.com/developers/docs/references/images-api/) pode ser usada para capturar imagens armazenadas no Contentful. Para saber mais, revise [API de Entrega de Conteúdo](https://www.contentful.com/developers/docs/references/content-delivery-api/).

{% alert note %}
Diferentes endpoints podem exigir novas variáveis, por exemplo, a API de Imagens requer um `{asset_id}`, `{unique_id},` e `{name}`. Para mais orientações, entre em contato com o Contentful.
{% endalert %}

{% raw %}
```json
        {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
        {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
        {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
        {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
         {% connected_content https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}?access_token={access_token}
         :method get
         :headers {
             "Authorization": "YOUR_CONTENTFUL_ACCESS_TOKEN"
                 }
               :content_type application/json
               :save response %}
```
{% endraw %}

{: start="4"}
4\. Use "Test Endpoint" para testar se o Braze pode se conectar com sucesso à API do Contentful e recuperar os dados desejados.
5\. Selecione **Concluído** para salvar seu bloco de conteúdo.
6\. Dê ao seu bloco de conteúdo um nome descritivo, como "API Contentful", e então selecione **Iniciar Bloco de Conteúdo**.

### Etapa 3: Use Conteúdo Conectado em campanhas e Canvases

1. No Braze, crie uma nova campanha ou edite uma existente.
2. Use o bloco de conteúdo conectado para inserir dados buscados do Contentful. Use os caminhos de dados que você definiu durante a configuração para preencher dinamicamente o conteúdo da campanha.<br><br>
- **Jornada de resposta:** Após incluir o bloco de conteúdo em uma campanha Braze ou canva, a resposta se torna disponível quando você insere a variável `{response}` na sua mensagem.<br><br>A notação de ponto JSON permite que você especifique qual parte do corpo da resposta do Contentful deseja incluir em sua mensagem. Isso vai variar com base no seu caso de uso. Por exemplo, você pode usar o valor do título ({% raw %}```liquid{{response.items[0].fields.title}}```{% endraw %}) do endpoint de Entrada do Contentful e receber uma resposta como esta:

{% raw %}
```json
   {
  "fields": {
    "title": {
      "en-US": "Hello!"
    },
    "body": {
      "en-US": "This is a sample message!"
    }
  },
  "metadata": {
    "tags": [
      {
        "sys": {
          "type": "Link",
          "linkType": "Tag",
          "id": "nyCampaign"
        }
      }
    ]
  },
  "sys": {
    "id": "5KsDBWseXY6QegucYAoacS",
    "type": "Entry",
    "version": 1,
    "space": {
      "sys": {
        "type": "Link",
        "linkType": "Space",
        "id": "yadj1kx9rmg0"
      }
    },
    "contentType": {
      "sys": {
        "type": "Link",
        "linkType": "ContentType",
        "id": "hfM9RCJIk0wIm06WkEOQY"
      }
    },
    "createdAt": "2016-12-20T10:43:35.772Z",
    "updatedAt": "2016-12-20T10:43:35.772Z",
    "revision": 1
  }
}
```
{% endraw %}

{: start="3" }
3\. Prévia e teste sua campanha para confirmar que os dados do Conteúdo Conectado são exibidos corretamente.
4\. Depois que você estiver satisfeito com a configuração, lance sua campanha.

## Solução de problemas

### Resposta da API

Certifique-se de que suas credenciais da API do Contentful e a URL do endpoint estão corretas. Verifique se há mensagens de erro no Braze que possam indicar problemas com a chamada da API.

### Mapeamento de dados

Verifique se os mapeamentos de caminho da resposta estão configurados corretamente e se a estrutura da resposta da API corresponde às suas expectativas.

## Recursos adicionais

- [Documentação da API de Entrega de Conteúdo do Contentful](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Braze Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)
- [Braze Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)

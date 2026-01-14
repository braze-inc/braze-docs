---
nav_title: Criando uma transformação
article_title: Criando uma transformação
page_order: 1
page_type: reference
description: "Este artigo de referência fornece as etapas para criar uma transformação usando o Braze Data Transformation."
---

# Criando uma transformação

> O Braze Data Transformation permite que você crie e gerencie integrações de webhook para automatizar o fluxo de dados de plataformas externas para o Braze. Essas integrações de webhooks podem, então, potencializar casos de uso de marketing ainda mais sofisticados. Você pode criar sua transformação de dados a partir do código padrão ou usar nossa biblioteca de modelos dedicada para ajudá-lo a começar com determinadas plataformas externas.

## Pré-requisitos 

| Requisito | Descrição |
| --- | --- |
| Autenticação de dois fatores ou SSO | Você deve ter [a autenticação de dois fatores]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#two-factor-authentication) (2FA) ou o [logon único]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#single-sign-on-sso-authentication) (SSO) ativado para sua conta. |
| Permissões corretas | Você deve ser administrador da conta ou do espaço de trabalho, ou ter permissões de usuário "Manage Transformations" (Gerenciar transformações). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Etapa 1: Identificar uma plataforma de origem

Identifique uma plataforma externa que você deseja conectar ao Braze e verifique se ela é compatível com webhooks. Essas configurações às vezes são chamadas de "notificações de API" ou "solicitações de serviço da Web".

A seguir, um exemplo de [webhook do Typeform](https://www.typeform.com/help/a/webhooks-360029573471/), que pode ser configurado ao fazer login na plataforma:

\![]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## Etapa 2: Criar uma transformação

{% multi_lang_include create_transformation.md location="default" %}

## Etapa 3: Enviar um webhook de teste (recomendado)

Esta etapa é opcional, mas recomendamos o envio de um webhook de teste de sua plataforma de origem para a transformação recém-criada.

1. Copie o URL de sua transformação.
2. Em sua plataforma de origem, localize um recurso "Send Test" (Enviar teste) para que ele gere um webhook de amostra a ser enviado para essa URL. 
- Se sua plataforma de origem solicitar um tipo de solicitação, selecione **POST**.
- Se sua plataforma de origem fornecer opções de autenticação, selecione **Sem autenticação**.
- Se sua plataforma de origem solicitar segredos, selecione **No secrets (Sem segredos**).
3. Atualize sua página no painel do Braze para ver se o webhook foi recebido. Se ele foi recebido, você deverá ver uma carga de webhook em **Most recent webhook (Webhook mais recente**).

Esta é a aparência do Typeform:

Exemplo de código de transformação de dados que mapeia o webhook para os perfis de usuário do Braze.]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
A Braze Data Transformation pode ainda não oferecer suporte a plataformas externas que exijam verificação ou autenticação especial para webhooks. Considere deixar [um feedback sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) se você estiver interessado em usar esse tipo de plataforma com o Braze Data Transformation.
{% endalert %}

## Etapa 4: Escrever código de transformação

Se você tiver pouca ou nenhuma experiência com código JavaScript ou se preferir instruções mais detalhadas, siga o site **Beginner - POST: Rastrear usuários** ou **Iniciante - PUT: Atualize vários itens do catálogo** guia para escrever seu código de transformação.

Se você for um desenvolvedor ou tiver experiência significativa com código JavaScript, siga o endereço **Advanced - POST: Acompanhe os usuários na guia** para obter instruções de alto nível sobre como escrever seu código de transformação.

{% alert tip %}
O Braze Data Transformation tem um copiloto de IA que pede ao ChatGPT para ajudá-lo a escrever seu código. Para acessar o copiloto de IA, selecione <i class="fa-solid fa-wand-magic-sparkles"></i> **Generate transformation code (Gerar código de transformação**). Para usar isso, um webhook deve ser enviado para sua transformação. Você também pode acessar a biblioteca de modelos selecionando **Inserir código** > **Inserir modelo**.

\![]({% image_buster /assets/img/data_transformation/data_transformation3.png %})
{% endalert %}

{% tabs %}
{% tab Beginner - Track users %}

Aqui, escreva o código de transformação para definir como mapear vários valores de webhook para os perfis de usuário do Braze.

1. As novas transformações têm esse modelo padrão na seção **Código de transformação**:

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\. Para incluir atributos personalizados, eventos personalizados e compras em suas chamadas de transformação, pule para a etapa 3. Caso contrário, exclua as seções desnecessárias.<br><br>
3\. Cada atributo, evento e objeto de compra requer um identificador de usuário, seja um `external_id`, `user_alias`, `braze_id`, `email`, ou `phone`. Localize o identificador do usuário na carga útil do webhook de entrada e inclua esse valor no seu código de transformação por meio de uma linha de carga útil. Use a notação de ponto para acessar as propriedades do objeto de carga útil. <br><br>
4\. Encontre os valores do webhook que você gostaria de representar como atributos, eventos ou compras e modele esses valores em seu código de transformação por meio de uma linha de carga útil. Use a notação de ponto para acessar as propriedades do objeto de carga útil.<br><br>
5\. Para cada atributo, evento e objeto de compra, examine o valor `_update_existing_only`. Defina essa opção como `false` se quiser que a transformação crie um novo usuário que talvez não exista. Deixe essa opção em `true` para atualizar apenas os perfis existentes.<br><br>
6\. Clique em **Validate (Validar** ) para retornar uma visualização da saída do seu código e verificar se é uma solicitação `/users/track` aceitável.<br><br>
7\. Ative sua transformação. Para obter ajuda adicional com seu código antes de ativá-lo, entre em contato com seu gerente de conta Braze.<br><br>
7\. Faça com que sua plataforma de origem comece a enviar webhooks. Seu código de transformação será executado para cada webhook recebido, e os perfis de usuário começarão a ser atualizados. 

Sua integração com o webhook está concluída!

{% endtab %}
{% tab Beginner - Update catalog items %}

Aqui, você pode escrever um código de transformação para definir como deseja mapear vários valores de webhook para atualizações de itens do catálogo Braze.

1. As novas transformações incluirão esse modelo padrão na seção **Código de transformação**:

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",
  
  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\. As transformações para os destinos de `/catalogs` exigem que um `catalog_name` defina o catálogo específico a ser atualizado. Você pode codificar esse campo ou modelar o campo com um campo de webhook por meio de uma linha de carga útil. Use a notação de ponto para acessar as propriedades do objeto de carga útil.<br><br>
3\. Defina quais itens você gostaria de atualizar no catálogo com os campos `id` na matriz de itens. Você pode codificar esses campos ou criar um modelo em um campo de webhook por meio de uma linha de carga útil. <br><br> Lembre-se de que `catalog_column` é um valor de espaço reservado. Certifique-se de que os objetos de item contenham apenas campos existentes no catálogo.<br><br>
4\. Selecione **Validate (Validar** ) para retornar uma visualização da saída do seu código e verificar se é uma solicitação aceitável para o [ponto de extremidade Update multiple catalog items (Atualizar vários itens de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)).<br><br>
5\. Ative sua transformação. Para obter ajuda adicional com seu código antes de ativá-lo, entre em contato com seu gerente de conta Braze.<br><br>
6\. Certifique-se de verificar se sua plataforma de origem tem uma configuração para começar a enviar webhooks. Seu código de transformação será executado para cada webhook recebido, e os itens do catálogo começarão a ser atualizados.

Sua integração com o webhook está concluída!

{% endtab %}
{% tab Advanced - Track users %}

Nesta etapa, você transformará a carga útil do webhook da plataforma de origem em um valor de retorno de objeto JavaScript. Esse valor de retorno deve seguir o formato do corpo da solicitação do ponto de extremidade `/users/track`:

- O código de transformação é aceito na linguagem de programação JavaScript. Qualquer fluxo de controle JavaScript padrão, como a lógica if/else, é suportado.
- O código de transformação acessa o corpo da solicitação do webhook por meio da variável `payload`. Essa variável é um objeto preenchido pela análise do JSON do corpo da solicitação.
- Qualquer recurso suportado em nosso endpoint `/users/track` é suportado, inclusive:
  - Objetos de atributos de usuário, objetos de evento e objetos de compra
  - Atributos aninhados e propriedades de eventos personalizados aninhados
  - Atualizações do grupo de assinaturas
  - Endereço de e-mail como identificador

Selecione **Validate (Validar** ) para retornar uma visualização da saída do seu código e verificar se é uma solicitação `/users/track` aceitável.

{% alert note %}
No momento, não há suporte para solicitações de rede externa, bibliotecas de terceiros e webhooks que não sejam JSON.
{% endalert %}

{% endtab %}
{% endtabs %}

## Etapa 5: Monitore sua transformação

Depois de ativar sua transformação, consulte as análises na página principal de **Transformações** para obter um resumo do desempenho.

* **Solicitações recebidas:** Esse é o número de webhooks recebidos no URL dessa transformação. Se as solicitações de entrada forem 0, sua plataforma de origem não enviou nenhum webhook ou a conexão não pode ser feita.
* **Entregas:** Depois de receber as solicitações, o Data Transformation aplica seu código de transformação para enviar ao destino Braze selecionado.

É uma boa meta ter 100% das solicitações recebidas resultando em entregas. O número de entregas nunca excederá o número de solicitações recebidas.

### Solução de problemas

Para monitoramento e solução de problemas mais detalhados, consulte a página **Logs** para obter logs específicos, onde são registradas as últimas 1.000 solicitações de entrada para todas as transformações em seus espaços de trabalho. Você pode selecionar cada registro para visualizar o corpo da solicitação de entrada, a saída da transformação e o corpo da resposta do destino da transformação.

Se não houver entregas, verifique se há erros de sintaxe em seu código de transformação e confirme se o código está sendo compilado. Em seguida, verifique se a saída é uma solicitação de destino válida.

Entregas menores que o número de solicitações recebidas indicam que pelo menos alguns webhooks foram entregues com êxito. Consulte os registros de transformação para ver exemplos de erros e verifique se a saída da transformação é a esperada. É possível que seu código de transformação não esteja levando em conta todas as variações de webhooks recebidos.



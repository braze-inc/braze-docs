---
nav_title: Postman e Solicitações de Amostra
article_title: Postman e Solicitações de Amostra
page_order: 3
description: "Este artigo de referência fala sobre a coleção Postman, o que é, como configurar e usar a coleção, bem como como editar e enviar solicitações."
page_type: reference

---

# Postman e solicitações de amostra

> A Braze permite que você gere solicitações de API de amostra para todos os nossos endpoints por meio da Coleção Postman. Este artigo de referência fala sobre a coleção Postman, o que é, como configurar e usar a coleção, bem como como editar e enviar solicitações.

## O que é o Postman?

O Postman é uma ferramenta de edição visual gratuita para criar e testar solicitações de API. Ao contrário de outros métodos para interagir com APIs (por exemplo, usando cURL), o Postman permite que você edite facilmente as solicitações de API, visualize as informações do cabeçalho e muito mais. O Postman tem a capacidade de salvar Coleções ou bibliotecas de solicitações de API pré-fabricadas de amostra. Para facilitar que nossos clientes comecem a usar nossa API REST, criamos uma Coleção com exemplos prontos para todos os nossos endpoints de API.

Visualize ou baixe nossa Coleção do Postman clicando em **Executar no Postman** em nossos [documentos do Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) para começar.

## Como usar a coleção Postman da Braze

Se você tiver uma conta no Postman (você pode baixar as versões para MacOS, Windows e Linux do [site do Postman](https://www.getpostman.com)), você pode abrir nossa documentação do Postman no seu próprio app do Postman clicando no botão laranja **Executar no Postman**. Você pode então [criar um ambiente](#setting-up-your-postman-environment), ou usar nosso ambiente de API REST Braze como um modelo, e editar as `POST` e `GET` solicitações disponíveis para atender às suas próprias necessidades.

### Configurando seu ambiente Postman

{% raw %}
A Coleção Postman usa uma variável de modelo, `{{instance_url}}`, para substituir a URL da API REST da sua instância da Braze nas solicitações pré-construídas, e a variável `{{api_key}}` para sua chave de API. Em vez de ter que editar manualmente todas as solicitações na Coleção, você pode configurar essa variável no seu ambiente do Postman. Você pode selecionar nosso ambiente modelado (modelo de ambiente da API REST do Braze) no menu suspenso e substituir os valores das variáveis pelos seus próprios, ou você pode configurar seu próprio ambiente.
{% endraw %}

Para configurar seu próprio ambiente, execute as seguintes etapas:

1. Na guia **Workspaces**, selecione **Environments**.
2. Clique no botão de **+** para criar um novo ambiente.
3. Dê um nome a esse ambiente (por exemplo, "Braze API Requests") e adicione chaves para `instance_url` e `api_key` com valores correspondentes à sua [instância do Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) e à [chave da API REST do Braze]({{site.baseurl}}/api/api_key/).
4. Clique em **Salvar**.

{% alert note %}
Em `POST` corpos da solicitação, o `api_key` deve ser encapsulado em aspas: `"MY-API-KEY-EXAMPLE"`. Em `GET` URLs, não deveria ser. Já fornecemos esta formatação para você nos corpos da solicitação `POST` desta documentação, `GET` URLs e modelo de ambiente para `YOUR-API-KEY-HERE`.
{% endalert %}

![Adição de variáveis para chave de API e URL de instância ao ambiente da API REST do Braze no Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Usando as solicitações pré-construídas da coleção

Depois de configurar seu ambiente, você pode usar qualquer uma das solicitações pré-construídas na coleção como um modelo para criar novas solicitações de API. Para começar a usar uma das solicitações pré-construídas, clique nela no menu **Collections** do Postman. Isso abrirá a solicitação como uma nova guia na janela principal do app Postman.

Em geral, existem dois tipos de solicitações que os endpoints da API da Braze aceitam - `GET` e `POST`. Dependendo de qual `HTTP` método o endpoint usa, você precisará editar a solicitação pré-construída de forma diferente.

#### Editar uma solicitação POST

Ao editar uma `POST` solicitação, abra a solicitação e navegue até a seção **Corpo** no editor de solicitações. Para legibilidade, selecione o botão de rádio **raw** para formatar o corpo da solicitação `JSON`.

![Guia Corpo ao editar uma solicitação POST de rastreamento de usuário no Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Editar uma solicitação GET

Ao editar uma solicitação `GET`, edite os parâmetros passados no URL da solicitação. Para fazer isso, selecione a guia **Params** e edite os pares chave-valor nos campos que aparecem.

![Guia Params ao editar uma solicitação GET Query List of Unsubscribed Email Addresses no Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Envie sua solicitação

Depois que sua solicitação de API estiver pronta, clique em **Enviar**. A solicitação é enviada e os dados da resposta são preenchidos em uma seção abaixo do editor de solicitações. A partir daqui, você pode visualizar os dados brutos retornados da API da Braze, ver o código de resposta HTTP, ver quanto tempo a solicitação levou para processar e visualizar as informações do cabeçalho.

![Exemplo de dados de resposta do corpo de uma solicitação POST com status 201 Created e tempo de resposta de 269 milissegundos.]({% image_buster /assets/img_archive/postman_response.png %})


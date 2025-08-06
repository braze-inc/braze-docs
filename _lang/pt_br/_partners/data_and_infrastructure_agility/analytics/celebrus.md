---
nav_title: Celebrus
article_title: Integração do Celebrus
description: "Integração entre Braze e Celebrus."
---

# Celebrus

> A Celebrus se integra perfeitamente ao SDK da Braze nos canais de aplicativos móveis e da Web, facilitando o preenchimento da Braze com dados de atividade do canal. Isso inclui insights abrangentes sobre o tráfego de visitantes em ativos digitais durante períodos específicos. <br><br>Além disso, a Celebrus captura dados de perfil ricos para cada cliente individual, que podem ser sincronizados com a Braze. Isso permite criar estratégias eficazes de análise e comunicação da Braze com base em dados primários abrangentes, precisos e detalhados. Esse recurso é ainda mais reforçado pelos sinais orientados por machine learning da Celebrus, que permitem a captura de dados sem complicações e sem a necessidade de tag extensa. Com um robusto gráfico de identidade primário implementado, todos os dados se tornam instantaneamente acessíveis para uso imediato. 

_Esta integração é mantida pelo Celebrus._

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Celebrus | É necessário ter uma conta Celebrus para aproveitar essa parceria. |
| Data warehouse (opcional) | Ao usar o conector da Celebrus para atributos personalizados da Braze, você deve ter um data warehouse compatível com a integração da ingestão de dados para nuvem (CDI) da Braze e configurar a CDI no dashboard da Braze. |
| Definições de configuração do Braze SDK (opcional) | Ao usar o conector da Celebrus para o SDK da Braze, você deve passar o endpoint do SDK e a chave da API do SDK. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Implementação
Depois de instalar sua implementação da Celebrus, use os conectores da Celebrus para a Braze para integrar os dados da Celebrus à Braze. Há dois elementos na integração da Celebrus para a Braze: o SDK da Braze e os atributos personalizados da Braze. Você pode implantar um ou ambos, dependendo de como você usa a Braze e dos casos de uso de que precisa.

Se ainda não tiver o SDK da Braze implementado no seu canal da Web, você poderá usar a Celebrus para implantar o SDK da Braze. O Celebrus adicionará o SDK do Braze às páginas da Web e configurará a identidade do Braze para o visitante da Web usando o gráfico de identidade do Celebrus. Os atributos do cliente podem ser sincronizados com a Braze por meio de uma ingestão de dados na nuvem (CDI). Isso requer um data warehouse suportado pela CDI da Braze e a configuração da CDI na Braze.

### Conector Celebrus para Braze SDK

O conector da Celebrus para o SDK da Braze fornece dados de alto nível de canais de aplicativos móveis e da Web para a Braze. No SDK da Braze, o `System Identity` da Celebrus do gráfico de identidade da Celebrus será usado como o identificador para a integração da Braze. Outros identificadores são suportados para a sincronização de atributos personalizados por meio do conector Celebrus de atributos personalizados do Braze.

O conector implanta e configura o SDK da Braze no seu canal, então você precisará definir algumas configurações no fluxo de dados do SDK da Braze e fornecer os valores para estas três configurações:

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
O conector da Celebrus para o SDK da Braze inserirá e inicializará o SDK da Braze para identificar o usuário e adicionar o identificador ao gráfico de identidade da Celebrus. Esse conector não registrará dados do perfil do usuário nem disparará outros métodos do SDK da Braze. <br><br>Você pode chamar quaisquer métodos desejados diretamente na sua base de código para registrar dados por meio do [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) ou aproveitar outros recursos suportados pelo Braze SDK.
{% endalert%}

### Conector Celebrus para atributos personalizados Braze

#### Etapa 1: configure detalhes conectados na Celebrus 

O conector Celebrus para atributos personalizados do Braze envia atributos personalizados para um banco de dados intermediário, pré-formatado da maneira que o Braze espera recebê-lo. No Celebrus, você configura os detalhes da conexão para o banco de dados, o que dependerá do tipo de banco de dados que estiver usando (como Snowflake ou Redshift). 

#### Etapa 2: configure a ingestão de dados na nuvem no seu dashboard da Braze

Essa integração usa a ingestão de dados do Braze Cloud. Siga as instruções em [Integrações de data warehouse]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/) para definir as [configurações da ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) de acordo com o tipo de data warehouse usado. 

#### Etapa 3: Sincronização de dados do Celebrus para o Braze

A Celebrus captura e atribui identificadores exclusivos a um indivíduo, como e-mail, telefone, `external_id`ou alias de usuário, e os envia à Braze via CDI. Isso permite que os dados sejam sincronizados com a Braze para o mesmo indivíduo.

O Celebrus usará os identificadores definidos para enviar os atributos do cliente que estão definidos no construtor de perfil do Celebrus, mas somente quando os valores dos atributos forem alterados. Observe que os nomes dos atributos definidos no construtor de perfil do Celebrus serão usados no Braze por padrão. Portanto, certifique-se de atualizar esses nomes para aderir às [convenções de nomenclatura do Braze]({{site.baseurl}}/api/objects_filters/user_attributes_object/).

{% alert important %}
Por enquanto, esta versão não oferece suporte a eventos e compras.<br><br> Esta integração envia atribuições como valores de string, então alguns atributos são listas (como sinais). Por enquanto, as listas não podem ser convertidas em vetores. Não há atribuições aninhadas.
{% endalert%}


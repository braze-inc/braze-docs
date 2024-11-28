---
nav_title: Modelos de dados B2B
article_title: Criação de um modelo de dados B2B
page_order: 0
page_type: reference
description: "Saiba como usar as ferramentas de dados do Braze para criar modelos B2B."
---

# Criação de um modelo de dados B2B

> Esse caso de uso demonstra como você pode usar as ferramentas de dados do Braze para criar um modelo de dados B2B eficaz e eficiente que o ajude a direcionar, disparar, personalizar e enviar mensagens para seus usuários comerciais. 

{% alert note %}
Essas recomendações podem mudar com o tempo, à medida que o Braze desenvolve nossos recursos B2B.
{% endalert %}

Antes de falarmos sobre como configurar seu modelo de dados B2B, vamos abordar vários conceitos e termos que você deve conhecer.

Há quatro objetos principais de B2B que você precisa para executar campanhas de B2B.

| Objeto | Descrição |
| --- | --- |
| Leads | Um registro de clientes potenciais que demonstraram interesse em um produto ou serviço, mas ainda não foram qualificados como uma oportunidade. |
| Contatos | Normalmente, indivíduos que foram qualificados e convertidos de lead em contato para buscar uma oportunidade de vendas. |
| Oportunidades | Um registro que rastreia os detalhes de uma possível venda ou de um negócio em andamento
| Contas | Um registro de uma organização que é um cliente potencial qualificado, um cliente existente, um parceiro ou um concorrente que tem um relacionamento de importância semelhante. |
{: .reset-td-br-1 .reset-td-br-2 }

No Braze, esses quatro objetos são combinados e reduzidos a dois objetos: perfis de usuário e objetos de negócios.

| Objeto de Braze B2B | Descrição | Objetos B2B originais  |
| --- | --- | --- |
| Perfis de usuário | Eles são mapeados diretamente para leads e contatos em seu sistema CRM de vendas. Como os leads são capturados pelo Braze, eles são automaticamente criados como leads em seu sistema de CRM de vendas. À medida que são convertidos em contatos, os IDs e os detalhes dos contatos são sincronizados de volta ao Braze. |Leads<br> Contatos |
| Objetos de negócios | Eles mapeiam qualquer objeto não usuário no seu sistema CRM de vendas. Isso inclui seus objetos específicos de vendas, como objetos de conta e objetos de oportunidade. | Contas<br> Oportunidades |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Etapa 1: Crie seus business objects no Braze

Objetos de negócios são qualquer conjunto de dados não centrado no usuário. Em um contexto B2B, isso inclui os dados de contas e oportunidades e qualquer outro conjunto de dados pertinente não centrado no usuário que sua empresa rastreia.

Há dois métodos para criar e gerenciar seus objetos de negócios no Braze: catálogos e fontes conectadas. 

| Método | Descrição |
| --- | --- |
| [Catálogos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) | Esses são objetos de dados independentes (objetos de dados suplementares) no perfil do usuário principal no Braze. Em um contexto B2B, você provavelmente teria catálogos para suas contas e oportunidades. |
| [Fontes conectadas]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources/) | Isso permite que o Braze consulte diretamente seu data warehouse. É provável que você já esteja sincronizando regularmente seus objetos de lead, contato, oportunidade e conta com o data warehouse, de modo que possa apontar a segmentação do Braze diretamente para esse data warehouse e ativá-la em um ambiente de cópia zero. |
{: .reset-td-br-1 .reset-td-br-2 }

### Opção 1: Usar catálogos para contas e oportunidades

Os catálogos são tabelas de dados hospedadas e gerenciadas no Braze. Embora os dados de contas e oportunidades sejam originários do sistema de CRM de vendas de sua escolha, você os duplicaria no Braze para serem usados para fins de marketing: segmentação baseada em contas, marketing baseado em contas, gerenciamento de leads e muito mais.

Para essa opção, recomendamos criar um catálogo para suas contas e outro para suas oportunidades e atualizá-los com frequência enviando atualizações do Braze por meio de nossa [API de catálogos]({{site.baseurl}}/api/endpoints/catalogs/) ou da [CDI (Cloud Data Ingestion) de catálogos]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/). Ao criar esses catálogos, certifique-se de que a `id` (primeira coluna) de seu catálogo corresponda à `id` em seu sistema CRM de vendas.

#### Mapeie seus campos de CRM

As tabelas abaixo incluem alguns exemplos de campos que você pode mapear a partir dos objetos de conta e oportunidade do seu CRM.

{% tabs %}
{% tab Catálogo de contas %}

Nesse caso de uso, o Salesforce é o sistema de CRM de exemplo. Você pode mapear qualquer campo incluído nos objetos do seu CRM.

<table border="1">
  <tr>
    <th><b>Objeto de Braze</b></th>
    <th><b>Campo de Braze</b></th>
    <th><b>Objeto CRM (Salesforce)</b></th>
    <th><b>Campo de CRM (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">Catálogo > Catálogo de contas</td>
    <td><code>id</code></td>
    <td><code>account</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td><code>account</code></td>
    <td><code>Account Name</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>account</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>account</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
</table>

##### Exemplo de tabela de campos de conta mapeados

![Tabela de contas do Salesforce com as respectivas informações, como endereço de cobrança e proprietário da conta.]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endtab %}
{% tab Catálogo de oportunidades %}

Nesse caso de uso, o Salesforce é o sistema de CRM de exemplo. Você pode mapear qualquer campo incluído nos objetos do seu CRM.

<table border="1">
  <tr>
    <th><b>Objeto de Braze</b></th>
    <th><b>Campo de Braze</b></th>
    <th><b>Objeto CRM (Salesforce)</b></th>
    <th><b>Campo de CRM (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">Catálogo > Catálogo de oportunidades</td>
    <td><code>id</code></td>
    <td><code>opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territory</code></td>
    <td><code>opportunity</code></td>
    <td><code>Territory</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
</table>

##### Exemplo de tabela de campos de oportunidade mapeados

![Tabela de oportunidades do Salesforce com as respectivas informações, como endereço de cobrança e proprietário da conta.]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endtab %}
{% endtabs %}

### Opção 2: Usar fontes conectadas para contas e oportunidades

Fontes conectadas são tabelas de dados hospedadas por você em seu próprio data warehouse e consultadas pelos [segmentos do Braze CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/). Ao contrário dos catálogos, em vez de duplicar seus objetos de negócios (contas e oportunidades) no Braze, você os manteria em seu data warehouse e os usaria como a fonte da verdade.

Para configurar fontes conectadas, consulte [Integração de fontes conectadas]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources#integrating-connected-sources).

## Etapa 2: Relacione seus business objects aos perfis de usuário

Os perfis de usuário são o principal objeto no Braze, que alimenta a maior parte de sua segmentação demográfica, disparo e personalização. Os perfis de usuários incluem [dados de usuários padrão]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/) coletados por nosso SDK e outras fontes, incluindo [dados personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/), que assumem a forma de atributos (dados demográficos), eventos (dados comportamentais) ou compras (dados transacionais).

### Etapa 2.1: Mapear IDs de CRM de vendas para o Braze

Primeiro, certifique-se de que o Braze e o CRM de sua escolha tenham um identificador comum para compartilhar dados. Sugerimos usar a tabela a seguir para mapear os campos de ID do CRM de vendas de volta para o objeto de usuário Braze. A tabela abaixo tem o Salesforce como sistema de CRM, mas isso pode ser feito com qualquer CRM.

#### Objeto de Braze: Usuário

| Campo de Braze | Objeto CRM (Salesforce) | Campo de CRM (Salesforce) | Informações adicionais |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Liderança | `id` |  \- Etiqueta de alias de usuário: `salesforce_lead_id` <br>\- Nome do alias do usuário: `lead_id`|
| `Aliases.salesforce_contact_id` | Fale com | `id` | \- Etiqueta de alias de usuário: `salesforce_contact_id` <br>\- Nome do alias do usuário: `contact_id` |
| `AccountId` | Fale com | `AccountId` | 
| `OpportunityId` (opcional, escalar) <br>ou<br> `Opportunities` (opcional, matriz) | Oportunidade | `id` | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% alert note %}
Recomendamos o uso de [aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) em vez de `external_id` para mapear os identificadores de leads e contatos do Salesforce de volta ao Braze. Isso se deve ao fato de reduzir a quantidade de pesquisas necessárias ao identificar e executar suas iniciativas de estilo de crescimento lideradas por produtos.
{% endalert %}

Depois de sincronizar seus IDs, é necessário relacionar os perfis de usuário do Braze com seus objetos de negócios. 

### Etapa 2.2: Crie uma relação entre os perfis de usuário e seus business objects

#### Opção 1: Ao usar catálogos para business objects

Agora que os detalhes da oportunidade e da conta são contabilizados como catálogos do Braze, é necessário criar um relacionamento entre esses catálogos e os perfis de usuário para os quais você deseja enviar mensagens. Currents, isso requer duas etapas:

1. Inclua a conta (como `account_id (string)`), o ID da oportunidade (como `opportunity_ids (array)`) ou ambos no perfil do usuário como atribuições.
2. Registre um evento (como `account_linked`) que inclua o ID da conta como uma propriedade do evento.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

#### Opção 2: Ao usar fontes conectadas

Uma das tabelas da sua fonte conectada deve incluir um `user_id` que corresponda ao `external_user_id` definido no Braze para seus usuários. A configuração do perfil de usuário acima usa seu lead e `contact_ids` como seu `external_id`, portanto, você deve garantir que suas tabelas de lead/contato incluam esses IDs.

Além de garantir a correspondência dos IDs, recomendamos gravar dados básicos no nível da conta, como `account_id`, `opportunity_id` e até mesmo atribuições firmográficas comuns, como `industry`, nos perfis de usuários para uma segmentação e personalização eficientes.
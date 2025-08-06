---
nav_title: Mergulho
article_title: Análise de dados de mergulho
description: "Esta referência técnica do Scuba e da Braze descreve como ativar o insight de dados em tempo real do Scuba usando Braze Segments."
alias: /partners/scuba/
page_type: partner
search_tag: Partner
---

# Análise de dados de mergulho

>[O Scuba Analytics](https://scuba.io) é uma plataforma de colaboração de dados full-stack, com machine learning, projetada para dados de séries temporais de alta velocidade. O Scuba permite exportar usuários (também chamados de atores) de forma seletiva e carregá-los na plataforma Braze. No Scuba, as propriedades de atores personalizados são usadas para analisar tendências comportamentais, ativar seus dados em várias plataformas e realizar modelagem de previsão usando machine learning.

_Essa integração é mantida pela Scuba Analytics._

## Pré-requisitos

Para usar o Scuba Analytics com a Braze, você precisará do seguinte:

| Requisito | Descrição |
|---|---|
|Token da API do Scuba | Um token da API do Scuba que você pode recuperar do endpoint `https://{scuba_hostname}/api/create_token`. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância](https://scuba.io). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Como fazer upload de seus dados do Scuba para a Braze

{% alert important %}
A solicitação a seguir usa curl. Para um melhor gerenciamento de solicitações de API, recomendamos o uso de um cliente de API, como o Postman.
{% endalert %}

Para fazer upload de seus dados do Scuba para a Braze, faça uma solicitação POST para `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` usando o content-type `application/json`:

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

Substitua o seguinte:

| Espaço reservado             | Descrição                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | O URL do endpoint Braze REST de sua instância atual do Braze. Para saber mais, consulte [Chaves da API REST]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Sua chave da API REST do Braze com a permissão `users.track`.                                                                                                                                      |
| `HOSTNAME`              | O nome do host de sua instância atual do Scuba.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Seu token da API do Scuba.                                                                                                                                                                           |
| `TABLE_NAME`            | A tabela à qual seu conjunto de dados pertence. Para saber mais, consulte [Glossário: Tabela do conjunto de dados](https://docs.scuba.io/glossary/dataset-table).                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | A propriedade de ator à qual seu conjunto de dados pertence. Somente os dados correspondentes a esse nome serão retornados. Para saber mais, consulte [Glossário: Propriedade do ator](https://docs.scuba.io/glossary/actor-property).                                             |
| `ACTOR_PROPERTY_FILTER` | O filtro de pesquisa de público para sua propriedade de ator.                                                                                                                                             |
| `ACTOR_ID`              | A ID da propriedade do ator à qual seu conjunto de dados pertence. Esse ID corresponde ao seu `external_id` no Braze. Para saber mais, consulte [Glossário: Ator](https://docs.scuba.io/glossary/actor).                                              |
| `PERIOD_START`          | O período inicial como uma data compatível com BQL. Para saber mais, consulte [Sintaxe e uso do BQL](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                 |
| `PERIOD_END`            | O período final como uma data compatível com BQL. Para saber mais, consulte [Sintaxe e uso do BQL](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                   |
| `RECORD_LIMIT`          | **Opcional**: O número máximo de registros a serem retornados. Se `scuba_record_limit` for omitido, o Scuba retornará um máximo de 100 registros. Para alterar isso, atribua qualquer número não negativo para `scuba_record_limit`.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comportamento padrão

Por padrão, `update_existing_only` é definido como `false`, o que atualiza os registros existentes na Braze, bem como cria novos registros para aqueles que não existem. Para evitar que o Scuba crie novos registros, defina `update_existing_only` como `true`.

### Limite de taxa

O Scuba aplica um limite de frequência de 50.000 solicitações por minuto a esse endpoint.

## Criação de segmentos usando os dados comportamentais do Scuba

Depois de [fazer upload de seus dados](#uploading-your-scuba-data-to-braze), você pode criar segmentos de usuários na Braze usando os dados comportamentais do Scuba.

### Etapa 1: Criar um novo segmento

No Braze, acesse **Público** > **Segmentos** e, em seguida, selecione **Criar segmento** e digite um nome para seu segmento.

![Criando um novo segmento no Braze.]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### Etapa 2: Encontre e selecione a atribuição Scuba

Em **Segment Details** > **Filters** (Detalhes do segmento > Filtros), selecione **Custom Attributes** (Atributos personalizados).

![Selecionando o filtro "Atributo personalizado" em "Detalhes do segmento".]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

Selecione **Search custom attributes (Pesquisar atributos personalizados**) e, em seguida, escolha o nome da propriedade do ator que você usou na solicitação POST anterior.

![Selecionando a propriedade do ator como um atributo personalizado.]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### Etapa 3: Configurar a atribuição

Ao lado do nome da propriedade do ator, escolha um operador e um valor (se aplicável). Esses valores são determinados pelas propriedades do ator que você definiu no Scuba. Quando terminar, selecione **Salvar**.

![Escolha de um valor operacional e de um valor para o site ] selecionado ({% image_buster /assets/img/scuba/analytics/operator_end.png %})



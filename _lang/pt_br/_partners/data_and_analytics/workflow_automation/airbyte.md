---
nav_title: Airbyte
article_title: Airbyte
description: "Este artigo de referência aborda a integração entre a Braze e o Airbyte. O Airbyte é um mecanismo de integração de dados de código aberto que ajuda você a consolidar os dados em data warehouses, lakes e bancos de dados, encaminhando eventos em tempo real do Airbyte para a Braze."
alias: /partners/airbyte/
page_type: partner
search_tag: Airbyte

---

# Airbyte

> O [Airbyte](https://airbyte.com/) é um mecanismo de integração de dados de código aberto que ajuda a consolidar os dados em data warehouses, lakes e bancos de dados.

_Essa integração é mantida pela Airbyte._

## Sobre a integração

A integração Braze e Airbyte permite que os usuários criem um pipeline de dados para coletar e analisar dados do Braze, conectando todos os seus aplicativos e bancos de dados a um data warehouse central. Depois que os dados são coletados no data warehouse central, as equipes de dados podem explorar os dados da Braze de forma eficaz usando suas ferramentas de business intelligence preferidas.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Airbyte Cloud | É necessário ter uma conta [Airbyte Cloud](https://cloud.airbyte.io/workspaces) para usar a integração. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com todas as permissões. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST  do Braze | Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

1. Em sua conta Airbyte Cloud, navegue até **Sources > + New Source > Set up the Source** (Fontes > + Nova fonte > Configurar fonte).
2. Digite "Braze" como o nome da fonte e selecione **Braze** na lista suspensa de fontes.
3. Forneça o URL de seu endpoint, a chave da API REST da Braze e a data de início. Clique em **Set up Source** (Configurar fonte).

### Modos de sincronização suportados

O conector de fonte Braze da Airbyte é compatível com os seguintes [modos de sincronização](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):
- **Full Refresh | Overwrite** (Recarregamento completo | Sobrescrever): sincroniza todos os registros da fonte e substitui os dados no destino ao sobrescrevê-los.
- **Incremental Sync | Append** (Sincronização incremental | Acrescentar): Sincronize novos registros da origem e adicione-os ao destino sem excluir nenhum dado.

### Fluxos suportados

- [`campaigns`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18)
- [`campaigns_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1)
- [`canvases`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1)
- [`canvases_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73)
- [`events`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1)
- [`events_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c)
- [`kpi_daily_new_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01)
- [`kpi_daily_active_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986)
- [`kpi_daily_app_uninstalls`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae)
- [`cards`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e)
- [`cards_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8)
- [`segments`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f)
- [`segments_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e)

{% alert note %}
Os limites de frequência variam de acordo com o fluxo. Acesse a [tabela de limites de frequência]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type) para saber mais.
{% endalert %}

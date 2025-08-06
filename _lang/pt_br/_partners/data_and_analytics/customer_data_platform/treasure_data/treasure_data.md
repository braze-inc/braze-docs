---
nav_title: Treasure Data
article_title: Treasure Data
description: "Este artigo de referência descreve a parceria entre a Braze e o Treasure Data, uma plataforma de dados do cliente que permite escrever os resultados do trabalho diretamente na Braze."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# Treasure Data

> [O Treasure Data](https://www.treasuredata.com/) é uma plataforma de dados do cliente (CDP) que coleta e encaminha informações de várias fontes para uma variedade de outros locais em sua pilha de marketing.

A integração entre a Braze e o Treasure Data permite escrever os resultados do trabalho da Treasure Data diretamente na Braze. Dessa forma, é possível:
* **Mapear IDs externas**: Mapeie os IDs para a conta de usuário do Braze a partir do seu sistema CRM. 
* **Gerenciar cancelamentos de inscrição**: Quando um usuário final atualiza seu consentimento, optando por não participar.
* **Fazer upload de seu rastreamento de eventos, compras ou atributos personalizados de perfil**. Essas informações podem ajudá-lo a criar segmentos de clientes precisos que melhoram a experiência do usuário em suas campanhas.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta do Treasure Data | É necessário ter uma [conta do Treasure Data](https://www.treasuredata.com/custom-demo/) para usar a parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com as permissões `users.track`, `users.delete`, `users.alias.new` e `users.identify`.<br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá da [Braze URL para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Casos de uso

Você pode sincronizar seus perfis de clientes consolidados do Treasure Data na Braze para criar segmentos de direcionamento. O Treasure Data é compatível com dados primários de cookies, IDs móveis, sistemas de terceiros (como seu CRM) e muitos outros.

## Integração

### Etapa 1: Criar uma nova conexão

No Treasure Data, navegue até **Catalog** (Catálogo) no **Integrations Hub** (Hub de integrações), pesquise e selecione **Braze**. 

No prompt **New Authentication** (Nova autenticação) exibido, dê um nome à sua conexão e forneça a chave da API REST e o endpoint REST da Braze. Selecione **Done** (Concluído) quando terminar.

![]({% image_buster /assets/img/treasure_data/braze_authentication.png %}){: style="max-width:80%;"}

### Etapa 2: defina sua consulta

No Treasure Data, navegue até **Queries** (Consultas) no **Data Workbench** (Workbench de dados) e selecione uma consulta para a qual você gostaria de exportar dados. Execute essa consulta para validar o conjunto de resultados.

{% alert note %}
Para os usuários que usam o HIVE para criar consultas, o HIVE exige que todas as colunas ou tabelas que comecem com um sublinhado sejam envolvidas por aspas. Por exemplo, `_merge_objects`.
{% endalert %}

Em seguida, selecione **Export Results** (Exportar resultados) e selecione uma autenticação de integração existente.

![]({% image_buster /assets/img/treasure_data/query_2.png %}){: style="max-width:80%;"}

Defina parâmetros adicionais de resultados de exportação, conforme descrito na [seção de personalização](#customization) a seguir. No seu conteúdo de integração de exportação, revise os parâmetros de integração.

![A página "Export Results" (Exportar resultados). Nessa página, há campos para "mode", "track record type" e "pre-formatted fields" ("modo", "tipo de registro de rastreamento" e "campos pré-formatados"). Para este exemplo, "User-Track" e "Custom Events" estão definidos para esses campos, respectivamente.]({% image_buster /assets/img/treasure_data/braze_export_configuration.png %}){: style="max-width:80%;"}

Por fim, selecione **Done** (Concluído), execute sua consulta e valide se seus dados foram movidos para a Braze.

### Personalização

Os parâmetros dos resultados da exportação estão incluídos na tabela a seguir:

| Parâmetro                 | Valores | Descrição |
|---------------------------|---|---|
| `mode`                    | Usuário - Novo alias<br>Usuário - Identificação<br>Usuário - Rastreamento<br>Usuário - Excluir | Modo conector |
| `pre_formatted_fields`    | String | Use para colunas de matriz ou JSON para manter o formato. |
| `track_record_type`       | Eventos personalizados<br>Compras<br>Atribuições do perfil do usuário| Tipo de registro para o modo **Usuário - Rastreamento**  |
| `skip_on_invalid_records` | Booleano | Se ativada, continue e ignore quaisquer registros inválidos para a coluna JSON. <br> Caso contrário, o trabalho será interrompido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Visite [Treasure Data](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration) para saber mais sobre campos pré-formatados, exemplos de consultas, detalhes de parâmetros e agendamento de tarefas de exportação de consultas.
{% endalert %}

## Webhooks

Os usuários do Treasure Data podem ingerir dados por meio da API REST pública. Você pode usar o Treasure Data para criar webhooks personalizados para seus dados. Para saber mais, visite [Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API)


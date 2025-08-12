---
nav_title: "Atribuições do perfil do usuário"
article_title: Visualizações de atribuição de usuário no Snowflake 
page_order: 10
page_type: partner
search_tag: Partner
---

# Atribuições padrão do perfil de usuário

> Esta página serve como referência para as visualizações de atribuição padrão no Snowflake. Há três exibições, cada uma projetada para um caso de uso específico com suas próprias considerações de performance.

{% alert important %}
Os atributos de perfil de usuário estão atualmente em versão beta para os clientes do Snowflake Data Sharing. Se estiver usando o Snowflake Data Sharing e quiser ter acesso a essa versão beta, entre em contato com o gerente de sucesso do cliente ou com o suporte da Braze.
{% endalert %}

## Visualizações disponíveis

- `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`  
- `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

Essa visualização fornece um instantâneo periódico das atribuições padrão do perfil do usuário. Os dados são postergados em até 8 horas, o que os torna úteis para consultas que não exigem atualizações em tempo real.

#### Esquema

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | NÚMERO        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Notas de uso

* Fornece um instantâneo das atribuições do usuário com uma **postergação** de até **8 horas**.
* Apresenta bom desempenho para consultas que não exigem precisão em tempo real.
* Execução mais rápida da consulta, especialmente ao filtrar por atribuições diferentes de `USER_ID`.
* **Limitação:** Os dados não são atualizados em tempo real.

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`

Essa visualização fornece atualizações quase em tempo real sobre as atribuições do perfil do usuário, com postergação de dados de até 10 minutos após a ocorrência de uma atualização no Braze.

#### Esquema

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | NÚMERO        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Notas de uso

* Fornece atribuições atualizadas do usuário com postergação mínima (~10 minutos).
* Útil para análises em tempo real e cenários em que são necessários dados recentes.
* **Considerações sobre a performance:**
    * As consultas sobre usuários individuais são mais rápidas (menos de um minuto usando um grande depósito).
    * As consultas sem filtros USER_ID exigem agregação em todos os usuários, o que leva a tempos de execução significativamente mais longos.
    * As consultas em um grande conjunto de dados (como mais de 100 milhões de usuários) podem levar muitos minutos.

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`

Essa visualização armazena registros históricos de alterações de atribuições do usuário, capturando alterações com granularidade de 8 horas.

#### Esquema

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | NÚMERO        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
| `EFF_DT`        | TIMESTAMP_NTZ |
| `END_DT`        | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Notas de uso

* Fornece um registro de alterações históricas nas atribuições do usuário.
* Os dados são capturados a cada oito horas, o que significa que várias atualizações nessa janela são combinadas em um único registro. As alterações individuais dentro desse período não são mantidas separadamente.
* `EFF_DT` e `END_DT` marcam o início e o fim do estado de atribuição de um usuário.

## Melhores práticas

### Uso recomendado da consulta

| Caso de uso                                               | Visualização recomendada                                   | Notas                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Consultas gerais** que não requerem atualizações recentes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`              | Execução rápida, com dados de até 8 horas.                          |
| Consultas que exigem as **atribuições mais recentes do usuário**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` | Fornece atualizações quase em tempo real, mas pode ser mais lento para grandes conjuntos de dados. |
| **Rastreamento histórico** de alterações de atribuições           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Armazena alterações de atribuições com granularidade de 8 horas.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

### Considerações sobre performance

* As consultas em `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` devem retornar em menos de 10 segundos para grandes conjuntos de dados (~1 bilhão de usuários) em um grande armazém.
* As consultas em `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` para um único usuário retornam em menos de um minuto, mas são mal dimensionadas sem a filtragem `USER_ID`.
* Consultas sobre mais de 100 milhões de usuários em `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` podem levar vários minutos devido à agregação por usuário.



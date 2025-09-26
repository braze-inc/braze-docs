---
nav_title: "Atribuições do perfil do usuário"
article_title: Visualizações de atribuição de usuário no Snowflake 
page_order: 10
page_type: partner
search_tag: Partner
---

# Atribuições do perfil do usuário

> Esta página serve como referência para as visualizações de atributos padrão e personalizados no Snowflake. Há três visualizações para atributos padrão e três visualizações para atributos personalizados, cada uma projetada para um caso de uso específico com suas próprias considerações de performance.

{% alert important %}
Os atributos de perfil de usuário estão atualmente em versão beta para os clientes do Snowflake Data Sharing. Se estiver usando o Snowflake Data Sharing e quiser ter acesso a essa versão beta, entre em contato com o gerente de sucesso do cliente ou com o suporte da Braze.
{% endalert %}

# Visualizações disponíveis

<table>
  <thead>
    <tr>
      <th>Tipo</th>
      <th>Visualização</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Atributo padrão</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantâneos do perfil do usuário</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Perfis de usuário em tempo real</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Registros históricos de alterações</td>
    </tr>
    <tr>
      <td rowspan="3">Atributo personalizado</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantâneos do perfil do usuário</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Perfis de usuário em tempo real</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Registros históricos de alterações</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Instantâneos do perfil do usuário

Essas exibições fornecem instantâneos periódicos das atribuições do perfil do usuário. Os dados são postergados em até 12 horas, o que os torna úteis para consultas que não exigem atualizações em tempo real. 

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`  

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

#### Esquema

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NÚMERO |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

#### Esquema

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NÚMERO |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIÁVEL |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}  

### Instantâneos do perfil do usuário - notas de uso

* Fornece um instantâneo das atribuições do usuário com uma **postergação** de até **12 horas**.
* Apresenta bom desempenho para consultas que não exigem precisão em tempo real.
* Execução mais rápida da consulta, especialmente ao filtrar por atribuições diferentes de `USER_ID`.
* **Limitação:** Os dados não são atualizados em tempo real.

## Visualizações de perfil de usuário em tempo real

Essas exibições fornecem atualizações quase em tempo real sobre as atribuições do perfil do usuário, com postergação de dados de até 10 minutos após a ocorrência de uma atualização no Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` 

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
#### Esquema

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NÚMERO |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`
#### Esquema

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NÚMERO |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJETO |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### Visualizações do perfil do usuário em tempo real - notas de uso

* Fornece atribuições atualizadas do usuário com postergação mínima (~10 minutos).
* Útil para análises em tempo real e cenários em que são necessários dados recentes.
* **Considerações sobre a performance:**
    * As consultas sobre usuários individuais são mais rápidas (menos de um minuto usando um grande depósito).
    * As consultas sem filtros USER_ID exigem agregação em todos os usuários, o que leva a tempos de execução significativamente mais longos.
    * As consultas em um grande conjunto de dados (como mais de 100 milhões de usuários) podem levar muitos minutos.

## Registros históricos de alterações

Essas exibições armazenam registros históricos de alterações de atribuições do usuário, capturando alterações com granularidade de 12 horas.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### Esquema

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NÚMERO |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### Esquema

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NÚMERO |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIÁVEL |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### Registros históricos de alterações - notas de uso

* Fornece um registro de alterações históricas nas atribuições do usuário.
* Os dados são capturados a cada 12 horas, o que significa que várias atualizações nessa janela são combinadas em um único registro. As alterações individuais dentro desse período não são mantidas separadamente.
* `EFF_DT` e `END_DT` marcam o início e o fim do estado de atribuição de um usuário.

# Melhores práticas

## Uso recomendado da consulta

| Caso de uso                                               | Visualizações recomendadas                                   | Notas                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Consultas gerais** que não requerem atualizações recentes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` e `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Execução rápida, com dados de até 12 horas.                          |
| Consultas que exigem as **atribuições mais recentes do usuário**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` e `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Fornece atualizações quase em tempo real, mas pode ser mais lento para grandes conjuntos de dados. |
| **Rastreamento histórico** de alterações de atribuições           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` e `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Armazena alterações de atribuições com granularidade de 12 horas.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

## Considerações sobre performance

* As consultas em `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` devem retornar em menos de 10 segundos para grandes conjuntos de dados (~1 bilhão de usuários) em um grande armazém.
* As consultas em `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` para um único usuário retornam em menos de um minuto, mas são mal dimensionadas sem a filtragem `USER_ID`.
* Consultas sobre mais de 100 milhões de usuários em `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` podem levar vários minutos devido à agregação por usuário.



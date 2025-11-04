---
nav_title: "Atributos del perfil de usuario"
article_title: Vistas de atributos de usuario en Snowflake 
page_order: 10
page_type: partner
search_tag: Partner
---

# Atributos del perfil de usuario

> Esta página sirve de referencia para las vistas de atributos predeterminados y personalizados en Snowflake. Hay tres vistas para atributos predeterminados y tres vistas para atributos personalizados, cada una diseñada para un caso de uso específico con sus propias consideraciones de rendimiento.

{% alert important %}
Los atributos de perfil de usuario están actualmente en fase beta para los clientes de Snowflake Data Sharing. Si utilizas Snowflake Data Sharing y deseas acceder a esta versión beta, ponte en contacto con tu administrador del éxito del cliente o con el soporte de Braze.
{% endalert %}

# Vistas disponibles

<table>
  <thead>
    <tr>
      <th>Tipo</th>
      <th>Visualizar</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Atributo predeterminado</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantáneas del perfil de usuario</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Perfiles de usuario en tiempo real</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historial de cambios</td>
    </tr>
    <tr>
      <td rowspan="3">Atributo personalizado</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantáneas del perfil de usuario</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Perfiles de usuario en tiempo real</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historial de cambios</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Instantáneas del perfil de usuario

Estas vistas proporcionan instantáneas periódicas de los atributos del perfil de usuario. Los datos se retrasan hasta 12 horas, por lo que resulta útil para consultas que no requieren actualizaciones en tiempo real. 

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`  

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

#### Esquema

| Nombre de columna     | Tipo de datos     |
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

| Nombre de columna     | Tipo de datos     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NÚMERO |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANTE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}  

### Instantáneas del perfil de usuario - notas de uso

* Proporciona una instantánea de los atributos del usuario con un **retraso de hasta 12 horas**.
* Funciona bien para consultas que no requieren precisión en tiempo real.
* Ejecución más rápida de la consulta, sobre todo al filtrar por atributos distintos de `USER_ID`.
* **Limitación:** Los datos no están actualizados en tiempo real.

## Vistas del perfil de usuario en tiempo real

Estas vistas proporcionan actualizaciones casi en tiempo real de los atributos del perfil de usuario, con datos retrasados hasta 10 minutos después de que se produzca una actualización en Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` 

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
#### Esquema

| Nombre de columna     | Tipo de datos     |
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

| Nombre de columna     | Tipo de datos     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NÚMERO |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJETO |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### Vistas del perfil de usuario en tiempo real - notas de uso

* Proporciona atributos de usuario actualizados con un retraso mínimo (~10 minutos).
* Útil para análisis en tiempo real y situaciones en las que se necesitan datos recientes.
* **Consideraciones sobre el rendimiento:**
    * Las consultas a usuarios individuales son más rápidas (menos de un minuto utilizando un almacén grande).
    * Las consultas sin filtrar el USER_ID requieren la agregación de todos los usuarios, lo que conlleva tiempos de ejecución significativamente mayores.
    * Las consultas en un gran conjunto de datos (como más de 100 millones de usuarios) pueden tardar muchos minutos.

## Historial de cambios

Estas vistas almacenan registros de cambios históricos de los atributos de los usuarios, capturando los cambios con una granularidad de 12 horas.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### Esquema

| Nombre de columna     | Tipo de datos     |
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

| Nombre de columna     | Tipo de datos     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NÚMERO |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANTE |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### Historial de cambios - notas de uso

* Proporciona un registro de los cambios históricos en los atributos de los usuarios.
* Los datos se instantaneizan cada 12 horas, lo que significa que varias actualizaciones en esta ventana se combinan en un único registro. Los cambios individuales dentro de este periodo no se conservan por separado.
* `EFF_DT` y `END_DT` marcan el inicio y el final del estado de atributo de un usuario.

# Buenas prácticas

## Uso recomendado de la consulta

| Casos de uso                                               | Vistas recomendadas                                   | Notas                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Consultas generales** que no requieren actualizaciones recientes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` y `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Ejecución rápida, con datos de hasta 12 horas de antigüedad.                          |
| Consultas que requieren los **últimos atributos del usuario**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` y `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Proporciona actualizaciones casi en tiempo real, pero puede ser más lento para grandes conjuntos de datos. |
| **Seguimiento histórico** de los cambios de atributos           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` y `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Almacena los cambios de atributo con una granularidad de 12 horas.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

## Consideraciones sobre el rendimiento

* Las consultas en `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` o `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` deberían dar resultados en menos de 10 segundos para grandes conjuntos de datos (~1.000 millones de usuarios) en un gran almacén.
* Las consultas en `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` o `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` para un solo usuario se devuelven en menos de un minuto, pero se escalan mal sin filtrar `USER_ID`.
* Las consultas sobre más de 100 millones de usuarios en `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` o `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` pueden tardar varios minutos debido a la agregación por usuario.



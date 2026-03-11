---
nav_title: importação de CSV
article_title: "importação de CSV"
description: "Aprenda a gravar e atualizar atributos de usuário e eventos personalizados usando importação CSV."
page_order: 1.2
---

# importação de CSV

> Aprenda a gravar e atualizar atributos de usuário e eventos personalizados usando importação CSV.

## Sobre a importação CSV

Você pode usar a importação CSV para gravar e atualizar os seguintes atributos de usuário e eventos personalizados.

|Tipo|Definição|Exemplo|Tamanho máximo do arquivo|
|---|---|---|---|
|Atributos padrão|Atributos de usuário reservados reconhecidos pelo Braze.|`first_name`, `email`|500 MB|
|Atributos personalizados|Atributos de usuário exclusivos para o seu negócio.|`last_destination_searched`|500 MB|
|Eventos personalizados|Eventos exclusivos para o seu negócio que representam ações do usuário.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Usando a importação CSV

### Etapa 1: Baixar um modelo CSV

Para abrir a importação CSV, acesse **Audiências** > **Importar Usuários**. Aqui, você encontrará uma tabela que lista detalhes sobre as importações mais recentes, como a data de upload, nome do uploader, nome do arquivo, disponibilidade de direcionamento, número de linhas importadas e status da importação.

Para começar com seu CSV, baixe um modelo para atributos ou eventos.

![A página "Importar usuários" no dashboard do Braze.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Etapa 2: Escolha um identificador {#choose-an-identifier}

O CSV que você importar precisará de um identificador dedicado. Você pode escolher entre os seguintes:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Ao importar seus dados de cliente, você pode usar um `external_id` para servir como o identificador exclusivo de cada cliente. Quando você fornece um `external_id` em sua importação, o Braze atualiza qualquer usuário existente com o mesmo `external_id` ou cria um novo usuário identificado com esse `external_id` definido, se um não for encontrado.

- Baixar: [Modelo de Importação de Atributos CSV: ID Externo]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Baixar: [Modelo de Importação de Eventos CSV: ID Externo](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Se você estiver fazendo upload de uma mistura de usuários com um `external_id` e usuários sem, você precisa criar um CSV para cada importação. Um CSV não pode conter tanto `external_ids` quanto apelidos de usuário.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Para direcionar usuários que não têm um `external_id`, você pode importar uma lista de usuários com apelidos de usuário. Um apelido serve como um identificador único alternativo de usuário e pode ser útil se você estiver tentando fazer marketing para usuários anônimos que não se inscreveram ou criaram uma conta com seu app.

Se você estiver carregando ou atualizando perfis de usuário que são apenas alias, você deve ter as seguintes duas colunas em seu CSV:

- `user_alias_name`: Um identificador único de usuário; uma alternativa ao `external_id`  
- `user_alias_label`: Um rótulo comum pelo qual agrupar aliases de usuário

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | VERDADEIRO |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSO |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

Quando você fornece tanto um `user_alias_name` quanto um `user_alias_label` na sua importação, a Braze atualiza qualquer usuário existente com o mesmo `user_alias_name` e `user_alias_label`. Se um usuário não for encontrado, a Braze cria um novo usuário identificado com aquele `user_alias_name` definido.

{% alert important %}
Você não pode usar uma importação CSV para atualizar um usuário existente com um `user_alias_name` se ele já tiver um `external_id`. Em vez disso, isso cria um novo perfil de usuário com o `user_alias_name` associado. Para associar um usuário apenas com alias a um `external_id`, use o [endpoint de Identificar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Baixar: [Modelo de Importação de Atributos CSV: Apelido do Usuário]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Para atualizar perfis de usuário existentes na Braze usando um valor de ID interno da Braze em vez de um `external_id` ou `user_alias_name` e `user_alias_label`, especifique `braze_id` como um cabeçalho de coluna.

Isso pode ser útil se você exportou dados de usuários do Braze através da nossa opção de exportação CSV dentro da segmentação e deseja adicionar um novo atributo personalizado a esses usuários existentes.

{% alert important %}
Você não pode usar uma importação CSV para criar um novo usuário usando `braze_id`. Este método só pode ser usado para atualizar usuários pré-existentes na plataforma Braze.  
{% endalert %}

{% alert tip %}
O valor `braze_id` pode ser rotulado como `Appboy ID` nas exportações CSV do dashboard da Braze. Este ID será o mesmo que o `braze_id` para um usuário, então você pode renomear esta coluna para `braze_id` quando reimportar o CSV.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
É possível omitir uma ID externa ou um alias de usuário e usar um endereço de e-mail ou número de telefone para importar usuários. Antes de importar um arquivo CSV com endereços de e-mail ou números de telefone, verifique o seguinte:

- Verifique se não há IDs externos ou aliases de usuário para esses perfis no arquivo CSV. Se o fizer, o Braze priorizará o uso da ID externa ou do alias do usuário antes do endereço de e-mail para identificar perfis.  
- Confirme se o arquivo CSV está formatado corretamente.  

{% alert note %}
Se incluir endereços de e-mail e números de telefone em seu arquivo CSV, o endereço de e-mail terá prioridade sobre o número de telefone ao procurar perfis.
{% endalert %}

Se um perfil existente tiver esse endereço de e-mail ou número de telefone, esse perfil é atualizado, e a Braze não cria um novo perfil. Se houver vários perfis com o mesmo endereço de e-mail, o Braze usará a mesma lógica do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), no qual o perfil atualizado mais recentemente será atualizado.

Se um perfil com esse endereço de e-mail ou número de telefone não existir, a Braze cria um novo perfil com aquele identificador. Você pode usar o [endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) para identificar esse perfil posteriormente. Para excluir um perfil de usuário, você também pode usar o endpoint [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
{% endtab %}
{% endtabs %}

### Etapa 3: Construa seu arquivo CSV

Você pode fazer upload de qualquer um dos seguintes tipos de dados como um único arquivo CSV. Para fazer upload de mais de um tipo de dado, faça upload de múltiplos arquivos CSV.

- **Atributos do Usuário:** Isso inclui tanto atributos de usuário padrão quanto personalizados. Atributos de usuário padrão são chaves reservadas no Braze (como `first_name` ou `email`) e atributos personalizados são atributos de usuário únicos para o seu negócio (como `last_destination_searched`).  
- **Eventos Personalizados:** Estes são únicos para o seu negócio e refletem ações que um usuário realizou, como `trip_booked` para um aplicativo de reserva de viagens.

Quando você estiver pronto para começar a construir seu arquivo CSV, consulte as seguintes informações:

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Identificadores obrigatórios {#required-identifiers-attributes}

Embora `external_id` não seja obrigatório, você **deve** incluir **um** dos seguintes identificadores como cabeçalho em seu arquivo CSV. Para detalhes sobre cada um, revise [Escolha um identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **e** `user_alias_label`
- `email`
- `phone`

#### Atributos personalizados

Os seguintes tipos de dados podem ser usados como atributos personalizados para importação de CSV. Cabeçalhos de coluna que não correspondem exatamente a um [atributo padrão](#default-attributes) são importados como atributos personalizados no Braze.

| Tipo de dados | Descrição |
|---|---|
| Datetime | Deve ser armazenado no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). |
| Booleano | Aceita `true` ou `false`. |
| Número | Deve ser um inteiro ou float sem espaços ou vírgulas. Floats devem usar um ponto (`.`) como separador decimal. |
| String | Podem conter vírgulas se o valor estiver entre aspas duplas (`""`). |
| Em branco | Valores em branco não substituirão valores existentes no perfil do usuário, e você não precisa incluir todos os atributos de usuário existentes em seu arquivo CSV. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Arrays, tokens de push e tipos de dados de eventos personalizados não são suportados na importação de usuários, pois vírgulas em seu arquivo CSV serão interpretadas como um separador de coluna e causarão erros ao analisar seu arquivo.<br><br>Para fazer upload desses tipos de valores, use o [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou [Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/) em vez disso.
{% endalert %} 

#### Atributos padrão

{% alert important %}
Ao importar atributos padrão, os cabeçalhos de coluna que você usar devem corresponder exatamente à ortografia e capitalização dos atributos de usuário padrão. Caso contrário, o Braze detecta isso como [atributos personalizados](#custom-attributes).
{% endalert %}

Os seguintes atributos padrão estão disponíveis para importação de usuário.

| Campo de perfil do usuário | Tipo de dados | Descrição | Necessário? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Um identificador único de usuário para seu cliente. | Condicionalmente. Veja [Identificadores Obrigatórios](#required-identifiers-attributes). |
| `user_alias_name` | String | Um identificador de usuário único para usuários anônimos que é uma alternativa a `external_id`. Deve ser usado com `user_alias_label`. | Condicionalmente. Veja [Identificadores Obrigatórios](#required-identifiers-attributes). |
| `user_alias_label` | String | Um rótulo comum pelo qual agrupar aliases de usuário. Deve ser usado com `user_alias_name`. | Condicionalmente. Veja [Identificadores Obrigatórios](#required-identifiers-attributes). |
| `first_name` | String | O nome dos seus usuários conforme indicado (por exemplo, `Jane`). | Não |
| `last_name` | String | O último nome de seus usuários conforme indicado (por exemplo, `Doe`). | Não |
| `email` | String | O e-mail dos seus usuários conforme indicado (por exemplo, `jane.doe@braze.com`). | Não |
| `country` | String | Os códigos de país devem ser passados para a Braze no padrão ISO-3166-1 alpha-2 (por exemplo, `GB`). | Não |
| `dob` | String | Deve ser passado no formato “AAAA-MM-DD” (por exemplo, `1980-12-21`). Isso importa a Data de Nascimento do seu usuário e permite que você segmente usuários cujo aniversário é “hoje”. | Não |
| `gender` | String | “M”, “F”, “O” (outro), “N” (não aplicável), “P” (prefiro não dizer), ou nil (desconhecido). | Não |
| `home_city` | String | A cidade natal dos seus usuários conforme indicado (por exemplo, `London`). | Não |
| `language` | String | O idioma deve ser passado para a Braze no padrão ISO-639-1 (por exemplo, `en`). Consulte nossa [lista de idiomas aceitos]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/). | Não |
| `phone` | String | Um número de telefone conforme indicado pelos seus usuários, no formato `E.164` (por exemplo, `+442071838750`). Consulte [Números de Telefone do Usuário]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) para obter orientações sobre formatação. | Não |
| `email_open_tracking_disabled` | Booleano | verdadeiro ou falso aceito. Defina como verdadeiro para desativar o pixel de rastreamento de abertura de ser adicionado a todos os futuros e-mails enviados a este usuário. Disponível apenas para SparkPost e SendGrid. | Não |
| `email_click_tracking_disabled` | Booleano | verdadeiro ou falso aceito. Defina como verdadeiro para desativar o rastreamento de cliques para todos os links dentro de um futuro e-mail, enviado para este usuário. Disponível apenas para SparkPost e SendGrid. | Não |
| `email_subscribe` | String | Os valores disponíveis são `opted_in` (explicitamente registrado para receber e-mail), `unsubscribed` (explicitamente optou por não receber e-mails) e `subscribed` (não optou por receber nem por não receber). | Não |
| `push_subscribe` | String | Os valores disponíveis são `opted_in` (registrado explicitamente para receber push mensagens), `unsubscribed` (optou explicitamente por não receber push mensagens) e `subscribed` (nem optou por receber nem por não receber). | Não |
| `time_zone` | String | O fuso horário deve ser passado para a Braze no mesmo formato que o Banco de Dados de Fuso Horário da IANA (por exemplo, `America/New_York` ou `Eastern Time (US & Canada)`). | Não |
| `date_of_first_session`  `date_of_last_session` | String | Pode ser passado em um dos seguintes formatos ISO 8601: "AAAA-MM-DD" "AAAA-MM-DDTHH:MM:SS+00:00" "AAAA-MM-DDTHH:MM:SSZ" "AAAA-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) | Não |
| `subscription_group_id` | String | O `id` do seu grupo de inscrições. Este identificador pode ser encontrado na página do grupo de inscrições do seu dashboard. | Não |
| `subscription_state` | String | O estado da inscrição para o grupo de inscrições especificado por `subscription_group_id`. Os valores permitidos são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições). | Não, mas fortemente recomendado se `subscription_group_id` for usado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Atualizando o status do grupo de inscrições (opcional)

Além disso, você pode adicionar usuários a grupos de inscrições de e-mail ou SMS através da importação de usuário. Isso é particularmente útil para SMS, porque um usuário deve estar inscrito em um grupo de inscrições de SMS para ser enviado uma mensagem pelo canal de SMS. Para saber mais, consulte os [grupos de inscrição de SMS](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Se estiver atualizando os status do grupo de inscrições, é necessário ter as duas colunas a seguir no CSV:

- `subscription_group_id`: O `id` do [grupo de inscrições](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state`: Os valores disponíveis são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
Apenas um único `subscription_group_id` pode ser definido por linha na importação de usuário. Diferentes linhas podem ter diferentes valores de `subscription_group_id`. No entanto, se você precisar inscrever os mesmos usuários em vários grupos de inscrições, precisará fazer várias importações.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Identificadores obrigatórios {#required-identifiers-custom-events}

Embora `external_id` não seja obrigatório, você **deve** incluir **um** dos seguintes identificadores como cabeçalho em seu arquivo CSV. Para detalhes sobre cada um, revise [Escolha um identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **e** `user_alias_label`
- `email`
- `phone`

#### Campos de evento personalizado

Além do seguinte, seu CSV também pode conter cabeçalhos de coluna adicionais para propriedades de evento. Essas propriedades devem ter um cabeçalho de coluna de `<event_name>.properties.<property name>.`

Por exemplo, o evento personalizado `trip_booked` pode ter as propriedades `destination` e `duration`. Esses podem ser importados tendo os cabeçalhos de coluna `trip_booked.properties.destination` e `trip_booked.properties.duration`.

| Campo de perfil do usuário | Tipo de dados | Informações | Necessário? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Um identificador único de usuário para seu usuário. | Condicionalmente. Veja [Identificadores obrigatórios](#required-identifiers-custom-events). |
| `braze_id` | String | Um identificador atribuído pela Braze para o seu usuário. | Condicionalmente. Veja [Identificadores obrigatórios](#required-identifiers-custom-events). |
| `user_alias_name` | String | Um identificador de usuário único para usuários anônimos, que é uma alternativa a `external_id`. Deve ser usado com `user_alias_label`. | Condicionalmente. Veja [Identificadores obrigatórios](#required-identifiers-custom-events). |
| `user_alias_label` | String | Um rótulo comum pelo qual agrupar aliases de usuário. Deve ser usado com `user_alias_name`. | Condicionalmente. Veja [Identificadores obrigatórios](#required-identifiers-custom-events). |
| `email` | String | O e-mail dos seus usuários conforme indicado (por exemplo, `jane.doe@braze.com`). | Não, e só pode ser usado na ausência de outros identificadores. Veja a seguinte nota. |
| `phone` | String | Um número de telefone conforme indicado pelos seus usuários, no formato `E.164` (por exemplo, `+442071838750`). Consulte [Números de Telefone do Usuário]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) para obter orientações sobre formatação. | Não, e só pode ser usado na ausência de outros identificadores. Veja a seguinte nota. |
| `name` | String | Um evento personalizado dos seus usuários. | Sim |
| `time` | String | A hora do evento. Pode ser passado em um dos seguintes formatos ISO-8601: "AAAA-MM-DD" "AAAA-MM-DDTHH:MM:SS+00:00" "AAAA-MM-DDTHH:MM:SSZ" "AAAA-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) | Sim |
| `<event name>.properties.<property name>` | Múltiplas | Uma propriedade de evento associada a um evento personalizado. Um exemplo é `trip_booked.properties.destination` | Não |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### Etapa 4: Fazer upload do seu arquivo

Para fazer upload do seu arquivo, selecione **Atributos** ou **Eventos**, clique em **Navegar Arquivos** e faça upload do seu CSV. A Braze exibe uma prévia das primeiras linhas e um resumo dos campos detectados.

![O modal de upload concluído mostrando uma prévia do arquivo, campo de nome de importação, preferências de direcionamento e caixa de seleção de validação de arquivo.]({% image_buster /assets/img/csv_import/upload_completed.png %})

No campo **Nome da importação**, você pode renomear sua importação. Por padrão, o nome do arquivo é usado.

{% alert note %}
A prévia do arquivo mostra apenas as primeiras linhas do seu arquivo. Para verificar cada linha antes de importar, use [validação de arquivo](#file-validation).
{% endalert %}

### Etapa 5: Valide seu arquivo (opcional) {#file-validation}

Antes de iniciar sua importação, você pode executar a validação do arquivo para verificar cada linha em busca de erros e avisos. Para validar seu arquivo, selecione **Validar arquivo antes de importar**, em seguida, clique em **Iniciar importação**.

A validação pode levar até 2 minutos para arquivos no tamanho máximo permitido. Enquanto a validação é executada, você pode selecionar **Ignorar validação** para ignorá-la e prosseguir imediatamente.

#### Resultados da validação

Quando a validação é concluída, um dos seguintes resultados aparece.

| Resultado | O que isso significa | Próxima etapa |
|---|---|---|
| **Validação completa** | Nenhum problema encontrado. | Selecione **Importar dados**. |
| **Problemas encontrados** | Algumas linhas têm erros ou avisos. | Baixe o relatório de erros para revisá-los, depois selecione **Importar mesmo assim** para prosseguir ou **Cancelar** para corrigir seu arquivo primeiro. |
| **Validação expirada** | A validação excedeu o tempo limite. As linhas que foram verificadas não tinham problemas. | Selecione **Importar dados**. Um relatório completo estará disponível em alguns minutos. |
| **Validação expirada com problemas** | A validação excedeu o tempo limite e encontrou erros em algumas das linhas que verificou. | Baixe o relatório parcial para revisar o que foi encontrado, depois selecione **Importar mesmo assim** ou **Cancelar**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

![O diálogo de problemas encontrados mostrando a contagem de linhas com erros e avisos, com opções para cancelar, baixar o relatório de erros ou importar mesmo assim.]({% image_buster /assets/img/csv_import/validation_issues.png %})

#### Entendendo o relatório de erros

O relatório de erros é um arquivo CSV que contém cada linha sinalizada junto com seus dados originais e uma descrição do problema.

| Tipo de problema | Descrição |
|---|---|
| **Erro** | A linha será totalmente ignorada durante a importação. |
| **Atenção** | A linha será importada, mas alguns valores serão descartados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Após revisar o relatório, você pode corrigir os problemas em seu arquivo original e fazer o upload novamente, ou prosseguir com a importação e aceitar os resultados parciais.

### Etapa 6: Escolha as preferências de direcionamento

Você também pode escolher entre as seguintes preferências de direcionamento. Se você não precisar criar um novo filtro ou segmento de direcionamento a partir da sua importação, selecione **Não tornar esta lista disponível como um filtro de direcionamento**.

| Opção | Descrição |
|---|---|
| Filtro de direcionamento | Para converter seu arquivo CSV em uma opção de redirecionamento ao construir segmentos de usuários, escolha seu arquivo no menu suspenso **Atualizado/Importado de CSV**, em seguida, selecione **Criar filtro de direcionamento**. |
| Novos segmentos | Para também criar um novo segmento a partir do seu novo filtro de direcionamento, selecione **Criar filtro de direcionamento e adicionar ao novo segmento**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Um grupo de filtros com o filtro "Atualizado/Importado de CSV" incluindo um arquivo CSV intitulado "Diversão da temporada de Halloween".]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Etapa 7: Inicie sua importação de CSV

Quando estiver pronto, clique em **Iniciar importação**. Você pode acompanhar o progresso atual na página **Importar Usuários**, que atualiza automaticamente a cada 5 segundos.

{% alert note %}
Você pode importar mais de um CSV ao mesmo tempo. As importações de CSV são executadas simultaneamente, o que significa que a ordem das atualizações não é garantida como serial. Se você precisar que as importações de CSV sejam executadas uma após a outra, espere uma importação de CSV terminar para enviar outra.
{% endalert %}

#### Status da importação

Após iniciar sua importação, você pode verificar seu status na página **Importar Usuários**.

| Status | Descrição |
|---|---|
| **Concluir** | Todas as linhas importadas com sucesso. |
| **Sucesso parcial** | Algumas linhas falharam. Selecione o menu de três pontos ao lado da importação para baixar um relatório de erros ou o CSV original enviado. |
| **Em andamento** | A importação está em andamento. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![A página Importar Usuários mostrando um status de sucesso parcial com o menu de contexto aberto, exibindo opções de Baixar relatório de erro e Baixar CSV enviado.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

O relatório de erro pós-importação inclui linhas que falharam por razões que a validação não cobre, como quando um usuário não existe no Braze.

## Considerações sobre pontos de dados

Cada dado de cliente importado de um arquivo CSV sobrescreve o valor existente nos perfis de usuário e registra um ponto de dados, exceto para IDs externos e valores em branco. Se você tiver alguma dúvida sobre as nuances dos pontos de dados do Braze, seu gerente de conta do Braze pode respondê-las.

| Considerações | Informações |
|---|---|
| IDs externos | Fazendo upload de um CSV com apenas `external_id` não registra pontos de dados. Isso permite que você segmente usuários existentes do Braze sem impactar os limites de dados. No entanto, incluir campos como `email` ou `phone` sobrescreve os dados de usuários existentes e **faz** log de pontos de dados. <br><br>Importações de CSV usadas apenas para segmentação não registram pontos de dados, como aquelas contendo apenas `external_id`, `braze_id` ou `user_alias_name`. |
| Valores em branco | Valores em branco no seu CSV não sobrescrevem os dados do perfil de usuário existentes. Você não precisa incluir todos os atributos de usuário ou eventos personalizados ao importar. |
| Estados de inscrição | Atualizar `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` **não** conta para o uso de pontos de dados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Definir `language` ou `country` em um usuário através da importação de CSV ou API impede que o Braze capture automaticamente essas informações através do SDK.
{% endalert %}

## Solução de problemas

Se você usou [validação de arquivo](#file-validation), comece com o relatório de erros—ele inclui o problema específico para cada linha sinalizada e uma descrição de como corrigi-lo. Para linhas que falharam durante a importação em vez da validação, baixe o relatório de erros no menu de três pontos na página **Importar Usuários**.

Se você está tendo problemas com a importação de CSV, revise esses problemas comuns abaixo. Ainda precisa de ajuda? Entre em contato com [support@braze.com](mailto:support@braze.com).

### Problemas de formatação de arquivo

#### Linha malformada

Se seu upload foi concluído com erros, pode haver uma linha malformada no seu arquivo CSV. 

Para importar dados corretamente, deve haver uma linha de cabeçalho. Cada linha deve ter o mesmo número de células que a linha de cabeçalho. Linhas com um comprimento de mais ou menos valores do que a linha de cabeçalho serão excluídas da importação. As vírgulas em um valor serão interpretadas como um separador e podem levar a esse erro. Além disso, todos os dados devem ser codificados em UTF-8.

Se seu arquivo CSV tem linhas em branco e importa menos linhas do que o total de linhas no arquivo CSV, isso pode não indicar um problema com a importação, já que as linhas em branco não precisariam ser importadas. Verifique o número de linhas que foram importadas corretamente e certifique-se de que corresponde ao número de usuários que você está tentando importar.

#### Linha ausente

Há algumas razões pelas quais o número de usuários importados pode não corresponder ao total de linhas no seu arquivo CSV:

| Problema | Resolução |
|---|---|
| IDs externos duplicados, aliases de usuário, IDs do Braze, endereços de e-mail ou números de telefone | Se houver colunas de ID externas duplicadas, isso poderá causar linhas malformadas ou não importadas, mesmo que as linhas estejam formatadas corretamente. Em alguns casos, isso pode não relatar um erro específico. Verifique se há duplicatas e remova-as antes de re-enviar. |
| Caracteres acentuados | Seu CSV pode incluir nomes ou atributos com acentos. Certifique-se de que o arquivo esteja codificado em UTF-8 para evitar problemas de importação. |
| O ID do Braze pertence a um usuário órfão | Se um usuário foi mesclado em outro e o Braze não consegue associar o ID do Braze ao perfil restante, a linha não será importada. |
| Linha vazia | Linhas em branco no CSV podem causar erros de dados malformados. Verifique usando um editor de texto simples, não Excel ou Sheets. |
| Aspas duplas não escapadas ou desequilibradas (`"`) | Aspas duplas envolvem valores de string que contêm vírgulas. Se um valor em si contém uma aspa dupla, escape-a duplicando-a (`""`). Aspas duplas não escapadas ou desequilibradas causam uma linha malformada. |
| Quebras de linha inconsistentes | Quebras de linha misturadas (e.g., `\n` e `\r\n`) podem fazer com que a primeira linha de dados seja tratada como parte do cabeçalho. Use um editor de texto hex ou avançado para inspecionar e corrigir. |
| Arquivo codificado incorretamente | Mesmo que acentos sejam permitidos, o arquivo deve estar codificado em UTF-8. Outros formatos de codificação podem funcionar parcialmente, mas não são totalmente suportados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### String com aspas

Os valores encapsulados entre aspas simples (`''`) ou duplas (`""`) serão lidos como strings na importação.

#### Datas formatadas incorretamente

As datas que não estiverem no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) não serão lidas como `datetimes` na importação.

### Problemas na estrutura de dados

#### Endereços de e-mail inválidos

Se o seu upload foi concluído com erros, pode haver um ou mais endereços de e-mail criptografados inválidos. Confirme que todos os endereços de e-mail estão criptografados corretamente antes de importá-los para o Braze.

- **Quando [atualizando ou importando endereços de e-mail]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)<1> no Braze, use o valor de e-mail hash sempre que um e-mail for incluído. Esses valores de e-mail hash são fornecidos pela sua equipe interna. 
- **Ao criar um novo usuário**, você deve adicionar `email_encrypted` com o valor de e-mail criptografado do usuário. Caso contrário, o Braze não criará o usuário. Da mesma forma, se você estiver adicionando um endereço de e-mail a um usuário existente que não tem um e-mail, você deve adicionar `email_encrypted`. Caso contrário, o Braze não atualizará o usuário.

#### Dados importados como atributo personalizado

Se uma parte dos dados padrão de usuários (como `email` ou `first_name`) for importada como um atributo personalizado, verifique as letras maiúsculas e minúsculas e o espaçamento do arquivo CSV. Por exemplo, `First_name` é importado como um atributo personalizado, enquanto `first_name` é corretamente importado no campo "primeiro nome" no perfil de um usuário.

#### Múltiplos tipos de dados

Braze espera que cada valor em uma coluna seja do mesmo tipo de dado. Valores que não correspondem ao tipo de dados do atributo causam erros na segmentação.

Além disso, começar um atributo numérico com zero causará problemas, pois números que começam com zeros são considerados strings. Quando o Braze converte essa string, ela pode ser tratada como um valor octal (que usa dígitos de zero a sete), o que significa que é convertida para seu valor decimal correspondente. Por exemplo, se o valor no arquivo CSV for 0130, o perfil do Braze mostrará 88. Para evitar esse problema, use atributos com tipos de dados string. No entanto, esse tipo de dado não está disponível na comparação de números de segmentação.

#### Tipos de atributos padrão

Alguns atributos padrão podem aceitar apenas certos valores como válidos para atualizações de usuários. Para orientação, consulte [Construindo seu arquivo CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Espaços em branco no final e diferenças na capitalização podem fazer com que um valor seja interpretado como inválido. Por exemplo, no seguinte arquivo CSV, apenas o usuário na primeira linha (`brazetest1`) teve seus e-mails e status de push atualizados com sucesso porque os valores aceitos são `unsubscribed`, `subscribed` e `opted_in`. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### "Selecionar arquivo CSV" não está funcionando

Existem várias razões pelas quais o botão **Selecionar arquivo CSV** pode não funcionar:

| Problema | Resolução |
|---|---|
| Bloqueador de pop-ups | Isso pode impedir que a página seja exibida. Confirme que seu navegador está permitindo pop-ups no site do dashboard da Braze. |
| Navegador desatualizado | Certifique-se de que seu navegador está atualizado; se não estiver, atualize para a versão mais recente. |
| Processos em segundo plano | Feche todas as instâncias do navegador e reinicie seu computador. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

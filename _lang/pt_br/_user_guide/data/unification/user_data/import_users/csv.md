---
nav_title: Usando um CSV
article_title: "Importação de CSV"
description: "Saiba como registrar e atualizar atributos de usuário e eventos personalizados usando a importação de CSV."
page_order: 1.2
---

# Importação de CSV

> Saiba como registrar e atualizar atributos de usuário e eventos personalizados usando a importação de CSV.

## Sobre a importação de CSV

Você pode usar a importação de CSV para registrar e atualizar os seguintes atributos de usuário e eventos personalizados.

|Tipo|Definição|Exemplo|Tamanho máximo do arquivo|
|---|---|---|---|
|Atributos padrão|Atributos de usuário reservados reconhecidos pelo Braze.|`first_name`, `email`|500 MB|
|Atributos personalizados|Atributos de usuário exclusivos da sua empresa.|`last_destination_searched`|500 MB|
|Eventos personalizados|Eventos exclusivos da sua empresa que representam ações do usuário.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Usando a importação de CSV

### Etapa 1: Faça o download de um modelo CSV

Para abrir a importação de CSV, vá para **Audiences** > **Import Users**( **Públicos** > **Importar usuários**). Aqui, você encontrará uma tabela que lista detalhes sobre as importações mais recentes, como a data de upload, o nome do carregador, o nome do arquivo, a disponibilidade de destino, o número de linhas importadas e o status da importação.

Para começar a criar seu CSV, faça o download de um modelo para atributos ou eventos.

A página "Importar usuários" no painel de controle do Braze.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Etapa 2: Escolha um identificador {#choose-an-identifier}

O CSV que você importar precisará de um identificador dedicado. Você pode escolher entre as seguintes opções:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Ao importar os dados de seus clientes, você pode usar um `external_id` para servir como identificador exclusivo de cada cliente. Quando você fornecer um `external_id` em sua importação, o Braze atualizará qualquer usuário existente com o mesmo `external_id` ou criará um usuário recém-identificado com esse conjunto `external_id`, caso não seja encontrado um.

- Faça o download: [Modelo de importação de atributos CSV: ID externa]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Faça o download: [Modelo de importação de eventos CSV: ID externa](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Se estiver fazendo upload de uma mistura de usuários com `external_id` e usuários sem , será necessário criar um CSV para cada importação. Um CSV não pode conter `external_ids` e aliases de usuário.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Para segmentar usuários que não têm um `external_id`, você pode importar uma lista de usuários com aliases de usuário. Um alias serve como um identificador de usuário exclusivo alternativo e pode ser útil se você estiver tentando comercializar para usuários anônimos que não se inscreveram ou fizeram uma conta no seu aplicativo.

Se você estiver carregando ou atualizando perfis de usuário que sejam apenas alias, deverá ter as duas colunas a seguir no seu CSV:

- `user_alias_name`: Um identificador de usuário exclusivo; uma alternativa ao `external_id`  
- `user_alias_label`: Um rótulo comum para agrupar aliases de usuário

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | VERDADEIRO |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSO |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

Quando você fornecer um `user_alias_name` e um `user_alias_label` em sua importação, o Braze atualizará qualquer usuário existente com os mesmos `user_alias_name` e `user_alias_label`. Se um usuário não for encontrado, o Braze criará um novo usuário identificado com esse conjunto `user_alias_name`.

{% alert important %}
Não é possível usar uma importação de CSV para atualizar um usuário existente com um `user_alias_name` se ele já tiver um `external_id`. Em vez disso, isso criará um novo perfil de usuário com o `user_alias_name` associado. Para associar um usuário somente de alias a um `external_id`, use o [ponto de extremidade Identificar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Faça o download: [Modelo de importação de atributos CSV: Apelido de usuário]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Para atualizar os perfis de usuário existentes no Braze usando um valor de ID interno do Braze em vez de um valor `external_id` ou `user_alias_name` e `user_alias_label`, especifique `braze_id` como um cabeçalho de coluna.

Isso pode ser útil se você exportou dados de usuários do Braze por meio de nossa opção de exportação CSV dentro da segmentação e deseja adicionar um novo atributo personalizado a esses usuários existentes.

{% alert important %}
Não é possível usar uma importação de CSV para criar um novo usuário usando `braze_id`. Esse método só pode ser usado para atualizar usuários pré-existentes na plataforma Braze.  
{% endalert %}

{% alert tip %}
O valor `braze_id` pode ser rotulado como `Appboy ID` nas exportações CSV do painel do Braze. Esse ID será o mesmo que o `braze_id` de um usuário, portanto, você pode renomear essa coluna para `braze_id` ao reimportar o CSV.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
É possível omitir uma ID externa ou um alias de usuário e usar um endereço de e-mail ou número de telefone para importar usuários. Antes de importar um arquivo CSV com endereços de e-mail ou números de telefone, verifique o seguinte:

- Verifique se não há IDs externas ou aliases de usuário para esses perfis no arquivo CSV. Se você fizer isso, o Braze priorizará o uso da ID externa ou do alias do usuário antes do endereço de e-mail para identificar os perfis.  
- Confirme se o arquivo CSV está formatado corretamente.  

{% alert note %}
Se você incluir endereços de e-mail e números de telefone no seu arquivo CSV, o endereço de e-mail terá prioridade sobre o número de telefone ao procurar perfis.
{% endalert %}

Se um perfil existente tiver esse endereço de e-mail ou número de telefone, esse perfil será atualizado, e o Braze não criará um novo perfil. Se houver vários perfis com o mesmo endereço de e-mail, o Braze usará a mesma lógica do [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), no qual o perfil atualizado mais recentemente será atualizado.

Se não houver um perfil com esse endereço de e-mail ou número de telefone, o Braze criará um novo perfil com esse identificador. Você pode usar o [ponto de extremidade`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) para identificar esse perfil posteriormente. Para excluir um perfil de usuário, você também pode usar o ponto de extremidade [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) ponto de extremidade.
{% endtab %}
{% endtabs %}

### Etapa 3: Crie seu arquivo CSV

Você pode carregar qualquer um dos seguintes tipos de dados como um único arquivo CSV. Para carregar mais de um tipo de dados, carregue vários arquivos CSV.

- **Atributos do usuário:** Isso inclui atributos de usuário padrão e personalizados. Os atributos de usuário padrão são chaves reservadas no Braze (como `first_name` ou `email`) e os atributos personalizados são atributos de usuário exclusivos da sua empresa (como `last_destination_searched`).  
- **Eventos personalizados:** Eles são exclusivos da sua empresa e refletem as ações realizadas por um usuário, como `trip_booked` para um aplicativo de reserva de viagens.

Quando estiver pronto para começar a criar seu arquivo CSV, consulte as informações a seguir:

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Identificadores necessários {#required-identifiers-attributes}

Embora o site `external_id` não seja obrigatório, você **deve** incluir **um** dos seguintes identificadores como cabeçalho em seu arquivo CSV. Para obter detalhes sobre cada um deles, consulte [Escolha um identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **e** `user_alias_label`
- `email`
- `phone`

#### Atributos personalizados

Os seguintes tipos de dados podem ser usados como atributos personalizados para importação de CSV. Os cabeçalhos de coluna que não corresponderem exatamente a um [atributo padrão](#default-attributes) receberão um atributo personalizado no Braze.

| Tipo de dados | Descrição |
|---|---|
| Data e hora | Deve ser armazenado no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). |
| Booleano | Aceita `true` ou `false`. |
| Número | Deve ser um número inteiro ou float, sem espaços ou vírgulas. Os valores flutuantes devem usar um ponto (`.`) como separador decimal. |
| Cordas | Pode conter vírgulas se o valor estiver entre aspas duplas (`""`). |
| Em branco | Os valores em branco não substituirão os valores existentes no perfil do usuário, e não é necessário incluir todos os atributos de usuário existentes no arquivo CSV. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Matrizes, tokens push e tipos de dados de eventos personalizados não são compatíveis com a importação de usuários, pois as vírgulas no seu arquivo CSV serão interpretadas como um separador de colunas e causarão erros ao analisar o arquivo.<br><br>Para fazer upload desses tipos de valores, use o [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou o [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %} 

#### Atributos padrão

{% alert important %}
Ao importar atributos padrão, os cabeçalhos de coluna usados devem corresponder exatamente à ortografia e à capitalização dos atributos padrão do usuário. Caso contrário, o Braze os detectará como [atributos personalizados](#custom-attributes).
{% endalert %}

| Campo de perfil do usuário | Tipo de dados | Descrição | Necessário? |
| :---- | :---- | :---- | :---- |
| `external_id` | Cordas | Um identificador de usuário exclusivo para o seu cliente. | Condicionalmente. Consulte [Identificadores obrigatórios](#required-identifiers-attributes). |
| `user_alias_name` | Cordas | Um identificador de usuário exclusivo para usuários anônimos que é uma alternativa ao `external_id`. Deve ser usado com `user_alias_label`. | Condicionalmente. Consulte [Identificadores obrigatórios](#required-identifiers-attributes). |
| `user_alias_label` | Cordas | Um rótulo comum para agrupar aliases de usuário. Deve ser usado com `user_alias_name`. | Condicionalmente. Consulte [Identificadores obrigatórios](#required-identifiers-attributes). |
| `first_name` | Cordas | O primeiro nome dos seus usuários, conforme indicado por eles (por exemplo, `Jane`). | Não |
| `last_name` | Cordas | O sobrenome dos seus usuários, conforme indicado por eles (por exemplo, `Doe`). | Não |
| `email` | Cordas | O e-mail dos seus usuários, conforme indicado por eles (por exemplo, `jane.doe@braze.com`). | Não |
| `country` | Cordas | Os códigos de país devem ser passados para o Braze no padrão ISO-3166-1 alfa-2 (por exemplo, `GB`). | Não |
| `dob` | Cordas | Deve ser passado no formato "YYYY-MM-DD" (por exemplo, `1980-12-21`). Isso importará a data de nascimento do usuário e permitirá que você segmente usuários cujo aniversário seja "hoje". | Não |
| `gender` | Cordas | "M", "F", "O" (outro), "N" (não aplicável), "P" (prefere não dizer) ou nulo (desconhecido). | Não |
| `home_city` | Cordas | A cidade de origem dos seus usuários, conforme indicado por eles (por exemplo, `London`). | Não |
| `language` | Cordas | O idioma deve ser passado para o Braze no padrão ISO-639-1 (por exemplo, `en`). Consulte nossa [lista de idiomas aceitos]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/). | Não |
| `phone` | Cordas | Um número de telefone conforme indicado pelos usuários, no formato `E.164` (por exemplo, `+442071838750`). Consulte [Números de telefone do usuário]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) para obter orientação sobre formatação. | Não |
| `email_open_tracking_disabled` | Booleano | aceito como verdadeiro ou falso. Defina como true para desativar a adição do pixel de rastreamento de abertura a todos os e-mails futuros enviados a esse usuário. Disponível apenas para SparkPost e SendGrid. | Não |
| `email_click_tracking_disabled` | Booleano | aceito como verdadeiro ou falso. Defina como true para desativar o rastreamento de cliques para todos os links em um e-mail futuro enviado a esse usuário. Disponível apenas para SparkPost e SendGrid. | Não |
| `email_subscribe` | Cordas | Os valores disponíveis são `opted_in` (explicitamente registrado para receber mensagens de e-mail), `unsubscribed` (explicitamente optado por não receber mensagens de e-mail) e `subscribed` (nem optado nem não optado). | Não |
| `push_subscribe` | Cordas | Os valores disponíveis são `opted_in` (explicitamente registrado para receber mensagens push), `unsubscribed` (explicitamente optado por não receber mensagens push) e `subscribed` (nem optado nem não). | Não |
| `time_zone` | Cordas | O fuso horário deve ser passado ao Braze no mesmo formato do banco de dados de fuso horário da IANA (por exemplo, `America/New_York` ou `Eastern Time (US & Canada)`). | Não |
| `date_of_first_session`  `date_of_last_session` | Cordas | Pode ser transmitido em um dos seguintes formatos ISO 8601: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) | Não |
| `subscription_group_id` | Cordas | O endereço `id` de seu grupo de assinaturas. Esse identificador pode ser encontrado na página do grupo de assinaturas de seu painel. | Não |
| `subscription_state` | Cordas | O estado da assinatura do grupo de assinatura especificado por `subscription_group_id`. Os valores permitidos são `unsubscribed` (não está no grupo de assinaturas) ou `subscribed` (está no grupo de assinaturas). | Não, mas é altamente recomendável se o site `subscription_group_id` for usado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Atualização do status do grupo de assinaturas (opcional)

Além disso, você pode adicionar usuários a grupos de assinatura de e-mail ou SMS por meio da importação de usuários. Isso é particularmente útil para SMS, porque um usuário deve estar inscrito em um grupo de assinatura de SMS para receber mensagens com o canal SMS. Para obter mais informações, consulte [Grupos de assinatura de SMS](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Se estiver atualizando os status do grupo de assinaturas, é necessário ter as duas colunas a seguir no CSV:

- `subscription_group_id`: O endereço `id` do [grupo de assinaturas](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state`: Os valores disponíveis são `unsubscribed` (não está no grupo de assinaturas) ou `subscribed` (está no grupo de assinaturas).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | inscrito |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | inscrito |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
Somente um único `subscription_group_id` pode ser definido por linha na importação do usuário. Linhas diferentes podem ter valores diferentes em `subscription_group_id`. No entanto, se precisar inscrever os mesmos usuários em vários grupos de assinatura, será necessário fazer várias importações.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Identificadores necessários {#required-identifiers-custom-events}

Embora o site `external_id` não seja obrigatório, você **deve** incluir **um** dos seguintes identificadores como cabeçalho em seu arquivo CSV. Para obter detalhes sobre cada um deles, consulte [Escolha um identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **e** `user_alias_label`
- `email`
- `phone`

#### Campos de eventos personalizados

Além dos itens a seguir, seu CSV também pode conter cabeçalhos de coluna adicionais para propriedades de eventos. Essas propriedades devem ter um cabeçalho de coluna de `<event_name>.properties.<property name>.`

Por exemplo, o evento personalizado `trip_booked` pode ter as propriedades `destination` e `duration`. Eles podem ser importados com os cabeçalhos de coluna `trip_booked.properties.destination` e `trip_booked.properties.duration`.

| Campo de perfil do usuário | Tipo de dados | Informações | Necessário? |
| :---- | :---- | :---- | :---- |
| `external_id` | Cordas | Um identificador de usuário exclusivo para o seu usuário. | Condicionalmente. Consulte [Identificadores necessários](#required-identifiers-custom-events). |
| `braze_id` | Cordas | Um identificador atribuído pelo Braze para seu usuário. | Condicionalmente. Consulte [Identificadores necessários](#required-identifiers-custom-events). |
| `user_alias_name` | Cordas | Um identificador de usuário exclusivo para usuários anônimos, que é uma alternativa ao `external_id`. Deve ser usado com `user_alias_label`. | Condicionalmente. Consulte [Identificadores necessários](#required-identifiers-custom-events). |
| `user_alias_label` | Cordas | Um rótulo comum para agrupar aliases de usuário. Deve ser usado com `user_alias_name`. | Condicionalmente. Consulte [Identificadores necessários](#required-identifiers-custom-events). |
| `email` | Cordas | O e-mail dos seus usuários, conforme indicado por eles (por exemplo, `jane.doe@braze.com`). | Não, e só pode ser usado na ausência de outros identificadores. Veja a nota a seguir. |
| `phone` | Cordas | Um número de telefone conforme indicado pelos usuários, no formato `E.164` (por exemplo, `+442071838750`). Consulte [Números de telefone do usuário]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) para obter orientação sobre formatação. | Não, e só pode ser usado na ausência de outros identificadores. Veja a nota a seguir. |
| `name` | Cordas | Um evento personalizado de seus usuários. | Sim |
| `time` | Cordas | A hora do evento. Pode ser passado em um dos seguintes formatos ISO-8601: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) | Sim |
| `<event name>.properties.<property name>` | Múltiplos | Uma propriedade de evento associada a um evento personalizado. Um exemplo é `trip_booked.properties.destination` | Não |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### Etapa 4: Faça upload e visualize seus dados

Antes de o Braze processar seu CSV, ele gerará uma visualização das primeiras linhas para que você possa verificar se há algum problema. Para gerar sua visualização, escolha **Attributes (Atributos** ) ou **Events (Eventos**), selecione **Browse Files (Procurar arquivos**) e carregue seu CSV. 

<!-- old image -->
\![Upload de CSV concluído com erros envolvendo tipos de dados mistos em uma única coluna]({% image_buster /assets/img/csv_import/upload_csv.png %}){: style="max-width:70%"}

{% alert important %}
A visualização da importação do usuário não verifica todas as linhas do arquivo de entrada. Os erros após as primeiras linhas podem não ser detectados, portanto, considere examinar o arquivo CSV por completo.
{% endalert %}

### Etapa 5: Escolha as preferências de segmentação

Você também pode escolher entre as seguintes preferências de segmentação. Se não for necessário criar um novo filtro ou segmento de segmentação a partir de sua importação, selecione **Não disponibilizar essa lista como um filtro de segmentação**.

| Opção | Descrição |
|---|---|
| Filtro de direcionamento | Para converter seu arquivo CSV em uma opção de redirecionamento ao criar segmentos de usuários, escolha seu arquivo no menu suspenso **Atualizado/Importado de CSV** e selecione **Criar filtro de direcionamento**. |
| Novos segmentos | Para criar também um novo segmento a partir de seu novo filtro de segmentação, selecione **Criar filtro de segmentação e adicionar a um novo segmento**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

\![Um grupo de filtros com o filtro "Updated/Imported from CSV" (Atualizado/Importado de CSV), incluindo um arquivo CSV intitulado "Halloween season fun" (Diversão na temporada de Halloween).]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Etapa 6: Iniciar sua importação de CSV

Quando estiver pronto, selecione **Iniciar importação**. Você pode acompanhar o progresso atual na página **User Import**, que é atualizada automaticamente a cada cinco segundos.

Se não houver problemas, o status será atualizado para **Complete** e o número de linhas processadas será exibido. Todos os dados das linhas processadas serão adicionados aos perfis existentes ou aos perfis recém-criados.

{% alert note %}
Você pode importar mais de um CSV ao mesmo tempo. As importações de CSV são executadas simultaneamente, portanto, não é garantido que a ordem das atualizações seja serial. Se você precisar que as importações de CSV sejam executadas uma após a outra, aguarde até que uma importação de CSV seja concluída antes de fazer o upload de uma segunda.
{% endalert %}

## Considerações sobre os pontos de dados

Cada dado de cliente importado de um arquivo CSV substituirá o valor existente nos perfis de usuário e registrará um ponto de dados, exceto para IDs externos e valores em branco. Se você tiver alguma dúvida sobre as nuances dos pontos de dados Braze, seu gerente de conta Braze poderá respondê-la.

| Considerações | Detalhes |
|---|---|
| IDs externas | O upload de um CSV com apenas `external_id` não registrará pontos de dados. Isso permite que você segmente os usuários existentes do Braze sem afetar os limites de dados. No entanto, a inclusão de campos como `email` ou `phone` substituirá os dados de usuário existentes e **registrará** os pontos de dados. <br><br>As importações de CSV usadas apenas para segmentação não registram pontos de dados, como os que contêm apenas `external_id`, `braze_id` ou `user_alias_name`. |
| Valores em branco | Os valores em branco no seu CSV não substituirão os dados de perfil de usuário existentes. Não é necessário incluir todos os atributos de usuário ou eventos personalizados ao importar. |
| Estados de assinatura | A atualização de `email_subscribe`, `push_subscribe`, `subscription_group_id`, ou `subscription_state` **não** conta para o uso do ponto de dados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
A configuração de `language` ou `country` em um usuário por meio de importação de CSV ou API impedirá que o Braze capture automaticamente essas informações por meio do SDK.
{% endalert %}

## Solução de problemas

Analise esses problemas comuns se estiver tendo problemas com a importação de CSV. Ainda precisa de ajuda? Entre em contato com o [suporte@braze.com](mailto:support@braze.com).

### Problemas de formatação de arquivos

#### Linha malformada

Se o upload foi concluído com erros, pode haver uma linha malformada em seu arquivo CSV. 

Para importar dados corretamente, deve haver uma linha de cabeçalho. Cada linha deve ter o mesmo número de células que a linha do cabeçalho. As linhas com um comprimento de mais ou menos valores do que a linha do cabeçalho serão excluídas da importação. As vírgulas em um valor serão interpretadas como um separador e podem levar a esse erro. Além disso, todos os dados devem ser codificados em UTF-8.

Se o seu arquivo CSV tiver linhas em branco e importar menos linhas do que o total de linhas no arquivo CSV, isso pode não indicar um problema com a importação, pois as linhas em branco não precisariam ser importadas. Verifique o número de linhas que foram importadas corretamente e certifique-se de que ele corresponde ao número de usuários que você está tentando importar.

#### Linha ausente

Há alguns motivos pelos quais o número de usuários importados pode não corresponder ao total de linhas no seu arquivo CSV:

| Problema | Resolução |
|---|---|
| Duplicar IDs externas, aliases de usuário, IDs do Braze, endereços de e-mail ou números de telefone | Se houver colunas de ID externas duplicadas, isso poderá causar linhas malformadas ou não importadas, mesmo que as linhas estejam formatadas corretamente. Em alguns casos, isso pode não informar um erro específico. Verifique se há duplicatas e remova-as antes de fazer novo upload. |
| Caracteres acentuados | Seu CSV pode incluir nomes ou atributos com acentos. Certifique-se de que o arquivo esteja codificado em UTF-8 para evitar problemas de importação. |
| O Braze ID pertence a um usuário órfão | Se um usuário tiver sido mesclado com outro e o Braze não puder associar o Braze ID ao perfil restante, a linha não será importada. |
| Linha vazia | As linhas em branco no CSV podem causar erros de dados malformados. Verifique usando um editor de texto simples, não o Excel ou o Sheets. |
| Incluindo aspas duplas (`"` ) | Esse caractere é inválido e causará uma linha malformada. Em vez disso, use aspas simples (`'`). |
| Quebras de linha inconsistentes | Quebras de linha mistas (e.g., `\n` e `\r\n`) podem fazer com que a primeira linha de dados seja tratada como parte do cabeçalho. Use um editor de texto hexadecimal ou avançado para inspecionar e corrigir. |
| Arquivo codificado incorretamente | Mesmo que os acentos sejam permitidos, o arquivo deve ser codificado em UTF-8. Outras codificações podem funcionar parcialmente, mas não são totalmente compatíveis. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Cotação de strings

Os valores encapsulados entre aspas simples (`''`) ou duplas (`""`) serão lidos como cadeias de caracteres na importação.

#### Datas formatadas incorretamente

As datas que não estiverem no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) não serão lidas como `datetimes` na importação.

### Problemas de estrutura de dados

#### Endereços de e-mail inválidos

Se o upload for concluído com erros, pode haver um ou mais endereços de e-mail criptografados inválidos. Confirme se todos os endereços de e-mail estão criptografados corretamente antes de importá-los para o Braze.

- **Ao [atualizar ou importar um endereço de e-mail]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)** no Braze, use o valor de e-mail com hash sempre que um e-mail for incluído. Esses valores de e-mail hash são fornecidos pela sua equipe interna. 
- **Ao criar um novo usuário**, é necessário adicionar o endereço `email_encrypted` com o valor do e-mail criptografado do usuário. Caso contrário, o usuário não será criado. Da mesma forma, se você estiver adicionando um endereço de e-mail a um usuário existente que não tenha um e-mail, deverá adicionar `email_encrypted`. Caso contrário, o usuário não será atualizado.

#### Dados importados como atributo personalizado

Se uma parte dos dados padrão do usuário (como `email` ou `first_name`) for importada como um atributo personalizado, verifique as letras maiúsculas e minúsculas e o espaçamento do arquivo CSV. Por exemplo, `First_name` seria importado como um atributo personalizado, enquanto `first_name` seria importado corretamente para o campo "primeiro nome" no perfil de um usuário.

#### Vários tipos de dados

O Braze espera que cada valor em uma coluna seja do mesmo tipo de dados. Os valores que não corresponderem ao tipo de dados do atributo causarão erros na segmentação.

Além disso, iniciar um atributo numérico com zero causará problemas porque os números que começam com zeros são considerados cadeias de caracteres. Quando o Braze converte essa string, ela pode ser tratada como um valor octal (que usa dígitos de zero a sete), o que significa que será convertida em seu valor decimal correspondente. Por exemplo, se o valor no arquivo CSV for 0130, o perfil Braze mostrará 88. Para evitar esse problema, use atributos com tipos de dados de cadeia de caracteres. No entanto, esse tipo de dados não está disponível na comparação de números de segmentação.

#### Tipos de atributos padrão

Alguns atributos padrão podem aceitar apenas determinados valores como válidos para atualizações de usuários. Para obter orientação, consulte [Construção de seu CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Espaços finais e diferenças na capitalização podem fazer com que um valor seja interpretado como inválido. Por exemplo, no arquivo CSV a seguir, somente o usuário da primeira linha (`brazetest1`) terá seus status de e-mail e push atualizados com êxito porque os valores aceitos são `unsubscribed`, `subscribed` e `opted_in`. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### "Select CSV File" (Selecionar arquivo CSV) não está funcionando

Há vários motivos pelos quais o botão **Selecionar arquivo CSV** pode não funcionar:

| Problema | Resolução |
|---|---|
| Bloqueador de pop-up | Isso pode impedir a exibição da página. Confirme se o seu navegador está permitindo pop-ups no site do painel de controle do Braze. |
| Navegador desatualizado | Certifique-se de que seu navegador esteja atualizado; caso contrário, atualize-o para a versão mais recente. |
| Processos em segundo plano | Feche todas as instâncias do navegador e reinicie o computador. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

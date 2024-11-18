---
nav_title: Importar dados de usuários e eventos CSV
article_title: Importar dados de usuários e eventos CSV
permalink: "/csv_events/"
description: "Este artigo de referência cobre como importar dados de usuários e como importar eventos personalizados usando arquivos CSV."
page_type: reference
---

# Importação de dados de usuários (acesso antecipado a eventos em CVS)

> A Braze oferece uma variedade de maneiras de importar dados de usuários para a plataforma: SDKs, APIs, ingestão de dados na nuvem, integrações com parceiros tecnológicos e arquivos CSV. Este artigo fornece instruções detalhadas sobre como importar dados de usuários, incluindo como [importar eventos personalizados via arquivos CSV (acesso antecipado)](#importing-custom-events).

{% multi_lang_include email-via-sms-warning.md %}

Antes de prosseguir, vale frisar que a Braze não sanitiza (valida ou formata corretamente) os dados HTML durante a importação. Isso significa que as tags de script devem ser removidas de todos os dados de importação destinados à personalização da web.

## API REST

Você pode usar o [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar eventos personalizados, atributos de usuário e compras para usuários.

## importação de CSV

Você pode fazer upload e atualizar perfis de usuários através de arquivos CSV de **público** > **Importar Usuários**.

A importação de dados de usuários por arquivos CSV suporta o registro e a atualização de atributos de usuários, como nome e e-mail, além de atributos personalizados, como tamanho de calçados. Você pode importar um CSV especificando um dos dois identificadores únicos de usuário: um `external_id` ou um alias de usuário.

{% alert important %}
A importação de usuário também suporta o registro e a atualização de eventos personalizados do usuário. Semelhante aos atributos do usuário, é possível importar com um `external_id`, `braze_id` ou com `user_alias_name` e `user_alias_label`. Para saber mais, veja [Importação de eventos personalizados](#importing-custom-events).
{% endalert %}

{% alert note %}
Se você estiver enviando vários usuários com e sem `external_id`, você precisa criar um arquivo CSV para cada importação. Um arquivo CSV não pode conter ambos `external_ids` e aliases de usuário.
{% endalert %}

### Importando com ID externo

Ao importar seus dados de cliente, você precisará especificar o identificador único de cada cliente, também conhecido como `external_id`. Antes de iniciar sua importação de CSV, é importante entender com sua equipe de engenharia como os usuários serão identificados no Braze. Normalmente, este é um ID de banco de dados interno. Isso deve estar alinhado com a forma como os usuários serão identificados pelo Braze SDK em dispositivos móveis e web e é projetado para que cada cliente tenha um único perfil de usuário no Braze em todos os seus dispositivos. Leia mais sobre o [ciclo de vida do perfil de usuário][13] da Braze.

Quando você fornece um `external_id` na sua importação, a Braze atualizará qualquer usuário existente com o mesmo `external_id` ou criará um novo usuário identificado com esse conjunto de `external_id` se um não for encontrado.

- **Baixar:** [Modelo de Importação de Atributos CSV][import_template]
- **Baixar:** [Modelo de Importação de Eventos CSV][events_template]

### Importando com alias de usuário

Para direcionar os usuários que não têm um `external_id`, é possível importar uma lista de usuários com aliases de usuário. Um alias serve como um identificador único de usuário alternativo e pode ser útil se você estiver tentando fazer marketing para usuários anônimos que não se inscreveram ou criaram uma conta no seu app.

Se você estiver carregando ou atualizando perfis de usuário que são apenas alias, você deve ter as seguintes duas colunas em seu CSV:

- `user_alias_name`: Um identificador único de usuário; uma alternativa ao `external_id`
- `user_alias_label`: Um rótulo comum pelo qual agrupar aliases de usuário

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | VERDADEIRO |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSO |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Quando você fornece tanto um `user_alias_name` quanto um `user_alias_label` na sua importação, a Braze atualizará qualquer usuário existente com o mesmo `user_alias_name` e `user_alias_label`. Se um usuário não for encontrado, a Braze criará um novo usuário identificado com esse `user_alias_name` definido.

{% alert important %}
Você não pode usar uma importação CSV para atualizar um usuário existente com um `user_alias_name` se ele já tiver um `external_id`. Em vez disso, isso criará um novo perfil de usuário com o associado `user_alias_name`. Para associar um usuário apenas com alias a um `external_id`, use o [endpoint de Identificar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

- **Baixar:** [Modelo de Importação de Atributos de Alias CSV][template_alias_attributes]
- **Baixar:** [Modelo de Importação de Eventos de Alias CSV][template_alias_events]

### Importando com Braze ID

Para atualizar perfis de usuário existentes na Braze usando um valor de ID interno da Braze em vez de um `external_id` ou `user_alias_name` e `user_alias_label`, especifique `braze_id` como um cabeçalho de coluna.

Isso pode ser útil se você exportou dados de usuários do Braze através da nossa opção de exportação CSV dentro da segmentação e deseja adicionar um novo atributo personalizado a esses usuários existentes.

{% alert important %}
Você não pode usar uma importação CSV para criar um novo usuário usando `braze_id`. Este método só pode ser usado para atualizar usuários pré-existentes na plataforma Braze.
{% endalert %}

{% alert tip %}
O valor `braze_id` pode ser rotulado como `Appboy ID` nas exportações CSV do dashboard da Braze. Este ID será o mesmo que o `braze_id` para um usuário, então você pode renomear esta coluna para `braze_id` quando reimportar o CSV.
{% endalert %}

### Importando atributos padrão

Para importar atributos padrão para usuários, acessar **Importar Usuários** > **Atributos**. Os atributos padrão do usuário são chaves reservadas no Braze. Por exemplo, `first_name` ou `email`. Atributos personalizados são personalizados para o seu negócio. Por exemplo, um app de reserva de viagens pode ter um atributo personalizado chamado `last_destination_searched`.

{% alert important %}
Ao importar dados de cliente como atributos, os cabeçalhos das colunas que você usa devem corresponder exatamente à ortografia e capitalização dos atributos padrão do usuário. Caso contrário, a Braze criará automaticamente um atributo personalizado no perfil desse usuário.
{% endalert %}

#### Cabeçalhos de colunas de dados de usuários padrão

| USER PROFILE FIELD | DATA TYPE | INFORMATION | REQUIRED |
|---|---|---|---|
| `external_id` | String | Um identificador único de usuário para seu cliente. | Sim, veja a [seguinte nota](#about-external-ids). |
| `user_alias_name` | String | Um identificador de usuário único para usuários anônimos. Uma alternativa ao `external_id`. | Não, veja a [seguinte nota](#about-external-ids). |
| `user_alias_label` | String | Um rótulo comum pelo qual agrupar aliases de usuário. | Sim, se `user_alias_name` for usado. |
| `first_name` | String | O nome dos seus usuários conforme indicado (por exemplo, `Jane`). | Não |
| `last_name` | String | O último nome de seus usuários conforme indicado (por exemplo, `Doe`). | Não |
| `email` | String | O e-mail dos seus usuários conforme indicado (por exemplo, `jane.doe@braze.com`). | Não |
| `country` | String | Os códigos de país devem ser passados para a Braze no padrão ISO-3166-1 alpha-2 (por exemplo, `GB`). | Não |
| `dob` | String | Deve ser passado no formato "AAAA-MM-DD" (por exemplo, `1980-12-21`). Isso importará a Data de Nascimento do seu usuário e ativará você para segmentar usuários cujo aniversário é "hoje". | Não |
| `gender` | String | "M", "F", "O" (outro), "N" (não aplicável), "P" (prefere não dizer) ou nil (desconhecido). | Não |
| `home_city` | String | A cidade natal dos seus usuários conforme indicado (por exemplo, `London`). | Não |
| `language` | String | O idioma deve ser passado para a Braze no padrão ISO-639-1 (por exemplo, `en`). <br>Consulte nossa [lista de idiomas aceitos][1]. | Não |
| `phone` | String | Um número de telefone conforme indicado pelos seus usuários, no formato `E.164` (por exemplo, `+442071838750`). <br> Consulte [Números de Telefone do Usuário][2] para orientação sobre formatação. | Não |
| `email_open_tracking_disabled` | Booleano | verdadeiro ou falso aceito.  Defina como verdadeiro para desativar o pixel de rastreamento de abertura de ser adicionado a todos os futuros e-mails enviados a este usuário.   | Não |
| `email_click_tracking_disabled` | Booleano | verdadeiro ou falso aceito.  Defina como verdadeiro para desativar o rastreamento de cliques para todos os links dentro de um futuro e-mail, enviado para este usuário. | Não |
| `email_subscribe` | String | Os valores disponíveis são `opted_in` (explicitamente registrado para receber e-mail), `unsubscribed` (explicitamente optou por não receber e-mails) e `subscribed` (não optou por receber nem por não receber). | Não |
| `push_subscribe` | String | Os valores disponíveis são `opted_in` (registrado explicitamente para receber push mensagens), `unsubscribed` (optou explicitamente por não receber push mensagens) e `subscribed` (nem optou por receber nem por não receber). | Não |
| `time_zone` | String | O fuso horário deve ser passado para a Braze no mesmo formato que o Banco de Dados de Fuso Horário da IANA (por exemplo, `America/New_York` ou `Eastern Time (US & Canada)`).  | Não |
| `date_of_first_session` <br><br> `date_of_last_session`| String | Pode ser passado em um dos seguintes formatos ISO-8601: {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) </li> </ul> {:/} | Não |
| `subscription_group_id` | String | O `id` do seu grupo de inscrições. Este identificador pode ser encontrado na página do grupo de inscrições do seu dashboard. | Não |
| `subscription_state` | String | O estado da inscrição para o grupo de inscrições especificado por `subscription_group_id`. Os valores permitidos são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições). | Não, mas fortemente recomendado se `subscription_group_id` for usado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### Sobre IDs externos

Embora `external_id` não seja obrigatório, você **deve** incluir um desses campos: 
- `external_id`: Um identificador único de usuário para seu cliente, **ou**
- `braze_id`: Um identificador único de usuário extraído para usuários existentes do Braze, **ou**
- `user_alias_name` e `user_alias_label` : Um identificador de usuário único para um usuário anônimo

### Importando atributos personalizados

Você pode importar atributos personalizados para usuários indo para **Importar Usuários** > **Atributos**. Qualquer cabeçalho que não corresponda exatamente aos atributos padrão cria um atributo personalizado dentro do Braze.

Os seguintes tipos de dados são aceitos na importação de usuário:

| Tipo de dados | Descrição |
|-----------|-------------|
| Data e hora | Deve ser armazenado no formato ISO-8601 |
| Booleano | VERDADEIRO ou FALSO |
| Número | Número inteiro ou decimal sem espaços ou vírgulas, decimais devem usar um ponto (.) como separador decimal |
| String | Pode conter vírgulas, desde que haja aspas duplas ao redor do valor da coluna |
| Em branco | Valores em branco não substituirão os valores existentes no perfil do usuário, e você não precisa incluir todos os atributos de usuário existentes no seu arquivo CSV |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Arrays e push tokens não são suportados na importação de usuário. Especialmente para matrizes, vírgulas no seu arquivo CSV serão interpretadas como um separador de coluna, então quaisquer vírgulas nos valores causarão erros ao analisar o arquivo. <br>Para fazer upload desses tipos de valores, use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou a [ingestão de dados da nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/).
{% endalert %}

### Atualização do status do grupo de inscrições

Você pode adicionar usuários em grupos de inscrição de e-mail ou SMS através da importação de usuário. Isso é particularmente útil para SMS, porque um usuário deve estar inscrito em um grupo de inscrições de SMS para ser enviado uma mensagem pelo canal de SMS. Para saber mais, consulte os [grupos de inscrição de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Se você estiver atualizando o status do grupo de inscrições, deve ter as seguintes duas colunas em seu CSV:

- `subscription_group_id`: O `id` do [grupo de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state`: Os valores disponíveis são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
</tbody>
</table>

{% alert important %}
Apenas um único `subscription_group_id` pode ser definido por linha na importação de usuário. Diferentes linhas podem ter diferentes valores de `subscription_group_id`. No entanto, se você precisar inscrever os mesmos usuários em vários grupos de inscrição, será necessário fazer várias importações.
{% endalert %}

### Importando eventos personalizados (acesso antecipado) {#importing-custom-events}

{% alert important %}
A importação de eventos personalizados está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

Para importar eventos personalizados para seus usuários, acessar **Importar Usuários** > **Eventos**.

Eventos personalizados são personalizados para o seu negócio. Por exemplo, um app de streaming pode ter um evento personalizado chamado rented_movie. Seu CSV deve ter cabeçalhos de coluna para:

- Um dos seguintes:
  - `external_id`, **ou**
  - `braze_id`, **ou** 
  - `user_alias_name` e `user_alias_label`
- Nome
- Horário

Eventos personalizados podem ter propriedades de eventos. Por exemplo, o evento personalizado rented_movie pode ter as propriedades título e gênero. Essas propriedades de evento devem ter um cabeçalho de coluna de `<event_name>.properties.<property name>`. Um exemplo é `rented_movie.properties.title`.

| USER PROFILE FIELD                      | DATA TYPE | INFORMATION                                                                                                                                                                                                             | REQUIRED                                                                                        |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id`                           | String    | Um identificador único de usuário para seu usuário.                                                                                                                                                                                 | Sim, um de `external_id`, `braze_id`, ou `user_alias_name` e `user_alias_label` é necessário. |
| `braze_id`                              | String    | Um identificador atribuído pela Braze para o seu usuário.                                                                                                                                                                              | Sim, um de `external_id`, `braze_id`, ou `user_alias_name` e `user_alias_label` é necessário. |
| `user_alias_name`                       | String    | Um identificador de usuário único para usuários anônimos. Uma alternativa ao external_id.                                                                                                                                        | Sim, um de `external_id`, `braze_id`, ou `user_alias_name` e `user_alias_label` é necessário. |
| `user_alias_label`                      | String    | Um rótulo comum pelo qual agrupar aliases de usuário.                                                                                                                                                                          | Sim, um de `external_id`, `braze_id`, ou `user_alias_name` e `user_alias_label` é necessário. |
| `name`                                  | String    | Um evento personalizado dos seus usuários.                                                                                                                                                                                           | Sim                                                                                             |
| `time`                                  | String    | A hora do evento. Pode ser passado em um dos seguintes formatos ISO-8601: {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) </li> </ul> {:/} | Sim                                                                                             |
| `<event name>.properties.<property name>` | Múltiplas  | Uma propriedade de evento associada a um evento personalizado. Um exemplo é `rented_movie.properties.title`                                                                                                                        | Não                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Embora o próprio external_id não seja obrigatório, você deve incluir um dos seguintes campos: <br>- `external_id`: Um identificador único de usuário para seu cliente <br>- `braze_id`: Um identificador único de usuário extraído para usuários existentes do Braze <br>- `user_alias_name`: Um identificador de usuário único para um usuário anônimo
{% endalert %}

#### tamanho do CSV

A Braze aceita dados de usuários no formato CSV padrão de arquivos com até 500 MB de tamanho. Para baixar um de nossos modelos de arquivo CSV, consulte [Importando com ID externo](#importing-with-external-id) ou [Importando com alias de usuário](#importing-with-user-alias).

#### Considerações sobre pontos de dados

Cada peça de dados de cliente importada via CSV substituirá o valor existente nos perfis de usuário e contará como um ponto de dados, exceto IDs externos e valores em branco.

- IDs externos carregados via importação CSV não consumirão pontos de dados. Se você estiver carregando um arquivo CSV para segmentar usuários existentes do Braze carregando apenas IDs externos, isso pode ser feito sem consumir pontos de dados. Se você adicionar dados adicionais, como o e-mail ou número de telefone de um usuário em sua importação, isso substituirá os dados de usuários existentes e consumirá seus pontos de dados.
    - Importações de CSV para fins de segmentação (importações feitas com `external_id`, `braze_id` ou `user_alias_name` como o único campo) não consumirão pontos de dados.
- Valores em branco não substituirão os valores existentes no perfil do usuário, e você não precisa incluir todos os atributos de usuário existentes ou eventos personalizados no seu arquivo CSV.
- A atualização de `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` não contará para o consumo de dados.

{% alert important %}
Definir idioma ou país em um usuário via importação CSV ou API impedirá que a Braze capture automaticamente essas informações via SDK.
{% endalert %}

## Importando um CSV

Para importar seu arquivo CSV:
1. Acessar **público** > **Importar Usuários**. 
2. Selecione **Pesquisar arquivos** e selecione seu arquivo de interesse, depois selecione **Começar importação**. Braze fará upload do seu arquivo e verificará os cabeçalhos das colunas, bem como os tipos de dados de cada coluna.

{% alert important %}
Importações de CSV são sensíveis a maiúsculas e minúsculas. Isso significa que letras maiúsculas em importações CSV escreverão o campo como um atributo personalizado em vez de um padrão. Por exemplo, "email" está correto, mas "Email" seria gravado como um atributo personalizado.
{% endalert %}

![A opção "Eventos" é selecionada como o tipo de informação do usuário a ser importada.][5]

Após a conclusão do upload, você pode ver uma prévia do conteúdo do seu arquivo. As informações na tabela são baseadas nos valores das primeiras linhas do seu arquivo CSV.

Você pode acompanhar o progresso na página **Importar Usuários**, que atualiza a cada FIVE segundos, ou quando você seleciona **Atualizar tabela**. Você ainda pode usar o restante do dashboard do Braze durante a importação, e você receberá notificações quando a importação começar e terminar.

Você também pode visualizar suas importações mais recentes, seus nomes de arquivo, tipo de CSV, número de linhas no arquivo, número de linhas importadas com sucesso, total de linhas em cada arquivo e o status de cada importação.

Você pode importar mais de um arquivo CSV ao mesmo tempo. As importações de CSV serão executadas simultaneamente, o que significa que a ordem das atualizações não é garantida como serial. Se você precisar que as importações de CSV sejam executadas uma após a outra, espere uma importação de CSV terminar para enviar outra.

Se o processo de importação encontrar um erro, um ícone de aviso aparecerá ao lado do número total de linhas no arquivo. Você pode passar o mouse sobre o ícone para ver detalhes sobre por que certas linhas falharam. Após a importação ser concluída, todos os dados serão adicionados aos perfis existentes, ou novos perfis serão criados.

![O upload do arquivo CSV foi concluído com erros envolvendo tipos de dados misturados em uma única coluna][4]{: style="max-width:70%"}

### Considerações

Se a Braze notar algo malformado nas primeiras linhas do arquivo durante o upload, esses erros aparecerão no resumo. Por exemplo, se o seu arquivo incluir uma linha malformada, esse erro será observado na prévia quando você importar o arquivo. Embora um arquivo possa ser importado com erros, é recomendável que você corrija esses erros em seu arquivo antes de continuar com a importação.

Além disso, é importante examinar o arquivo CSV completo antes de fazer upload, pois a Braze não verifica todas as linhas do arquivo de entrada para a prévia. Isso significa que podem existir erros que a Braze não detecta ao gerar esta prévia.

Linhas malformadas e linhas sem um ID externo não serão importadas. Todos os outros erros podem ser importados, mas podem interferir na filtragem ao criar um segmento. Para saber mais, consulte a seção de [Resolução de Problemas](#troubleshooting).

{% alert warning %}
Erros são baseados apenas no tipo de dado e na estrutura do arquivo. Por exemplo, um endereço de e-mail mal formatado ainda seria importado, pois ainda pode ser analisado como uma string.
{% endalert %}

### Importação de CSV do usuário Lambda

Você pode usar nosso script de importação CSV Lambda S3 sem servidor para fazer upload de atributos de usuário para a plataforma. Essa solução funciona como um carregador de CSV onde você solta seus CSVs em um bucket S3, e os scripts fazem upload através da nossa API.

Os tempos estimados de execução para um arquivo com um milhão de linhas devem ser em torno de 5 minutos. Para saber mais, consulte [CSV de atributos do usuário para importação da Braze]({{site.baseurl}}/user_csv_lambda/).

## Segmentação

A importação de usuário cria e atualiza perfis de usuário e também pode ser usada para criar segmentos. Para criar um segmento, selecione **Gerar automaticamente um segmento a partir dos usuários que são importados deste CSV** antes de iniciar a importação.

Você pode definir o nome do segmento ou aceitar o padrão, que é o nome do seu arquivo. Os arquivos que foram usados para criar um segmento terão um link para visualizar o segmento após a importação ser concluída.

O filtro usado para criar o segmento seleciona usuários que foram criados ou atualizados em uma importação selecionada e está disponível com todos os outros filtros na página de edição do segmento.

## Solução de problemas {#troubleshooting}

### Linhas ausentes

Há algumas razões pelas quais o número de usuários importados pode não corresponder ao total de linhas no seu arquivo CSV:

- **IDs externos duplicados:** Se houver colunas de ID externo duplicadas, isso pode causar linhas malformadas ou não importadas, mesmo que as linhas estejam formatadas corretamente. Em alguns casos, isso pode não relatar um erro específico. Verifique se há IDs externos duplicados no seu CSV. Se for o caso, remova os duplicados e tente fazer o upload novamente.
- **Caracteres acentuados:** Seu arquivo CSV pode ter nomes ou atributos que incluem acentos. Certifique-se de que seu arquivo esteja codificado em UTF-8 para evitar quaisquer problemas.

### Linha malformada

Você deve incluir uma linha de cabeçalho no seu arquivo CSV para importar seus dados corretamente. Cada linha deve ter o mesmo número de células que a linha de cabeçalho. Linhas com um comprimento de mais ou menos valores do que a linha de cabeçalho serão excluídas da importação. As vírgulas em um valor serão interpretadas como um separador e podem levar a este erro. Além disso, todos os dados devem ser codificados em UTF-8.

Se o seu arquivo CSV tiver linhas em branco e importar menos linhas do que o total de linhas no arquivo CSV, isso pode não indicar um problema com a importação, pois as linhas em branco não precisariam ser importadas. Verifique o número de linhas que foram importadas corretamente e certifique-se de que corresponde ao número de usuários que você está tentando importar.

### Múltiplos tipos de dados

Braze espera que cada valor em uma coluna seja do mesmo tipo de dado. Valores que não correspondem ao tipo de dado do seu atributo causarão erros na segmentação.

### Datas formatadas incorretamente

Datas que não estiverem no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) não serão lidas como datetimes na importação.

### String com aspas

Valores encapsulados em aspas simples ('') ou duplas ('') serão lidos como strings na importação.

### Dados importados como atributo personalizado

Se você estiver vendo um pedaço de dados de usuários padrão (por exemplo, `email` ou `first_name`) importado como um atributo personalizado, verifique o caso e o espaçamento do seu arquivo CSV. Por exemplo, `First_name` seria importado como um atributo personalizado, enquanto `first_name` seria corretamente importado no campo "first name" no perfil de um usuário.

[import_template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[events_template]: {% image_buster /assets/download_file/braze-csv-events-import-template.csv %}
[template_alias_attributes]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
[template_alias_events]: {% image_buster /assets/download_file/braze-events-csv-example-user-alias.csv %}
[errors]:#common-errors
[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[5]: {% image_buster /assets/img/importcsv3.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
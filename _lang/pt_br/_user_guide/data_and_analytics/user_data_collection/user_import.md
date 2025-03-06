---
nav_title: Importação de usuários
article_title: Importação de usuários
page_order: 4
page_type: reference
description: "Este artigo de referência cobre como importar usuários para o seu dashboard da Braze usando a API REST, ingestão de dados na nuvem, CSV e melhores práticas de importação."

---
# importação de usuário

> A Braze oferece uma variedade de maneiras de importar dados de usuários para a plataforma: SDKs, APIs, ingestão de dados na nuvem, integrações com parceiros tecnológicos e arquivos CSV.

Antes de prosseguir, vale frisar que a Braze não sanitiza (valida ou formata corretamente) os dados HTML durante a importação. Isso significa que as tags de script devem ser removidas para todos os dados de importação destinados à personalização da web.

Ao importar dados para o Braze que são especificamente destinados ao uso de personalização em um navegador web, certifique-se de que eles estejam livres de HTML, JavaScript ou qualquer outra tag de script que possa ser potencialmente usada de forma maliciosa quando renderizada em um navegador web.  

Alternativamente, para HTML, você pode usar os filtros de Liquid (`strip_html`) da Braze para escapar o texto renderizado em HTML. Por exemplo:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Saída %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## API REST

Use o [endpoint`/users/track`][12] para registrar eventos personalizados, atributos de usuário e compras para usuários.

## Ingestão de dados na nuvem

Use o Braze [Cloud Data Ingestion][14] para importar e manter as atribuições de usuários. 

## importação de CSV

Você pode fazer upload e atualizar perfis de usuários através de arquivos CSV de **público** > **Importar Usuários**.

A importação de CSV suporta o registro e a atualização de atribuições do usuário, como nome e e-mail, além de atributos personalizados, como tamanho do sapato. Você pode importar um CSV especificando um dos dois identificadores exclusivos de usuário: um `external_id` ou um alias de usuário.

{% alert note %}
Se você estiver enviando vários usuários com e sem `external_id`, é preciso criar um arquivo CSV para cada importação. Um CSV não pode conter ambos `external_ids` e aliases de usuário.
{% endalert %}

### Construindo seu CSV

Existem vários tipos de dados no Braze. Ao importar ou atualizar perfis de usuários com um arquivo CSV, você pode criar ou atualizar atributos de usuário padrão ou atributos personalizados.

- Os atributos padrão do usuário são chaves reservadas no Braze. Por exemplo, `first_name` ou `email`.
- Atributos personalizados são personalizados para o seu negócio. Por exemplo, um app de reserva de viagens pode ter um atributo personalizado chamado `last_destination_searched`.

{% alert important %}
Ao importar dados de cliente, os cabeçalhos das colunas que você usa devem corresponder exatamente à ortografia e capitalização dos atributos padrão do usuário. Caso contrário, a Braze criará automaticamente um atributo personalizado no perfil desse usuário.
{% endalert %}

A Braze aceita dados de usuários no formato CSV padrão de arquivos com até 500 MB de tamanho. Consulte as seções anteriores sobre importação para modelos de CSV disponíveis para download.

#### Considerações sobre pontos de dados

Cada peça de dados de cliente importada de um arquivo CSV substituirá o valor existente nos perfis de usuário e contará como um ponto de dados, exceto para IDs externos e valores em branco. 

- IDs externos carregados de um arquivo CSV não consumirão pontos de dados. Se você estiver carregando um CSV para segmentar usuários existentes do Braze carregando apenas IDs externos, isso pode ser feito sem consumir pontos de dados. Se você adicionar mais dados como e-mails de usuários ou números de telefone na sua importação, isso substituirá os dados de usuários existentes, consumindo seus pontos de dados.
  - Importações de CSV para fins de segmentação (importações feitas com `external_id`, `braze_id` ou `user_alias_name` como o único campo) não consumirão pontos de dados.
- Valores em branco não substituirão os valores existentes no perfil do usuário, e você não precisa incluir todos os atributos de usuário existentes no seu arquivo CSV.
- A atualização de `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` não contará para o consumo de dados.

{% alert important %}
A configuração de `language` ou `country` em um usuário por importação de CSV ou API impedirá que a Braze capture automaticamente essas informações por meio do SDK.
{% endalert %}

#### Cabeçalhos de colunas de dados de usuários padrão

| USER PROFILE FIELD | DATA TYPE | INFORMATION | REQUIRED |
|---|---|---|---|
| `external_id` | String | Um identificador único de usuário para seu cliente. | Sim, veja a seguinte nota |
| `user_alias_name` | String | Um identificador de usuário único para usuários anônimos. Uma alternativa ao `external_id`. | Não, veja a seguinte nota |
| `user_alias_label` | String | Um rótulo comum pelo qual agrupar aliases de usuário. | Sim se `user_alias_name` for usado |
| `first_name` | String | O nome dos seus usuários conforme indicado (por exemplo, `Jane`). | Não |
| `last_name` | String | O último nome de seus usuários conforme indicado (por exemplo, `Doe`). | Não |
| `email` | String | O e-mail dos seus usuários conforme indicado (por exemplo, `jane.doe@braze.com`). | Não |
| `country` | String | Os códigos de país devem ser passados para a Braze no padrão ISO-3166-1 alpha-2 (por exemplo, `GB`). | Não |
| `dob` | String | Deve ser passado no formato "AAAA-MM-DD" (por exemplo, `1980-12-21`). Isso importará a Data de Nascimento do seu usuário e ativará você para segmentar usuários cujo aniversário é "hoje". | Não |
| `gender` | String | "M", "F", "O" (outro), "N" (não aplicável), "P" (prefere não dizer) ou nil (desconhecido). | Não |
| `home_city` | String | A cidade natal dos seus usuários conforme indicado (por exemplo, `London`). | Não |
| `language` | String | O idioma deve ser passado para a Braze no padrão ISO-639-1 (por exemplo, `en`). <br>Consulte nossa [lista de idiomas aceitos][1]. | Não |
| `phone` | String | Um número de telefone conforme indicado pelos seus usuários, no formato `E.164` (por exemplo, `+442071838750`). <br> Consulte [Números de Telefone do Usuário][2] para obter orientações sobre formatação. | Não |
| `email_open_tracking_disabled` | Booleano | verdadeiro ou falso aceito.  Defina como verdadeiro para desativar o pixel de rastreamento de abertura de ser adicionado a todos os futuros e-mails enviados a este usuário.   | Não |
| `email_click_tracking_disabled` | Booleano | verdadeiro ou falso aceito.  Defina como verdadeiro para desativar o rastreamento de cliques para todos os links dentro de um futuro e-mail, enviado para este usuário. | Não |
| `email_subscribe` | String | Os valores disponíveis são `opted_in` (explicitamente registrado para receber e-mail), `unsubscribed` (explicitamente optou por não receber e-mails) e `subscribed` (não optou por receber nem por não receber). | Não |
| `push_subscribe` | String | Os valores disponíveis são `opted_in` (registrado explicitamente para receber push mensagens), `unsubscribed` (optou explicitamente por não receber push mensagens) e `subscribed` (nem optou por receber nem por não receber). | Não |
| `time_zone` | String | O fuso horário deve ser passado para a Braze no mesmo formato que o Banco de Dados de Fuso Horário da IANA (por exemplo, `America/New_York` ou `Eastern Time (US & Canada)`).  | Não |
| `date_of_first_session` <br><br> `date_of_last_session`| String | Pode ser passado em um dos seguintes formatos ISO 8601: {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) </li> </ul> {:/} | Não |
| `subscription_group_id` | String | O `id` do seu grupo de inscrições. Este identificador pode ser encontrado na página do grupo de inscrições do seu dashboard. | Não |
| `subscription_state` | String | O estado da inscrição para o grupo de inscrições especificado por `subscription_group_id`. Os valores permitidos são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições). | Não, mas fortemente recomendado se `subscription_group_id` for usado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Embora `external_id` não seja obrigatório, você **deve** incluir um desses campos:
- `external_id`: Um identificador único de usuário para seu cliente <br> \- OU -
- `braze_id`: Um identificador único de usuário extraído para usuários existentes do Braze <br> \- OU -
- `user_alias_name`: Um identificador de usuário único para um usuário anônimo
{% endalert %}

### Importando um CSV

Para importar o arquivo CSV, acesse **Públicos** > **Importação de usuário**. Aqui, você encontrará uma tabela que lista as importações mais recentes, que inclui detalhes como a data de fazer upload, o nome do responsável pelo upload, nome do arquivo, disponibilidade de direcionamento, número de linhas importadas e status de cada importação.

![A página "Importar usuários" no dashboard do Braze.][3]

Selecione **Procurar Arquivos** e seu arquivo. Braze fará upload do seu arquivo e verificará os cabeçalhos das colunas e os tipos de dados de cada coluna.

Para baixar um modelo CSV, consulte as seções [Importando com ID externo](#importing-with-external-id) ou [Importando com alias de usuário](#importing-with-user-alias) nesta página.

{% alert important %}
Importações de CSV são sensíveis a maiúsculas e minúsculas. Isso significa que letras maiúsculas em importações CSV escreverão o campo como um atributo personalizado em vez de um padrão. Por exemplo, "email" está correto, mas "Email" seria gravado como um atributo personalizado.
{% endalert %}

Após a conclusão do upload, você pode ver uma prévia do conteúdo do seu arquivo. Todas as informações nesta tabela são baseadas nos valores das primeiras linhas do seu arquivo CSV. Para cabeçalhos de coluna, os atributos padrão são escritos em texto normal, enquanto os atributos personalizados são <i>italicizados</i> e têm seu tipo anotado entre parênteses. Há também um resumo do seu arquivo no topo do pop-up.

Você pode importar mais de um CSV ao mesmo tempo. As importações de CSV são executadas simultaneamente, o que significa que a ordem das atualizações não é garantida como serial. Se você precisar que as importações de CSV sejam executadas uma após a outra, espere uma importação de CSV terminar para enviar outra.

Se a Braze notar algo malformado no arquivo durante o upload, esses erros aparecerão no resumo. Por exemplo, se o seu arquivo incluir uma linha malformada, esse erro será anotado na prévia quando você importar o arquivo. Então, um arquivo pode ser importado com erros, mas uma importação não pode ser cancelada ou revertida depois de iniciada. Revise a prévia e, se encontrar algum erro, cancele a importação e modifique seu arquivo. 

{% alert important %}
Examine todo o arquivo CSV antes de fazer o upload, pois a Braze não verifica todas as linhas do arquivo de entrada para a prévia. Isso significa que podem existir erros que a Braze não detecta ao gerar esta prévia.
{% endalert %}

Linhas malformadas e linhas sem um ID externo não serão importadas. Todos os outros erros podem ser importados, mas podem interferir na filtragem ao criar um segmento. Para saber mais, pule para a seção [Resolução de Problemas](#troubleshooting).

![O upload do arquivo CSV foi concluído com erros envolvendo tipos de dados misturados em uma única coluna][4]{: style="max-width:70%"}

{% alert warning %}
Erros são baseados apenas no tipo de dado e na estrutura do arquivo. Por exemplo, um endereço de e-mail mal formatado ainda seria importado, pois ainda pode ser analisado como uma string.
{% endalert %}

Quando você estiver satisfeito com o upload, inicie a importação. O pop-up será fechado e a importação começará em segundo plano. Você pode acompanhar o progresso na página de **importação de usuário**, que será atualizada a cada FIVE segundos, ou ao pressionar o botão de atualização na caixa de **Importações Recentes**.

Sob **Linhas Processadas** está o progresso da importação; o status mudará para **Concluído** quando terminado. Você ainda pode usar o restante do dashboard do Braze durante a importação e receberá notificações quando a importação começar e terminar.

Se o processo de importação encontrar um erro, um ícone de aviso amarelo será exibido ao lado do número total de linhas no arquivo. Você pode passar o cursor sobre o ícone para ver detalhes sobre por que certas linhas falharam. Após a importação ser concluída, todos os dados serão adicionados aos perfis existentes ou novos perfis serão criados.

### Importando com ID externo

Ao importar os dados de seus clientes, você precisará especificar o identificador exclusivo de cada cliente (`external_id`). Antes de iniciar sua importação de CSV, é importante entender com sua equipe de engenharia como os usuários serão identificados no Braze. Normalmente, este é um ID de banco de dados interno. Isso deve estar alinhado com a forma como os usuários serão identificados pelo Braze SDK em dispositivos móveis e web e é projetado para que cada cliente tenha um único perfil de usuário no Braze em todos os seus dispositivos. Leia mais sobre o [ciclo de vida do perfil de usuário][13] da Braze.

Quando você fornece um `external_id` na sua importação, a Braze atualizará qualquer usuário existente com o mesmo `external_id` ou criará um novo usuário identificado com esse conjunto de `external_id` se não for encontrado nenhum.

**Baixe:** [Modelo de importação CSV][template]

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

**Baixe:** [Modelo de Importação de eventos de alias CSV][template_alias_events]

### Importando com Braze ID

Para atualizar perfis de usuário existentes na Braze usando um valor de ID interno da Braze em vez de um `external_id` ou `user_alias_name` e `user_alias_label`, especifique `braze_id` como um cabeçalho de coluna.

Isso pode ser útil se você exportou dados de usuários do Braze através da nossa opção de exportação CSV dentro da segmentação e deseja adicionar um novo atributo personalizado a esses usuários existentes.

{% alert important %}
Você não pode usar uma importação CSV para criar um novo usuário usando `braze_id`. Este método só pode ser usado para atualizar usuários pré-existentes na plataforma Braze.
{% endalert %}

{% alert tip %}
O valor `braze_id` pode ser rotulado como `Appboy ID` nas exportações CSV do dashboard da Braze. Este ID será o mesmo que o `braze_id` para um usuário, então você pode renomear esta coluna para `braze_id` quando reimportar o CSV.
{% endalert %}

### Importação com endereços de e-mail e números de telefone

É possível omitir uma ID externa ou um alias de usuário e usar apenas um endereço de e-mail ou número de telefone para a importação de usuários. Antes de importar um arquivo CSV com endereços de e-mail ou números de telefone, verifique o seguinte:

- Verifique se não há IDs externos ou aliases de usuário para esses perfis.
- Confirme se o arquivo CSV está formatado corretamente.

{% alert note %}
Se incluir endereços de e-mail e números de telefone em seu arquivo CSV, o endereço de e-mail terá prioridade sobre o número de telefone ao procurar perfis.
{% endalert %}

Se um perfil existente tiver esse endereço de e-mail ou número de telefone, esse perfil será atualizado e o Braze não criará um novo perfil. Se houver vários perfis com o mesmo endereço de e-mail, o Braze usará a mesma lógica do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), no qual o perfil atualizado mais recentemente será atualizado.

Se não houver um perfil com esse endereço de e-mail ou número de telefone, o Braze criará um novo perfil com esse identificador. Você pode usar o [endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) para identificar esse perfil posteriormente. Para excluir um perfil de usuário, você também pode usar o endpoint [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete).

### Importando dados personalizados

Todos os cabeçalhos que não corresponderem exatamente aos dados de usuários padrão criarão um atributo personalizado no Braze.

Os seguintes tipos de dados são aceitos na importação de usuário:
- **Data e hora:** Deve ser armazenado no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)
- **Booleano:** `true` ou `false`
- **Número:** Inteiro ou float sem espaços ou vírgulas; os floats devem usar um ponto (`.`) como separador decimal
- **String:** Pode conter vírgulas se houver aspas duplas (`""`) ao redor do valor da coluna
- **Em branco:** Os valores em branco não substituirão os valores existentes no perfil do usuário, e não é necessário incluir todas as atribuições do usuário existentes no arquivo CSV

{% alert important %}
Vetores, tokens de push e tipos de dados de eventos personalizados não são aceitos na importação de usuários.
Especialmente para matrizes, as vírgulas em seu arquivo CSV serão interpretadas como um separador de coluna, portanto, qualquer vírgula nos valores causará erros na análise do arquivo.<br><br>Para fazer upload desses tipos de valores, use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou a [ingestão de dados da nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/).
{% endalert %}

### Importação de CSV do usuário Lambda

Você pode usar nosso script de importação CSV Lambda S3 sem servidor para fazer upload de atributos de usuário para a plataforma. Essa solução funciona como um carregador de CSV onde você solta seus CSVs em um bucket S3, e os scripts fazem upload através da nossa API.

O tempo de execução estimado para um arquivo com 1.000.000 de linhas deve ser de cerca de cinco minutos. Para saber mais, consulte [CSV de atributos do usuário para importação da Braze]({{site.baseurl}}/user_csv_lambda/).

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
Apenas um único `subscription_group_id` pode ser definido por linha na importação de usuário. Diferentes linhas podem ter diferentes valores de `subscription_group_id`. No entanto, se for necessário inscrever os mesmos usuários em vários grupos de inscrições, será necessário fazer várias importações.
{% endalert %}

## Criação de segmentos a partir de uma importação de usuário

A importação de usuários também pode ser usada para criar segmentos, selecionando **Gerar automaticamente um segmento a partir dos usuários que são importados desse CSV** antes de iniciar a importação.

Você pode definir o nome do segmento ou aceitar o padrão, que é o nome do seu arquivo. Os arquivos que foram usados para criar um segmento terão um link para visualizar o segmento após a importação ser concluída.

O filtro usado para criar o segmento seleciona usuários que foram criados ou atualizados em uma importação selecionada e está disponível com todos os outros filtros na página de edição do segmento.

## Considerações

{% multi_lang_include email-via-sms-warning.md %}

## Solução de problemas

### Linhas ausentes

Há algumas razões pelas quais o número de usuários importados pode não corresponder ao total de linhas no seu arquivo CSV:

- **IDs externos duplicados:** Se houver colunas de ID externas duplicadas, isso poderá causar linhas malformadas ou não importadas, mesmo que as linhas estejam formatadas corretamente. Em alguns casos, isso pode não relatar um erro específico. Verifique se há IDs externos duplicados no seu CSV. Se for o caso, remova os duplicados e tente fazer o upload novamente.
- **Caracteres acentuados:** Seu CSV pode ter nomes ou atributos que incluem acentos. Certifique-se de que seu arquivo esteja codificado em UTF-8 para evitar quaisquer problemas.

### Linha malformada

Deve haver uma linha de cabeçalho para importar os dados corretamente. Cada linha deve ter o mesmo número de células que a linha de cabeçalho. Linhas com um comprimento de mais ou menos valores do que a linha de cabeçalho serão excluídas da importação. As vírgulas em um valor serão interpretadas como um separador e podem levar a esse erro. Além disso, todos os dados devem ser codificados em UTF-8.

Se o seu arquivo CSV tiver linhas em branco e importar menos linhas do que o total de linhas no arquivo CSV, isso pode não indicar um problema com a importação, pois as linhas em branco não precisariam ser importadas. Verifique o número de linhas que foram importadas corretamente e certifique-se de que corresponde ao número de usuários que você está tentando importar.

### Múltiplos tipos de dados

Braze espera que cada valor em uma coluna seja do mesmo tipo de dado. Os valores que não corresponderem ao tipo de dados do atributo causarão erros na segmentação.

### Datas formatadas incorretamente

As datas que não estiverem no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) não serão lidas como `datetimes` na importação.

### String com aspas

Os valores encapsulados entre aspas simples (`''`) ou duplas (`""`) serão lidos como strings na importação.

### Dados importados como atributo personalizado

Se uma parte dos dados padrão de usuários (como `email` ou `first_name`) for importada como um atributo personalizado, verifique as letras maiúsculas e minúsculas e o espaçamento do arquivo CSV. Por exemplo, `First_name` seria importado como um atributo personalizado, enquanto `first_name` seria corretamente importado no campo "first name" no perfil de um usuário.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[errors]:#common-errors
[template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}

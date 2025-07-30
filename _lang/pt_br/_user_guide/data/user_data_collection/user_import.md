---
nav_title: Importação de usuários
article_title: Importação de usuários
page_order: 4
description: "Saiba mais sobre as várias opções de importação de usuários do Braze, como importação de CSV, API REST, ingestão de dados na nuvem e muito mais."

---
# importação de usuário

> Saiba mais sobre as várias opções de importação de usuários do Braze, como importação de CSV, API REST, ingestão de dados na nuvem e muito mais.

## Sobre a validação de HTML

Lembre-se de que o Braze não higieniza, valida ou reformata dados HTML durante a importação, o que significa que as tags de script devem ser removidas de todos os dados de importação que você usar para personalização da Web.

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

## Opções de importação

### Importação de CSV da Braze

É possível usar a importação de CSV para registrar e atualizar os seguintes atributos de usuário e eventos personalizados. Para começar, consulte [Importação de CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

|Tipo|Definição|Exemplo|Tamanho máximo do arquivo|
|---|---|---|---|
|Atributos padrão|Atribuições reservadas do usuário reconhecidas pelo Braze.|`first_name`, `email`|500 MB|
|Atributos personalizados|Atribuições do usuário exclusivas para a sua empresa.|`last_destination_searched`|500 MB|
|Eventos personalizados|Eventos exclusivos da sua empresa que representam ações do usuário.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Importação de CSV do usuário Lambda

Você pode usar nosso script de importação de CSV S3 Lambda sem servidor para fazer upload das atribuições do usuário para o Braze. Essa solução funciona como um carregador de CSV onde você solta seus CSVs em um bucket S3, e os scripts fazem upload através da nossa API.

O tempo de execução estimado para um arquivo com 1.000.000 de linhas deve ser de cerca de cinco minutos. Para saber mais, consulte [CSV de atributos do usuário para importação da Braze](https://www.braze.com/docs/user_guide/data/cloud_ingestion/).

### API REST

Use o [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar eventos personalizados, atributos de usuário e compras para usuários.

### Ingestão de dados na nuvem

Use [a Ingestão de Dados]({{site.baseurl}}/user_guide/data/cloud_ingestion/) do Braze [Cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/) para importar e manter as atribuições de usuários.

## E-mails de transações legalmente exigidas

{% multi_lang_include email-via-sms-warning.md %}

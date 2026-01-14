---
nav_title: Importando usuários
article_title: Importando usuários
page_order: 4.1
description: "Saiba mais sobre as várias opções de importação de usuários do Braze, como importação CSV, API REST, Ingestão de Dados na Nuvem e mais."

---
# Importando usuários

> Saiba mais sobre as várias opções de importação de usuários do Braze, como importação CSV, API REST, Ingestão de Dados na Nuvem e mais.

## Sobre a validação de HTML

Tenha em mente que o Braze não sanitiza, valida ou reformata dados HTML durante a importação, o que significa que as tags de script devem ser removidas de todos os dados de importação que você usa para personalização na web.

Ao importar dados para o Braze que são especificamente destinados ao uso de personalização em um navegador da web, certifique-se de que estejam livres de HTML, JavaScript ou qualquer outra tag de script que possa ser utilizada maliciosamente quando renderizada em um navegador da web.

Alternativamente, para HTML, você pode usar filtros Liquid do Braze (`strip_html`) para escapar texto renderizado em HTML. Por exemplo:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Opções de importação

### Importação CSV do Braze

Você pode usar a importação CSV para registrar e atualizar os seguintes atributos de usuário e eventos personalizados. Para começar, veja [Importação CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

|Tipo|Definição|Exemplo|Tamanho máximo do arquivo|
|---|---|---|---|
|Atributos padrão|Atributos de usuário reservados reconhecidos pelo Braze.|`first_name`, `email`|500 MB|
|Atributos Personalizados|Atributos de usuário únicos para o seu negócio.|`last_destination_searched`|500 MB|
|Eventos Personalizados|Eventos únicos para o seu negócio que representam ações do usuário.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Importação de CSV de usuário Lambda

Você pode usar nosso script de importação de CSV Lambda S3 sem servidor para enviar atributos de usuário para o Braze. Esta solução funciona como um carregador de CSV onde você coloca seus CSVs em um bucket S3, e os scripts os enviam através da nossa API.

Os tempos de execução estimados para um arquivo com 1.000.000 de linhas devem ser em torno de cinco minutos. Veja [Atributo de usuário CSV para importação no Braze](https://www.braze.com/docs/user_guide/data/cloud_ingestion/) para mais informações.

### API REST

Use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar eventos personalizados, atributos de usuário e compras para usuários.

### Ingestão de Dados na Nuvem

Use o [Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/) do Braze para importar e manter atributos de usuário.

## E-mails transacionais exigidos por lei

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

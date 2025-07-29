---
nav_title: Importação de usuários
article_title: Importação de usuários
page_order: 4
description: ""

---
# importação de usuário

> 

## 



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

## 

### 

 

|||||
|---|---|---|---|
|||||
|||||
|||||


### Importação de CSV do usuário Lambda

 Essa solução funciona como um carregador de CSV onde você solta seus CSVs em um bucket S3, e os scripts fazem upload através da nossa API.

O tempo de execução estimado para um arquivo com 1.000.000 de linhas deve ser de cerca de cinco minutos. 

### API REST



### Ingestão de dados na nuvem



## 

{% multi_lang_include email-via-sms-warning.md %}

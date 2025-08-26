---
nav_title: Filtros avançados
article_title: Filtros avançados para líquidos
page_order: 4
description: "Este artigo de referência lista filtros avançados, exemplos e como eles podem ser usados em sua campanha."

---

# Filtros avançados

> Este artigo de referência fornece uma visão geral dos filtros avançados em Liquid e como eles podem ser usados.

## Filtros de codificação

{% raw %}
| Nome do filtro | Descrição do filtro | Exemplo de entrada | Exemplo de saída
\|---|---|---|---|
`md5` | Retorna uma string codificada em md5 | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
`sha1` | Retorna uma string codificada em sha1 | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
`sha2` | Retorna uma string codificada em sha2 (256 bits, também conhecida como SHA-256) | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204
`base64` | Retorna uma string codificada em base64 | `{{'blah' | base64_encode}}` | YmxhaA==== |
`hmac_sha1_hex` (anteriormente `hmac_sha1`) | Retorna a assinatura hmac-sha1, codificada como uma string hexadecimal | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
`hmac_sha1_base64` | Retorna a assinatura hmac-sha1, codificada como uma string base64. `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
`hmac_sha256_hex` | Retorna a assinatura hmac-sha256, codificada como uma string hexadecimal | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
`hmac_sha256_base64` | Retorna a assinatura hmac-sha256, codificada como uma string base64 | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros de URL

| nome do filtro | descrição do filtro | exemplo de entrada | exemplo de saída |
|---|---|---|---|
| `url_escape` | Identifica todos os caracteres em uma string que não são permitidos em URLS e substitui os caracteres por suas variantes com escape | `{{'hey<>hi' | url_escape}}` | ei%3C%3Ehi |
| `url_param_escape` | Substitui todos os caracteres em uma string que não são permitidos em URLs por suas variantes com escape, incluindo o E comercial (&) | `{{'hey<&>hi' | url_param_escape}` | ei%3C%26%3Ehi |
| `url_encode` | Codifica uma string que é compatível com o URL | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}
{% alert tip %}
A tag `assign` pode ser combinada com HTML para economizar tempo e esforço ao criar vários hiperlinks.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## Filtro de acessório de propriedade

| nome do filtro | descrição do filtro |
|---|---|---|---|
| `property_accessor` | Recebe um hash e uma chave de hash e retorna o valor nesse hash com essa chave |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Exemplo de hash:** `{"a" => 42, "b" => 0}`
**Exemplo de entrada:** `{{hash | property_accessor: 'a'}}`
**Exemplo de saída:** `42`

Além disso, o filtro acessório de propriedade permite modelar um atributo personalizado em uma chave de hash para acessar um valor de hash específico.

{% endraw %}

{% alert note %}
Não há como instanciar um hash como uma variável (como uma expressão) no Liquid dentro da Braze.
{% endalert %}

{% raw %}

## Filtros de formatação de números

| nome do filtro | descrição do filtro | exemplo de entrada | exemplo de saída |
|---|---|---|---|
| `number_with_delimiter` | Formata um número com vírgulas | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Filtro de escape JSON / escape de string

| nome do filtro | descrição do filtro |
|---|---|
| `json_escape` | Escapa todos os caracteres especiais em uma string (como aspas duplas `""` e barra invertida ''). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Esse filtro deve ser sempre usado ao personalizar uma string em um dicionário JSON e é útil principalmente para webhooks.

## filtros de formatação JSON

| nome do filtro | descrição do filtro |
|---|---|
| `json_parse` | Converte uma string JSON em uma estrutura de dados correspondente, como um objeto ou array. | 
| `as_json_string` | Converte uma estrutura de dados, como um objeto ou array, em uma string JSON correspondente. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

{% details exemplo de entrada e saída json_parse %}

### Entrada 

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
```

### Resultado

```liquid
{% for item in my_data %}
Item ID: {{ item.id }}
Item Name: {{ item.store_name }}
{% endfor %}
```
{% endraw %}

{% enddetails %}

{% details exemplo de entrada e saída as_json_string %}

### Entrada

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
{% assign json_string = my_data | as_json_string %}
```

### Resultado

```liquid
{{json_string}}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values

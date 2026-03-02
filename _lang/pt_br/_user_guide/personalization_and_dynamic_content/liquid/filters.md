---
nav_title: Filtros
article_title: Filtros Liquid
page_order: 3
description: "Esta página de referência lista os filtros que podem ser usados para reformatar conteúdo estático ou dinâmico."

---

# Filtros

> Este artigo de referência fornece uma visão geral dos filtros no Liquid e aborda quais filtros são compatíveis com a Braze. Está procurando ideias de como usar esses filtros? Confira nossa [biblioteca de casos de uso do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

Os filtros são a forma como você pode modificar a saída de números, strings, variáveis e objetos no Liquid. Você pode usar filtros para reformatar textos estáticos ou dinâmicos, como alterar uma string de minúscula para maiúscula, ou para realizar operações matemáticas, como adição ou divisão.

{% alert important %}
A Braze não é compatível com todos os filtros Liquid da Shopify. Esta página tenta listar os filtros Liquid que a Braze testou, mas pode não ser uma lista completa. Sempre teste seu Liquid antes de enviar qualquer mensagem. <br><br>Se tiver alguma dúvida sobre um filtro que não esteja listado aqui, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Sintaxe do filtro

{% raw %}

Os filtros devem ser colocados em uma tag de saída `{{ }}` e são indicados por um caractere de pipe `|`.

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

Neste exemplo, `Big Sale` é uma string e `upcase` é o filtro que está sendo aplicado.

{% alert note %}
Os filtros podem ser usados em instruções `assign` e tags de saída {% raw %}(`{{ }}`){% endraw %}, mas não em condicionais (`if`, `elsif`, `unless`), `case`/`when`, loops `for` ou colchetes de acesso a arrays. Para usar um valor filtrado em um desses contextos, atribua o resultado a uma variável primeiro. Para mais detalhes, consulte [Onde usar operadores e filtros]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#where-to-use-operators-and-filters).
{% endalert %}

### Sintaxe para vários filtros

Você pode usar vários filtros em uma saída. Eles são aplicados da esquerda para a direita.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de array

Os filtros de array são usados para alterar a saída dos arrays.

| Filtro               | Definição                                                                                                         | Compatível |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join](https://shopify.dev/docs/api/liquid/filters/join)          | Une os elementos de um array com o caractere passado como parâmetro. O resultado é uma única string.          | ✅  Sim   |
| [first](https://shopify.dev/docs/api/liquid/filters/first)         | Retorna o primeiro elemento de um array. Em um array de atributos personalizados, esse é o valor adicionado mais antigo.                | ✅  Sim   |
| [last](https://shopify.dev/docs/api/liquid/filters/last)          | Retorna o último elemento de um array. Em um array de atributos personalizados, esse é o valor adicionado mais recentemente.          | ✅  Sim   |
| [compact](https://shopify.dev/api/liquid/filters/compact)       | Remove todos os itens `nil` de um array.                                                                             | ✅  Sim   |
| [concat](https://shopify.dev/api/liquid/filters/concat)        | Combina um array com outro array.                                                                              | ✅  Sim   |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index)         | Retorna o item no local de índice especificado em um array. O primeiro item em um array é referenciado com `[0]`. | ⛔  Não   |
| [map](https://shopify.dev/api/liquid/filters/map)           | Aceita o atributo de um elemento do array como parâmetro e cria um array a partir do valor de cada elemento do array.        | ✅  Sim   |
| [reverse](https://shopify.dev/api/liquid/filters/reverse)       | Inverte a ordem dos itens em um array.                                                                       | ✅  Sim   |
| [size](https://shopify.dev/api/liquid/filters/size)          | Retorna o tamanho de uma string (o número de caracteres) ou de um array (o número de elementos).                      | ✅  Sim   |
| [slice](https://shopify.dev/api/liquid/filters/slice)        | Retorna uma substring de uma string ou um subconjunto de um array, começando no índice especificado.                          | ✅  Sim   |
| [sort](https://shopify.dev/api/liquid/filters/sort)         | Classifica os elementos de um array por um determinado atributo de um elemento do array.                                    | ✅  Sim   |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | Classifica os itens de um array em ordem alfabética sem distinção entre maiúsculas e minúsculas.                                                | ✅  Sim   |
| [uniq](https://shopify.dev/api/liquid/filters/uniq)         | Remove quaisquer instâncias duplicadas de elementos em um array.                                                           | ✅  Sim   |
| [where](https://shopify.dev/api/liquid/where)        | Filtra um array para incluir apenas itens com um valor de propriedade específico.                                             | ✅  Sim   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros de cores

[Os filtros de cores](https://shopify.dev/api/liquid/filters/color-filters) não são compatíveis com a Braze.

## Filtros de fonte

[Os filtros de fonte](https://shopify.dev/api/liquid/filters/font-filters) não são compatíveis com a Braze.

## Filtros matemáticos

Os filtros matemáticos permitem que você realize operações matemáticas. Se você usar vários filtros em uma saída, eles serão aplicados da esquerda para a direita.

| Filtro  | Definição      | Compatível |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/abs)        | Retorna o valor absoluto de um número.     | ✅  Sim   |
| [at_most](https://shopify.dev/api/liquid/filters/at_most)    | Limita um número a um valor máximo.   | ✅  Sim   |
| [at_least](https://shopify.dev/api/liquid/filters/at_least)   | Limita um número a um valor mínimo.   | ✅  Sim   |
| [ceil](https://shopify.dev/api/liquid/filters/ceil)       | Arredonda uma saída para cima até o número inteiro mais próximo.  | ✅  Sim   |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | Divide uma saída por um número. A saída é arredondada para baixo até o número inteiro mais próximo. Confira a dica a seguir para evitar o arredondamento. | ✅  Sim   |
| [floor](https://shopify.dev/api/liquid/filters/floor)      | Arredonda uma saída para baixo até o número inteiro mais próximo.        | ✅  Sim   |
| [minus](https://shopify.dev/api/liquid/filters/minus)      | Subtrai um número de uma saída.          | ✅  Sim   |
| [plus](https://shopify.dev/api/liquid/filters/plus)       | Adiciona um número a uma saída.     | ✅  Sim   |
| [round](https://shopify.dev/api/liquid/filters/round)      | Arredonda a saída para o número inteiro mais próximo ou para o número especificado de casas decimais.  | ✅  Sim   |
| [times](https://shopify.dev/api/liquid/filters/times)     | Multiplica uma saída por um número.       | ✅  Sim   |
| [modulo](https://shopify.dev/api/liquid/filters/modulo)    | Divide uma saída por um número e retorna o resto.   | ✅  Sim   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Ao dividir números inteiros por números inteiros no Liquid, se a resposta for um float (número com decimal), o Liquid arredondará automaticamente para baixo até o número inteiro mais próximo. No entanto, a divisão de números inteiros por floats sempre resultará em um float. Isso significa que você pode transformar seus números inteiros em float (1.0, 2.0, 3.0) para retornar um float.
{% raw %}
<br><br>Por exemplo,`{{15 | divided_by: 2}}` produzirá `7`, enquanto `{{15 | divided_by: 2.0}}` produzirá `7.5`.
{% endraw %}
{% endalert %}

### Operações matemáticas com atributos personalizados

Lembre-se de que não é possível realizar operações matemáticas entre dois atributos personalizados.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Esse exemplo não funcionaria porque não é possível fazer referência a vários atributos personalizados em uma linha do Liquid. Em vez disso, você precisaria atribuir uma variável a pelo menos um desses valores antes de executar as funções matemáticas. A adição de dois atributos personalizados exigiria duas linhas de Liquid:

1. Uma para atribuir o atributo personalizado a uma variável,
2. Uma para realizar a adição.

#### Caso de uso: Calcular o saldo atual

Digamos que queremos calcular o saldo atual de um usuário adicionando o saldo do cartão-presente e o saldo de recompensas.

1. Use a tag `assign` para substituir o atributo personalizado de `current_rewards_balance` pelo termo "balance". Isso significa que agora você tem uma variável chamada `balance`, que pode ser manipulada.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2. Use o filtro `plus` para combinar o saldo do cartão-presente de cada usuário com seu saldo de recompensas, representado pelo objeto `{{balance}}`. 
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de dinheiro

Se estiver atualizando um usuário sobre uma compra, um saldo de conta ou qualquer coisa relacionada a dinheiro, você deve usar filtros de dinheiro. Os filtros de dinheiro garantem que as casas decimais estejam no lugar correto e que nenhuma parte da sua atualização seja perdida (como aquele incômodo `0` no final).

| Filtro         | Definição          | Compatível |
| :--------------- | :--------------- | :-------- |
| [money](https://shopify.dev/api/liquid/filters/money)      | Formata números para garantir que os decimais estejam no lugar correto e que zeros não sejam eliminados no final de nenhum número.   | ✅  Sim   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency)    | Formata números com o símbolo de moeda.     | ⛔  Não    |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency)     | Formata números sem o símbolo de moeda.      | ⛔  Não    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Para formatar corretamente um número com o filtro `money`, remova todas as vírgulas do número e adicione o filtro `plus: 0` antes do filtro `money`. Por exemplo, veja o seguinte Liquid:<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Filtro de dinheiro da Shopify versus filtro de dinheiro da Braze

{% alert warning %}
O comportamento do filtro `money` da Shopify é diferente de como ele é usado na Braze. Consulte os exemplos a seguir para obter uma descrição precisa do comportamento esperado.
{% endalert %}

{% raw %}
Caso esteja inserindo um atributo personalizado (como `account_balance`), sempre use o filtro `money` para colocar as casas decimais no lugar correto e evitar que os zeros sejam eliminados no final de qualquer número:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| COM O FILTRO DE DINHEIRO                       | SEM O FILTRO DE DINHEIRO                    |
| :------------------------------------------ | :------------------------------------------ |
| ![Com filtro de dinheiro]({% image_buster /assets/img/with_money_filter.png %})                     | ![Sem filtro de dinheiro]({% image_buster /assets/img/without_money_filter.png %})                  |
| Onde `account_balance` é a entrada em `17.8`. | Onde `account_balance` é a entrada em `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

O filtro `money` na Braze é diferente do da Shopify porque não aplica automaticamente os pontos decimais de acordo com uma configuração predefinida. Por exemplo, considere o seguinte cenário em que `rewards_redeemed` contém um valor de `145`:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

De acordo com o filtro [money](https://shopify.dev/api/liquid/filters/money) da Shopify, a saída deveria ser `$1.45`, no entanto, na Braze, a saída será `$145.00`. Como solução alternativa, podemos usar o filtro `divided_by` para transformar o número em um decimal antes de aplicar o filtro de dinheiro:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de string

Os filtros de string são usados para manipular as saídas e as variáveis das strings. As strings são uma combinação de caracteres alfanuméricos e devem ser colocadas entre aspas retas.

{% alert note %}
As aspas retas são diferentes das aspas curvas no Liquid. Tenha cuidado ao copiar e colar o Liquid de um editor de texto para a Braze, pois as aspas curvas causarão erros em seu Liquid. Se estiver escrevendo seu Liquid diretamente na Braze, as aspas retas serão aplicadas automaticamente.
{% endalert %}

| Filtro          | Descrição     | Compatível |
| :--------------- | ------------- | --------- |
| [append](https://shopify.dev/api/liquid/filters/append)     | Acrescenta caracteres a uma string.           | ✅  Sim   |
| [camelize](https://shopify.dev/docs/api/liquid/filters/camelize)     | Converte uma string em CamelCase.             | ⛔  Não    |
| [capitalize](https://shopify.dev/api/liquid/filters/capitalize)     | Coloca a primeira palavra em maiúscula em uma string e converte os caracteres restantes para minúsculas.         | ✅  Sim   |
| [downcase](https://shopify.dev/api/liquid/filters/downcase)      | Converte uma string em letras minúsculas.         | ✅  Sim   |
| [escape](https://shopify.dev/api/liquid/filters/escape)    | Escapa uma string.             | ✅  Sim   |
| [handleize](https://shopify.dev/api/liquid/filters/handleize)        | Formata uma string em um identificador.        | ⛔  Não    |
| [md5](https://shopify.dev/api/liquid/filters/md5)    | Converte uma string em um hash MD5. Consulte [Filtros de codificação]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters) para obter mais informações.   | ✅  Sim   |
| [sha1](https://shopify.dev/api/liquid/filters/sha1)    | Converte uma string em um hash SHA-1. Consulte [Filtros de codificação]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters) para obter mais informações.  | ✅  Sim   |
| hmac_sha1_hex<br>(anteriormente [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | Converte uma string em um hash SHA-1 usando um código de autenticação de mensagem baseado em hash (HMAC). Passe a chave secreta da mensagem como parâmetro para o filtro. Consulte [Filtros de codificação]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters) para obter mais informações. | ✅  Sim   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256)    | Converte uma string em um hash SHA-256 usando um código de autenticação de mensagem baseado em hash (HMAC). Passe a chave secreta da mensagem como parâmetro para o filtro.       | ✅  Sim   |
| hmac_sha512 | Converte uma string em um hash SHA-512 usando um código de autenticação de mensagem baseado em hash (HMAC). Passe a chave secreta da mensagem como parâmetro para o filtro. | ✅  Sim  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br)     | Insere uma tag HTML de quebra de linha `<br>` na frente de cada quebra de linha em uma string.        | ✅  Sim   |
| [pluralize](https://shopify.dev/api/liquid/filters/pluralize)   | Emite a versão singular ou plural de uma string em inglês com base no valor de um número.      | ⛔  Não    |
| [prepend](https://shopify.dev/api/liquid/filters/prepend)     | Adiciona caracteres no início de uma string.      | ✅  Sim   |
| [remove](https://shopify.dev/api/liquid/filters/remove)      | Remove todas as ocorrências de uma substring de uma string.       | ✅  Sim   |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first)    | Remove apenas a primeira ocorrência de uma substring de uma string.      | ✅  Sim   |
| [replace](https://shopify.dev/api/liquid/filters/replace)        | Substitui todas as ocorrências de uma string por uma substring.   | ✅  Sim   |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first)        | Substitui a primeira ocorrência de uma string por uma substring.      | ✅  Sim   |
| [slice](https://shopify.dev/api/liquid/filters/slice)       | O filtro slice retorna uma substring, começando no índice especificado.       | ✅  Sim   |
| [split](https://shopify.dev/api/liquid/filters/split)  | O filtro split recebe uma substring como parâmetro. A substring é usada como delimitador para dividir uma string em um array.            | ✅  Sim   |
| [strip](https://shopify.dev/api/liquid/filters/strip)   | Remove tabulações, espaços e novas linhas (todos os espaços em branco) dos lados esquerdo e direito de uma string.                                                                                                    | ✅  Sim   |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip)     | Remove tabulações, espaços e novas linhas (todos os espaços em branco) do lado esquerdo de uma string.    | ⛔  Não    |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip)             | Remove tabulações, espaços e novas linhas (todos os espaços em branco) do lado direito de uma string.          | ⛔  Não    |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html)         | Remove todas as tags HTML de uma string.        | ✅  Sim   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines)  | Remove todas as quebras de linha/novas linhas de uma string.        | ✅  Sim   |
| [truncate](https://shopify.dev/api/liquid/filters/truncate)    | Trunca uma string até o número de caracteres passado como primeiro parâmetro. Uma reticência (...) é anexada à string truncada e é incluída na contagem de caracteres.    | ✅  Sim   |
| [truncatewords](https://shopify.dev/api/liquid/filters/truncatewords)   | Trunca uma string até o número de palavras passado como primeiro parâmetro. Uma reticência (...) é anexada à string truncada.    | ✅  Sim   |
| [upcase](https://shopify.dev/api/liquid/filters/upcase)   | Converte uma string em maiúsculas.      | ✅  Sim   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros adicionais

Os filtros gerais a seguir têm muitas finalidades, incluindo a formatação ou a conversão de conteúdo.

| Filtro                | Descrição                                                                                                                      | Compatível |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date](https://shopify.dev/api/liquid/filters/date)           | Converte um registro de data e hora em outro formato de data. Consulte [Filtro de data](#date-filter) para obter mais informações.         | ✅  Sim   |
| [default](https://shopify.dev/api/liquid/filters/default)        | Define um valor padrão para qualquer variável sem valor atribuído. Pode ser usado com strings, arrays e hashes.      | ✅  Sim   |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | Formata um endereço para imprimir os elementos do endereço em ordem, de acordo com o local.        | ⛔  Não    |
| [highlight](https://shopify.dev/api/liquid/filters/highlight)      | Envolve as palavras dentro dos resultados da pesquisa com uma tag HTML `<strong>` com a classe highlight se corresponder aos termos de pesquisa enviados. | ⛔  Não    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Você pode encontrar mais filtros compatíveis, como filtros de codificação e de URL, em nossa página [Filtros avançados]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/).

### Filtro de data {#date-filter}

O filtro `date` pode ser usado para converter um registro de data e hora em um formato de data diferente. Você pode passar parâmetros para o filtro `date` para reformatar o registro de data e hora. Para obter exemplos desses parâmetros, consulte [strfti.me](http://www.strfti.me/).

Por exemplo, digamos que o valor de `date_attribute` seja o registro de data e hora `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

Além das opções de formatação do `strftime`, a Braze também oferece suporte à conversão de um registro de data e hora para o horário Unix com o filtro de data `%s`. Por exemplo, para obter o `date_attribute` em horário Unix:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}
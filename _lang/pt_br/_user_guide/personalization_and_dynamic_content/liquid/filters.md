---
nav_title: Filtros
article_title: Filtros de líquidos
page_order: 3
description: "Esta página de referência lista os filtros que podem ser usados para reformatar conteúdo estático ou dinâmico."

---

# Filtros

> Este artigo de referência fornece uma visão geral dos filtros no Liquid e aborda quais filtros são compatíveis com o Braze. Está procurando ideias de como usar esses filtros? Confira nossa [biblioteca de casos de uso do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

Os filtros são a forma como você pode modificar a saída de números, cadeias de caracteres, variáveis e objetos no Liquid. Você pode usar filtros para reformatar texto estático ou dinâmico, como alterar uma cadeia de caracteres de minúsculas para maiúsculas ou realizar operações matemáticas, como adição ou divisão.

{% alert important %}
O Braze não é compatível com todos os filtros Liquid da Shopify. Esta página tenta delinear os filtros líquidos que a Braze testou, mas pode não ser uma lista completa. Sempre teste seu Liquid antes de enviar qualquer mensagem. <br><br>Se você tiver alguma dúvida sobre um filtro que não esteja listado aqui, entre em contato com o gerente de sucesso do cliente.
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

Neste exemplo, `Big Sale` é uma cadeia de caracteres e `upcase` é o filtro que está sendo aplicado.

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

## Filtros de matriz

Os filtros de matriz são usados para alterar a saída das matrizes.

| Filtro               | Definição                                                                                                         | Com suporte |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [unir-se](https://shopify.dev/docs/api/liquid/filters/join)          | Une os elementos de uma matriz com o caractere passado como parâmetro. O resultado é uma única string.          | ✅ Sim   |
| [primeiro](https://shopify.dev/docs/api/liquid/filters/first)         | Retorna o primeiro elemento de uma matriz. Em uma matriz de atributos personalizados, esse é o valor adicionado mais antigo.                | ✅ Sim   |
| [último](https://shopify.dev/docs/api/liquid/filters/last)          | Retorna o último elemento de uma matriz. Em uma matriz de atributos personalizados, esse é o valor adicionado mais recentemente.          | ✅ Sim   |
| [compacto](https://shopify.dev/api/liquid/filters/compact)       | Remove todos os itens `nil` de uma matriz.                                                                             | ✅ Sim   |
| [concatenar](https://shopify.dev/api/liquid/filters/concat)        | Combina uma matriz com outra matriz.                                                                              | ✅ Sim   |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index)         | Retorna o item no local de índice especificado em uma matriz. O primeiro item em uma matriz é referenciado com `[0]`. | ⛔ Não   |
| [mapa](https://shopify.dev/api/liquid/filters/map)           | Aceita o atributo de um elemento da matriz como parâmetro e cria uma matriz a partir do valor de cada elemento da matriz.        | ✅ Sim   |
| [reverso](https://shopify.dev/api/liquid/filters/reverse)       | Inverte a ordem dos itens em uma matriz.                                                                       | ✅ Sim   |
| [tamanho](https://shopify.dev/api/liquid/filters/size)          | Retorna o tamanho de uma string (o número de caracteres) ou de uma matriz (o número de elementos).                      | ✅ Sim   |
| [classificar](https://shopify.dev/api/liquid/filters/sort)         | Classifica os elementos de uma matriz por um determinado atributo de um elemento da matriz.                                    | ✅ Sim   |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | Classifica os itens em uma matriz em ordem alfabética sem distinção entre maiúsculas e minúsculas.                                                | ✅ Sim   |
| [uniq](https://shopify.dev/api/liquid/filters/uniq)         | Remove quaisquer instâncias duplicadas de elementos em uma matriz.                                                           | ✅ Sim   |
| [onde](https://shopify.dev/api/liquid/where)        | Filtra uma matriz para incluir apenas itens com um valor de propriedade específico.                                             | ✅ Sim   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros coloridos

[Os filtros de cores](https://shopify.dev/api/liquid/filters/color-filters) não são compatíveis com o Braze.

## Filtros de fonte

[Os filtros de fonte](https://shopify.dev/api/liquid/filters/font-filters) não são compatíveis com o Braze.

## Filtros matemáticos

Os filtros matemáticos permitem que você realize operações matemáticas. Se você usar vários filtros em uma saída, eles serão aplicados da esquerda para a direita.

| Filtro  | Definição      | Com suporte |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/abs)        | Retorna o valor absoluto de um número.     | ✅ Sim   |
| [at_most](https://shopify.dev/api/liquid/filters/at_most)    | Limita um número a um valor máximo.   | ✅ Sim   |
| [at_least](https://shopify.dev/api/liquid/filters/at_least)   | Limita um número a um valor mínimo.   | ✅ Sim   |
| [teto](https://shopify.dev/api/liquid/filters/ceil)       | Arredonda uma saída até o número inteiro mais próximo.  | ✅ Sim   |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | Divide uma saída por um número. A saída é arredondada para o número inteiro mais próximo. Confira a dica a seguir para evitar o arredondamento. | ✅ Sim   |
| [piso](https://shopify.dev/api/liquid/filters/floor)      | Arredonda uma saída para o número inteiro mais próximo.        | ✅ Sim   |
| [menos](https://shopify.dev/api/liquid/filters/minus)      | Subtrai um número de uma saída.          | ✅ Sim   |
| [mais](https://shopify.dev/api/liquid/filters/plus)       | Adiciona um número a uma saída.     | ✅ Sim   |
| [rodada](https://shopify.dev/api/liquid/filters/round)      | Arredonda a saída para o número inteiro mais próximo ou para o número especificado de casas decimais.  | ✅ Sim   |
| [horários](https://shopify.dev/api/liquid/filters/times)     | Multiplica uma saída por um número.       | ✅ Sim   |
| [módulo](https://shopify.dev/api/liquid/filters/modulo)    | Divide uma saída por um número e retorna o restante.   | ✅ Sim   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Ao dividir números inteiros (números inteiros) por números inteiros no Liquid, se a resposta for um float (número com um decimal), o Liquid arredondará automaticamente para o número inteiro mais próximo. No entanto, a divisão de números inteiros por números flutuantes sempre resultará em um número flutuante. Isso significa que você pode transformar seus números inteiros em um float (1,0, 2,0, 3,0) para retornar um float.
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

Esse exemplo não funcionaria porque não é possível fazer referência a vários atributos personalizados em uma linha do Liquid. Em vez disso, você precisaria atribuir uma variável a pelo menos um desses valores antes de executar as funções matemáticas. Adicionar dois atributos personalizados juntos exigiria duas linhas de Liquid:

1. Um para atribuir o atributo personalizado a uma variável,
2. Um para realizar a adição.

#### Caso de uso: Calcular o saldo atual

Digamos que queremos calcular o saldo atual de um usuário adicionando o saldo do cartão-presente e o saldo de recompensas.

1. Use a tag `assign` para substituir o atributo personalizado de `current_rewards_balance` pelo termo "balance". Isso significa que agora você tem uma variável chamada `balance`, que pode ser manipulada.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2\. Use o filtro `plus` para combinar o saldo do cartão-presente de cada usuário com seu saldo de recompensas, representado pelo objeto `{{balance}}`.
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

| Filtro         | Definição          | Com suporte |
| :--------------- | :--------------- | :-------- |
| [dinheiro](https://shopify.dev/api/liquid/filters/money)      | Formata números para garantir que os decimais estejam no lugar correto e que não haja zeros no final de nenhum número.   | ✅ Sim   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency)    | Formata números com o símbolo de moeda.     | ⛔ Não    |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency)     | Formata números sem o símbolo de moeda.      | ⛔ Não    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Para formatar corretamente um número com o filtro `money`, remova todas as vírgulas do número e adicione o filtro `plus: 0` antes do filtro `money`. Por exemplo, consulte o Liquid a seguir:<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Filtro de dinheiro do Shopify versus filtro de dinheiro do Braze

{% alert warning %}
O comportamento do filtro `money` do Shopify é diferente de como ele é usado no Braze. Consulte os exemplos a seguir para obter uma descrição precisa do comportamento esperado.
{% endalert %}

{% raw %}
Caso esteja inserindo um atributo personalizado (como `account_balance`), você deve sempre usar o filtro `money` para colocar as casas decimais no lugar correto e evitar que os zeros caiam no final dos números:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| COM O FILTRO DE DINHEIRO                       | SEM O FILTRO DE DINHEIRO                    |
| :------------------------------------------ | :------------------------------------------ |
| \![Com filtro de dinheiro]({% image_buster /assets/img/with_money_filter.png %})                     | \![Sem filtro de dinheiro]({% image_buster /assets/img/without_money_filter.png %})                  |
| Onde `account_balance` é a entrada em `17.8`. | Onde `account_balance` é a entrada em `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

O filtro `money` no Braze é diferente do Shopify porque não aplica automaticamente os pontos decimais de acordo com uma configuração predefinida. Por exemplo, considere o seguinte cenário em que `rewards_redeemed` contém um valor de `145`:

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

De acordo com o filtro de [dinheiro](https://shopify.dev/api/liquid/filters/money) da Shopify, isso deveria ter uma saída de `$1.45`, no entanto, no Braze, isso terá uma saída de `$145.00`. Como solução alternativa, podemos usar o filtro `divided_by` para manipular o número em um decimal, antes de aplicar o filtro de dinheiro:

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

## Filtros de cadeia de caracteres

Os filtros de cadeia de caracteres são usados para manipular as saídas e as variáveis das cadeias de caracteres. As cadeias de caracteres são uma combinação de caracteres alfanuméricos e devem ser colocadas entre aspas retas.

{% alert note %}
As aspas retas são diferentes das aspas curvas no Liquid. Tenha cuidado ao copiar e colar o Liquid de um editor de texto no Braze, pois as aspas curvas causarão erros em seu Liquid. Se você estiver escrevendo seu Liquid diretamente no Braze, as cotações diretas serão aplicadas automaticamente.
{% endalert %}

| Filtro          | Descrição     | Com suporte |
| :--------------- | ------------- | --------- |
| [anexar](https://shopify.dev/api/liquid/filters/append)     | Acrescenta caracteres a uma cadeia de caracteres.           | ✅ Sim   |
| [camelizar](https://shopify.dev/docs/api/liquid/filters/camelize)     | Converte uma string em CamelCase.             | ⛔ Não    |
| [capitalizar](https://shopify.dev/api/liquid/filters/capitalize)     | Coloca a primeira palavra em maiúscula em uma cadeia de caracteres e reduz a minúscula dos caracteres restantes.         | ✅ Sim   |
| [downcase](https://shopify.dev/api/liquid/filters/downcase)      | Converte uma cadeia de caracteres em letras minúsculas.         | ✅ Sim   |
| [fuga](https://shopify.dev/api/liquid/filters/escape)    | Escapa uma cadeia de caracteres.             | ✅ Sim   |
| [manipular](https://shopify.dev/api/liquid/filters/handleize)        | Formata uma cadeia de caracteres em um identificador.        | ⛔ Não    |
| [md5](https://shopify.dev/api/liquid/filters/md5)    | Converte uma string em um hash MD5. Para obter mais informações, consulte [Filtros de codificação]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters).   | ✅ Sim   |
| [sha1](https://shopify.dev/api/liquid/filters/sha1)    | Converte uma cadeia de caracteres em um hash SHA-1. Para obter mais informações, consulte [Filtros de codificação]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters).  | ✅ Sim   |
| hmac_sha1_hex<br>(anteriormente [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | Converte uma cadeia de caracteres em um hash SHA-1 usando um código de autenticação de mensagem de hash (HMAC). Passe a chave secreta da mensagem como um parâmetro para o filtro. Para obter mais informações, consulte [Filtros de codificação]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters). | ✅ Sim   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256)    | Converte uma cadeia de caracteres em um hash SHA-256 usando um código de autenticação de mensagem de hash (HMAC). Passe a chave secreta da mensagem como um parâmetro para o filtro.       | ✅ Sim   |
| hmac_sha512 | Converte uma cadeia de caracteres em um hash SHA-512 usando um código de autenticação de mensagem de hash (HMAC). Passe a chave secreta da mensagem como um parâmetro para o filtro. | ✅ Sim  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br)     | Insere uma tag HTML de quebra de linha `<br>` na frente de cada quebra de linha em uma string.        | ✅ Sim   |
| [pluralizar](https://shopify.dev/api/liquid/filters/pluralize)   | Emite a versão singular ou plural de uma cadeia de caracteres em inglês com base no valor de um número.      | ⛔ Não    |
| [prefixar](https://shopify.dev/api/liquid/filters/prepend)     | Anexa caracteres a uma cadeia de caracteres.      | ✅ Sim   |
| [remover](https://shopify.dev/api/liquid/filters/remove)      | Remove todas as ocorrências de uma substring de uma string.       | ✅ Sim   |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first)    | Remove apenas a primeira ocorrência de uma substring de uma string.      | ✅ Sim   |
| [substituir](https://shopify.dev/api/liquid/filters/replace)        | Substitui todas as ocorrências de uma cadeia de caracteres por uma substring.   | ✅ Sim   |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first)        | Substitui a primeira ocorrência de uma cadeia de caracteres por uma substring.      | ✅ Sim   |
| [fatia](https://shopify.dev/api/liquid/filters/slice)       | O filtro de fatia retorna uma substring, começando no índice especificado.       | ✅ Sim   |
| [dividir](https://shopify.dev/api/liquid/filters/split)  | O filtro de divisão recebe uma substring como parâmetro. A substring é usada como um delimitador para dividir uma string em uma matriz.            | ✅ Sim   |
| [faixa](https://shopify.dev/api/liquid/filters/strip)   | Remove tabulações, espaços e novas linhas (todos os espaços em branco) dos lados esquerdo e direito de uma cadeia de caracteres.                                                                                                    | ✅ Sim   |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip)     | Remove tabulações, espaços e novas linhas (todos os espaços em branco) do lado esquerdo de uma cadeia de caracteres.    | ⛔ Não    |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip)             | Remove tabulações, espaços e novas linhas (todos os espaços em branco) do lado direito de uma cadeia de caracteres.          | ⛔ Não    |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html)         | Remove todas as tags HTML de uma string.        | ✅ Sim   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines)  | Remove todas as quebras de linha/novas linhas de uma string.        | ✅ Sim   |
| [truncar](https://shopify.dev/api/liquid/filters/truncate)    | Trunca uma cadeia de caracteres até o número de caracteres passado como o primeiro parâmetro. Uma elipse (...) é anexada à cadeia de caracteres truncada e incluída na contagem de caracteres.    | ✅ Sim   |
| [truncatewords](https://shopify.dev/api/liquid/filters/truncatewords)   | Trunca uma cadeia de caracteres até o número de palavras passado como o primeiro parâmetro. Uma elipse (...) é anexada à cadeia de caracteres truncada.    | ✅ Sim   |
| [caixa alta](https://shopify.dev/api/liquid/filters/upcase)   | Converte uma cadeia de caracteres em maiúsculas.      | ✅ Sim   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros adicionais

Os filtros gerais a seguir servem para muitas finalidades, incluindo a formatação ou a conversão de conteúdo.

| Filtro                | Descrição                                                                                                                      | Com suporte |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [data](https://shopify.dev/api/liquid/filters/date)           | Converte um carimbo de data/hora em outro formato de data. Consulte [Filtro de data](#date-filter) para obter mais informações.         | ✅ Sim   |
| [padrão](https://shopify.dev/api/liquid/filters/default)        | Define um valor padrão para qualquer variável sem valor atribuído. Pode ser usado com strings, matrizes e hashes.      | ✅ Sim   |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | Formata um endereço para imprimir os elementos do endereço em ordem, de acordo com sua localidade.        | ⛔ Não    |
| [destaque](https://shopify.dev/api/liquid/filters/highlight)      | Envolve as palavras dentro dos resultados da pesquisa com uma tag HTML `<strong>` com o destaque da classe se corresponder aos termos de pesquisa enviados. | ⛔ Não    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Você pode encontrar mais filtros compatíveis, como filtros de codificação e de URL, em nossa página [Advanced Filters (Filtros avançados]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/) ).

### Filtro de data {#date-filter}

O filtro `date` pode ser usado para converter um carimbo de data/hora em um formato de data diferente. Você pode passar parâmetros para o filtro `date` para reformatar o registro de data e hora. Para obter exemplos desses parâmetros, consulte [strfti.me](http://www.strfti.me/).

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

Além das opções de formatação do site `strftime`, o Braze também suporta a conversão de um carimbo de data/hora para a hora Unix com o filtro de data `%s`. Por exemplo, para obter o `date_attribute` em tempo Unix:

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
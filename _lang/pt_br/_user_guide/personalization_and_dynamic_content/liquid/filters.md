---
nav_title: Filtros
article_title: Filtros Liquid
page_order: 3
description: "Esta página de referência lista os filtros que podem ser usados para reformatar conteúdo estático ou dinâmico."

---

# Filtros

> Este artigo de referência fornece uma visão geral dos filtros no Liquid e aborda quais filtros são suportados pela Braze. Está procurando ideias de como usar esses filtros? Confira nossa [biblioteca de casos de uso do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

Os filtros são a forma como você pode modificar a saída de números, strings, variáveis e objetos no Liquid. Você pode usar filtros para reformatar textos estáticos ou dinâmicos, como alterar uma string de minúscula para maiúscula, ou para realizar operações matemáticas, como adição ou divisão.

{% alert important %}
O Braze não é compatível com todos os filtros Liquid da Shopify. Esta página tenta delinear os filtros Liquid que a Braze testou, mas pode não ser uma lista completa. Sempre teste seu Liquid antes de enviar qualquer mensagem. <br><br>Se tiver alguma dúvida sobre um filtro que não esteja listado aqui, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Sintaxe do filtro

{% raw %}

Os filtros devem ser colocados em uma tag de saída `{{ }}` e são indicados por um caractere de pipe `|`.

{% endraw %}

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Saída %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

Neste exemplo, `Big Sale` é uma string e `upcase` é o filtro que está sendo aplicado.

### Sintaxe para vários filtros

Você pode usar vários filtros em uma saída. Eles são aplicados da esquerda para a direita.

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Saída %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de matriz

Os filtros de matriz são usados para alterar a saída das matrizes.

| Filtrar               | Definição                                                                                                         | Com suporte |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join][1.1]          | Une os elementos de uma matriz com o caractere passado como parâmetro. O resultado é uma única string.          | ✅ Sim   |
| [first][1.2]         | Retorna o primeiro elemento de uma matriz. Em uma matriz de atributos personalizados, esse é o valor adicionado mais antigo.                | ✅ Sim   |
| [last][1.3]          | Retorna o último elemento de uma matriz. Em uma matriz de atributos personalizados, esse é o valor adicionado mais recentemente.          | ✅ Sim   |
| [compacto][1.4]       | Remove todos os itens `nil` de uma matriz.                                                                             | ✅ Sim   |
| [concat][1.5]        | Combina uma matriz com outra matriz.                                                                              | ✅ Sim   |
| [index][1.6]         | Retorna o item no local de índice especificado em uma matriz. O primeiro item em uma matriz é referenciado com `[0]`. | ✅ Sim   |
| [map][1.7]           | Aceita a atribuição de um elemento da matriz como parâmetro e cria uma matriz a partir do valor de cada elemento da matriz.        | ✅ Sim   |
| [reverse][1.8]       | Inverte a ordem dos itens em uma matriz.                                                                       | ✅ Sim   |
| [size][1.9]          | Retorna o tamanho de uma string (o número de caracteres) ou de uma matriz (o número de elementos).                      | ✅ Sim   |
| [sort][1.10]         | Classifica os elementos de uma matriz por uma determinada atribuição de um elemento da matriz.                                    | ✅ Sim   |
| [sort_natural][1.11] | Classifica os itens de uma matriz em ordem alfabética sem distinção entre maiúsculas e minúsculas.                                                | ✅ Sim   |
| [uniq][1.12]         | Remove quaisquer instâncias duplicadas de elementos em uma matriz.                                                           | ✅ Sim   |
| [onde][1.13]        | Filtra uma matriz para incluir apenas itens com um valor de propriedade específico.                                             | ✅ Sim   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros coloridos

[Os filtros de cores][2.1] não são suportados no Braze.

## Filtros de fonte

[Os filtros de fonte][3.1] não são suportados no Braze.

## Filtros matemáticos

Os filtros matemáticos permitem que você realize operações matemáticas. Se você usar vários filtros em uma saída, eles serão aplicados da esquerda para a direita.

| Filtrar  | Definição      | Com suporte |
| :------ |:----------------| :-------- |
| [abs][4.1]        | Retorna o valor absoluto de um número.     | ✅ Sim   |
| [at_most][4.2]    | Limita um número a um valor máximo.   | ✅ Sim   |
| [pelo menos][4.3]   | Limita um número a um valor mínimo.   | ✅ Sim   |
| [teto][4.4]       | Arredonda uma saída até o número inteiro mais próximo.  | ✅ Sim   |
| [dividido_por][4.5] | Divide uma saída por um número. A saída é arredondada para o número inteiro mais próximo. Confira a dica a seguir para evitar o arredondamento. | ✅ Sim   |
| [floor][4.6]      | Arredonda uma saída para o número inteiro mais próximo.        | ✅ Sim   |
| [minus][4.7]      | Subtrai um número de uma saída.          | ✅ Sim   |
| [plus][4.8]       | Adiciona um número a uma saída.     | ✅ Sim   |
| [round][4.9]      | Arredonda a saída para o número inteiro mais próximo ou para o número especificado de casas decimais.  | ✅ Sim   |
| [vez][4.10]     | Multiplica uma saída por um número.       | ✅ Sim   |
| [módulo][4.11]    | Divide uma saída por um número e retorna o restante.   | ✅ Sim   |
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

Esse exemplo não funcionaria porque não é possível fazer referência a vários atributos personalizados em uma linha do Liquid. Em vez disso, você precisaria atribuir uma variável a pelo menos um desses valores antes de executar as funções matemáticas. A adição de dois atributos personalizados juntos exigiria duas linhas de Liquid:

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
{% tab Entrada %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Saída %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de dinheiro

Se estiver atualizando um usuário sobre uma compra, um saldo de conta ou qualquer coisa relacionada a dinheiro, você deve usar filtros de dinheiro. Os filtros de dinheiro garantem que as casas decimais estejam no lugar correto e que nenhuma parte de sua atualização seja perdida (como aquele incômodo `0` de ponta a ponta).

| Filtrar         | Definição          | Com suporte |
| :--------------- | :--------------- | :-------- |
| [dinheiro][5.1]      | Formata números para garantir que os decimais estejam no lugar correto e que não haja zeros na ponta de nenhum número.   | ✅ Sim   |
| [money_with_currency][5.2]    | Formata números com o símbolo de moeda.     | ⛔ Não    |
| [money_without_currency][5.4]     | Formata números sem o símbolo de moeda.      | ⛔ Não    |
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
O comportamento do filtro do Shopify `money` é diferente de como ele é usado no Braze. Consulte os exemplos a seguir para obter uma descrição precisa do comportamento esperado.
{% endalert %}

{% raw %}
Caso esteja inserindo um atributo personalizado (como `account_balance`), sempre use o filtro `money` para colocar as casas decimais no lugar correto e evitar que os zeros caiam de ponta a ponta em qualquer número:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| COM O FILTRO DE DINHEIRO                       | SEM O FILTRO DE DINHEIRO                    |
| :------------------------------------------ | :------------------------------------------ |
| ![Com filtro de dinheiro][1]                     | ![Sem filtro de dinheiro][2]                  |
| Onde `account_balance` é a entrada em `17.8`. | Onde `account_balance` é a entrada em `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

O filtro `money` no Braze é diferente do Shopify porque não aplica automaticamente os pontos decimais de acordo com uma configuração predefinida. Por exemplo, considere o seguinte cenário em que `rewards_redeemed` contém um valor de `145`:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Saída %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

De acordo com o filtro de [dinheiro][5.1] da Shopify, isso deveria ter uma saída de `$1.45`, no entanto, na Braze, isso terá uma saída de `$145.00`. Como solução alternativa, podemos usar o filtro `divided_by` para manipular o número em um decimal, antes de aplicar o filtro de dinheiro:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Saída %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de string

Os filtros de strings são usados para manipular as saídas e as variáveis das strings. As strings são uma combinação de caracteres alfanuméricos e devem ser colocadas entre aspas retas.

{% alert note %}
As aspas retas são diferentes das aspas curvas no Liquid. Tenha cuidado ao copiar e colar o Liquid de um editor de texto para o Braze, pois as aspas curvas causarão erros em seu Liquid. Se estiver escrevendo seu Liquid diretamente no Braze, as cotações diretas serão aplicadas automaticamente.
{% endalert %}

| Filtrar          | Descrição     | Com suporte |
| :--------------- | ------------- | --------- |
| [append][6.1]     | Acrescenta caracteres a uma string.           | ✅ Sim   |
| [camelcase][6.2]     | Converte uma string em CamelCase.             | ⛔ Não    |
| [capitalize][6.3]     | Coloca a primeira palavra em maiúscula em uma string e reduz a minúscula dos caracteres restantes.         | ✅ Sim   |
| [downcase][6.4]      | Converte uma string em letras minúsculas.         | ✅ Sim   |
| [escape][6.5]    | Escapa uma string.             | ✅ Sim   |
| [handle/handleize][6.6]        | Formata uma string em um identificador.        | ⛔ Não    |
| [md5][6.7]    | Converte uma string em um hash MD5. Consulte Filtros de codificação][3] para saber mais.   | ✅ Sim   |
| [sha1][6.8]    | Converte uma string em um hash SHA-1. Consulte Filtros de codificação][3] para saber mais.  | ✅ Sim   |
| hmac_sha1_hex<br>(anteriormente [hmac_sha_1][6.10]) | Converte uma string em um hash SHA-1 usando um código de autenticação de mensagem de hash (HMAC). Passe a chave secreta da mensagem como um parâmetro para o filtro. Consulte Filtros de codificação][3] para saber mais. | ✅ Sim   |
| [hmac_sha256][6.11]    | Converte uma string em um hash SHA-256 usando um código de autenticação de mensagem de hash (HMAC). Passe a chave secreta da mensagem como um parâmetro para o filtro.       | ✅ Sim   |
| hmac_sha512 | Converte uma string em um hash SHA-512 usando um código de autenticação de mensagem de hash (HMAC). Passe a chave secreta da mensagem como um parâmetro para o filtro. | ✅ Sim  |
| [newline_to_br][6.12]     | Insere uma tag HTML de quebra de linha `<br>` na frente de cada quebra de linha em uma string.        | ✅ Sim   |
| [pluralize][6.13]   | Emite a versão singular ou plural de uma string em inglês com base no valor de um número.      | ⛔ Não    |
| [prepend][6.14]     | Anexa caracteres a uma string.      | ✅ Sim   |
| [remover][6.15]      | Remove todas as ocorrências de uma substring de uma string.       | ✅ Sim   |
| [remove_first][6.16]    | Remove apenas a primeira ocorrência de uma substring de uma string.      | ✅ Sim   |
| [replace][6.17]        | Substitui todas as ocorrências de uma string por uma substring.   | ✅ Sim   |
| [replace_first][6.18]        | Substitui a primeira ocorrência de uma string por uma substring.      | ✅ Sim   |
| [slice][6.19]       | O filtro de fatia retorna uma substring, começando no índice especificado.       | ✅ Sim   |
| [split][6.20]  | O filtro de divisão recebe uma substring como parâmetro. A substring é usada como um delimitador para dividir uma string em uma matriz.            | ✅ Sim   |
| [strip][6.21]   | Remove guias, espaços e novas linhas (todos os espaços em branco) dos lados esquerdo e direito de uma string.                                                                                                    | ✅ Sim   |
| [lstrip][6.22]     | Retira guias, espaços e novas linhas (todos os espaços em branco) do lado esquerdo de uma string.    | ⛔ Não    |
| [rstrip][6.23]             | Retira guias, espaços e novas linhas (todos os espaços em branco) do lado direito de uma string.          | ⛔ Não    |
| [strip_html][6.24]         | Retira todas as tags HTML de uma string.        | ✅ Sim   |
| [strip_newlines][6.25]  | Remove todas as quebras de linha/novas linhas de uma string.        | ✅ Sim   |
| [truncate][6.26]    | Trunca uma string até o número de caracteres passado como primeiro parâmetro. Uma elipse (...) é anexada à string truncada e é incluída na contagem de caracteres.    | ✅ Sim   |
| [truncatewords][6.27]   | Trunca uma string até o número de palavras passadas como primeiro parâmetro. Uma elipse (...) é anexada à string truncada.    | ✅ Sim   |
| [upcase][6.28]   | Converte uma string em maiúsculas.      | ✅ Sim   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros adicionais

Os filtros gerais a seguir têm muitas finalidades, inclusive a formatação ou a conversão de conteúdo.

| Filtrar                | Descrição                                                                                                                      | Com suporte |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [data][7.1]           | Converte um registro de data e hora em outro formato de data. Consulte [Filtro de data](#date-filter) para obter mais informações.         | ✅ Sim   |
| [default][7.2]        | Define um valor padrão para qualquer variável sem valor atribuído. Pode ser usado com strings, matrizes e hashes.      | ✅ Sim   |
| [format_address][7.3] | Formata um endereço para imprimir os elementos do endereço em ordem, de acordo com sua localização.        | ⛔ Não    |
| [highlight][7.4]      | Envolve as palavras dentro dos resultados da pesquisa com uma tag HTML `<strong>` com o destaque da classe se corresponder aos termos de pesquisa enviados. | ⛔ Não    |
| `time_zone`             | Consulte [Filtro de fuso horário](#time-zone-filter).     | ✅ Sim   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Você pode encontrar mais filtros compatíveis, como filtros de codificação e de URL, em nossa página [Advanced Filters (Filtros avançados]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/) ).

### Filtro de data {#date-filter}

O filtro `date` pode ser usado para converter um carimbo de data/hora em um formato de data diferente. Você pode passar parâmetros para o filtro `date` para reformatar o registro de data e hora. Para obter exemplos desses parâmetros, consulte [strfti.me](http://www.strfti.me/).

Por exemplo, digamos que o valor de `date_attribute` seja o registro de data e hora `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Saída %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

Além das opções de formatação do site `strftime`, a Braze também oferece suporte à conversão de um registro de data e hora para a hora Unix com o filtro de data `%s`. Por exemplo, para obter o `date_attribute` em tempo Unix:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Saída %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Filtro de fuso horário {#time-zone-filter}

{% raw %}
Além dos filtros que você encontrará listados na documentação da Shopify, o Braze também oferece suporte ao filtro `time_zone`.

O filtro `time_zone` usa uma hora, um fuso horário e um formato de data e retorna a hora nesse fuso horário no formato de data especificado. Por exemplo, digamos que o valor de `{{custom_attribute.$date_attribute}}}` seja `2021-08-04 9:00:00 UTC`:
{% endraw %}

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | time_zone: 'America/Los_Angeles' | date: '%a %b %e %T' }}
```
{% endraw %}
{% endtab %}
{% tab Saída %}
{% raw %}
```liquid
Wed August 4 2:00:00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Também é possível usar a variável reservada `now` para acessar a data e a hora atuais para manipulação.

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{ 'now' | date: '%Y-%m-%d %H:%M:%S' }}
```
{% endraw %}
{% endtab %}
{% tab Saída %}
{% raw %}
```liquid
2021-08-04 18:13:13
```
{% endraw %}
{% endtab %}
{% endtabs %}


[1.1]: https://shopify.dev/api/liquid/filters/array-filters#join
[1.2]: https://shopify.dev/api/liquid/filters/array-filters#first
[1.3]: https://shopify.dev/api/liquid/filters/array-filters#last
[1.4]: https://shopify.dev/api/liquid/filters#compact
[1.5]: https://shopify.dev/api/liquid/filters/array-filters#concat
[1.6]: https://shopify.dev/api/liquid/filters/array-filters#index
[1.7]: https://shopify.dev/api/liquid/filters/array-filters#map
[1.8]: https://shopify.dev/api/liquid/filters/array-filters#reverse
[1.9]: https://shopify.dev/api/liquid/filters/array-filters#size
[1.10]: https://shopify.dev/api/liquid/filters/array-filters#sort
[1.11]: https://shopify.dev/api/liquid/filters#sort_natural
[1.12]: https://shopify.dev/api/liquid/filters/array-filters#uniq
[1.13]: https://shopify.dev/api/liquid/filters#where

[2.1]: https://shopify.dev/api/liquid/filters/color-filters
[3.1]: https://shopify.dev/api/liquid/filters/font-filters

[4.1]: https://shopify.dev/api/liquid/filters/math-filters#abs
[4.2]: https://shopify.dev/api/liquid/filters/math-filters#at_most
[4.3]: https://shopify.dev/api/liquid/filters/math-filters#at_least
[4.4]: https://shopify.dev/api/liquid/filters/math-filters#ceil
[4.5]: https://shopify.dev/api/liquid/filters/math-filters#divided_by
[4.6]: https://shopify.dev/api/liquid/filters/math-filters#floor
[4.7]: https://shopify.dev/api/liquid/filters/math-filters#minus
[4.8]: https://shopify.dev/api/liquid/filters/math-filters#plus
[4.9]: https://shopify.dev/api/liquid/filters/math-filters#round
[4.10]: https://shopify.dev/api/liquid/filters/math-filters#times
[4.11]: https://shopify.dev/api/liquid/filters/math-filters#modulo

[5.1]: https://shopify.dev/api/liquid/filters/money-filters#money
[5.2]: https://shopify.dev/api/liquid/filters/money-filters#money_with_currency
[5.3]: https://shopify.dev/api/liquid/filters/money-filters#money_without_trailing_zeros
[5.4]: https://shopify.dev/api/liquid/filters/money-filters#money_without_currency

[6.1]: https://shopify.dev/api/liquid/filters/string-filters#append
[6.2]: https://shopify.dev/api/liquid/filters/string-filters#camelcase
[6.3]: https://shopify.dev/api/liquid/filters/string-filters#capitalize
[6.4]: https://shopify.dev/api/liquid/filters/string-filters#downcase
[6.5]: https://shopify.dev/api/liquid/filters/string-filters#escape
[6.6]: https://shopify.dev/api/liquid/filters/string-filters#handle-handleize
[6.7]: https://shopify.dev/api/liquid/filters/string-filters#md5
[6.8]: https://shopify.dev/api/liquid/filters/string-filters#sha1
[6.10]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1
[6.11]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha256
[6.12]: https://shopify.dev/api/liquid/filters/string-filters#newline_to_br
[6.13]: https://shopify.dev/api/liquid/filters/string-filters#pluralize
[6.14]: https://shopify.dev/api/liquid/filters/string-filters#prepend
[6.15]: https://shopify.dev/api/liquid/filters/string-filters#remove
[6.16]: https://shopify.dev/api/liquid/filters/string-filters#remove_first
[6.17]: https://shopify.dev/api/liquid/filters/string-filters#replace
[6.18]: https://shopify.dev/api/liquid/filters/string-filters#replace_first
[6.19]: https://shopify.dev/api/liquid/filters/string-filters#slice
[6.20]: https://shopify.dev/api/liquid/filters/string-filters#split
[6.21]: https://shopify.dev/api/liquid/filters/string-filters#strip
[6.22]: https://shopify.dev/api/liquid/filters/string-filters#lstrip
[6.23]: https://shopify.dev/api/liquid/filters/string-filters#rstrip
[6.24]: https://shopify.dev/api/liquid/filters/string-filters#strip_html
[6.25]: https://shopify.dev/api/liquid/filters/string-filters#strip_newlines
[6.26]: https://shopify.dev/api/liquid/filters/string-filters#truncate
[6.27]: https://shopify.dev/api/liquid/filters/string-filters#truncatewords
[6.28]: https://shopify.dev/api/liquid/filters/string-filters#upcase

[7.1]: https://shopify.dev/api/liquid/filters/additional-filters#date
[7.2]: https://shopify.dev/api/liquid/filters/additional-filters#default
[7.3]: https://shopify.dev/api/liquid/filters/additional-filters#format_address
[7.4]: https://shopify.dev/api/liquid/filters/additional-filters#highlight


[1]: {% image_buster /assets/img/with_money_filter.png %}
[2]: {% image_buster /assets/img/without_money_filter.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters

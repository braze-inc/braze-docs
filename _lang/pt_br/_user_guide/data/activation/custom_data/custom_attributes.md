---
nav_title: Atributos personalizados
article_title: Atributos personalizados
page_order: 10
page_type: reference
description: "Esta página descreve os atributos personalizados e explica os vários tipos de dados de atributos personalizados."
search_rank: 1
---

# [![Curso de aprendizado do Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"} Atributos personalizados

> Esta página aborda os atributos personalizados, que são uma coleção de características exclusivas dos usuários. Os atributos personalizados são melhores para armazenar atributos sobre seus usuários ou informações sobre ações de baixo valor dentro do seu aplicativo. 

Quando armazenados no Braze, os atributos personalizados podem ser usados para criar segmentos de público-alvo e personalizar as mensagens usando o Liquid. Lembre-se de que não armazenamos informações de séries temporais para atributos personalizados, portanto, você não poderá obter nenhum gráfico com base neles, como acontece com os eventos personalizados.

## Gerenciamento de atributos personalizados

Para criar e gerenciar atributos personalizados no painel, vá para **Configurações de dados** > **Atributos personalizados**. 

\![Quatro atributos personalizados que são booleanos.]({% image_buster /assets/img/export_custom_attributes.png %})

A coluna **Última atualização** lista a última vez que o atributo personalizado foi editado, por exemplo, quando foi definido pela última vez como lista de bloqueio ou ativo.

{% alert important %}
Para o direcionamento adequado de mensagens, certifique-se de que o tipo de dados do atributo personalizado corresponda ao atributo personalizado real.
{% endalert %}

Nessa página, você pode visualizar, gerenciar, criar ou colocar em lista de bloqueio os atributos personalizados existentes. Selecione o menu ao lado de um atributo personalizado para as seguintes ações:

### Lista de bloqueio

Os atributos personalizados podem ser colocados em listas de bloqueio individualmente no menu de ações ou até 100 atributos podem ser selecionados e colocados em listas de bloqueio em massa. Se você bloquear um atributo personalizado, nenhum dado será coletado com relação a esse atributo, os dados existentes ficarão indisponíveis, a menos que sejam reativados, e os atributos na lista de bloqueio não serão exibidos em filtros ou gráficos. Além disso, se o atributo for atualmente referenciado por filtros ou acionadores em outras áreas do painel do Braze, será exibido um modal de aviso explicando que todas as instâncias dos filtros ou acionadores que o referenciam serão removidas e arquivadas.

### Marcação como informações de identificação pessoal (PII)

Os administradores também podem criar atributos personalizados e marcá-los como PII nessa página. Esses atributos só serão visíveis para administradores e usuários do painel com a permissão "View Custom Attributes Marked as PII" (Exibir atributos personalizados marcados como PII).

### Adição de descrições

Você pode adicionar uma descrição a um atributo personalizado depois que ele for criado se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Edite o atributo personalizado e insira o que quiser, como uma nota para sua equipe.

### Adição de tags

Você pode adicionar tags a um atributo personalizado depois que ele for criado se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)"Manage Events, Attributes, Purchases" (Gerenciar eventos, atributos e compras). As tags podem então ser usadas para filtrar a lista de atributos. 

### Remoção de atributos personalizados

Há duas maneiras de remover atributos personalizados dos perfis de usuário:

* Selecione o nome do atributo personalizado a ser removido em uma [etapa de atualização do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes).
* Defina o valor `null` em sua solicitação de API para o [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Visualização de relatórios de uso

O relatório de uso lista todos os Canvases, campanhas e segmentos que usam um atributo personalizado específico. Essa lista não inclui os usos do Liquid. 

Você pode visualizar até 100 relatórios de uso por vez, marcando as caixas de seleção ao lado dos respectivos atributos personalizados e selecionando **Exibir relatório de uso**.

### Exportação de dados

Para exportar a lista de atributos personalizados como um arquivo CSV, selecione **Exportar tudo** na parte superior da página. O arquivo CSV será gerado e um link para download será enviado a você por e-mail.

## Definição de atributos personalizados

A seguir, listamos os métodos de várias plataformas que são usados para definir atributos personalizados.

{% details Expand for documentation by platform %}

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unidade]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Armazenamento de atributos personalizados

Todos os dados armazenados no **perfil do usuário**, inclusive os dados de atributos personalizados, são mantidos indefinidamente enquanto cada perfil estiver [ativo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Tipos de dados de atributos personalizados

Os atributos personalizados são ferramentas extraordinariamente flexíveis que permitem um ótimo direcionamento.

Os seguintes tipos de dados podem ser armazenados como atributos personalizados:

- [Booleanos](#booleans)
- [Números](#numbers)
- [Cordas](#strings)
- [Matrizes](#arrays)
- [Tempo](#time)
- [Objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Matrizes de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### Booleanos (verdadeiro/falso) {#booleans}

Os atributos booleanos são úteis para armazenar dados binários simples sobre seus usuários, como status de assinatura. É possível encontrar usuários que têm explicitamente uma variável definida como um valor verdadeiro ou falso, além daqueles que ainda não têm nenhum registro desse atributo.

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o valor booleano **é** verdadeiro, falso, verdadeiro ou não definido, ou falso ou não definido | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, ou **FALSE OR NOT SET** | Se esse filtro especificar `coffee_drinker`, um usuário corresponderá a esse filtro nas seguintes circunstâncias: <br> {::nomarkdown}<ul><li>Se esse filtro for <code>verdadeiro</code> e o usuário tiver o valor <code>coffee_drinker</code></li><li>Se esse filtro for <code>falso</code> e o usuário não tiver o valor <code>coffee_drinker</code></li><li>Se esse filtro for <code>verdadeiro ou não estiver definido</code> e o usuário tiver o valor <code>coffee_drinker</code> ou nenhum valor</li><li>Se esse filtro for <code>falso ou não estiver definido</code> e o usuário não tiver <code>coffee_drinker</code> ou qualquer valor</li></ul>{:/} |
| Verificar se o valor booleano **existe** no perfil de um usuário e se não é nulo | **NÃO ESTÁ EM BRANCO**  | **N/A** | Se esse filtro especificar `coffee_drinker` e um usuário tiver um valor para o atributo `coffee_drinker`, o usuário corresponderá a esse filtro. | 
| Verificar se o valor booleano **não** existe no perfil de um usuário ou é nulo | **ESTÁ EM BRANCO**  | **N/A** | Se esse filtro especificar `coffee_drinker`e um usuário não tiver o atributo `coffee_drinker` ou o valor de `coffee_drinker` for nulo, o usuário corresponderá a esse filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Números {#numbers}

Os atributos numéricos incluem [números inteiros](https://en.wikipedia.org/wiki/Integer) e [flutuantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic) e têm uma ampla variedade de casos de uso. Os atributos personalizados de incremento de número são úteis para armazenar o número de vezes que uma determinada ação ou evento ocorreu sem contar com o limite de dados. Os números padrão têm todos os tipos de uso, como gravação:

- Tamanho do calçado
- Tamanho da cintura
- Número de vezes que um usuário visualizou um determinado recurso ou categoria de produto

{% alert tip %}
O dinheiro gasto não deve ser registrado por esse método. Em vez disso, ele deve ser registrado por meio de nossos [métodos de compra](#purchase-revenue-tracking).
{% endalert %}

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo numérico **é exatamente** um **número**| **EXATAMENTE** | **NÚMERO** | Se esse filtro especificar `10` e um perfil de usuário tiver o valor `10`, o usuário corresponderá a esse filtro. |
| Verificar se o atributo numérico **não é igual a** um **número**| **NÃO É IGUAL** | **NÚMERO** | Se esse filtro especificar `10` e um perfil de usuário não tiver o valor `10`, o usuário corresponderá a esse filtro. |
| Verificar se o atributo numérico **é mais do que** um **número**| **MAIS DO QUE** | **NÚMERO** | Se esse filtro especificar `10` e um perfil de usuário tiver um valor maior que `10`, o usuário corresponderá a esse filtro. |
| Verificar se o atributo numérico **é menor que** um **número**| **MENOS DE** | **NÚMERO** | Se esse filtro especificar `10` e um perfil de usuário tiver um valor menor que `10`, o usuário corresponderá a esse filtro. |
| Verificar se o atributo numérico **existe** no perfil de um usuário e se não é nulo | **NÃO ESTÁ EM BRANCO** | **N/A** | Se um perfil de usuário contiver o atributo numérico especificado, independentemente do valor, o usuário corresponderá a esse filtro. |
| Verificar se o atributo numérico **não** existe no perfil de um usuário ou se é nulo | **ESTÁ EM BRANCO** | **N/A** | Se um perfil de usuário não contiver o atributo numérico especificado ou se o valor do atributo for nulo, o usuário corresponderá a esse filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Detalhes do atributo de número

- Os filtros "Exatamente 0" e "Menos que" incluem usuários com campos NULL
  - Para excluir usuários sem um valor para atributos personalizados, é necessário incluir o filtro **is not blank**.

### Strings (caracteres alfanuméricos) {#strings}

Os atributos de cadeia de caracteres são úteis para armazenar entradas do usuário, como uma marca favorita, um número de telefone ou uma última cadeia de pesquisa no aplicativo. Os atributos de cadeia de caracteres podem ter até 255 caracteres.

Observe que, se você inserir valores com espaços entre, antes ou depois das palavras, o Braze também verificará se há os mesmos espaços.

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo string **corresponde exatamente a** uma string inserida| **IGUAIS** | **STRING**<br>Diferença entre maiúsculas e minúsculas | Se esse filtro especificar `book` e um perfil de usuário tiver um atributo de cadeia de caracteres para `last_item_purchased` que contenha `book`, o usuário corresponderá a esse filtro. |
| Verificar se o atributo string **corresponde parcialmente a** uma string inserida **OU** a uma expressão regular | **REGEX DE CORRESPONDÊNCIAS** | **CORDA** **OU** **EXPRESSÃO REGULAR** <br>Não diferencia maiúsculas de minúsculas; máximo de 32.764 caracteres | 
| Verificar se o atributo string **não corresponde parcialmente a** uma string inserida **OU** a uma expressão regular | **NÃO CORRESPONDE AO REGEX** \* | **CORDA** **OU** **EXPRESSÃO REGULAR**<br>Não diferencia maiúsculas de minúsculas; máximo de 32.764 caracteres |
| Verificar se o atributo string **não corresponde a** uma string inserida| **NÃO É IGUAL** | **STRING**<br>Não diferencia maiúsculas de minúsculas  | Se esse filtro especificar `book` e um perfil de usuário tiver um atributo de cadeia de caracteres para `last_item_purchased` que não contenha `book`, o usuário corresponderá a esse filtro.|
| Verificar se o atributo string **existe** no perfil de um usuário e se não é uma string vazia | **NÃO ESTÁ EM BRANCO** | **N/A** | Se esse filtro especificar `favorite_genre` e um perfil de usuário tiver o atributo `favorite_genre`, o usuário corresponderá a esse filtro independentemente do valor do atributo. Por exemplo, o usuário pode ter `sci-fi`, `romance`, ou outro valor.|
| Verificar se o atributo string **não existe** no perfil de um usuário | **EM BRANCO** | **N/A** | Se esse filtro especificar `favorite_genre` e um perfil de usuário não tiver o atributo `favorite_genre`, o usuário corresponderá a esse filtro.|
| Verificar se a cadeia de caracteres corresponde exatamente a **qualquer uma** das cadeias de caracteres inseridas | **É QUALQUER UM DOS** | **STRING**<br>Diferencia maiúsculas de minúsculas; são permitidas várias cadeias de caracteres (máximo de 256) | Se esse filtro especificar `book`, `bookmark` e `reading light`, e um perfil de usuário tiver pelo menos uma dessas cadeias de caracteres, o usuário corresponderá a esse filtro. |
| Verificar se o atributo string **não corresponde exatamente a nenhuma** das strings inseridas | **NÃO É NENHUM DE** |**STRING**<br>Diferencia maiúsculas de minúsculas; são permitidas várias cadeias de caracteres (máximo de 256) | Se esse filtro especificar `book`, `bookmark` e `reading light`, e um perfil de usuário não contiver nenhuma dessas cadeias de caracteres, o usuário corresponderá ao filtro.|
| Verificar se o atributo string **corresponde parcialmente a alguma** das strings inseridas | **CONTÉM QUALQUER UM DOS** | **STRING**<br>Diferencia maiúsculas de minúsculas; são permitidas várias cadeias de caracteres (máximo de 256) | Se esse filtro especificar `gold` e um perfil de usuário contiver `gold` em qualquer cadeia de caracteres, como `gold_tier` ou `former_gold_tier`, o usuário corresponderá ao filtro. |
| Verificar se o atributo string **não corresponde parcialmente a nenhuma** das strings inseridas | **NÃO CONTÉM NENHUM DOS** | **STRING**<br>Diferencia maiúsculas de minúsculas; são permitidas várias cadeias de caracteres (máximo de 256) | Se esse filtro especificar `gold` e um perfil de usuário não contiver `gold` em nenhuma cadeia de caracteres, o usuário corresponderá a esse filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Uma cadeia de caracteres de data, como "12-1-2021" ou "12/1/2021", será convertida em um objeto datetime e tratada como um [atributo de tempo]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
Ao segmentar usando o filtro **DOES NOT MATCH REGEX**, você já deve ter um atributo personalizado com um valor atribuído nesse perfil de usuário. A Braze sugere o uso da lógica "OU" para verificar se um atributo personalizado está em branco para garantir que os usuários estejam sendo direcionados corretamente.
{% endalert %}

### Matrizes {#arrays}

Os atributos de matriz são bons para armazenar listas relacionadas de informações sobre seus usuários. Por exemplo, armazenar as últimas 100 partes do conteúdo que um usuário assistiu em uma matriz permitiria a segmentação por interesses específicos.

Por padrão, o comprimento de uma matriz para um atributo é de até 500 itens. Por exemplo, se você estiver enviando um atributo como "Movies Watched" (Filmes assistidos) e ele estiver definido como 500, quando um usuário assistir ao 501º filme, o primeiro filme será removido da matriz e o filme mais recente será adicionado.

Observe que, se você inserir valores com espaços entre, antes ou depois das palavras, o Braze também verificará se há os mesmos espaços.

{% alert note %}
A opção de aumentar o comprimento máximo não estará disponível se o atributo estiver definido para detectar automaticamente o tipo de dados; o tipo de dados deve ser definido como matriz.
{% endalert %}

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo de matriz **inclui um valor que corresponde exatamente a** um valor inserido| **INCLUI VALOR** | **STRING** | Se esse filtro especificar `sci-fi` e um perfil de usuário tiver o valor `sci-fi`, o usuário corresponderá a esse filtro.|
| Verificar se o atributo de matriz **não inclui um valor que corresponda exatamente a** um valor inserido| **NÃO INCLUI VALOR** | **STRING** | Se esse filtro especificar `sci-fi` e um perfil de usuário não tiver o valor `sci-fi`, o usuário corresponderá a esse filtro.|
| Verificar se o atributo de matriz **contém um valor que corresponde parcialmente a** um valor inserido **OU** a uma expressão regular | **REGEX DE CORRESPONDÊNCIAS** | **CORDA** **OU** **EXPRESSÃO REGULAR**<br>Máximo de 32.764 caracteres | |
| Verificar se o atributo da matriz **tem algum valor** ou se não está vazio | **TEM UM VALOR** | **N/A** | Se esse filtro especificar `favorite_genres` e um perfil de usuário contiver `favorite_genres` com qualquer valor, o usuário corresponderá a esse filtro. |
| Verificar se o atributo de matriz **está vazio** ou não existe | **ESTÁ VAZIO** | **N/A** | Se esse filtro especificar `favorite_genres` e um perfil de usuário não contiver `favorite_genres` ou contiver `favorite_genres`, mas não tiver valores, o usuário corresponderá a esse filtro.|
| Verificar se o atributo da matriz **inclui um valor que corresponde exatamente a qualquer um** dos valores inseridos | **INCLUI QUALQUER UM DOS** | **STRING**<br>Diferencia maiúsculas de minúsculas; são permitidos vários valores (máximo de 256) | Se esse filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário tiver qualquer combinação de `sci-fi`, `fantasy`, ou `romance`, incluindo apenas um deles (como apenas `sci-fi`). Um usuário pode ter `horror` ou outro valor em sua string se também tiver qualquer um dos valores `sci-fi`, `fantasy` e `romance`.|
| Verificar se o atributo da matriz **não inclui um valor que corresponda exatamente a qualquer um** dos valores inseridos | **NÃO INCLUI NENHUM DOS** | **STRING**<br>Diferencia maiúsculas de minúsculas; são permitidos vários valores (máximo de 256) | Se esse filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário não tiver nenhuma combinação de `sci-fi`, `fantasy` ou `romance`, o usuário corresponderá a esse filtro. O usuário pode ter `horror` ou outro valor se não tiver nenhum dos seguintes `sci-fi`, `fantasy`, ou `romance`.|
| Verificar se o atributo da matriz **contém um valor que corresponde parcialmente a qualquer um** dos valores inseridos | **CONTÊM QUALQUER UM DOS VALORES** | **STRING**<br>Diferencia maiúsculas de minúsculas; são permitidos vários valores (máximo de 256) | Se esse filtro especificar `gold` e uma matriz de perfil de usuário contiver `gold` em pelo menos uma string, o usuário corresponderá a esse filtro. Isso inclui valores de cadeia de caracteres como `gold_tier`, `former_gold_tier` e outros.|
| Verificar se o atributo da matriz **não inclui um valor que corresponda parcialmente a qualquer um** dos valores inseridos | **NÃO CONTÊM NENHUM DOS VALORES** | **STRING**<br>Diferencia maiúsculas de minúsculas; são permitidos vários valores (máximo de 256) | Se esse filtro especificar `gold` e uma matriz de perfil de usuário não contiver `gold` em nenhuma cadeia de caracteres, o usuário corresponderá a esse filtro. Isso significa que os usuários com valores de string como `gold_tier` e `former_gold_tier` não corresponderão a esse filtro.|
| Verificar se o atributo de matriz **inclui todos os** valores inseridos | **É TUDO DE** | **STRING**<br>Diferencia maiúsculas de minúsculas; são permitidos vários valores (máximo de 256) | Se esse filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário tiver todos esses valores, o usuário corresponderá a esse filtro. O usuário também pode ter `horror` ou outros valores e corresponder a esse filtro.|
| Verificar se o atributo de matriz **não inclui todos os** valores inseridos | **NÃO É TUDO DE** | **STRING**<br>Diferencia maiúsculas de minúsculas; são permitidos vários valores (máximo de 256)|  Se esse filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário não tiver todos esses valores, o usuário corresponderá a esse filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Para saber mais sobre como usar expressões regulares (regex), confira estes recursos:
- [Expressões regulares compatíveis com Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex com o Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Depurador e testador de regex](https://www.regex101.com/)
- [Tutorial de regex](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Tempo {#time}

Os atributos de tempo são úteis para armazenar a última vez em que uma ação específica foi realizada, para que você possa oferecer mensagens de reengajamento específicas de conteúdo aos seus usuários.

Os filtros de tempo que usam datas relativas (por exemplo, mais de 1 dia atrás, menos de 2 dias atrás) medem 1 dia como 24 horas. Qualquer campanha que você executar usando esses filtros incluirá todos os usuários em incrementos de 24 horas. Por exemplo, o site `last used app more than 1 day ago` capturará todos os usuários que "usaram o aplicativo pela última vez há mais de 24 horas" a partir do momento exato em que a campanha for executada. O mesmo se aplica a campanhas definidas com intervalos de datas mais longos - portanto, cinco dias após a ativação significarão as 120 horas anteriores.

Por exemplo, para criar um segmento que tenha como alvo usuários com um atributo de tempo entre 24 e 48 horas no futuro, aplique os filtros `in more than 1 day in the future` e `in less than 2 days in the future`.

{% alert warning %}
A última data em que ocorreu um evento personalizado ou um evento de compra é registrada automaticamente e não deve ser registrada novamente por meio de um atributo de tempo personalizado.
{% endalert %}

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo de tempo **é anterior a** uma **data selecionada**| **ANTES** | **SELETOR DE DATAS DO CALENDÁRIO** | Se esse filtro especificar `2024-01-31` e um perfil de usuário tiver uma data anterior a `2024-1-31`, o usuário corresponderá a esse filtro. |
| Verificar se o atributo de tempo **é posterior a** uma **data selecionada**| **DEPOIS** | **SELETOR DE DATAS DO CALENDÁRIO** | Se esse filtro especificar `2024-01-31` e um perfil de usuário tiver uma data posterior a `2024-1-31`, o usuário corresponderá a esse filtro. |
| Verificar se o atributo de tempo está há **mais de X** **dias** | **MAIS DO QUE** | **NÚMERO DE DIAS ATRÁS** | Se esse filtro especificar `7` e um perfil de usuário tiver uma data que seja de mais de sete dias atrás, o usuário corresponderá a esse filtro. |
| Verificar se o atributo de tempo é **inferior a X** **dias atrás**| **MENOS DE** | **NÚMERO DE DIAS ATRÁS** | Se esse filtro especificar `7` e um perfil de usuário tiver uma data inferior a sete dias atrás, o usuário corresponderá a esse filtro.|
| Verificar se o atributo de tempo está **em um número maior que X** de **dias no futuro** | **EM MAIS DE** | **NÚMERO DE DIAS NO FUTURO** | Se esse filtro especificar `7` e um perfil de usuário tiver uma data que esteja mais de sete dias no futuro, o usuário corresponderá a esse filtro.|
| Verificar se o atributo de tempo está a **menos de X** **dias no futuro** | **EM MENOS DE** | **NÚMERO DE DIAS NO FUTURO**  | Se esse filtro especificar `7` e um perfil de usuário tiver uma data que esteja a menos de sete dias no futuro, o usuário corresponderá a esse filtro.|
| Verificar se o atributo de tempo **existe** no perfil de um usuário e se não é nulo | **NÃO ESTÁ EM BRANCO** | **N/A** | Se esse filtro especificar um atributo de tempo que esteja em um perfil de usuário, o usuário corresponderá a esse filtro.|
| Verificar se o atributo time não **existe** no perfil de um usuário ou se é nulo | **ESTÁ EM BRANCO** | **N/A** | Se esse filtro especificar um atributo de tempo que não esteja em um perfil de usuário, o usuário corresponderá a esse filtro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Detalhes do atributo de tempo

- Dia do evento recorrente
  - Ao usar o filtro "Day of Recurring Event" e for solicitado a selecionar o "Calendar Day of Recurring Event", se você selecionar `IS LESS THAN` ou `IS MORE THAN`, a data atual será contada para esse filtro de segmentação.
  - Por exemplo, se em 10 de março de 2020 você selecionou a data do atributo para ser `LESS THAN ... March 10, 2020`, os atributos serão considerados para os dias até 10 de março de 2020, inclusive. 
- Há menos de X dias: O filtro "Less than X Days Ago" inclui datas entre X dias atrás e a data/hora atual.
- Menos de X dias no futuro: Inclui datas entre a data/hora atual e X dias no futuro.

### Objetos

Você pode usar atributos personalizados aninhados para enviar objetos como um tipo de dados para atributos personalizados. Para obter mais informações, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/).

### Matrizes de objetos

Use uma matriz de objetos para agrupar atributos relacionados. Para obter mais detalhes, consulte nosso artigo sobre [Array of objects]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/).

### Operadoras consolidadas

Consolidamos a lista de operadores disponíveis para uso em filtros de atributos, filtros de atributos personalizados e filtros de atributos personalizados aninhados. Se você tiver filtros existentes que usam esses operadores, eles serão atualizados automaticamente para usar os novos operadores.

| Tipo de dados | Operador antigo | Novo operador | Valor |
| --- | --- | --- | --- |
| Cordas | iguais | é qualquer um dos | Pelo menos 1 valor |
| Cordas | não é igual a | não é nenhum dos | Pelo menos 1 valor |
| Matriz | inclui valor | inclui qualquer um dos | Pelo menos 1 valor |
| Matriz | não inclui valor | não inclui nenhum dos | Pelo menos 1 valor |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Rastreamento de compras e receitas {#purchase-revenue-tracking}

O uso de nossos métodos de compra para registrar compras no aplicativo estabelece o Lifetime Value (LTV) para cada perfil de usuário individual. Esses dados podem ser visualizados em nossa página de receita em séries temporais.

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o número total de dólares gastos **é maior que** um **número**| **MAIOR DO QUE** | **NÚMERO** | Se esse filtro especificar `500` e um perfil de usuário tiver um valor maior que `500`, o usuário corresponderá a esse filtro. |
| Verificar se o número total de dólares gastos **é menor que** um **número**| **MENOS DE** | **NÚMERO** | Se esse filtro especificar `500` e um perfil de usuário tiver um valor menor que `500`, o usuário corresponderá a esse filtro.|
| Verificar se o número total de dólares gastos **é exatamente** um **número**| **EXATAMENTE** | **NÚMERO** | Se esse filtro especificar `500` e um perfil de usuário tiver o valor `500`, o usuário corresponderá a esse filtro. |
| Verifique se a última compra ocorreu **após a data X** | **DEPOIS** | **TEMPO** | Se esse filtro especificar `2024/31/1` e a última compra de um usuário for posterior a `2024/31/1`, o usuário corresponderá a esse filtro.|
| Verifique se a última compra ocorreu **antes da data X** | **ANTES** | **TEMPO** | Se esse filtro especificar `2024/31/1` e a última compra de um usuário for anterior a `2024/31/1`, o usuário corresponderá a esse filtro.|
| Verificar se a última compra ocorreu **há mais de X dias** | **MAIS DO QUE** | **TEMPO** | Se esse filtro especificar `7` e a última compra de um usuário tiver sido há mais de sete dias a partir de hoje, o usuário corresponderá a esse filtro.|
| Verificar se a última compra ocorreu **há menos de X dias** | **MENOS DE** | **TEMPO** |  Se esse filtro especificar `7` e a última compra de um usuário tiver sido feita há menos de sete dias a partir de hoje, o usuário corresponderá a esse filtro.|
| Verifique se a compra ocorreu **mais de X (máx. = 50) vezes** | **MAIS DO QUE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |  Se esse filtro especificar `7` times e `21` days, e um usuário tiver feito mais de sete compras nos últimos 21 dias, o usuário corresponderá a esse filtro.|
| Verificar se a compra ocorreu **menos de X (máx. = 50) vezes** | **MENOS DE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** | Se esse filtro especificar `7` times e `21` days, e um usuário tiver feito menos de sete compras nos últimos 21 dias, o usuário corresponderá a esse filtro.|
| Verificar se a compra ocorreu **exatamente X (máx. = 50) número de vezes** | **EXATAMENTE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** | Se esse filtro especificar `7` times e `21` days, e um usuário tiver feito sete compras nos últimos 21 dias, o usuário corresponderá a esse filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Se quiser segmentar o número de vezes que uma compra específica ocorreu, você também deve registrar essa compra individualmente como um [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

Você pode alterar o tipo de dados do seu atributo personalizado, mas deve estar ciente dos impactos da [alteração dos tipos de dados]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).


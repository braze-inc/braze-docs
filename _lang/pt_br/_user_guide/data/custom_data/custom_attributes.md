---
nav_title: Atributos personalizados
article_title: Atributos personalizados
page_order: 10
page_type: reference
description: "Esta página descreve os atributos personalizados e explica os vários tipos de dados de atributos personalizados."
search_rank: 1
---

# [![curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Atributos personalizados

> Esta página aborda os atributos personalizados, que são uma coleção de características exclusivas de seus usuários. Atributos personalizados são melhores para armazenar atributos sobre seus usuários ou informações sobre ações de baixo valor dentro do seu aplicativo. 

Quando armazenados no Braze, os atributos personalizados podem ser usados para criar segmentos de público e personalizar o envio de mensagens usando o Liquid. Lembre-se de que não armazenamos informações de séries temporais para atributos personalizados, portanto, você não poderá obter nenhum gráfico com base neles, como é possível para eventos personalizados.

## Gerenciando atributos personalizados

Para criar e gerenciar atributos personalizados no dashboard, Acessar **Configurações de Dados** > **Atributos Personalizados**. 

![Quatro atributos personalizados que são booleanos.]({% image_buster /assets/img/export_custom_attributes.png %})

A coluna **Última atualização** lista a última vez que o atributo personalizado foi editado, por exemplo, quando foi definido pela última vez como lista de bloqueio ou ativo.

{% alert important %}
Para o direcionamento adequado de mensagens, certifique-se de que o tipo de dados de seu atributo personalizado corresponda ao atributo personalizado real.
{% endalert %}

A partir desta página, você pode visualizar, gerenciar, criar ou bloquear atributos personalizados existentes. Selecione o menu ao lado de um atributo personalizado para as seguintes ações:

### Colocando na lista de bloqueio

Os atributos personalizados podem ser incluídos em uma lista de bloqueio individualmente no menu de ações ou até 100 atributos podem ser selecionados e incluídos em uma lista de bloqueio em massa. Se você bloquear um atributo personalizado, nenhum dado será coletado em relação a esse atributo, os dados existentes ficarão indisponíveis a menos que sejam reativados, e os atributos na lista de bloqueio não aparecerão em filtros ou gráficos. Além disso, se a atribuição estiver sendo referenciada por filtros ou disparadores em outras áreas do dashboard do Braze, será exibido um modal de aviso explicando que todas as instâncias dos filtros ou disparadores que fazem referência a ela serão removidas e arquivadas.

### Marcação como informações de identificação pessoal (IPI)

Os administradores também podem criar atributos personalizados e marcá-los como IPI nessa página. Esses atributos só serão visíveis para administradores e usuários do dashboard com a permissão “Ver Atributos Personalizados Marcados como IPI”.

### Adicionando descrições

Você pode adicionar uma descrição a um atributo personalizado depois que ele for criado, se você tiver a `Manage Events, Attributes, Purchases` [permissão de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/). Edite o atributo personalizado e insira o que quiser, como uma nota para sua equipe.

### Adicionando tags

Você pode adicionar tags a um atributo personalizado depois de criado, se você tiver a permissão de usuário "Gerenciar Eventos, Atributos, Compras" [user permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/). As tags podem então ser usadas para filtrar a lista de atributos. 

### Remoção de atributos personalizados

Existem duas maneiras de remover atributos personalizados dos perfis de usuário:

* Selecione o nome do atributo personalizado a ser removido em uma [etapa de Atualização do Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes).
* Defina o valor `null` em sua solicitação de API para o endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Visualizando relatórios de uso

O relatório de uso lista todas as canvas, campanhas e segmentos que utilizam um atributo personalizado específico. Essa lista não inclui os usos do Liquid. 

Você pode visualizar até 100 relatórios de utilização por vez, marcando as caixas de seleção ao lado dos respectivos atributos personalizados e, em seguida, selecionando **Visualizar relatório de utilização**.

### Exportação de dados

Para exportar a lista de atributos personalizados como um arquivo CSV, selecione **Exportar tudo** no topo da página. O arquivo CSV será gerado e um link para baixar será enviado para você por e-mail.

## Definindo atributos personalizados

A seguir estão listados métodos em várias plataformas que são usados para definir atributos personalizados.

{% details Expandir para documentação por plataforma %}

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## armazenamento de atributo personalizado

Todos os dados armazenados no **Perfil do Usuário**, incluindo dados de atributo personalizado, são retidos indefinidamente enquanto cada perfil estiver [ativo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## tipos de dados de atributo personalizado

Atributos personalizados são ferramentas extraordinariamente flexíveis que permitem um ótimo direcionamento.

Os seguintes tipos de dados podem ser armazenados como atributos personalizados:

- [Booleanos](#booleans)
- [Números](#numbers)
- [Strings](#strings)
- [Vetores](#arrays)
- [Horário](#time)
- [Objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Arrays de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### Booleanos (verdadeiro/falso) {#booleans}

Atributos booleanos são úteis para armazenar dados binários simples sobre seus usuários, como status de inscrição. Você pode encontrar usuários que explicitamente têm uma variável definida como verdadeira ou falsa, além daqueles que ainda não têm nenhum registro desse atributo registrado.

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verifique se o valor booleano **é** verdadeiro, falso, verdadeiro ou não definido, ou falso ou não definido | **É**  | **VERDADEIRO**, **FALSO**, **VERDADEIRO OU NÃO DEFINIDO**, ou **FALSO OU NÃO DEFINIDO** | Se este filtro especificar `coffee_drinker`, um usuário corresponderá a este filtro nas seguintes circunstâncias: <br> {::nomarkdown}<ul><li>Se este filtro é <code>true</code> e o usuário tem o valor <code>coffee_drinker</code></li><li>Se este filtro é <code>false</code> e o usuário não tem o valor <code>coffee_drinker</code></li><li>Se este filtro é <code>true or not set</code> e o usuário tem o valor <code>coffee_drinker</code> ou nenhum valor</li><li>Se este filtro é <code>false or not set</code> e o usuário não tem <code>coffee_drinker</code> ou qualquer valor</li></ul>{:/} |
| Verifique se o valor booleano **existe** no perfil de um usuário e não é nulo | **NÃO ESTÁ EM BRANCO**  | **N/D** | Se este filtro especificar `coffee_drinker` e um usuário tiver um valor para o atributo `coffee_drinker`, o usuário corresponderá a este filtro. | 
| Verifique se o valor booleano **não existe** no perfil de um usuário ou é nulo | **ESTÁ EM BRANCO**  | **N/D** | Se este filtro especificar `coffee_drinker` e um usuário não tiver o atributo `coffee_drinker` ou o valor para `coffee_drinker` for nulo, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Números {#numbers}

Atributos numéricos incluem [inteiros](https://en.wikipedia.org/wiki/Integer) e [pontos flutuantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic), e têm uma grande variedade de casos de uso. Atributos personalizados de número incremental são úteis para armazenar o número de vezes que uma determinada ação ou evento ocorreu sem contar contra o seu limite de dados. Números padrão têm todos os tipos de usos, como registrar:

- Tamanho do sapato
- Tamanho da cintura
- Número de vezes que um usuário visualizou um determinado recurso, ou categoria de produto

{% alert tip %}
O dinheiro gasto não deve ser registrado por este método. Em vez disso, deve ser registrado através dos nossos [métodos de compra](#purchase-revenue-tracking).
{% endalert %}

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verifique se o atributo numérico **é exatamente** um **número**| **EXATAMENTE** | **NÚMERO** | Se este filtro especificar `10` e um perfil de usuário tiver o valor `10`, o usuário corresponderá a este filtro. |
| Verifique se o atributo numérico **não é igual a** um **número**| **NÃO É IGUAL** | **NÚMERO** | Se este filtro especificar `10` e um perfil de usuário não tiver o valor `10`, o usuário corresponderá a este filtro. |
| Verifique se o atributo numérico **é maior que** um **número**| **MAIS DO QUE** | **NÚMERO** | Se este filtro especificar `10` e um perfil de usuário tiver um valor maior que `10`, o usuário corresponderá a este filtro. |
| Verifique se o atributo numérico **é menor que** um **número**| **MENOS QUE** | **NÚMERO** | Se este filtro especificar `10` e um perfil de usuário tiver um valor menor que `10`, o usuário corresponderá a este filtro. |
| Verifique se o atributo numérico **existe** no perfil de um usuário e não é nulo | **NÃO ESTÁ EM BRANCO** | **N/D** | Se um perfil de usuário contiver o atributo numérico especificado, independentemente do valor, o usuário corresponderá a este filtro. |
| Verifique se o atributo numérico **não existe** no perfil de um usuário ou é nulo | **ESTÁ EM BRANCO** | **N/D** | Se um perfil de usuário não contiver o atributo numérico especificado ou o valor do atributo for nulo, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Detalhes do atributo de número

- Os filtros "Exatamente 0" e "Menos que" incluem usuários com campos NULL
  - Para excluir usuários sem um valor para atributos personalizados, você precisa incluir o filtro **não está em branco**.

### Strings (caracteres alfanuméricos) {#strings}

Os atributos de string são úteis para armazenar a entrada do usuário, como uma marca favorita, um número de telefone ou uma última string de pesquisa dentro do seu aplicativo. Os atributos de string podem ter até 255 caracteres.

Note que se você inserir quaisquer valores com espaços entre, antes ou depois das palavras, então a Braze também verificará os mesmos espaços.

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verifique se o atributo de string **corresponde exatamente** a uma string inserida| **IGUAL** | **STRING**<br>Diferenciação entre maiúsculas e minúsculas | Se este filtro especificar `book` e um perfil de usuário tiver um atributo de string para `last_item_purchased` que contenha `book`, o usuário corresponderá a este filtro. |
| Verifique se o atributo de string **corresponde parcialmente** a uma string inserida **OU** expressão regular | **CORRESPONDE A UMA EXPRESSÃO REGULAR** | **STRING** **OU** **EXPRESSÃO REGULAR** <br>Não diferencia maiúsculas de minúsculas; máximo de 32.764 caracteres | 
| Verifique se o atributo string **não corresponde parcialmente** a uma string inserida **OU** expressão regular | **NÃO CORRESPONDE AO REGEX** \* | **STRING** **OU** **EXPRESSÃO REGULAR**<br>Não diferencia maiúsculas de minúsculas; máximo de 32.764 caracteres |
| Verifique se o atributo de string **não corresponde** a uma string inserida| **NÃO É IGUAL** | **STRING**<br>Não diferencia maiúsculas de minúsculas  | Se este filtro especificar `book` e um perfil de usuário tiver um atributo de string para `last_item_purchased` que não contenha `book`, o usuário corresponderá a este filtro.|
| Verifique se o atributo de string **existe** no perfil de um usuário e não é uma string vazia | **NÃO ESTÁ EM BRANCO** | **N/D** | Se este filtro especificar `favorite_genre` e um perfil de usuário tiver o atributo `favorite_genre`, o usuário corresponderá a este filtro independentemente do valor do atributo. Por exemplo, o usuário pode ter `sci-fi`, `romance` ou outro valor.|
| Verifique se o atributo de string **não existe** no perfil de um usuário | **EM BRANCO** | **N/D** | Se este filtro especificar `favorite_genre` e um perfil de usuário não tiver o atributo `favorite_genre`, o usuário corresponderá a este filtro.|
| Verifique se a string corresponde exatamente a **qualquer** das strings inseridas | **É QUALQUER UMA DE** | **STRING**<br>Diferenciação entre maiúsculas e minúsculas; várias strings permitidas (máximo de 256) | Se este filtro especificar `book`, `bookmark` e `reading light`, e um perfil de usuário tiver pelo menos uma dessas strings, o usuário corresponderá a este filtro. |
| Verifique se o atributo de string **não corresponde exatamente a nenhuma** das strings inseridas | **NÃO É NENHUM** |**STRING**<br>Diferenciação entre maiúsculas e minúsculas; várias strings permitidas (máximo de 256) | Se este filtro especificar `book`, `bookmark` e `reading light`, e um perfil de usuário não contiver nenhuma dessas strings, o usuário corresponderá ao filtro.|
| Verifique se o atributo de string **corresponde parcialmente a qualquer** das strings inseridas | **CONTÉM QUALQUER UM DOS** | **STRING**<br>Diferenciação entre maiúsculas e minúsculas; várias strings permitidas (máximo de 256) | Se este filtro especificar `gold` e um perfil de usuário contiver `gold` em qualquer string, como `gold_tier` ou `former_gold_tier`, o usuário corresponderá ao filtro. |
| Verifique se o atributo de string **não corresponde parcialmente a nenhum** dos strings inseridos | **NÃO CONTÉM NENHUM DE** | **STRING**<br>Diferenciação entre maiúsculas e minúsculas; várias strings permitidas (máximo de 256) | Se este filtro especificar `gold` e um perfil de usuário não contiver `gold` em nenhuma string, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Uma string de data como "12-1-2021" ou "12/1/2021" será convertida em um objeto datetime e tratada como um [atributo de tempo]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
Ao segmentar usando o filtro **NÃO CORRESPONDE À REGEX**, você deve já ter um atributo personalizado com um valor atribuído nesse perfil de usuário. Braze sugere usar a lógica "OU" para verificar se um atributo personalizado está em branco para garantir que os usuários sejam direcionados corretamente.
{% endalert %}

### Vetores {#arrays}

Os atributos de array são bons para armazenar listas relacionadas de informações sobre seus usuários. Por exemplo, armazenar os últimos 100 conteúdos que um usuário assistiu em um array permitiria a segmentação de interesses específicos.

Por padrão, o comprimento de uma matriz para um atributo é de até 500 itens. Por exemplo, se você estiver enviando uma atribuição como "Movies Watched" (Filmes assistidos) e ela estiver definida como 500, quando um usuário assistir ao 501º filme, o primeiro filme será removido da matriz e o filme mais recente será adicionado.

Observe que, se você inserir valores com espaços entre, antes ou depois das palavras, o Braze também verificará se há os mesmos espaços.

{% alert note %}
A opção para aumentar o comprimento máximo não estará disponível se o atributo estiver configurado para detectar automaticamente o tipo de dado; o tipo de dado deve ser configurado como array.
{% endalert %}

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verifique se o atributo do array **inclui um valor que corresponda exatamente** a um valor inserido| **INCLUI VALOR** | **STRING** | Se este filtro especificar `sci-fi` e um perfil de usuário tiver o valor `sci-fi`, o usuário corresponderá a este filtro.|
| Verifique se o atributo do vetor **não inclui um valor que corresponda exatamente** a um valor inserido| **NÃO INCLUI VALOR** | **STRING** | Se este filtro especificar `sci-fi` e um perfil de usuário não tiver o valor `sci-fi`, o usuário corresponderá a este filtro.|
| Verifique se o atributo do vetor **contém um valor que corresponde parcialmente** a um valor inserido **OU** expressão regular | **CORRESPONDE A UMA EXPRESSÃO REGULAR** | **STRING** **OU** **EXPRESSÃO REGULAR**<br>Máximo de 32.764 caracteres | |
| Verifique se o atributo do array **tem algum valor** ou não está vazio | **TEM UM VALOR** | **N/D** | Se este filtro especificar `favorite_genres` e um perfil de usuário contiver `favorite_genres` com qualquer valor, o usuário corresponderá a este filtro. |
| Verifique se o atributo do array **está vazio** ou não existe | **ESTÁ VAZIO** | **N/D** | Se este filtro especificar `favorite_genres` e um perfil de usuário não contiver `favorite_genres` ou contiver `favorite_genres` mas não tiver valores, o usuário corresponderá a este filtro.|
| Verifique se o atributo do array **inclui um valor que corresponda exatamente a qualquer** dos valores inseridos | **INCLUI QUALQUER UM DOS** | **STRING**<br>Diferencia maiúsculas de minúsculas; vários valores permitidos (256 no máximo) | Se este filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário tiver qualquer combinação de `sci-fi`, `fantasy` ou `romance`, incluindo apenas um deles (como apenas `sci-fi`). Um usuário pode ter `horror` ou outro valor em sua string se também tiver qualquer um de `sci-fi`, `fantasy` e `romance`.|
| Verifique se o atributo do array **não inclui um valor que corresponda exatamente a qualquer** dos valores inseridos | **NÃO INCLUI NENHUM** | **STRING**<br>Diferencia maiúsculas de minúsculas; vários valores permitidos (256 no máximo) | Se este filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário não tiver nenhuma combinação de `sci-fi`, `fantasy` ou `romance`, o usuário corresponderá a este filtro. O usuário pode ter `horror` ou outro valor se não tiver nenhum de `sci-fi`, `fantasy` ou `romance`.|
| Verifique se o atributo do array **contém um valor que corresponde parcialmente a qualquer** dos valores inseridos | **VALORES CONTÊM QUALQUER UM DOS** | **STRING**<br>Diferencia maiúsculas de minúsculas; vários valores permitidos (256 no máximo) | Se este filtro especificar `gold` e um vetor de perfil de usuário contiver `gold` em pelo menos uma string, o usuário corresponderá a este filtro. Isso inclui valores de string como `gold_tier`, `former_gold_tier` e outros.|
| Verifique se o atributo do array **não inclui um valor que corresponda parcialmente a qualquer** dos valores inseridos | **VALORES NÃO CONTÊM NENHUM DE** | **STRING**<br>Diferencia maiúsculas de minúsculas; vários valores permitidos (256 no máximo) | Se este filtro especificar `gold` e um vetor de perfil de usuário não contiver `gold` em nenhuma string, o usuário corresponderá a este filtro. Isso significa que usuários com valores de string como `gold_tier` e `former_gold_tier` não corresponderão a este filtro.|
| Verifique se o atributo do array **inclui todos** os valores inseridos | **ESTÁ TUDO DE** | **STRING**<br>Diferencia maiúsculas de minúsculas; vários valores permitidos (256 no máximo) | Se este filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário tiver todos esses valores, o usuário corresponderá a este filtro. O usuário também pode ter `horror` ou outros valores e corresponder a este filtro.|
| Verifique se o atributo do array **não inclui todos os** valores inseridos | **NÃO ESTÁ TUDO DE** | **STRING**<br>Diferencia maiúsculas de minúsculas; vários valores permitidos (256 no máximo)|  Se este filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário não tiver todos esses valores, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Para saber mais sobre como usar expressões regulares (regex), confira estes recursos:
- [Expressões regulares compatíveis com Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [regex com Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Depurador e testador de regex](https://www.regex101.com/)
- [Tutorial de regex](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Tempo {#time}

Os atributos de tempo são úteis para armazenar a última vez que uma ação específica foi realizada, para que você possa oferecer envio de mensagens de reengajamento específico de conteúdo aos seus usuários.

Os filtros de horas que usam datas relativas (por exemplo, mais de 1 dia atrás, menos de 2 dias atrás) medem 1 dia como 24 horas. Qualquer campanha que você executar usando esses filtros incluirá todos os usuários em incrementos de 24 horas. Por exemplo, `last used app more than 1 day ago` capturará todos os usuários que "usaram o app há mais de 24 horas" a partir do momento exato em que a campanha for executada. O mesmo será verdadeiro para campanhas definidas com intervalos de datas mais longos—então FIVE dias a partir da ativação significarão as 120 horas anteriores.

Por exemplo, para criar um segmento que visa usuários com um atributo de tempo entre 24 e 48 horas no futuro, aplique os filtros `in more than 1 day in the future` e `in less than 2 days in the future`.

{% alert warning %}
A última data em que um evento personalizado ou evento de compra ocorreu é registrada automaticamente e não deve ser registrada novamente por meio de um atributo de tempo personalizado.
{% endalert %}

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verifique se o atributo de tempo **é anterior a** uma **data selecionada**| **ANTES** | **SELETOR DE DATA DO CALENDÁRIO** | Se este filtro especificar `2024-01-31` e um perfil de usuário tiver uma data anterior a `2024-1-31`, o usuário corresponderá a este filtro. |
| Verifique se o atributo de tempo **é posterior** a uma **data selecionada**| **DEPOIS** | **SELETOR DE DATA DO CALENDÁRIO** | Se este filtro especificar `2024-01-31` e um perfil de usuário tiver uma data após `2024-1-31`, o usuário corresponderá a este filtro. |
| Verifique se o atributo de tempo é **maior do que X** **dias atrás** | **MAIS DO QUE** | **NÚMERO DE DIAS ATRÁS** | Se este filtro especificar `7` e um perfil de usuário tiver uma data que seja superior a sete dias, o usuário corresponderá a este filtro. |
| Verifique se o atributo de tempo é **menor do que X ** **dias atrás**| **MENOS QUE** | **NÚMERO DE DIAS ATRÁS** | Se este filtro especificar `7` e um perfil de usuário tiver uma data que seja inferior a sete dias, o usuário corresponderá a este filtro.|
| Verifique se o atributo de tempo está **em mais de X número** de **dias no futuro** | **EM MAIS DE** | **NÚMERO DE DIAS NO FUTURO** | Se este filtro especificar `7` e um perfil de usuário tiver uma data que seja superior a sete dias no futuro, o usuário corresponderá a este filtro.|
| Verifique se o atributo de tempo é **menor que X número** de **dias no futuro** | **EM MENOS DE** | **NÚMERO DE DIAS NO FUTURO**  | Se este filtro especificar `7` e um perfil de usuário tiver uma data que seja anterior a sete dias no futuro, o usuário corresponderá a este filtro.|
| Verifique se o atributo de tempo **existe** no perfil de um usuário e não é nulo | **NÃO ESTÁ EM BRANCO** | **N/D** | Se este filtro especificar um atributo de tempo que está no perfil de um usuário, o usuário corresponderá a este filtro.|
| Verifique se o atributo de tempo **não existe** no perfil de um usuário ou é nulo | **ESTÁ EM BRANCO** | **N/D** | Se este filtro especificar um atributo de tempo que não está no perfil de um usuário, o usuário corresponderá a este filtro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Detalhes do atributo de tempo

- Dia do evento recorrente
  - Ao usar o filtro "Dia do Evento Recorrente" e, em seguida, for solicitado a selecionar o "Dia do Calendário do Evento Recorrente", se você selecionar `IS LESS THAN` ou `IS MORE THAN`, a data atual será contada para esse filtro de segmentação.
  - Por exemplo, se no dia 10 de março de 2020, você selecionou a data do atributo para ser `LESS THAN ... March 10, 2020`, os atributos serão considerados para os dias até, e incluindo 10 de março de 2020. 
- Menos de X dias atrás: O filtro "Menos de X dias atrás" inclui datas entre X dias atrás e a data/hora atual.
- Menos de X dias no futuro: Inclui datas entre a data/hora atual e X dias no futuro.

### Objetos

Você pode usar atributos personalizados aninhados para enviar objetos como um tipo de dado para atributos personalizados. Para saber mais, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/).

### Arrays de objetos

Use um array de objetos para agrupar atributos relacionados. Para saber mais, consulte nosso artigo sobre [Array de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/).

### Operadores consolidados

Consolidamos uma lista de operadores disponíveis para usar nos filtros de atributos, filtros de atributos personalizados e filtros de atributos personalizados aninhados. Se você tiver filtros existentes usando esses operadores, eles serão atualizados automaticamente para usar os novos operadores.

| Tipo de dados | Operador antigo | Novo operador | Valor |
| --- | --- | --- | --- |
| String | é igual a | é qualquer uma de | Pelo menos 1 valor |
| String | não é igual a | não é nenhuma de | Pelo menos 1 valor |
| Vetor | inclui o valor | inclui qualquer um de | Pelo menos 1 valor |
| Vetor | não inclui o valor | não inclui nenhum de | Pelo menos 1 valor |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Rastreamento de compras e receitas {#purchase-revenue-tracking}

Usar nossos métodos de compra para registrar compras no app estabelece o valor do tempo de vida (LTV) para cada perfil de usuário individual. Esses dados podem ser visualizados em nossa página de receita em série temporal.

| Opções de segmentação | Filtro suspenso | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verifique se o número total de dólares gastos **é maior que** um **número**| **MAIOR QUE** | **NÚMERO** | Se este filtro especificar `500` e um perfil de usuário tiver um valor maior que `500`, o usuário corresponderá a este filtro. |
| Verifique se o número total de dólares gastos **é menor que** um **número**| **MENOS QUE** | **NÚMERO** | Se este filtro especificar `500` e um perfil de usuário tiver um valor menor que `500`, o usuário corresponderá a este filtro.|
| Verifique se o número total de dólares gastos **é exatamente** um **número**| **EXATAMENTE** | **NÚMERO** | Se este filtro especificar `500` e um perfil de usuário tiver o valor `500`, o usuário corresponderá a este filtro. |
| Verifique se a compra ocorreu **após a data X** | **DEPOIS** | **TIME** | Se este filtro especificar `2024/31/1` e a última compra de um usuário foi após `2024/31/1`, o usuário corresponderá a este filtro.|
| Verifique se a compra ocorreu **antes da data X** | **ANTES** | **TIME** | Se este filtro especificar `2024/31/1` e a última compra de um usuário foi antes de `2024/31/1`, o usuário corresponderá a este filtro.|
| Verifique se a compra ocorreu pela última vez **há mais de X dias** | **MAIS DO QUE** | **TIME** | Se este filtro especificar `7` e a última compra de um usuário foi há mais de sete dias a partir de hoje, o usuário corresponderá a este filtro.|
| Verifique se a compra ocorreu pela última vez **há menos de X dias** | **MENOS QUE** | **TIME** |  Se este filtro especificar `7` e a última compra de um usuário foi há menos de sete dias a partir de hoje, o usuário corresponderá a este filtro.|
| Verifique se a compra ocorreu **mais de X (Máx = 50) vezes** | **MAIS DO QUE** | nos últimos **D Dias (D = 1,3,7,14,21,30)** |  Se este filtro especificar `7` vezes e `21` dias, e um usuário fizer mais de sete compras nos últimos 21 dias, o usuário corresponderá a este filtro.|
| Verifique se a compra ocorreu **menos de X (Máx = 50) vezes** | **MENOS QUE** | nos últimos **D Dias (D = 1,3,7,14,21,30)** | Se este filtro especificar `7` vezes e `21` dias, e um usuário fizer menos de sete compras nos últimos 21 dias, o usuário corresponderá a este filtro.|
| Verifique se a compra ocorreu **exatamente X (Máx = 50) vezes** | **EXATAMENTE** | nos últimos **D Dias (D = 1,3,7,14,21,30)** | Se este filtro especificar `7` vezes e `21` dias, e um usuário fizer sete compras nos últimos 21 dias, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Se você gostaria de segmentar pelo número de vezes que uma compra específica ocorreu, você também deve registrar essa compra individualmente como um [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

Você pode alterar o tipo de dado do seu atributo personalizado, mas deve estar ciente dos impactos de [alterar tipos de dados]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).


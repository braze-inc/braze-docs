---
nav_title: Análise de dados
article_title: Sobre a análise de dados para o SDK Braze
page_order: 2.6
description: "Saiba mais sobre a análise de dados do SDK Braze, para que você possa entender melhor quais dados o Braze coleta, a diferença entre eventos personalizados e atributos personalizados, e as melhores práticas para gerenciar a análise de dados."
platform: 
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - Unreal Engine
  - .NET MAUI
---

# Análise de dados

> Saiba mais sobre a análise de dados do SDK Braze, para que você possa entender melhor quais dados o Braze coleta, a diferença entre eventos personalizados e atributos personalizados, e as melhores práticas para gerenciar a análise de dados.

{% alert tip %}
Durante a sua implementação do Braze, certifique-se de discutir as metas de marketing com sua equipe, para que você possa decidir da melhor forma quais dados deseja rastrear e como deseja rastreá-los com o Braze. Como exemplo, veja nosso estudo de caso de [Taxi/Viagem por aplicativo](#example-case) no final deste guia.
{% endalert %}

## Dados coletados automaticamente

Certos dados de usuários são coletados automaticamente pelo nosso SDK—por exemplo, Primeiro Uso do App, Último Uso do App, Contagem Total de Sessões, Sistema Operacional do Dispositivo, etc. Se você seguir nossos guias de integração para implementar nossos SDKs, poderá aproveitar esta [coleta de dados padrão]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). Verificar esta lista pode ajudá-lo a evitar armazenar as mesmas informações sobre os usuários mais de uma vez. Com exceção do início e término da sessão, todos os outros dados rastreados automaticamente não contam para sua alocação de pontos de dados.

Consulte nosso artigo [SDK primer]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/) para processos de lista de permissão que bloqueiam a coleta padrão de certos itens de dados.

## Eventos personalizados

Eventos personalizados são ações realizadas pelos seus usuários; eles são mais adequados para o rastreamento de interações de alto valor dos usuários com seu aplicativo. Registrar um evento personalizado pode disparar qualquer número de campanhas de acompanhamento com atrasos configuráveis e permite os seguintes filtros de segmentação em torno da recência e frequência desse evento:

| Opções de Segmentação | Filtro suspenso | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o evento personalizado ocorreu **mais de um número X de vezes** | **MAIS DO QUE** | **NÚMERO** |
| Verificar se o evento personalizado ocorreu **menos de um número X de vezes** | **MENOS QUE** | **NÚMERO** |
| Verificar se o evento personalizado ocorreu **exatamente X vezes** | **EXATAMENTE** | **NÚMERO** |
| Verificar se o evento personalizado ocorreu pela última vez **após a data X** | **DEPOIS** | **TIME** |
| Verificar se o evento personalizado ocorreu pela última vez **antes da data X** | **ANTES** | **TIME** |
| Verificar se o evento personalizado ocorreu pela última vez **há mais de X dias** | **MAIS DO QUE** | **QUANTIDADE DE DIAS ATRÁS** (Número Positivo) |
| Verifique se o evento personalizado ocorreu pela última vez **há menos de X dias** | **MENOS DO QUE** | **QUANTIDADE DE DIAS ATRÁS** (Número Positivo) |
| Verifique se o evento personalizado ocorreu **mais de X (Máx = 50) vezes** | **MAIS DO QUE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **menos de X (máx. = 50) vezes** | **MENOS QUE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **exatamente X (máx. = 50) vezes** | **EXATAMENTE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze registra o número de vezes que esses eventos ocorreram, bem como a última vez que foram realizados por cada usuário para segmentação. Na página de análise de dados de **Eventos Personalizados**, você pode ver em agregado com que frequência cada evento personalizado ocorre, bem como por segmento ao longo do tempo para uma análise mais detalhada. Isso é particularmente útil para ver como suas campanhas afetaram a atividade de evento personalizado, observando as linhas cinzas que a Braze sobrepõe na série temporal para indicar a última vez que uma campanha foi enviada.

![Um gráfico de análise de dados de evento personalizado mostrando estatísticas sobre usuários que adicionaram um cartão de crédito e fizeram uma pesquisa em um período de trinta dias.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
O [incremento de atributos personalizados]({{site.baseurl}}/api/endpoints/messaging/) pode ser usado para manter um contador em uma ação do usuário semelhante a um evento personalizado. No entanto, você não poderá visualizar os dados do atributo personalizado em uma série temporal. Ações do usuário que não precisam ser analisadas em séries temporais devem ser registradas por meio deste método.
{% endalert %}

### Armazenamento de eventos personalizados

Todos os dados do perfil do usuário (eventos personalizados, atributo personalizado, dados personalizados) são armazenados enquanto esses perfis estiverem ativos.

### Propriedades do evento personalizado

Com propriedades de evento personalizado, a Braze permite que você defina propriedades em eventos personalizados e compras. Essas propriedades podem então ser usadas para qualificar ainda mais as condições de disparo, aumentar a personalização no envio de mensagens e gerar análises de dados mais sofisticadas por meio da exportação de dados brutos. Os valores das propriedades podem ser string, número, booleano ou objetos de tempo. No entanto, os valores das propriedades não podem ser objetos de vetor.

Por exemplo, se um aplicativo de eCommerce quisesse enviar uma mensagem a um usuário quando ele abandona o carrinho, poderia ainda melhorar seu público-alvo e permitir uma maior personalização da campanha ao adicionar uma propriedade de evento personalizada do `cart_value` dos carrinhos dos usuários.

![Um exemplo de evento personalizado que enviará uma campanha a um usuário que abandonou seu carrinho e deixou o valor do carrinho em mais de 100 e menos de 200.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

As propriedades do evento personalizado também podem ser usadas para personalização dentro do modelo de envio de mensagens. Qualquer campanha que use a [Entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) com um evento de gatilho pode usar propriedades de evento personalizado desse evento para personalização de envio de mensagens. Se um aplicativo de jogos quisesse enviar uma mensagem aos usuários que completaram um nível, ele poderia personalizar ainda mais a mensagem com uma propriedade para o tempo que os usuários levaram para completar esse nível. Neste exemplo, a mensagem é personalizada para três segmentos diferentes usando [lógica condicional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/). A propriedade do evento personalizado chamada ``time_spent``, pode ser incluída na mensagem chamando ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players fromm around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

As propriedades do evento personalizado são projetadas para ajudá-lo a personalizar seu envio de mensagens ou criar campanhas de entrega baseada em ação granulares. Se você gostaria de criar segmentos com base na recência e frequência da propriedade do evento, entre em contato com seu gerente de sucesso do cliente ou nossa equipe de Suporte.

## Atributos personalizados

Atributos personalizados são ferramentas extraordinariamente flexíveis que permitem direcionar usuários com maior especificidade do que você faria com atributos padrão. Atributos personalizados são ótimos para armazenar informações específicas da marca sobre seus usuários. Você deve ter em mente que não armazenamos informações de séries temporais para atributos personalizados, então você não obterá nenhum gráfico baseado neles como o exemplo anterior para eventos personalizados.

### armazenamento de atributo personalizado

Todos os dados do perfil do usuário (eventos personalizados, atributo personalizado, dados personalizados) são armazenados enquanto esses perfis estiverem ativos.

### tipos de dados de atributo personalizado

Os seguintes tipos de dados podem ser armazenados como atributos personalizados:

#### Strings (caracteres alfanuméricos)

Atributos de string são úteis para armazenar a entrada do usuário, como uma marca favorita, um número de telefone ou uma última string de pesquisa dentro do seu aplicativo. Os atributos de string podem ter até 255 caracteres.

A tabela a seguir descreve as opções de segmentação disponíveis para atributos de string.

| Opções de Segmentação | Filtro suspenso | Opções de Entrada |
| ---------------------| --------------- | ------------- |
| Verifique se o atributo de string **corresponde exatamente** a uma string inserida| **IGUAL** | **STRING** |
| Verifique se o atributo string **corresponde parcialmente** a uma string inserida **OU** expressão regular | **CORRESPONDE A UMA EXPRESSÃO REGULAR** | **STRING** **OU** **EXPRESSÃO REGULAR** |
| Verifique se o atributo string **não corresponde parcialmente** a uma string inserida **OU** expressão regular | **NÃO CORRESPONDE AO REGEX** | **STRING** **OU** **EXPRESSÃO REGULAR** |
| Verifique se o atributo de string **não corresponde** a uma string inserida| **NÃO É IGUAL** | **STRING** |
| Verifique se o atributo de string **existe** no perfil de um usuário | **ESTÁ EM BRANCO** | **N/D** |
| Verifique se o atributo de string **não existe** no perfil de um usuário | **NÃO ESTÁ EM BRANCO** | **N/D** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Ao segmentar usando o filtro **DOES NOT MATCH REGEX**, é necessário que já exista um atributo personalizado com um valor atribuído nesse perfil de usuário. Braze sugere usar a lógica "OU" para verificar se um atributo personalizado está em branco, a fim de segmentar os usuários corretamente.
{% endalert %}

{% alert tip %}
Para mais informações sobre como usar nosso filtro de expressões regulares, confira esta documentação sobre [expressões regulares compatíveis com Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Mais recursos sobre regex:
- [regex com Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Depurador e Testador de regex](https://regex101.com/)
- [Tutorial de regex](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Vetores

Os atributos de array são bons para armazenar listas relacionadas de informações sobre seus usuários. Por exemplo, armazenar as últimas 100 peças de conteúdo que um usuário assistiu em um array permitiria a segmentação de interesses específicos.

Os arrays de atributo personalizado são conjuntos unidimensionais; arrays multidimensionais não são suportados. **Adicionar um elemento a uma matriz de atributos personalizados anexa o elemento ao final da matriz, a menos que ele já esteja presente, caso em que ele é movido de sua posição atual para o final da matriz.** Por exemplo, se um vetor `['hotdog','hotdog','hotdog','pizza']` for importado, ele será exibido no atributo de vetor como `['hotdog', 'pizza']` porque somente valores exclusivos são aceitos.

Se o array contiver seu número máximo de elementos, o primeiro elemento será descartado e o novo elemento adicionado ao final. A seguir estão listados alguns exemplos de código mostrando o comportamento do vetor no SDK da web:

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

O número máximo de elementos em vetores de atributos personalizados é, por padrão, 25. O máximo para arrays individuais pode ser aumentado para até 100 no dashboard da Braze, em **Configurações de Dados** > **Atributos Personalizados**. Se você gostaria que esse máximo fosse aumentado, entre em contato com seu gerente de atendimento ao cliente. Arrays que excederem o número máximo de elementos serão truncados para conter o número máximo de elementos.

A tabela a seguir descreve as opções de segmentação disponíveis para atributos de matriz.

| Opções de Segmentação | Filtro suspenso | Opções de Entrada |
| ---------------------| --------------- | ------------- |
| Verifique se o atributo do array **inclui um valor que corresponda exatamente** a um valor inserido| **INCLUI VALOR** | **STRING** |
| Verifique se o atributo do vetor **não inclui um valor que corresponda exatamente** a um valor inserido| **NÃO INCLUI VALOR** | **STRING** |
| Verifique se o atributo do vetor **contém um valor que corresponde parcialmente** a um valor inserido **OU** expressão regular | **CORRESPONDE A UMA EXPRESSÃO REGULAR** | **STRING** **OU** **EXPRESSÃO REGULAR** |
| Verifique se o atributo do array **tem algum valor** | **TEM UM VALOR** | **N/D** |
| Verifique se o atributo do array **está vazio** | **ESTÁ VAZIO** | **N/D** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Usamos [expressões regulares compatíveis com Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
{% endalert %}

#### Datas

Os atributos de tempo são úteis para armazenar a última vez que uma ação específica foi realizada, para que você possa oferecer envio de mensagens de reengajamento específico de conteúdo aos seus usuários.

{% alert note %}
A última data em que um evento personalizado ou evento de compra ocorreu é registrada automaticamente e não deve ser registrada em duplicidade por meio de um atributo de tempo personalizado.
{% endalert %}

Os filtros de data que usam datas relativas (por exemplo, mais de 1 dia atrás, menos de 2 dias atrás) medem 1 dia como 24 horas. Qualquer campanha que você executar usando esses filtros incluirá todos os usuários em incrementos de 24 horas. Por exemplo, o último app usado há mais de 1 dia capturará todos os usuários que "usaram o app pela última vez há mais de 24 horas" a partir do momento exato em que a campanha for executada. O mesmo será verdadeiro para campanhas definidas com intervalos de datas mais longos – então FIVE dias a partir da ativação significarão as 120 horas anteriores.

A tabela a seguir descreve as opções de segmentação disponíveis para atributos de tempo.

| Opções de Segmentação | Filtro suspenso | Opções de Entrada |
| ---------------------| --------------- | ------------- |
| Verifique se o atributo de tempo **é anterior** a uma **data selecionada**| **ANTES** | **SELETOR DE DATA DO CALENDÁRIO** |
| Verifique se o atributo de tempo **é posterior** a uma **data selecionada**| **DEPOIS** | **SELETOR DE DATA DO CALENDÁRIO** |
| Verifique se o atributo de tempo é **maior do que X** **dias atrás** | **MAIS DO QUE** | **NÚMERO DE DIAS ATRÁS** |
| Verifique se o atributo de tempo é **menor do que X ** **dias atrás**| **MENOS QUE** | **NÚMERO DE DIAS ATRÁS** |
| Verifique se o atributo de tempo está **em mais de X número** de **dias no futuro** | **EM MAIS DE** | **NÚMERO DE DIAS NO FUTURO** |
| Verifique se o atributo de tempo é **menor que X número** de **dias no futuro** | **EM MENOS DE** | **NÚMERO DE DIAS NO FUTURO**  |
| Verifique se o atributo de tempo **existe** no perfil de um usuário | **EM BRANCO** | **N/D** |
| Verifique se o atributo de tempo **não existe** no perfil de um usuário | **NÃO ESTÁ EM BRANCO** | **N/D** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Números {#integers}

Atributos numéricos têm uma ampla variedade de casos de uso. Atributos personalizados de número incremental são úteis para armazenar o número de vezes que uma determinada ação ou evento ocorreu. Números padrão têm todos os tipos de usos, como registrar o tamanho do sapato, o tamanho da cintura ou o número de vezes que um usuário visualizou um determinado recurso ou categoria de produto.

{% alert note %}
O dinheiro gasto não deve ser registrado por este método. Em vez disso, deve ser registrado através dos nossos [métodos de compra]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#purchase-events--revenue-tracking).
{% endalert %}

A tabela a seguir descreve as opções de segmentação disponíveis para atributos numéricos.

| Opções de Segmentação | Filtro suspenso | Opções de Entrada |
| ---------------------| --------------- | ------------- |
| Verifique se o atributo numérico **é mais do que** um **número**| **MAIS DO QUE** | **NÚMERO** |
| Verifique se o atributo numérico **é menor que** um **número**| **MENOS QUE** | **NÚMERO** |
| Verifique se o atributo numérico **é exatamente** um **número**| **EXATAMENTE** | **NÚMERO** |
| Verifique se o atributo numérico **não é igual a** um **número**| **NÃO É IGUAL** | **NÚMERO** |
| Verifique se o atributo numérico **existe** no perfil de um usuário | **EXISTE** | **N/D** |
| Verifique se o atributo numérico **não existe** no perfil de um usuário | **NÃO EXISTE** | **N/D** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Booleanos (verdadeiro/falso)

Atributos booleanos são úteis para armazenar status de inscrições e outros dados binários simples sobre seus usuários. As opções de entrada que fornecemos permitem que você encontre usuários que explicitamente tiveram uma variável definida como booleana, além daqueles que ainda não têm nenhum registro desse atributo registrado.

A tabela a seguir descreve as opções de segmentação disponíveis para atributos booleanos.

| Opções de Segmentação | Filtro suspenso | Opções de Entrada |
| ---------------------| --------------- | ------------- |
| Verifique se o valor booleano **é** | **É**  | **VERDADEIRO**, **FALSO**, **VERDADEIRO OU NÃO DEFINIDO**, ou **FALSO OU NÃO DEFINIDO** |
| Verifique se o valor booleano **existe** no perfil de um usuário | **EXISTE**  | **N/D** |
| Verifique se o valor booleano **não existe** no perfil de um usuário | **NÃO EXISTE**  | **N/D** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Acompanhamento de eventos de compra / rastreamento de receita

Usar nossos métodos de compra para registrar compras in-app estabelece o Valor de Vida Útil (LTV) para cada perfil de usuário individual. Esses dados podem ser visualizados em nossa página de receita em gráficos de séries temporais.

A tabela a seguir descreve as opções de segmentação disponíveis para eventos de compra.

| Opções de Segmentação | Filtro suspenso | Opções de Entrada |
| ---------------------| --------------- | ------------- |
| Verifique se o número total de dólares gastos **é maior que** um **número**| **MAIOR QUE** | **NÚMERO** |
| Verifique se o número total de dólares gastos **é menor que** um **número**| **MENOS QUE** | **NÚMERO** |
| Verifique se o número total de dólares gastos **é exatamente** um **número**| **EXATAMENTE** | **NÚMERO** |
| Verifique se a compra ocorreu **após a data X** | **DEPOIS** | **TIME** |
| Verifique se a compra ocorreu **antes da data X** | **ANTES** | **TIME** |
| Verifique se a compra ocorreu pela última vez **há mais de X dias** | **MAIS DO QUE** | **TIME** |
| Verifique se a compra ocorreu pela última vez **há menos de X dias** | **MENOS QUE** | **TIME** |
| Verifique se a compra ocorreu **mais de X (Máx = 50) vezes** | **MAIS DO QUE** | nos últimos **Y Dias (Y = 1,3,7,14,21,30)** |
| Verifique se a compra ocorreu **menos do que X (Máx = 50) vezes** | **MENOS QUE** | nos últimos **Y Dias (Y = 1,3,7,14,21,30)** |
| Verifique se a compra ocorreu **exatamente X (Máx = 50) vezes** | **EXATAMENTE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Se você gostaria de segmentar pelo número de vezes que uma compra específica ocorreu, você também deve registrar essa compra individualmente como um [atributo personalizado incremental](#integers).
{% endalert %}

## Caso de uso de táxi/viagem por app {#example-case}

Para este exemplo, vamos considerar uma viagem por aplicativo que deseja decidir quais dados de usuários coletar. As seguintes perguntas e processo de brainstorming são um ótimo modelo para as equipes de marketing e desenvolvimento seguirem. Até o final deste exercício, ambas as equipes devem ter uma compreensão sólida de quais eventos e atributos personalizados fazem sentido coletar para ajudar a alcançar seu objetivo.

**Questão de estudo de caso 1: Qual é o objetivo?**

O objetivo deles é simples, pois eles querem que os usuários chamem táxis via seu app.

**Questão de estudo de caso 2: Quais são as etapas intermediárias no caminho para esse objetivo a partir da instalação do app?**

1. Eles precisam que os usuários comecem o processo de registro e preencham suas informações pessoais.
2. Eles precisam que os usuários concluam e verifiquem o processo de registro inserindo um código no app que recebem via SMS.
3. Eles precisam tentar chamar um táxi.
4. Para chamar um táxi, ele deve estar disponível quando for procurado.

Essas ações poderiam então ser marcadas como os seguintes eventos personalizados:

- Início do registro
- Registro concluído
- Chamadas de táxi bem-sucedidas
- Tentativas de Táxi Mal-Sucedidas

Depois de implementar os eventos, você pode agora executar as seguintes campanhas:

1. Envie mensagens para os usuários que começaram o registro, mas não dispararam o evento de registro concluído em um determinado período de tempo.
2. Enviar mensagens de parabéns aos usuários que completam o registro.
3. Envie desculpas e crédito promocional aos usuários que tiveram tentativas de chamar táxi malsucedidas que não foram seguidas por uma tentativa bem-sucedida dentro de um determinado período de tempo.
4. Envie promoções para usuários avançados com muitos Táxis Bem-Sucedidos para agradecê-los por sua fidelidade.

E muitos mais!

**Questão de estudo de caso 3: Que outras informações podemos querer saber sobre nossos usuários que informarão nosso envio de mensagens?**

- Se eles têm ou não algum crédito promocional?
- A avaliação média que eles dão aos seus motoristas?
- Códigos promocionais únicos para o usuário?

Essas características poderiam então ser marcadas como os seguintes atributos personalizados:

- Saldo de Crédito Promocional (Tipo Decimal)
- Classificação Média do Motorista (Tipo Numérico)
- Código Promocional Único (Tipo string)

Adicionar esses atributos lhe daria a capacidade de enviar campanhas para os usuários, como:

1. Lembre os usuários que não fizeram login em sete dias, mas que têm um crédito promocional, que seu crédito existe e que eles devem voltar ao app para usá-lo!
2. Envie mensagens aos usuários que dão baixas avaliações aos motoristas para obter feedback direto dos clientes e entender por que eles não gostaram de suas viagens.
3. Use nossos [recursos de modelo de mensagem e personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) para arrastar o atributo de código promocional exclusivo para o envio de mensagens direcionadas aos usuários.

## Melhores práticas

### Práticas gerais recomendadas

#### Usar propriedades de evento

- Nomeie um evento personalizado algo que descreva uma ação que um usuário realiza.
- Faça uso generoso das propriedades de evento personalizado para representar dados importantes sobre um evento.
- Por exemplo, em vez de capturar um evento personalizado separado para assistir a cada um dos 50 filmes diferentes, seria mais eficaz capturar simplesmente assistir a um filme como um evento e ter uma propriedade de evento que inclua o nome do filme.

### Melhores práticas de desenvolvimento

#### Defina IDs de usuário para cada usuário

Os IDs de usuário devem ser definidos para cada um de seus usuários. Esses devem ser imutáveis e acessíveis quando um usuário abre o app. Recomendamos **fortemente** fornecer este identificador, pois isso permitirá que você:

- Acompanhe seus usuários em dispositivos e plataformas, melhorando a qualidade de seus dados comportamentais e demográficos.
- Importe dados de seus usuários usando nossa [API de dados de usuários]({{site.baseurl}}/api/endpoints/user_data/).
- Direcione-se a usuários específicos com nossa [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) para mensagens gerais e transacionais.

Os IDs de usuário devem ter menos de 512 caracteres e devem ser privados e não facilmente obtidos (por exemplo, não um endereço de e-mail simples ou nome de usuário). Se tal identificador não estiver disponível, a Braze atribuirá um identificador único aos seus usuários, mas você não terá as capacidades listadas para IDs de usuário. Você deve evitar definir IDs de usuário para usuários para os quais você não possui um identificador exclusivo que esteja vinculado a eles como indivíduos. Passar um identificador de dispositivo não oferece nenhum benefício em comparação com o rastreamento anônimo automático de usuários que o Braze oferece por padrão. A seguir estão alguns exemplos de IDs de usuário adequados e inadequados.

Boas opções para IDs de usuário:

- Endereço de e-mail com hash ou nome de usuário único
- Identificador único do banco de dados

Estes não devem ser usados como IDs de usuário:

- ID do dispositivo
- Número aleatório ou ID de sessão
- Qualquer ID não exclusivo
- Endereço de e-mail
- ID de usuário de outro fornecedor de terceiros

{% multi_lang_include sdk_auth_alert.md %}

#### Dê nomes legíveis a eventos e atributos personalizados

Imagine que você é um profissional de marketing que começa a usar a Braze um ou dois anos depois da implementação. Ler uma lista suspensa cheia de nomes como "usr_no_acct" sem mais contexto pode gerar apreensão no seu dia a dia. Dar nomes identificáveis e legíveis aos seus eventos e atributos facilitará as coisas para todos os usuários da sua plataforma. Considere as seguintes melhores práticas:

- Não comece um evento personalizado com um caractere numérico. A lista suspensa é classificada em ordem alfabética e começar com um caractere numérico dificulta a segmentação pelo filtro de sua escolha
- Tente não usar abreviações obscuras ou jargão técnico, sempre que possível
  - Exemplo: `usr_ctry` pode ser um bom nome de variável para o país de um usuário dentro de um código, mas o atributo personalizado deve ser enviado para a Braze como algo como `user_country` para dar alguma clareza a um profissional de marketing usando o dashboard no futuro.

#### Somente registrar atributos quando eles mudarem

Contamos cada atributo passado para a Braze como um ponto de dados, mesmo que o atributo passado contenha o mesmo valor salvo anteriormente. Registrar dados apenas quando eles mudam ajuda a evitar o uso redundante de pontos de dados e proporciona uma experiência mais fluida, evitando chamadas desnecessárias à API.

#### Evite gerar nomes de eventos programaticamente

Se você está constantemente criando novos nomes de eventos, será impossível segmentar seus usuários de maneira significativa. Você deve geralmente capturar eventos genéricos ("Assistiu a um Vídeo" ou "Leu um Artigo") em vez de eventos altamente específicos, como ("Assistiu Gangnam Style" ou "Leu Artigo:" Melhores 10 Lugares para Almoçar em Midtown Manhattan Os dados específicos sobre o evento devem ser incluídos como uma propriedade do evento, não como parte do nome do evento.

### Limitações e restrições técnicas

Esteja atento às seguintes limitações e restrições ao implementar eventos personalizados:

#### Restrições de comprimento

Todos os eventos personalizados, nomes de atributos personalizados (chaves) e valores de string de eventos personalizados com 255 caracteres ou mais serão truncados. Idealmente, estes devem ser o mais curtos possível para melhorar a performance da rede e da bateria para o seu app. Se possível, limite-os a 50 caracteres.

#### Restrições de conteúdo
O seguinte conteúdo será removido programaticamente de seus atributos e eventos. Tenha cuidado para não usar o seguinte:

- Espaço em branco à esquerda e à direita
- Novas linhas
- Todos os não dígitos dentro dos números de telefone
  - Exemplo: "(732) 178-1038" será condensado para "7321781038"
- Caracteres não-brancos devem ser convertidos em espaços
- $ não deve ser usado como prefixo para quaisquer eventos personalizados
- Quaisquer valores de codificação UTF-8 inválidos
  -  "Meu \\\\x80 Campo" seria condensado para "Meu Campo"

#### Chaves reservadas

As seguintes chaves são reservadas e não podem ser usadas como propriedades de eventos personalizados:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Definições de valor

- Os valores inteiros são de 64 bits
- Decimais têm 15 dígitos decimais por padrão

### Analisando um campo de nome genérico

Se existir apenas um único campo de nome genérico para um usuário (por exemplo, 'JohnDoe'), você pode atribuir este título inteiro ao atributo de Nome do seu usuário. Além disso, você pode tentar extrair tanto o primeiro quanto o último nome do usuário usando espaços, mas esse último método apresenta o risco potencial de errar o nome de alguns usuários.

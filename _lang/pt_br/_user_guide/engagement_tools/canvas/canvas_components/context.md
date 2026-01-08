---
nav_title: Contexto 
article_title: Contexto 
alias: /context/
page_order: 1.5
page_type: reference
toc_headers: "h2"
description: "Este artigo de referência aborda como criar e usar etapas de contexto em seu Canvas."
tool: Canvas

---

# Contexto

> As etapas de contexto permitem que você crie e atualize uma ou mais variáveis para um usuário à medida que ele se move pelo Canvas. Por exemplo, se você tiver um Canvas que gerencia descontos sazonais, poderá usar uma variável de contexto para armazenar um código de desconto diferente cada vez que um usuário entrar no Canvas.

{% alert important %}
As etapas de contexto estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.<br><br>Observe que a opção de acesso antecipado à etapa de contexto do Canvas fará alterações na forma como os carimbos de data/hora são tratados em todos os seus Canvases. Para saber mais sobre isso, consulte [Padronização da consistência do fuso horário](#time-zone-consistency-standardization).
{% endalert %}

## Como funciona

\![Uma etapa de contexto como a primeira etapa de um Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

As etapas de contexto permitem que você crie e use dados temporários durante a jornada de um usuário em um Canvas específico. Esses dados existem somente dentro dessa jornada do Canvas e não persistem em Canvases diferentes ou fora da sessão.

Dentro dessa estrutura, cada etapa do Context pode definir várias variáveis de contexto - dados temporários que permitem personalizar atrasos, segmentar usuários dinamicamente e enriquecer as mensagens sem alterar permanentemente as informações do perfil do usuário.

Por exemplo, se você estiver gerenciando reservas de voos, poderá criar uma variável de contexto para o horário de voo programado de cada usuário. Em seguida, é possível definir atrasos em relação ao horário de voo de cada usuário e enviar lembretes personalizados a partir do mesmo Canvas.

Você pode definir variáveis de contexto de duas maneiras:

- **Na entrada do Canvas:** Quando os usuários entram em um Canvas, os dados do evento ou do acionador da API podem preencher automaticamente as variáveis de contexto.
- **Em uma etapa do Contexto:** Você pode definir ou atualizar as variáveis de contexto manualmente dentro do Canvas adicionando uma etapa de Contexto.

Cada variável de contexto inclui:

- Um nome (como `flight_time` ou `subscription_renewal_date`)
- Um [tipo de dados](#context-variable-types) (como número, cadeia de caracteres, hora ou matriz)
- Um valor que você atribui usando o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou por meio da ferramenta **Add Personalization**.

Quando definida, você pode usar uma variável de contexto em todo o Canvas fazendo referência a ela no seguinte formato: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Por exemplo, o site {% raw %}`{{context.${flight_time}}}`{% endraw %} poderia retornar o horário do voo programado do usuário.

Toda vez que um usuário entrar no Canvas - mesmo que já tenha entrado antes - as variáveis de contexto serão redefinidas com base nos dados de entrada mais recentes e na configuração do Canvas. Essa abordagem de estado permite que cada entrada do Canvas mantenha seu próprio contexto independente, permitindo que os usuários tenham vários estados ativos na mesma jornada, mantendo o contexto específico de cada estado.

Por exemplo, se um cliente tiver dois voos futuros, ele terá dois estados de jornada separados em execução simultaneamente - cada um com suas próprias variáveis de contexto específicas do voo, como horário de partida e destino. Isso permite enviar lembretes personalizados sobre o voo das 14h para Nova York e, ao mesmo tempo, enviar atualizações diferentes sobre o voo das 8h para Los Angeles amanhã, de modo que cada mensagem permaneça relevante para a reserva específica.

## Considerações

- Você pode ter até 10 variáveis de contexto por etapa do Context.
- Cada nome de variável de contexto pode ter até 100 caracteres.
- Os nomes das variáveis de contexto devem ser identificadores válidos (somente letras, números e sublinhados).
- As definições de variáveis de contexto podem ter até 10.240 caracteres. 
- As variáveis de contexto passadas para um Canvas acionado por API compartilham os mesmos namespaces que as variáveis de contexto criadas em uma etapa de Contexto em um Canvas. Isso significa que se você enviar uma variável `purchased_item` no [objeto de contexto]({{site.baseurl}}/api/objects_filters/context_object) do ponto de extremidade `/canvas/trigger/send`, ela poderá ser referenciada como {% raw %}`{context.${purchased_item}}`{% endraw %}, e declarar novamente essa variável em uma etapa de contexto no Canvas substituirá o que foi enviado anteriormente.
- Você pode armazenar até 50 KB por etapa de contexto, distribuindo até 10 variáveis por etapa. Os tamanhos de variáveis que somam mais de 50 KB em uma etapa não serão avaliados nem armazenados para o usuário. Esses tamanhos são calculados em sequência. Por exemplo, se você tiver 3 variáveis em uma etapa do Context:
  - Variável 1: 30 KB
  - Variável 2: 19 KB
  - Variável 3: 2 KB
  - Isso significa que a variável 3 não será avaliada nem armazenada porque a soma de todas as outras variáveis de contexto excede 50 KB.

## Criando uma etapa de contexto

### Etapa 1: Adicionar uma etapa

Adicione uma etapa ao Canvas e, em seguida, arraste e solte o componente da barra lateral ou selecione o botão de adição <i class="fas fa-plus-circle"></i> e selecione **Context (Contexto**).

### Etapa 2: Definir as variáveis

{% alert note %}
Você pode definir até 10 variáveis de contexto para cada etapa do Context.
{% endalert %}

Para definir uma variável de contexto:

1. Dê um **nome** à sua variável de contexto.
2. Selecione um [tipo de dados](#context-variable-types).
3. Escreva uma expressão do Liquid manualmente ou use **Add Personalization** para criar um snippet do Liquid a partir de atributos pré-existentes.
4. Selecione **Preview** para verificar o valor de sua variável de contexto.
5. (Opcional) Para variáveis adicionais, selecione **Add Context variable (Adicionar variável de contexto** ) e repita as etapas 1 a 4.
6. Quando terminar, selecione **Concluído**.

Agora você pode usar a variável de contexto em qualquer lugar em que usar o Liquid, como nas etapas de Mensagem e Atualização do usuário, selecionando **Adicionar personalização**. Para obter um passo a passo completo, consulte [Uso de variáveis de contexto](#using-context-variables).

## Tipos de dados de variáveis de contexto {#context-variable-types}

As variáveis de contexto que são criadas ou atualizadas na etapa podem receber os seguintes tipos de dados.

{% alert note %}
As variáveis de contexto têm os mesmos formatos esperados para os tipos de dados que os [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Para objetos aninhados e matriz de objetos, use o [filtro`as_json_string` Liquid](#converting-connected-content-strings-to-json). Se estiver criando o mesmo objeto em uma etapa do Context, será necessário renderizar o objeto usando `as_json_string`, como {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Tipo de dados | Exemplo de nome de variável | Exemplo de valor |
|---|---|---|
|Booleano| loyalty_program |{% raw %}<code>verdadeiro</code>{% endraw %}| 
|Número| credit_score |{% raw %}<code>740{% endraw %}|
|Cordas| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Matriz| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Hora (em UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objeto (achatado) | user_profile|{% raw %}<code>{<br> "first_name": "{{user.first_name}}",<br> "last_name": "{{user.last_name}}",<br> "email": "{{user.email}}",<br> "loyalty_points": {{user.loyalty_points}},<br> "preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por padrão, o tipo de dados de hora está em UTC. Se você usar um tipo de dados de cadeia de caracteres para armazenar um valor de hora, poderá definir a hora como um fuso horário diferente, como PST. 

Por exemplo, se estiver enviando uma mensagem a um usuário no dia anterior ao aniversário dele, você salvaria a variável de contexto como um tipo de dados de tempo porque há uma lógica líquida associada ao envio no dia anterior. No entanto, se você estiver enviando uma mensagem de feriado no dia de Natal (25 de dezembro), não precisará fazer referência à hora como uma variável dinâmica, portanto, seria preferível usar um tipo de dados de cadeia de caracteres.

## Uso de variáveis de contexto {#using-context-variables}

Por exemplo, digamos que você queira notificar os passageiros sobre o acesso à sala VIP antes do próximo voo. Essa mensagem deve ser enviada apenas aos passageiros que compraram uma passagem de primeira classe. Uma variável de contexto é uma maneira flexível de rastrear essas informações.

Os usuários entrarão no Canvas quando comprarem uma passagem aérea. Para determinar a qualificação de acesso ao lounge, criaremos uma variável de contexto chamada `lounge_access_granted` em uma etapa de Contexto e, em seguida, faremos referência a essa variável de contexto nas etapas subsequentes da jornada do usuário.

Variável de contexto configurada para rastrear se um passageiro se qualifica para o acesso à sala VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Nesta etapa do Contexto, usaremos o site {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} para determinar se o tipo de voo que eles compraram é `first_class`.

Em seguida, criaremos uma etapa de mensagem para direcionar os usuários onde {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} é `true`. Essa mensagem será uma notificação por push que inclui informações personalizadas sobre o lounge. Com base nessa variável de contexto, os passageiros qualificados receberão as mensagens relevantes antes de seu voo.

- Os passageiros de bilhetes de primeira classe receberão: "Aproveite o acesso exclusivo à sala VIP!"
- Os passageiros das classes econômica e executiva receberão: "Faça upgrade de seu voo para ter acesso exclusivo à sala VIP."

\![Uma etapa de mensagem com diferentes mensagens a serem enviadas, dependendo do tipo de passagem aérea comprada.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
É possível adicionar [opções de atraso personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) com as informações da etapa Contexto, o que significa que você pode selecionar a variável que atrasa os usuários.
{% endalert %}

### Para caminhos de ação e critérios de saída

Você pode aproveitar a comparação de filtros de propriedade com variáveis de contexto ou atributos personalizados nessas ações de acionamento: **Realizar evento personalizado** e **fazer a compra**. Esses acionadores de ação também suportam filtros de propriedade para propriedades básicas e aninhadas. 

- Ao comparar com propriedades básicas, as comparações disponíveis corresponderão ao tipo de propriedade definido pelo evento personalizado. Por exemplo, as propriedades de string terão correspondências regex exatamente iguais. As propriedades booleanas serão verdadeiras ou falsas. 
- Ao comparar com propriedades aninhadas, os tipos não são predefinidos, portanto, você pode selecionar comparações entre vários tipos de dados para booleanos, números, cadeias de caracteres, hora e dia do ano, de forma semelhante às comparações para atributos personalizados aninhados. Se você selecionar um tipo de dados que não corresponda ao tipo de dados real da propriedade aninhada no momento da comparação, o usuário não corresponderá ao Caminho de ação ou aos critérios de saída.

#### Exemplos de caminhos de ação

{% alert important %}
Para comparações de atributos personalizados, usaremos o valor do atributo personalizado no momento em que a ação for executada. Isso significa que um usuário não corresponderá ao grupo Action Path se não tiver esse atributo personalizado preenchido no momento da comparação ou se o valor do atributo personalizado não corresponder às comparações de propriedades definidas. Esse é o caso mesmo que o usuário tenha feito a correspondência quando entrou na etapa do Caminho de Ação.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

O Action Path a seguir é configurado para classificar os usuários que realizaram o evento personalizado `Account_Created` com a propriedade básica `source` para a variável de contexto `app_source_variable`.

\![Um exemplo de Action Path que faz referência a uma variável de contexto ao executar um evento personalizado.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

O Action Path a seguir está configurado para corresponder a propriedade básica `brand` para o nome do produto específico `shoes` a uma variável de contexto `promoted_shoe_brand`.

\![Um exemplo de caminho de ação que faz referência a uma variável de contexto ao fazer uma compra.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exemplos de critérios de saída

{% tabs %}
{% tab Perform custom event %}

Os critérios de saída determinam que, em qualquer ponto da jornada de um usuário no Canvas, ele sairá do Canvas se:

- Eles executam o evento personalizado **Abandon Cart** e
- A propriedade básica **Item in Cart** corresponde ao valor da cadeia de caracteres da variável de contexto `cart_item_threshold`.

Critérios de saída configurados para sair de um usuário se ele executar um evento personalizado com base na variável de contexto.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Os critérios de saída determinam que, em qualquer ponto da jornada de um usuário no Canvas, ele sairá do Canvas se:

- Eles fazem uma compra específica para o nome do produto "livro", e
- A propriedade aninhada dessa compra "loyalty_program" é igual ao atributo personalizado do usuário "VIP".

\![Critérios de saída configurados para sair de um usuário se ele fizer uma compra.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Filtros de variáveis de contexto

Você pode criar filtros que usam variáveis de contexto declaradas anteriormente nas etapas [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) e [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

{% alert important %}
Os filtros de variáveis de contexto só estão disponíveis para as etapas Audience Paths e Decision Split.
{% endalert %}

As variáveis de contexto são declaradas e só podem ser acessadas no escopo de um Canvas, o que significa que não podem ser referenciadas em segmentos. Os filtros de variáveis de contexto funcionam de forma semelhante nas etapas de Caminhos de público-alvo e Divisão de decisão - as etapas de Caminho de público-alvo representam vários grupos, enquanto as etapas de Divisão de decisão representam decisões binárias.

Exemplo de etapa de divisão de decisão com a opção de criar um filtro com uma variável de contexto.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Da mesma forma que as variáveis de contexto do Canvas têm tipos predefinidos, as comparações entre variáveis de contexto e valores estáticos devem ter [tipos de dados correspondentes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). O filtro de variável de contexto permite comparações entre vários tipos de dados para booleanos, números, cadeias de caracteres, hora e dia do ano, semelhante às comparações para [atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Use o mesmo tipo de dados para sua variável de contexto e comparação. Por exemplo, se sua variável de contexto for um tipo de dados de tempo, use comparações de tempo (como "antes" ou "depois"). O uso de tipos de dados incompatíveis (como comparações de strings com uma variável de contexto de tempo) pode causar um comportamento inesperado.
{% endalert %}

Aqui está um exemplo de um filtro de variável de contexto que compara a variável de contexto `product_name` com a regex `/braze/`.

\![Uma configuração de filtro para a variável de contexto "product_name" para corresponder ao regex "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparação com variáveis de contexto ou atributos personalizados

Ao selecionar a opção **Comparar com uma variável de contexto ou atributo personalizado**, é possível criar filtros de variáveis de contexto que se comparam com variáveis de contexto previamente definidas ou atributos personalizados do usuário. Isso pode ser útil para realizar comparações que são dinâmicas por usuário, como as acionadas pela API `context`, ou para condensar a lógica de comparação complexa definida nas variáveis de contexto.

{% tabs %}
{% tab Example 1 %}

Digamos que você queira enviar um lembrete personalizado aos usuários após um período dinâmico de inatividade, o que inclui qualquer pessoa que não tenha feito login no seu aplicativo nos últimos três dias, que deverá receber uma mensagem.

Você tem uma variável de contexto `re_engagement_date` que é definida como {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Observe que `3 days` pode ser um valor variável que também é armazenado como um atributo personalizado do usuário. Portanto, se o `re_engagement_date` estiver após o `last_login_date` (armazenado como um atributo personalizado no perfil do usuário), ele receberá uma mensagem.

\![Uma configuração de filtro com atributos personalizados como o tipo de personalização para a variável de contexto "re_engagement_date" após o atributo personalizado "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

O filtro a seguir compara a variável de contexto `reminder_date` para estar antes da variável de contexto `appointment_deadline`. Isso pode ajudar a agrupar usuários em uma etapa do Audience Paths para determinar se eles devem receber lembretes adicionais antes do prazo final do compromisso.

\![Uma configuração de filtro com variáveis de contexto como o tipo de personalização para a variável de contexto "reminder_date" na variável de contexto "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Pré-visualização de caminhos de usuário

Recomendamos testar e [visualizar os caminhos do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) para garantir que as mensagens sejam enviadas ao público certo e que as variáveis de contexto sejam avaliadas de acordo com os resultados esperados.

{% alert note %}
Se você estiver visualizando seu Canvas na seção **Preview & Test Send** do editor, o carimbo de data/hora na visualização da mensagem de teste **não será** padronizado para UTC porque esse painel gera visualizações como strings. Isso significa que, se um Canvas estiver configurado para aceitar um objeto `time`, a visualização da mensagem não será uma visualização precisa do que ocorrerá quando o Canvas estiver ativo. Para testar o Canvas com mais precisão, recomendamos a visualização dos caminhos do usuário.
{% endalert %}

Não deixe de observar os cenários comuns que criam variáveis de contexto inválidas. Ao visualizar o caminho do usuário, você pode ver os resultados das etapas de Atraso personalizadas usando variáveis de contexto e quaisquer comparações de etapas de público-alvo, decisão ou Caminho de ação que correspondam a usuários com quaisquer variáveis de contexto.

Se a variável de contexto for válida, você poderá fazer referência a ela em todo o seu Canvas. No entanto, se a variável de contexto não tiver sido criada corretamente, as etapas futuras do Canvas também não serão executadas corretamente. Por exemplo, se você criar uma etapa de Contexto para atribuir aos usuários um horário de compromisso, mas definir o valor do horário de compromisso como uma data passada, o e-mail de lembrete na etapa Mensagem nunca será enviado.

## Conversão de strings de Connected Content em JSON

Ao fazer uma [chamada de Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) em uma etapa de Contexto, o JSON retornado da chamada será avaliado como um tipo de dados de cadeia de caracteres para fins de consistência e prevenção de erros. Se você quiser converter essa string em JSON, converta-a usando `as_json_string`. Por exemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Padronização da consistência do fuso horário

Com a adição do Canvas Context, todos os registros de [data]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) e hora com um [tipo de data e hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) das [propriedades de eventos de acionamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) em Canvases baseados em ações sempre serão normalizados para [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Anteriormente, os registros de data e hora das propriedades de eventos eram normalizados para UTC, com [algumas exceções]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know). Agora, isso proporcionará uma experiência mais consistente na edição de etapas e mensagens do Canvas.

Considere este exemplo de como essa alteração pode afetar um registro de data e hora no Canvas. Digamos que temos um Canvas baseado em ação que usa uma propriedade de evento na primeira etapa do Canvas com a seguinte etapa de Mensagem: 

{% raw %}
`Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!`
{% endraw %}

Jornada de contexto com uma etapa de Mensagem como a primeira etapa.]({% image_buster /assets/img/context_timezone_example.png %}){: style="max-width:50%"}

A etapa também terá uma carga útil de evento como: 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
}
```

Historicamente, a mensagem seria: `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

Com o acesso antecipado do Canvas Context, a mensagem agora será: `Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!` Isso se deve ao fato de o registro de data e hora estar em UTC, que está 8 horas à frente do horário do Pacífico (o fuso horário especificado no payload original com `-08:00`).

{% alert important %}
Para levar em conta essa mudança de carimbo de data/hora, em todas as circunstâncias, recomendamos enfaticamente [o uso de filtros Liquid]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) para que os carimbos de data/hora sejam representados no fuso horário desejado.
{% endalert %}

### Uso do Liquid para indicar um carimbo de data/hora em seu fuso horário preferido

Considere o seguinte trecho do Liquid:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Essa lógica resulta na seguinte saída: `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

O fuso horário preferencial também pode ser enviado na carga útil das propriedades do evento e usado na lógica do Liquid: 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

Este é um exemplo do snippet do Liquid:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: canvas_entry_properties.${user_timezone} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

## Solução de problemas {#troubleshooting}

### Variáveis de contexto inválidas

Uma variável de contexto é considerada inválida quando:
- Uma chamada para um Connected Content incorporado falha.
- A expressão Liquid em tempo de execução retorna um valor que não corresponde ao tipo de dados ou que está vazio (nulo).

Por exemplo, se o tipo de dados da variável de contexto for **Número**, mas a expressão Liquid retornar uma cadeia de caracteres, ela será inválida.

Nessas circunstâncias: 
- O usuário avançará para a próxima etapa. 
- A análise da etapa do Canvas contará isso como _Não atualizado_.

Ao solucionar problemas, monitore a métrica _Not Updated_ para verificar se sua variável de contexto está sendo atualizada corretamente. Se a variável de contexto for inválida, os usuários poderão continuar no Canvas após a etapa Context (Contexto), mas talvez não se qualifiquem para as etapas posteriores.

Consulte [Tipos de dados variáveis de contexto](#context-variable-types) para ver os exemplos de configuração de cada tipo de dados.

## Perguntas frequentes

### Como as variáveis de contexto diferem das propriedades de entrada do Canvas?

Se você estiver participando do acesso antecipado à etapa Contexto, as propriedades de entrada do Canvas agora estão incluídas como variáveis de contexto do Canvas. Isso significa que você pode enviar propriedades de entrada do Canvas usando a API do Braze e fazer referência a elas em outras etapas, de forma semelhante ao uso de uma variável de contexto com o snippet do Liquid.

### As variáveis podem fazer referência umas às outras em uma única etapa do Context?

Sim. Todas as variáveis em uma etapa de contexto são avaliadas em uma sequência, o que significa que você poderia ter a seguinte configuração de variáveis de contexto:

| Variável de contexto | Valor | Descrição |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | O tipo de cozinha favorito de um usuário. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | O código de desconto disponível para um usuário. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.promo_code}} "on delivery from your favorite" {{context.favorite_cuisine}} restaurants!"`{% endraw %} | Uma mensagem personalizada que combina as variáveis anteriores. Em uma etapa de mensagem, você pode usar o snippet do Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} para fazer referência à variável de contexto e enviar uma mensagem personalizada a cada usuário. Você também pode usar uma etapa de Contexto para salvar o valor [do código promocional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) e modelá-lo em outras etapas em um Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Isso também se aplica a várias etapas do Context. Por exemplo, imagine esta sequência:
1. Uma etapa inicial do Context cria uma variável chamada `JobInfo` com o valor `job_title`.
2. Uma etapa de Mensagem faz referência a {% raw %}`{{context.${JobInfo}}}`{% endraw %} e exibe `job_title` para o usuário.
3. Posteriormente, uma etapa do Contexto atualiza a variável de contexto, alterando o valor de `JobInfo` para `job_description`.
4. Todas as etapas subsequentes que fazem referência a `JobInfo` agora usarão o valor atualizado `job_description`.

As variáveis de contexto usam seu valor mais recente em todo o Canvas, com cada atualização afetando todas as etapas seguintes que fazem referência a essa variável.

### A padronização da consistência do fuso horário do Canvas Context afeta os Canvases acionados pela API?

Não, essa alteração afeta apenas as telas acionadas por ação. Os carimbos de data/hora enviados para Canvases acionados pela API terão o tipo de cadeia de caracteres, não o tipo de hora, de modo que o fuso horário original seja sempre preservado.

### Como isso se relaciona com as exceções observadas nas propriedades de entrada do Canvas e nas propriedades do evento?

A participação no acesso antecipado do Canvas Context remove [essas exceções]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know), independentemente de você estar usando uma etapa do Canvas Context.

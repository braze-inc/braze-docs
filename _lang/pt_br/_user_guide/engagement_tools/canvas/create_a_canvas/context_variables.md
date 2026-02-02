---
nav_title: Variáveis de contexto
article_title: Variáveis de contexto
page_type: reference
description: "Este artigo de referência explica as variáveis de contexto no Braze Canvas, incluindo seus tipos, uso e práticas recomendadas."
---

# Variáveis de contexto

> As variáveis de contexto são dados temporários que podem ser criados e usados na jornada de um usuário por meio de um Canva específico. Elas ativam a personalização de postergações, o segmento de usuários dinamicamente e o enriquecimento do envio de mensagens sem alterar permanentemente as informações do perfil do usuário. As variáveis de contexto existem somente dentro da sessão do Canvas e não persistem em diferentes Canvas ou fora da sessão.

## Como funcionam as variáveis de contexto

As variáveis de contexto podem ser definidas de duas maneiras:

- **Na entrada do canva:** Quando os usuários entram em um Canva, os dados do evento ou do disparo da API podem preencher automaticamente as variáveis de contexto.
- **Em uma etapa do Contexto:** Você pode definir ou atualizar as variáveis de contexto manualmente dentro do Canva, adicionando uma [etapa do Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

Cada variável de contexto inclui:

- Um nome (como `flight_time` ou `subscription_renewal_date`)
- Um tipo de dados (como número, string, hora ou matriz)
- Um valor que você atribui usando o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou por meio da ferramenta **Adicionar personalização**.

Quando definida, você pode usar uma variável de contexto em todo o Canva fazendo referência a ela no seguinte formato: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Por exemplo, o site {% raw %}`{{context.${flight_time}}}`{% endraw %} poderia retornar o horário do voo programado do usuário.

Cada vez que um usuário entrar no Canva - mesmo que já tenha entrado antes - as variáveis de contexto serão redefinidas com base nos dados de entrada mais recentes e na configuração do Canvas. Essa abordagem com estado permite que cada entrada do Canva mantenha seu próprio contexto independente, permitindo que os usuários tenham vários estados ativos na mesma jornada, mantendo o contexto específico de cada estado.

Por exemplo, se um cliente tiver dois voos futuros, ele terá dois estados de jornada separados em execução simultaneamente - cada um com suas próprias variáveis de contexto específicas do voo, como horário de partida e destinos. Isso permite enviar lembretes personalizados sobre o voo das 14h para Nova York e, ao mesmo tempo, enviar atualizações diferentes sobre o voo das 8h para Los Angeles amanhã, de modo que cada mensagem permaneça relevante para a reserva específica.

## Considerações

Você pode definir até 10 variáveis de contexto por [etapa do Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/). Cada nome de variável pode ter até 100 caracteres e deve usar apenas letras, números ou sublinhados.

As definições de variáveis de contexto podem ter até 10.240 caracteres. Se você passar variáveis de contexto para um Canva disparado pela API, elas compartilharão o mesmo espaço de nomes que as variáveis criadas em uma etapa do Context. Por exemplo, se você enviar uma variável `purchased_item` no objeto de contexto [do ponto de extremidade`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/), poderá referenciá-la como {% raw %}`{{context.${purchased_item}}}`{% endraw %}. Se você redefinir essa variável em uma etapa do Context, o novo valor substituirá o valor da API para a jornada desse usuário.

Você pode armazenar até 50 KB por etapa do Contexto, distribuídos em até 10 variáveis. Se o tamanho total de todas as variáveis em uma etapa exceder 50 KB, as variáveis que excederem o limite não serão avaliadas nem armazenadas. Por exemplo, se você tiver três variáveis em uma etapa do Context:

- Variável 1: 30 KB
- Variável 2: 19 KB
- Variável 3: 2 KB

A variável 3 não será avaliada ou armazenada porque a soma das variáveis anteriores excede 50 KB.

## Tipos de dados

As variáveis de contexto que são criadas ou atualizadas na etapa podem ser atribuídas aos seguintes tipos de dados.

{% alert note %}
As variáveis de contexto têm os mesmos formatos esperados para os tipos de dados que os [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Ao usar o tipo de matriz, o Braze tenta analisar o valor como JSON, o que permite que as matrizes de objetos sejam criadas com sucesso. Se os objetos em seus vetores não forem JSON válidos, o resultado será um vetor simples de strings. <br><br>Para objetos aninhados e vetor de objetos, use o [filtro`as_json_string` Liquid](#converting-connected-content-strings-to-json). Se estiver criando o mesmo objeto em uma etapa do Context, será necessário renderizar o objeto usando `as_json_string`, como {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Tipo de dados | Exemplo de nome de variável | Exemplo de valor |
|---|---|---|
|Booleano| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Número| credit_score |{% raw %}<code>740</code>{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Vetor| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Vetor de objetos| pet_details |{% raw %}<code>[_mem_lt_br>_mem_amp_emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }_mem_lt_br>_mem_amp_emsp;,_mem_lt_br>_mem_amp_emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }_mem_lt_br>]</code>{% endraw %}|
|Hora (em UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objeto (achatado) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por padrão, o tipo de dados de hora está em UTC. Se você usar um tipo de dados string para armazenar um valor de hora, poderá definir a hora como um fuso horário diferente, como PST. 

Por exemplo, se estiver enviando uma mensagem a um usuário no dia anterior ao seu aniversário, salve a variável de contexto como um tipo de dados de tempo porque há uma lógica Liquid associada ao envio no dia anterior. No entanto, se estiver enviando uma mensagem de feriado no dia de Natal (25 de dezembro), não será necessário fazer referência à hora como uma variável dinâmica, portanto, seria preferível usar um tipo de dados string.

## Uso de variáveis de contexto

É possível usar variáveis de contexto em qualquer lugar que use Liquid em um Canva, como nas etapas [de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) e [Atualização do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update), selecionando **Adicionar personalização**.

Por exemplo, digamos que você queira notificar os passageiros sobre o acesso à sala VIP antes do próximo voo. Essa mensagem deve ser enviada apenas aos passageiros que compraram um bilhete de primeira classe. Uma variável de contexto é uma maneira flexível de rastrear essas informações.

Os usuários entrarão no Canva quando comprarem uma passagem aérea. Para determinar a elegibilidade de acesso ao lounge, criaremos uma variável de contexto chamada `lounge_access_granted` em uma etapa de Contexto e, em seguida, faremos referência a essa variável de contexto nas etapas subsequentes da jornada do usuário.

![Variável de contexto configurada para rastrear se um passageiro se qualifica para o acesso à sala VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Nesta etapa do Contexto, usaremos o site {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} para determinar se o tipo de voo que eles compraram é `first_class`.

Em seguida, criaremos uma etapa de mensagens para direcionamento aos usuários onde {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} é `true`. Essa mensagem será uma notificação por push que inclui informações personalizadas sobre o lounge. Com base nessa variável de contexto, os passageiros elegíveis receberão as mensagens relevantes antes de seu voo.

- Os passageiros de bilhetes de primeira classe receberão: "Aproveite o acesso exclusivo à sala VIP!"
- Os passageiros das classes econômica e executiva receberão: "Faça upgrade de seu voo para ter acesso exclusivo à sala VIP."

![Uma etapa de Mensagem com diferentes mensagens a serem enviadas, dependendo do tipo de passagem aérea comprada.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
É possível adicionar [opções de postergação personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) com as informações da etapa Contexto, o que significa que você pode selecionar a variável que posterga os usuários.
{% endalert %}

### Para jornadas de ação e critérios de saída

Você pode aproveitar a comparação de filtros de propriedades com variáveis de contexto ou atributos personalizados nessas ações-gatilho: **Realize o evento personalizado** e **faça a compra**. Essas ações-gatilho também suportam filtros de propriedade para propriedades básicas e aninhadas. 

- Ao comparar com propriedades básicas, as comparações disponíveis corresponderão ao tipo de propriedade definido pelo evento personalizado. Por exemplo, as propriedades de string terão correspondências regex exatamente iguais. As propriedades booleanas serão verdadeiras ou falsas. 
- Ao comparar com propriedades aninhadas, os tipos não são predefinidos, portanto, você pode selecionar comparações entre vários tipos de dados para booleanos, números, strings, hora e dia do ano, semelhante às comparações para atributos personalizados aninhados. Se for selecionado um tipo de dados que não corresponda ao tipo de dados real da propriedade aninhada no momento da comparação, o usuário não corresponderá aos critérios de jornada de ação ou de saída.

#### Exemplos de jornadas de ação

{% alert important %}
Para comparações de atributos personalizados, usaremos o valor do atributo personalizado no momento em que a ação for executada. Isso significa que um usuário não corresponderá ao grupo da jornada de ação se não tiver esse atributo personalizado preenchido no momento da comparação ou se o valor do atributo personalizado não corresponder às comparações de propriedades definidas. Esse é o caso mesmo que o usuário tenha feito a correspondência quando entrou na etapa das jornadas de ação.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

A seguinte jornada de ação é configurada para classificar os usuários que realizaram o evento personalizado `Account_Created` com a propriedade básica `source` para a variável de contexto `app_source_variable`.

![Um exemplo de jornada de ação que faz referência a uma variável de contexto ao executar um evento personalizado.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

A seguinte jornada de ação está configurada para corresponder a propriedade básica `brand` para o nome do produto específico `shoes` a uma variável de contexto `promoted_shoe_brand`.

![Um exemplo de jornada de ação que faz referência a uma variável de contexto ao fazer uma compra.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exemplos de critérios de saída

{% tabs %}
{% tab Perform custom event %}

Os critérios de saída determinam que, em qualquer ponto da jornada de um usuário no Canva, ele sairá do Canva se:

- Eles executam o evento personalizado **Abandono de carrinho** e
- A propriedade básica **Item no carrinho** corresponde ao valor da string da variável de contexto `cart_item_threshold`.

![Critérios de saída configurados para sair de um usuário se ele realizar um evento personalizado com base na variável de contexto.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Os critérios de saída determinam que, em qualquer ponto da jornada de um usuário no Canva, ele sairá do Canva se:

- Eles fazem uma compra específica para o nome do produto "livro", e
- A propriedade aninhada dessa compra "loyalty_program" é igual ao atributo personalizado do usuário "VIP".

![Critérios de saída configurados para sair de um usuário se ele fizer uma compra.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Filtros de variáveis de contexto

Você pode criar filtros que usam variáveis de contexto declaradas anteriormente nas etapas de [jornadas do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) e [divisão de decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

{% alert note %}
Os filtros de variáveis de contexto só estão disponíveis para as etapas de jornadas do público e divisão de decisão.
{% endalert %}

As variáveis de contexto são declaradas e só podem ser acessadas no escopo de uma tela, o que significa que não podem ser referenciadas em segmentos. Os filtros de variáveis de contexto funcionam de forma semelhante nas jornadas do público e na divisão de decisão - as etapas de jornadas do público representam vários grupos, enquanto as etapas de divisão de decisão representam decisões binárias.

![Exemplo de etapa de divisão de decisão com a opção de criar um filtro com uma variável de contexto.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Da mesma forma que as variáveis de contexto do Canva têm tipos predefinidos, as comparações entre variáveis de contexto e valores estáticos devem ter [tipos de dados correspondentes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). O filtro de variável de contexto permite comparações entre vários tipos de dados para booleanos, números, strings, hora e dia do ano, semelhante às comparações para [atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Use o mesmo tipo de dados para sua variável de contexto e comparação. Por exemplo, se sua variável de contexto for um tipo de dados de tempo, use comparações de tempo (como "antes" ou "depois"). O uso de tipos de dados incompatíveis (como comparações de string com uma variável de contexto de tempo) pode causar um comportamento inesperado.
{% endalert %}

Aqui está um exemplo de um filtro de variável de contexto que compara a variável de contexto `product_name` com o regex `/braze/`.

![Uma configuração de filtro para a variável de contexto "product_name" para corresponder ao regex "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparação com variáveis de contexto ou atributos personalizados

Ao selecionar a opção **Comparar com uma variável de contexto ou atributo personalizado**, é possível criar filtros de variáveis de contexto que se comparam a variáveis de contexto previamente definidas ou a atributos personalizados do usuário. Isso pode ser útil para realizar comparações que são dinâmicas por usuário, como as disparadas pela API `context`, ou para condensar a lógica de comparação complexa definida nas variáveis de contexto.

{% tabs %}
{% tab Example 1 %}

Digamos que você queira enviar um lembrete personalizado aos usuários após um período dinâmico de inatividade, o que inclui qualquer pessoa que não tenha registrado seu app nos últimos três dias, que deverá receber uma mensagem.

Você tem uma variável de contexto `re_engagement_date` que é definida como {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Note que `3 days` pode ser um valor variável que também é armazenado como um atributo personalizado do usuário. Portanto, se o `re_engagement_date` estiver após o `last_login_date` (armazenado como um atributo personalizado no perfil do usuário), ele receberá uma mensagem.

![Uma configuração de filtro com atributos personalizados como o tipo de personalização para a variável de contexto "re_engagement_date" após o atributo personalizado "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

O filtro a seguir compara a variável de contexto `reminder_date` para estar antes da variável de contexto `appointment_deadline`. Isso pode ajudar a agrupar usuários em uma etapa de jornadas do público para determinar se eles devem receber lembretes adicionais antes do prazo final do compromisso.

![Uma configuração de filtro com variáveis de contexto como o tipo de personalização para a variável de contexto "reminder_date" na variável de contexto "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Padronização da consistência do fuso horário

Embora a maioria das propriedades de eventos que usam o tipo de carimbo de data/hora já esteja em UTC no Canva, há algumas exceções. Com a adição do Canvas Context, todas as propriedades padrão de eventos de registro de data e hora em Canvas baseadas em ações estarão consistentemente em UTC. Essa alteração faz parte de um esforço mais amplo para garantir uma experiência mais previsível e consistente ao editar etapas e mensagens do Canva. Note que essa alteração afetará todos os Canvas baseados em ações, independentemente de o Canvas específico estar usando uma etapa do Context ou não.

{% alert important %}
Em todas as circunstâncias, recomendamos enfaticamente o uso dos [filtros Liquid time_zone ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) para que os registros de data e hora sejam representados no fuso horário desejado. Você pode consultar essa [pergunta frequente no artigo sobre a etapa de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example) para obter um exemplo.
{% endalert %}

## Artigos relacionados

- [Etapa de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personalização e conteúdo dinâmico com Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

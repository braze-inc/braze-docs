---
nav_title: Variáveis de contexto
article_title: Variáveis de contexto
page_type: reference
description: "Este artigo de referência explica as variáveis de contexto em Canvases do Braze, incluindo seus tipos, uso e melhores práticas."
---

# Variáveis de contexto

> As variáveis de contexto são peças temporárias de dados que você pode criar e usar dentro da jornada de um usuário através de um Canvas específico. Elas permitem personalizar atrasos, segmentar usuários dinamicamente e enriquecer o envio de mensagens sem alterar permanentemente as informações do perfil de um usuário. As variáveis de contexto existem apenas dentro da sessão do Canvas e não persistem entre diferentes Canvases ou fora da sessão.

## Como as variáveis de contexto funcionam

As variáveis de contexto podem ser definidas de duas maneiras:

- **Na entrada do canva:** Quando os usuários entram em um Canvas, os dados do evento ou do disparador da API podem automaticamente preencher as variáveis de contexto.
- **Em uma etapa de Contexto:** Você pode definir ou atualizar variáveis de contexto manualmente dentro do Canvas adicionando uma [etapa de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

Cada variável de contexto inclui:

- Um nome (como `flight_time` ou `subscription_renewal_date`)
- Um tipo de dado (como número, string, tempo ou array)
- Um valor que você atribui usando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou através da **Adicionar Personalização** ferramenta.

Quando definido, você pode usar uma variável de contexto em todo o Canvas referenciando-a neste formato: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Por exemplo, {% raw %}`{{context.${flight_time}}}`{% endraw %} pode retornar o horário do voo agendado do usuário.

Cada vez que um usuário entra no Canvas—mesmo que já tenha entrado antes— as variáveis de contexto serão redefinidas com base nos dados de entrada mais recentes e na configuração do Canvas. Essa abordagem com estado permite que cada entrada no Canvas mantenha seu próprio contexto independente, permitindo que os usuários tenham múltiplos estados ativos dentro da mesma jornada enquanto retêm o contexto específico para cada estado.

Por exemplo, se um cliente tem dois voos futuros, ele terá dois estados de jornada separados rodando simultaneamente—cada um com suas próprias variáveis de contexto específicas do voo, como horário de partida e destino. Isso permite que você envie lembretes personalizados sobre o voo das 14h para Nova York enquanto envia atualizações diferentes sobre o voo das 8h para Los Angeles amanhã, para que cada mensagem permaneça relevante para a reserva específica.

## Considerações

Você pode definir até 10 variáveis de contexto por [Etapa de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/). Cada nome de variável pode ter até 100 caracteres e deve usar apenas letras, números ou sublinhados.

As definições de variáveis de contexto podem ter até 10.240 caracteres. Se você passar variáveis de contexto para um Canvas acionado por API, elas compartilham o mesmo namespace que as variáveis criadas em uma Etapa de contexto. Por exemplo, se você enviar uma variável `purchased_item` no objeto de contexto [`/canvas/trigger/send` ponto final]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/), você pode referenciá-la como {% raw %}`{{context.${purchased_item}}}`{% endraw %}. Se você redefinir essa variável em uma Etapa de contexto, o novo valor substituirá o valor da API para a jornada desse usuário.

Você pode armazenar até 50 KB por Etapa de contexto, distribuídos em até 10 variáveis. Se o tamanho total de todas as variáveis em uma etapa exceder 50 KB, quaisquer variáveis que excedam o limite não serão avaliadas ou armazenadas. Por exemplo, se você tiver três variáveis em uma Etapa de contexto:

- Variável 1: 30 KB
- Variável 2: 19 KB
- Variável 3: 2 KB

A variável 3 não será avaliada ou armazenada porque a soma das variáveis anteriores excede 50 KB.

## Tipos de dados

As variáveis de contexto que são criadas ou atualizadas na etapa podem ser atribuídas aos seguintes tipos de dados.

{% alert note %}
As variáveis de contexto têm os mesmos formatos esperados para tipos de dados que [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Ao usar o tipo de array, o Braze tenta analisar o valor como JSON, o que permite que arrays de objetos sejam criados com sucesso. Se os objetos dentro de seus arrays não forem JSON válidos, o resultado será um array simples de strings. <br><br>Para objetos aninhados e arrays de objetos, use o [`as_json_string` filtro Liquid](#converting-connected-content-strings-to-json). Se você estiver criando o mesmo objeto em uma etapa de Contexto, precisará renderizar o objeto usando `as_json_string`, como {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Tipo de dados | Nome da variável de exemplo | Valor de exemplo |
|---|---|---|
|Booleano| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Número| credit_score |{% raw %}<code>740</code>{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Vetor| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Array (de objetos)| pet_details |{% raw %}<code>[_mem_lt_br>_mem_amp_emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }_mem_lt_br>_mem_amp_emsp;,_mem_lt_br>_mem_amp_emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }_mem_lt_br>]</code>{% endraw %}|
|Hora (em UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objeto (achatado) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por padrão, o tipo de dado de hora está em UTC. Se você usar um tipo de dado string para armazenar um valor de hora, pode definir a hora como um fuso horário diferente, como PST. 

Por exemplo, se você estiver enviando uma mensagem a um usuário um dia antes do aniversário dele, você deve salvar a variável de contexto como um tipo de dado de hora, pois há lógica Liquid associada ao envio um dia antes. No entanto, se você estiver enviando uma mensagem de feriado no Dia de Natal (25 de dezembro), não precisaria referenciar a hora como uma variável dinâmica, então usar um tipo de dado string seria preferível.

## Usando variáveis de contexto

Você pode usar variáveis de contexto em qualquer lugar que usar Liquid em um Canvas, como em [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) e [Atualização do Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update) etapas, selecionando **Adicionar Personalização**.

Por exemplo, digamos que você queira notificar os passageiros sobre o acesso ao lounge VIP antes do próximo voo. Esta mensagem deve ser enviada apenas aos passageiros que compraram um bilhete de primeira classe. Uma variável de contexto é uma maneira flexível de rastrear essa informação.

Os usuários entrarão no Canvas quando comprarem um bilhete de avião. Para determinar a elegibilidade para acesso ao lounge, criaremos uma variável de contexto chamada `lounge_access_granted` em uma etapa de Contexto, e então referenciamos essa variável de contexto nas etapas subsequentes da jornada do usuário.

![Variável de contexto configurada para rastrear se um passageiro se qualifica para acesso ao lounge VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Nesta etapa de Contexto, usaremos {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} para determinar se o tipo de voo que eles compraram é `first_class`.

Em seguida, criaremos uma etapa de Mensagem para direcionar usuários onde {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} é `true`. Esta mensagem será uma notificação por push que inclui informações personalizadas sobre o lounge. Com base nesta variável de contexto, os passageiros elegíveis receberão as mensagens relevantes antes do voo.

- Os passageiros com bilhetes de primeira classe receberão: "Aproveite o acesso exclusivo ao lounge VIP!"
- Os passageiros com bilhetes de negócios e econômicos receberão: "Faça upgrade no seu voo para acesso exclusivo ao lounge VIP."

![Uma etapa de Mensagem com diferentes mensagens a serem enviadas, dependendo do tipo de bilhete de avião comprado.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
É possível adicionar [opções de postergação personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) com as informações da etapa Contexto, o que significa que você pode selecionar a variável que posterga os usuários.
{% endalert %}

### Para Jornadas de Ação e critérios de saída

Você pode aproveitar a comparação de filtros de propriedade com variáveis de contexto ou atributos personalizados nessas ações de disparo: **Executar Evento Personalizado** e **Fazer Compra**. Esses disparadores de ação também suportam filtros de propriedade para propriedades básicas e aninhadas. 

- Ao comparar com propriedades básicas, as comparações disponíveis corresponderão ao tipo da propriedade definida pelo evento personalizado. Por exemplo, propriedades string terão correspondências exatas e regex. Propriedades booleanas serão verdadeiras ou falsas. 
- Ao comparar com propriedades aninhadas, os tipos não são pré-definidos, então você pode selecionar comparações entre múltiplos tipos de dados para booleanos, números, strings, tempo e dia do ano, semelhante às comparações para atributos personalizados aninhados. Se você selecionar um tipo de dado que não corresponda ao tipo de dado real da propriedade aninhada no momento da comparação, o usuário não corresponderá à Jornada de Ação ou critérios de saída.

#### Exemplos de Jornada de Ação

{% alert important %}
Para comparações de atributos personalizados, usaremos o valor do atributo personalizado no momento em que a ação é realizada. Isso significa que um usuário não corresponderá ao grupo da Jornada de Ação se não tiver esse atributo personalizado preenchido no momento da comparação, ou se o valor do atributo personalizado não corresponder às comparações de propriedade definidas. Esse é o caso mesmo que o usuário tivesse correspondido quando entrou na etapa da Jornada de Ação.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

O seguinte Caminho de Ação está configurado para classificar usuários que realizaram o evento personalizado `Account_Created` com a propriedade básica `source` para a variável de contexto `app_source_variable`.

![Um exemplo de Caminho de Ação que faz referência a uma variável de contexto ao realizar um evento personalizado.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

O seguinte Caminho de Ação está configurado para corresponder à propriedade básica `brand` para o nome do produto específico `shoes` a uma variável de contexto `promoted_shoe_brand`.

![Um exemplo de Caminho de Ação que faz referência a uma variável de contexto ao realizar uma compra.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exemplos de critérios de saída

{% tabs %}
{% tab Perform custom event %}

Os critérios de saída afirmam que a qualquer momento na jornada de um usuário no Canva, eles sairão do Canva se:

- Eles realizarem o evento personalizado **Abandonar Carrinho**, e
- A propriedade básica **Item no Carrinho** corresponder ao valor da string da variável de contexto `cart_item_threshold`.

![Critérios de saída configurados para sair um usuário se eles realizarem um evento personalizado com base na variável de contexto.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Os critérios de saída afirmam que a qualquer momento na jornada de um usuário no Canva, eles sairão do Canva se:

- Eles fizerem uma compra específica para o nome do produto "livro", e
- A propriedade aninhada dessa compra "loyalty_program" é igual ao atributo personalizado do usuário "VIP".

![Critérios de saída configurados para sair um usuário se eles fizerem uma compra.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Filtros de variáveis de contexto

Você pode criar filtros que usam variáveis de contexto previamente declaradas em [Caminhos do Público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) e [Divisão de Decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) etapas.

{% alert note %}
Filtros de variáveis de contexto estão disponíveis apenas para etapas de Caminhos do Público e Divisão de Decisão.
{% endalert %}

Variáveis de contexto são declaradas e acessíveis apenas no escopo de um Canva, o que significa que não podem ser referenciadas em segmentos. Filtros de variáveis de contexto funcionam de maneira semelhante em Caminhos do Público e etapas de Divisão de Decisão—etapas de Caminhos do Público representam múltiplos grupos, enquanto etapas de Divisão de Decisão representam decisões binárias.

![Exemplo de etapa de Divisão de Decisão com a opção de criar um filtro com uma variável de contexto.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Semelhante a como as variáveis de contexto do Canva têm tipos pré-definidos, as comparações entre variáveis de contexto e valores estáticos devem ter [tipos de dados correspondentes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). O filtro de variável de contexto permite comparações entre múltiplos tipos de dados para booleanos, números, strings, tempo e dia do ano, semelhante às comparações para [atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Use o mesmo tipo de dado para sua variável de contexto e comparação. Por exemplo, se sua variável de contexto for um tipo de dado de tempo, use comparações de tempo (como "antes" ou "depois"). Usar tipos de dados incompatíveis (como comparações de string com uma variável de contexto de tempo) pode causar comportamentos inesperados.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

Aqui está um exemplo de um filtro de variável de contexto comparando a variável de contexto `product_name` com a regex `/braze/`.

![Uma configuração de filtro para a variável de contexto "product_name" para corresponder à regex "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparando com variáveis de contexto ou atributos personalizados

Ao selecionar o **Comparar com uma variável de contexto ou atributo personalizado** alternar, você pode construir filtros de variável de contexto que comparam com variáveis de contexto ou atributos personalizados definidos anteriormente. Isso pode ser útil para realizar comparações que são dinâmicas por usuário, como `context` acionadas por API, ou para condensar lógica de comparação complexa definida entre variáveis de contexto.

{% tabs %}
{% tab Example 1 %}

Vamos supor que você queira enviar um lembrete personalizado para os usuários após um período dinâmico de inatividade, que inclui qualquer um que não tenha feito login no seu app nos últimos três dias, deve receber uma mensagem.

Você tem uma variável de contexto `re_engagement_date` que é definida como {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Observe que `3 days` pode ser uma quantidade variável que também é armazenada como um atributo personalizado do usuário. Então, se o `re_engagement_date` for depois do `last_login_date` (armazenado como um atributo personalizado no perfil do usuário), eles receberão uma mensagem.

![Uma configuração de filtro com atributos personalizados como o tipo de personalização para a variável de contexto "re_engagement_date" após o atributo personalizado "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

O seguinte filtro compara a variável de contexto `reminder_date` para ser antes da variável de contexto `appointment_deadline`. Isso pode ajudar a agrupar usuários em uma etapa de Caminhos de Público para determinar se eles devem receber lembretes adicionais antes do prazo de sua consulta.

![Uma configuração de filtro com variáveis de contexto como o tipo de personalização para a variável de contexto "reminder_date" na variável de contexto "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Padronização de consistência de fuso horário

Embora a maioria das propriedades de evento usando o tipo de timestamp já estejam em UTC no Canva, há algumas exceções. Com a adição do Contexto do Canva, todas as propriedades de evento de timestamp padrão em Canvases baseados em ação estarão consistentemente em UTC. Essa mudança faz parte de um esforço mais amplo para garantir uma experiência mais previsível e consistente ao editar etapas e mensagens do canva. Observe que essa mudança impactará todos os canva baseados em ações, independentemente de o canva específico estar usando uma etapa de contexto ou não.

{% alert important %}
Em todas as circunstâncias, recomendamos fortemente o uso de [filtros Liquid time_zone para que os timestamps sejam representados no fuso horário desejado.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) Você pode consultar esta [pergunta frequente no artigo da etapa de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example) para um exemplo.
{% endalert %}

## Artigos relacionados

- [etapa de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personalização e conteúdo dinâmico com Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

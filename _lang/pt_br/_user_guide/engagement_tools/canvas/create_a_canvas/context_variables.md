---
nav_title: Variáveis de contexto
article_title: Variáveis de contexto
page_type: reference
description: "Este artigo de referência explica as variáveis de contexto nos canvas da Braze, incluindo seus tipos, uso e melhores práticas."
---

# Variáveis de contexto

> As variáveis de contexto são dados temporários que você pode criar e usar dentro da jornada de um usuário em um canva específico. Elas permitem personalizar postergações, segmentar usuários dinamicamente e enriquecer o envio de mensagens sem alterar permanentemente as informações do perfil de um usuário. As variáveis de contexto existem apenas dentro da sessão do canva e não persistem entre diferentes canvas ou fora da sessão.

## Como as variáveis de contexto funcionam

As variáveis de contexto podem ser definidas de duas maneiras:

- **Na entrada do canva:** Quando os usuários entram em um canva, os dados do evento ou do gatilho da API podem preencher automaticamente as variáveis de contexto.
- **Em uma etapa de Contexto:** Você pode definir ou atualizar variáveis de contexto manualmente dentro do canva adicionando uma [etapa de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

Cada variável de contexto inclui:

- Um nome (como `flight_time` ou `subscription_renewal_date`)
- Um tipo de dado (como número, string, tempo ou array)
- Um valor que você atribui usando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou pela ferramenta **Adicionar Personalização**.

Quando definida, você pode usar uma variável de contexto em todo o canva referenciando-a neste formato: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Por exemplo, {% raw %}`{{context.${flight_time}}}`{% endraw %} pode retornar o horário do voo agendado do usuário.

Cada vez que um usuário entra no canva — mesmo que já tenha entrado antes — as variáveis de contexto serão redefinidas com base nos dados de entrada mais recentes e na configuração do canva. Essa abordagem com estado permite que cada entrada no canva mantenha seu próprio contexto independente, possibilitando que os usuários tenham múltiplos estados ativos dentro da mesma jornada enquanto retêm o contexto específico para cada estado.

Por exemplo, se um cliente tem dois voos futuros, ele terá dois estados de jornada separados rodando simultaneamente — cada um com suas próprias variáveis de contexto específicas do voo, como horário de partida e destino. Isso permite que você envie lembretes personalizados sobre o voo das 14h para Nova York enquanto envia atualizações diferentes sobre o voo das 8h para Los Angeles amanhã, para que cada mensagem permaneça relevante para a reserva específica.

## Considerações

Você pode definir até 10 variáveis de contexto por [etapa de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/). Cada nome de variável pode ter até 100 caracteres e deve usar apenas letras, números ou sublinhados.

As definições de variáveis de contexto podem ter até 10.240 caracteres. Se você passar variáveis de contexto para um canva disparado por API, elas compartilham o mesmo namespace que as variáveis criadas em uma etapa de Contexto. Por exemplo, se você enviar uma variável `purchased_item` no objeto de contexto do [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/), você pode referenciá-la como {% raw %}`{{context.${purchased_item}}}`{% endraw %}. Se você redefinir essa variável em uma etapa de Contexto, o novo valor substituirá o valor da API para a jornada desse usuário.

Você pode armazenar até 50 KB por etapa de Contexto, distribuídos em até 10 variáveis. Se o tamanho total de todas as variáveis em uma etapa exceder 50 KB, quaisquer variáveis que excedam o limite não serão avaliadas ou armazenadas. Por exemplo, se você tiver três variáveis em uma etapa de Contexto:

- Variável 1: 30 KB
- Variável 2: 19 KB
- Variável 3: 2 KB

A variável 3 não será avaliada ou armazenada porque a soma das variáveis anteriores excede 50 KB.

## Tipos de dados

As variáveis de contexto criadas ou atualizadas na etapa podem receber os seguintes tipos de dados.

{% alert note %}
As variáveis de contexto têm os mesmos formatos esperados para tipos de dados que os [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Ao usar o tipo array, a Braze tenta analisar o valor como JSON, o que permite que arrays de objetos sejam criados com sucesso. Se os objetos dentro dos seus arrays não forem JSON válidos, o resultado será um array simples de strings. <br><br>Para objetos aninhados e arrays de objetos, use o [filtro Liquid `as_json_string`](#converting-connected-content-strings-to-json). Se você estiver criando o mesmo objeto em uma etapa de Contexto, precisará renderizar o objeto usando `as_json_string`, como {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Tipo de dados | Nome da variável de exemplo | Valor de exemplo |
|---|---|---|
|booleano| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Número| credit_score |{% raw %}<code>740</code>{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Array| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Array (de objetos)| pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
|Hora (em UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objeto (achatado) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por padrão, o tipo de dado de hora está em UTC. Se você usar um tipo de dado string para armazenar um valor de hora, pode definir a hora em um fuso horário diferente, como PST. 

Por exemplo, se você estiver enviando uma mensagem a um usuário um dia antes do aniversário dele, salve a variável de contexto como um tipo de dado de hora, pois há lógica Liquid associada ao envio um dia antes. No entanto, se você estiver enviando uma mensagem de feriado no Dia de Natal (25 de dezembro), não precisaria referenciar a hora como uma variável dinâmica, então usar um tipo de dado string seria preferível.

Para tipos de dados de objeto, você pode usar notação de ponto para especificar um caminho através dos dados. Por exemplo, se sua etapa de Contexto define uma variável de contexto `order_summary` com esta estrutura:

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

Em um filtro de [jornada do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) ou [divisão de decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/), insira o caminho como o nome da variável de contexto usando notação de ponto (por exemplo, `order_summary.shipping.carrier`). Quando o filtro é avaliado, a Braze resolve esse caminho para o valor `overnight`.

Em Liquid (como em uma etapa de [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)), use {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %}.

## Usando variáveis de contexto

Você pode usar variáveis de contexto em qualquer lugar que usar Liquid em um canva, como em etapas de [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) e [Atualização do Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update), selecionando **Adicionar Personalização**. Para mensagens no app e Banners em etapas de Mensagem, você pode selecionar variáveis de contexto para determinar quando a mensagem deve expirar.

Por exemplo, digamos que você queira notificar os passageiros sobre o acesso ao lounge VIP antes do próximo voo. Essa mensagem deve ser enviada apenas aos passageiros que compraram um bilhete de primeira classe. Uma variável de contexto é uma maneira flexível de rastrear essa informação.

Os usuários entrarão no canva quando comprarem um bilhete de avião. Para determinar a elegibilidade para acesso ao lounge, criaremos uma variável de contexto chamada `lounge_access_granted` em uma etapa de Contexto e, em seguida, referenciaremos essa variável de contexto nas etapas subsequentes da jornada do usuário.

![Variável de contexto configurada para rastrear se um passageiro se qualifica para acesso ao lounge VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Nesta etapa de Contexto, usaremos {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} para determinar se o tipo de voo comprado é `first_class`.

Em seguida, criaremos uma etapa de Mensagem para direcionar usuários onde {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} é `true`. Essa mensagem será uma notificação por push que inclui informações personalizadas sobre o lounge. Com base nessa variável de contexto, os passageiros elegíveis receberão as mensagens relevantes antes do voo.

- Os passageiros com bilhetes de primeira classe receberão: "Aproveite o acesso exclusivo ao lounge VIP!"
- Os passageiros com bilhetes de classe executiva e econômica receberão: "Faça upgrade no seu voo para acesso exclusivo ao lounge VIP."

![Uma etapa de Mensagem com diferentes mensagens a serem enviadas, dependendo do tipo de bilhete de avião comprado.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
É possível adicionar [opções de postergação personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) com as informações da etapa de Contexto, o que significa que você pode selecionar a variável que posterga os usuários.
{% endalert %}

### Para jornadas de ação e critérios de saída

Você pode aproveitar a comparação de filtros de propriedade com variáveis de contexto ou atributos personalizados nestas ações-gatilho: **Executar Evento Personalizado** e **Fazer Compra**. Esses gatilhos de ação também suportam filtros de propriedade para propriedades básicas e aninhadas. 

- Ao comparar com propriedades básicas, as comparações disponíveis corresponderão ao tipo da propriedade definida pelo evento personalizado. Por exemplo, propriedades string terão correspondências exatas e regex. Propriedades booleanas serão verdadeiras ou falsas. 
- Ao comparar com propriedades aninhadas, os tipos não são pré-definidos, então você pode selecionar comparações entre múltiplos tipos de dados para booleanos, números, strings, tempo e dia do ano, semelhante às comparações para atributos personalizados aninhados. Se você selecionar um tipo de dado que não corresponda ao tipo de dado real da propriedade aninhada no momento da comparação, o usuário não corresponderá à jornada de ação ou aos critérios de saída.

#### Exemplos de jornada de ação

{% alert important %}
Para comparações de atributos personalizados, usaremos o valor do atributo personalizado no momento em que a ação é realizada. Isso significa que um usuário não corresponderá ao grupo da jornada de ação se não tiver esse atributo personalizado preenchido no momento da comparação, ou se o valor do atributo personalizado não corresponder às comparações de propriedade definidas. Esse é o caso mesmo que o usuário tivesse correspondido quando entrou na etapa da jornada de ação.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

A seguinte jornada de ação está configurada para classificar usuários que realizaram o evento personalizado `Account_Created` com a propriedade básica `source` para a variável de contexto `app_source_variable`.

![Um exemplo de jornada de ação que faz referência a uma variável de contexto ao realizar um evento personalizado.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

A seguinte jornada de ação está configurada para corresponder à propriedade básica `brand` para o nome do produto específico `shoes` a uma variável de contexto `promoted_shoe_brand`.

![Um exemplo de jornada de ação que faz referência a uma variável de contexto ao realizar uma compra.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exemplos de critérios de saída

{% tabs %}
{% tab Perform custom event %}

Os critérios de saída determinam que, a qualquer momento na jornada de um usuário no canva, ele sairá do canva se:

- Realizar o evento personalizado **Abandonar Carrinho**, e
- A propriedade básica **Item no Carrinho** corresponder ao valor da string da variável de contexto `cart_item_threshold`.

![Critérios de saída configurados para remover um usuário se ele realizar um evento personalizado com base na variável de contexto.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Os critérios de saída determinam que, a qualquer momento na jornada de um usuário no canva, ele sairá do canva se:

- Fizer uma compra específica para o nome do produto "livro", e
- A propriedade aninhada dessa compra "loyalty_program" for igual ao atributo personalizado do usuário "VIP".

![Critérios de saída configurados para remover um usuário se ele fizer uma compra.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Definir uma expiração

Para [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/) e [mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) em uma etapa de [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) do canva, selecione **Uma duração após a etapa estar disponível** para expiração e, em seguida, ative **Personalizar duração** para controlar o período de disponibilidade a partir de uma variável de contexto — por exemplo, para corresponder a uma promoção ou duração de reserva de uma etapa de Contexto.

**Personalizar duração** se aplica a essa opção de expiração baseada em duração. Se você escolher **Em uma data e hora específicas**, defina a expiração usando os controles de data e hora.

### Postergações de jornada de ação

Em uma etapa de [jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), em **Período de Avaliação**, ative **Personalizar postergação** para definir por quanto tempo os usuários são mantidos na etapa a partir de uma variável de contexto. Use isso quando o período de espera deve variar por usuário com base em informações como nível ou região.

### Filtros de variáveis de contexto

Você pode criar filtros que usam variáveis de contexto previamente declaradas em etapas de [jornada do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) e [divisão de decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

{% alert note %}
Filtros de variáveis de contexto estão disponíveis apenas para etapas de jornada do público e divisão de decisão.
{% endalert %}

Variáveis de contexto são declaradas e acessíveis apenas no escopo de um canva, o que significa que não podem ser referenciadas em segmentos. Filtros de variáveis de contexto funcionam de maneira semelhante em etapas de jornada do público e divisão de decisão — etapas de jornada do público representam múltiplos grupos, enquanto etapas de divisão de decisão representam decisões binárias.

![Exemplo de etapa de divisão de decisão com a opção de criar um filtro com uma variável de contexto.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Assim como as variáveis de contexto do canva têm tipos pré-definidos, as comparações entre variáveis de contexto e valores estáticos devem ter [tipos de dados correspondentes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). O filtro de variável de contexto permite comparações entre múltiplos tipos de dados para booleanos, números, strings, tempo e dia do ano, semelhante às comparações para [atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Use o mesmo tipo de dado para sua variável de contexto e comparação. Por exemplo, se sua variável de contexto for um tipo de dado de tempo, use comparações de tempo (como "antes" ou "depois"). Usar tipos de dados incompatíveis (como comparações de string com uma variável de contexto de tempo) pode causar comportamentos inesperados.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

Aqui está um exemplo de um filtro de variável de contexto comparando a variável de contexto `product_name` com a regex `/braze/`.

![Uma configuração de filtro para a variável de contexto "product_name" para corresponder à regex "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparando com variáveis de contexto ou atributos personalizados

Ao selecionar a opção **Comparar com uma variável de contexto ou atributo personalizado**, você pode construir filtros de variável de contexto que comparam com variáveis de contexto ou atributos personalizados definidos anteriormente. Isso pode ser útil para realizar comparações dinâmicas por usuário, como `context` disparado por API, ou para condensar lógica de comparação complexa definida entre variáveis de contexto.

{% tabs %}
{% tab Example 1 %}

Digamos que você queira enviar um lembrete personalizado para os usuários após um período dinâmico de inatividade, incluindo qualquer um que não tenha feito login no seu app nos últimos três dias e que deve receber uma mensagem.

Você tem uma variável de contexto `re_engagement_date` que é definida como {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Note que `3 days` pode ser uma quantidade variável que também é armazenada como um atributo personalizado do usuário. Então, se o `re_engagement_date` for depois do `last_login_date` (armazenado como um atributo personalizado no perfil do usuário), eles receberão uma mensagem.

![Uma configuração de filtro com atributos personalizados como o tipo de personalização para a variável de contexto "re_engagement_date" após o atributo personalizado "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

O seguinte filtro compara a variável de contexto `reminder_date` para ser antes da variável de contexto `appointment_deadline`. Isso pode ajudar a agrupar usuários em uma etapa de jornada do público para determinar se eles devem receber lembretes adicionais antes do prazo da consulta.

![Uma configuração de filtro com variáveis de contexto como o tipo de personalização para a variável de contexto "reminder_date" na variável de contexto "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Padronização de consistência de fuso horário

Embora a maioria das propriedades de evento usando o tipo timestamp já estejam em UTC no canva, há algumas exceções. Com a adição do Contexto do canva, todas as propriedades de evento de timestamp padrão em canvas baseados em ação estarão consistentemente em UTC. Essa mudança faz parte de um esforço mais amplo para garantir uma experiência mais previsível e consistente ao editar etapas e mensagens do canva. Note que essa mudança impactará todos os canvas baseados em ação, independentemente de o canva específico estar usando uma etapa de Contexto ou não.

{% alert important %}
Em todas as circunstâncias, recomendamos fortemente o uso de [filtros Liquid time_zone]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) para que os timestamps sejam representados no fuso horário desejado. Você pode consultar esta [pergunta frequente no artigo da etapa de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example) para ver um exemplo.
{% endalert %}

## Artigos relacionados

- [Etapa de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personalização e conteúdo dinâmico com Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)
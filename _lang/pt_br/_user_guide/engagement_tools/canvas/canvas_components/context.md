---
nav_title: Contexto 
article_title: Contexto 
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "Este artigo de referência cobre como criar e usar etapas de Contexto em seu canva."
tool: Canvas

---

# Contexto

> As etapas de Contexto permitem que você crie e atualize uma ou mais variáveis para um usuário enquanto ele navega por um canva. Por exemplo, se você tiver um canva que gerencia descontos sazonais, pode usar uma variável de contexto para armazenar um código de desconto diferente cada vez que um usuário entra no canva.

## Como funciona

![Uma etapa de Contexto como a primeira etapa de um canva.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

As etapas de Contexto permitem que você crie e use dados temporários durante a jornada de um usuário por um canva específico. Esses dados existem apenas dentro daquela jornada do canva e não persistem em diferentes canvas ou fora da sessão.

As variáveis de contexto existem apenas para aquela jornada específica do canva. Elas não alteram permanentemente o perfil do usuário e não aparecem em outros canvas. Isso as torna ideais para informações temporárias que são relevantes apenas para uma campanha ou fluxo de trabalho específico.

{% alert tip %}
Para uma referência completa sobre variáveis de contexto, incluindo tipos de dados, uso e melhores práticas, consulte a [referência de variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).
{% endalert %}

Dentro de uma etapa de Contexto, você pode definir ou atualizar até 10 variáveis de contexto. Essas variáveis podem ser usadas para personalizar postergações, segmentar usuários dinamicamente e enriquecer o envio de mensagens ao longo do canva. Por exemplo, você poderia criar uma variável de contexto para o horário do voo agendado de um usuário e então usá-la para definir postergações personalizadas e enviar lembretes.

Você pode definir variáveis de contexto de duas maneiras:

- **Na entrada do canva:** Os dados do evento ou do gatilho da API podem preencher automaticamente as variáveis de contexto.
- **Em uma etapa de Contexto:** Defina ou atualize variáveis de contexto manualmente adicionando uma etapa de Contexto.

Cada variável de contexto requer um nome, um tipo de dado e um valor (definido usando Liquid ou a ferramenta Adicionar Personalização). Quando definidas, você pode referenciar variáveis de contexto ao longo do canva usando Liquid, como {% raw %}`{{context.${flight_time}}}`{% endraw %}. No campo **Nome da variável de contexto**, você também pode digitar o nome da variável de contexto ou selecioná-lo no menu suspenso do editor de etapas. Para mais detalhes, consulte a [referência de variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

Cada entrada no canva redefine variáveis de contexto com base nos dados da última entrada e na configuração do canva, permitindo que os usuários tenham várias jornadas ativas com seu próprio contexto. Por exemplo, se um cliente tem dois voos futuros, ele terá dois estados de jornada separados rodando simultaneamente&#8212;cada um com suas próprias variáveis de contexto específicas do voo, como horário de partida e destino. Isso permite que você envie lembretes personalizados sobre o voo das 14h para Nova York enquanto envia atualizações diferentes sobre o voo das 8h para Los Angeles amanhã, para que cada mensagem permaneça relevante para a reserva específica.

### Processamento e agrupamento de usuários

As etapas de Contexto processam usuários em lotes para otimizar a performance. Quando os usuários entram em uma etapa de Contexto, a Braze os processa em lotes de 1.000 usuários por padrão. Esses lotes são processados em paralelo, mas dentro de cada lote, os usuários são processados sequencialmente.

Isso significa:

**Exemplo**: Se 3.500 usuários entrarem em uma etapa de Contexto com Conteúdo conectado que leva 650ms por usuário:
- A Braze cria 4 lotes de usuários (1.000, 1.000, 1.000 e 500 usuários neste exemplo).
- Cada lote processa usuários sequencialmente, então um lote de 1.000 usuários leva aproximadamente 10,8 minutos (650 segundos; 1.000 × 650ms).
- Os lotes são concluídos em momentos diferentes, então os usuários entram na próxima etapa à medida que seu lote termina.
- Os primeiros usuários podem alcançar a próxima etapa vários minutos antes dos últimos usuários, dependendo do tamanho do lote e dos tempos de resposta do Conteúdo conectado.

Sem Conteúdo conectado, as etapas de Contexto processam muito mais rápido porque não há chamadas de API externas para esperar.

## Considerações

- Você pode definir até 10 variáveis de contexto por etapa de Contexto.
- Cada variável requer um nome único (apenas letras, números e sublinhados, até 100 caracteres).
- O tamanho total de todas as variáveis em uma etapa não pode exceder 50 KB.
- As variáveis passadas usando gatilhos de API compartilham o mesmo namespace que aquelas criadas em etapas de Contexto; redefinir uma variável em uma etapa de Contexto substitui o valor da API.

Para mais detalhes e uso avançado, veja a [referência de variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

## Criando uma etapa de Contexto

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Etapa 1: Adicionar uma etapa

Adicione uma etapa ao seu canva, depois arraste e solte o componente da barra lateral, ou selecione o botão <i class="fas fa-plus-circle"></i> de mais e selecione **Contexto**.

### Etapa 2: Defina as variáveis

{% alert note %}
Você pode definir até 10 variáveis de contexto para cada etapa de Contexto.
{% endalert %}

Para definir uma variável de contexto:

1. Dê um **nome** à sua variável de contexto.
2. Selecione um [tipo de dado]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types).
3. Escreva uma expressão Liquid manualmente ou use **Adicionar Personalização** para criar um trecho Liquid a partir de atributos pré-existentes.
4. Selecione **Prévia** para verificar o valor da sua variável de contexto.
5. (Opcional) Para adicionar variáveis adicionais, selecione **Adicionar variável de contexto** e repita as etapas 1-4.
6. Quando terminar, selecione **Concluir**.

Agora você pode usar sua variável de contexto em qualquer lugar que usar Liquid, como nas etapas de Mensagem e Atualização de Usuário, selecionando **Adicionar Personalização**. No campo **Nome da variável de contexto**, você também pode digitar o nome da variável de contexto ou selecioná-lo no menu suspenso do editor de etapas. Para um guia completo, veja a [referência de variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

{% alert important %}
Ao referenciar variáveis de contexto, sempre use o formato {% raw %}`{{context.${variable_name}}}`{% endraw %}.
{% endalert %}

### Filtros de variável de contexto

Você pode criar filtros usando variáveis de contexto nas etapas [Jornadas do Público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) e [Divisão de Decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split). Para configuração de filtros, lógica de comparação e exemplos avançados, veja a [referência de variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters).

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## Visualizando jornadas do usuário

Recomendamos testar e [visualizar suas jornadas do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) para garantir que suas mensagens sejam enviadas ao público certo e que as variáveis de contexto sejam avaliadas com os resultados esperados.

{% alert note %}
Se você estiver visualizando seu canva na seção **Prévia e Envio de Teste** do editor, o timestamp na prévia da mensagem de teste **não** é padronizado para UTC porque esse painel gera prévias como strings. Isso significa que, se um canva estiver configurado para aceitar um objeto `time`, a prévia da mensagem não reflete com precisão o que ocorre quando o canva está ativo. Para testar seu canva com mais precisão, recomendamos visualizar as jornadas do usuário.
{% endalert %}

Certifique-se de observar quaisquer cenários comuns que criem variáveis de contexto inválidas. Ao visualizar sua jornada do usuário, você pode ver os resultados das etapas de postergação personalizadas usando variáveis de contexto, e quaisquer comparações de público ou decisão que correspondam os usuários a variáveis de contexto.

Se a variável de contexto for válida, você pode referenciá-la em todo o seu canva. No entanto, se a variável de contexto não foi criada corretamente, as etapas futuras em seu canva também não funcionarão corretamente. Por exemplo, se você criar uma etapa de Contexto para atribuir aos usuários um horário de compromisso e definir o valor do horário do compromisso para uma data passada, o e-mail de lembrete na sua etapa de Mensagem não será enviado.

## Convertendo strings de Conteúdo conectado para JSON

Ao fazer uma [chamada de Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) em uma etapa de Contexto, o JSON retornado da chamada é avaliado como um tipo de dado string para consistência e prevenção de erros. Se você quiser converter essa string em JSON, use `as_json_string`. Por exemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Solução de problemas

### Variáveis de contexto inválidas

Uma variável de contexto é considerada inválida quando:

- Uma chamada para um Conteúdo conectado embutido falha.
- A expressão Liquid em tempo de execução retorna um valor que não corresponde ao tipo de dado ou está vazio (nulo).

Por exemplo, se o tipo de dado da variável de contexto for **Número**, mas a expressão Liquid retornar uma string, ela é inválida.

Nessas circunstâncias:
- O usuário avança para a próxima etapa.
- A análise de dados da etapa do canva conta isso como _Não Atualizado_.

Ao solucionar problemas, monitore a métrica _Não Atualizado_ para verificar se sua variável de contexto está sendo atualizada corretamente. Se a variável de contexto for inválida, seus usuários podem continuar no canva após a etapa de Contexto, mas podem não se qualificar para etapas posteriores.

Consulte [Tipos de dados]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) para os exemplos de configuração de cada tipo de dado.

### Atrasos no envio com Conteúdo conectado

Todos os usuários em um lote são processados antes que qualquer usuário avance. Após a conclusão do processamento em lote, os usuários bem-sucedidos avançam para a próxima etapa, enquanto os usuários com falha são tentados novamente separadamente — os usuários bem-sucedidos não esperam que as tentativas de reexecução sejam bem-sucedidas antes de avançar.

**Comportamento de reexecução**: As etapas de Contexto (e todas as etapas do canva) usam mecanismos de reexecução específicos do canva, não o comportamento padrão de reexecução do Conteúdo conectado. Se uma chamada de Conteúdo conectado falhar, a Braze tenta novamente a etapa aproximadamente 13 vezes com retrocesso exponencial. Se todas as tentativas falharem, o usuário sai do canva.

{% alert note %}
A tag `:retry` usada no Conteúdo conectado padrão não se aplica às chamadas de Conteúdo conectado feitas dentro das etapas do canva. As etapas do canva têm sua própria lógica de reexecução otimizada para fluxos de trabalho do canva.
{% endalert %}

**Tempo de processamento**: O tempo necessário para processar todos os usuários em uma etapa de Contexto depende de:
- O número de usuários entrando na etapa
- Se o Conteúdo conectado é usado (e seu tempo de resposta)
- O tamanho do lote (padrão de 1.000 usuários por lote)

Se seu endpoint de Conteúdo conectado tem limites de taxa, considere que as etapas de Contexto processam usuários sequencialmente dentro de cada lote, o que ajuda a respeitar os limites de taxa naturalmente. No entanto, vários lotes são processados em paralelo, então certifique-se de que seu endpoint pode lidar com solicitações simultâneas de vários lotes.

## Padronização de consistência de fuso horário

Embora a maioria das propriedades de evento que usam o tipo timestamp já estejam em UTC no Canvas, há algumas exceções. Com a adição do Contexto do Canvas, todas as propriedades de evento de timestamp padrão em canvas baseados em ação estão em UTC. Essa mudança faz parte de um esforço mais amplo para garantir uma experiência mais previsível e consistente ao editar etapas e mensagens do canva. Observe que essa mudança impacta todos os canvas baseados em ação, independentemente de o canva específico estar usando uma etapa de Contexto ou não.

{% alert important %}
Em todas as circunstâncias, recomendamos fortemente o uso de [filtros Liquid time_zone]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) para que os timestamps sejam representados no fuso horário desejado. Você pode consultar esta [pergunta frequente](#faq-example) para ver um exemplo.
{% endalert %}

## Perguntas frequentes

### O que mudou desde que o Contexto do Canvas se tornou disponível para todos?

Agora que o Contexto do Canvas está disponível para todos, os seguintes detalhes se aplicam:

- Todos os timestamps com um [tipo datetime]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) das [propriedades de evento de gatilho]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) em canvas baseados em ação estão em [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).
- Essa mudança impacta todos os canvas baseados em ação, independentemente de o canva específico estar usando uma etapa de Contexto ou não.

#### Qual é a razão para essa mudança?

Essa mudança faz parte de um esforço mais amplo para criar uma experiência mais previsível e consistente ao editar etapas e mensagens do canva.

#### Canvas disparados por API ou agendados são impactados por essa mudança?

Não.

#### Essa mudança impacta as propriedades de entrada do canva?

Sim, isso impacta `canvas_entry_properties` se o `canvas_entry_property` estiver sendo usado em um canva baseado em ação e o tipo de propriedade for `time`. Em todas as circunstâncias, recomendamos o uso de filtros Liquid `time_zone` para que os timestamps sejam representados no fuso horário desejado.

Aqui está um exemplo de como fazer isso:

| Liquid na etapa de Mensagem | Resultado | É assim que se representa fusos horários corretamente no Liquid? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Não |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Não
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Sim |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Qual é um exemplo prático de como o novo comportamento de timestamp pode afetar minhas mensagens? {#faq-example}

Vamos supor que temos um canva baseado em ação que contém o seguinte conteúdo em uma etapa de Mensagem:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Isso resulta na seguinte mensagem: 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Como nenhum fuso horário é especificado usando Liquid, o timestamp aqui está em UTC. 

Para especificar um fuso horário claramente, podemos usar filtros Liquid `time_zone` assim: 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Isso resulta na seguinte mensagem: 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Como o fuso horário America/Los Angeles é especificado usando Liquid, o timestamp aqui está em PST.

O fuso horário preferido também pode ser enviado na carga útil das propriedades do evento e usado na lógica Liquid:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### Como as variáveis de contexto diferem das propriedades de entrada do canva?

As propriedades de entrada do canva estão incluídas como variáveis de contexto do canva. Isso significa que você pode enviar propriedades de entrada do canva usando a API da Braze e referenciá-las em outras etapas, de forma semelhante ao uso de uma variável de contexto com o trecho Liquid.

### As variáveis podem referenciar umas às outras em uma única etapa de Contexto?

Sim. Todas as variáveis em uma etapa de Contexto são avaliadas em sequência, o que significa que você pode ter as seguintes variáveis de contexto configuradas:

| Variável de contexto | Valor | Descrição |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | O tipo de culinária favorito de um usuário. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | O código de desconto disponível para um usuário. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | Uma mensagem personalizada que combina as variáveis anteriores. Em uma etapa de Mensagem, você pode usar o trecho Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} para referenciar a variável de contexto e entregar uma mensagem personalizada a cada usuário. Você também pode usar uma etapa de Contexto para salvar o valor do [código promocional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) e usá-lo como modelo em outras etapas ao longo de um canva. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Isso também se aplica a várias etapas de Contexto. Por exemplo, imagine esta sequência:

1. Uma etapa de Contexto inicial cria uma variável chamada `JobInfo` com o valor `job_title`.
2. Uma etapa de Mensagem referencia {% raw %}`{{context.${JobInfo}}}`{% endraw %} e exibe `job_title` para o usuário.
3. Mais tarde, uma etapa de Contexto atualiza a variável de contexto, mudando o valor de `JobInfo` para `job_description`.
4. Todas as etapas subsequentes que referenciam `JobInfo` agora usam o valor atualizado `job_description`.

As variáveis de contexto usam seu valor mais recente ao longo do canva, com cada atualização afetando todas as etapas seguintes que referenciam essa variável.
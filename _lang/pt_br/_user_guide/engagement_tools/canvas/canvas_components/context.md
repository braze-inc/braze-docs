---
nav_title: Contexto 
article_title: Contexto 
alias: /context/
page_order: 1.5
page_type: reference
toc_headers: "h2"
description: "Este artigo de referência aborda como criar e usar etapas de contexto em seu Canva."
tool: Canvas

---

# Contexto

> As etapas de contexto permitem criar e atualizar uma ou mais variáveis para um usuário à medida que ele se move pelo Canva. Por exemplo, se você tiver um Canva que gerencia descontos sazonais, poderá usar uma variável de contexto para armazenar um código de desconto diferente cada vez que um usuário entrar no Canvas.

{% alert important %}
As etapas de contexto estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.<br><br>Observe que a aceitação do acesso antecipado à etapa do Canva Context atualiza a forma como os registros de data e hora são tratados em todos os seus Canvas. Para saber mais sobre isso, consulte [Padronização da consistência do fuso horário](#time-zone-consistency-standardization).
{% endalert %}

## Como funciona?

![Uma etapa do Context como a primeira etapa de um Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

As etapas do contexto permitem criar e usar dados temporários durante a jornada de um usuário em um Canva específico. Esses dados existem somente dentro dessa jornada do Canvas e não persistem em diferentes Canvas ou fora da sessão.

Para obter uma referência completa sobre variáveis de contexto, incluindo tipos de dados, uso e práticas recomendadas, consulte a [referência sobre variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

Em uma etapa do Contexto, você pode definir ou atualizar até 10 variáveis de contexto. Essas variáveis podem ser usadas para personalizar as postergações, segmentar os usuários dinamicamente e enriquecer o envio de mensagens em todo o Canva. Por exemplo, é possível criar uma variável de contexto para o horário programado do voo de um usuário e usá-la para definir postergações personalizadas e enviar lembretes.

Você pode definir variáveis de contexto de duas maneiras:

- **Na entrada do canva:** Os dados do evento ou do disparo da API podem preencher automaticamente as variáveis de contexto.
- **Em uma etapa do Contexto:** Defina ou atualize as variáveis de contexto manualmente, adicionando uma etapa de contexto.

Cada variável de contexto requer um nome, um tipo de dados e um valor (definido usando o Liquid ou a ferramenta Adicionar personalização). Quando definidas, você pode fazer referência a variáveis de contexto em todo o Canva usando Liquid, como {% raw %}`{{context.${flight_time}}}`{% endraw %}.

Cada entrada do Canvas redefine as variáveis de contexto com base nos dados de entrada mais recentes e na configuração do Canvas, permitindo que os usuários tenham várias jornadas ativas com seu próprio contexto. Por exemplo, se um cliente tiver dois voos futuros, ele terá dois estados de jornada separados em execução simultaneamente - cada um com suas próprias variáveis de contexto específicas do voo, como horário de partida e destinos. Isso permite enviar lembretes personalizados sobre o voo das 14h para Nova York e, ao mesmo tempo, enviar atualizações diferentes sobre o voo das 8h para Los Angeles amanhã, de modo que cada mensagem permaneça relevante para a reserva específica.

### Processamento e loteamento de usuários

As etapas de contexto processam os usuários em lotes para otimizar o desempenho. Quando os usuários entram em uma etapa de contexto, o Braze os processa em lotes de 1.000 usuários por padrão. Esses lotes são processados em paralelo, mas dentro de cada lote, os usuários são processados sequencialmente.

Isso significa que:
- **Processamento paralelo em lote**: Vários lotes de 1.000 usuários são processados simultaneamente, permitindo que grandes públicos sejam tratados com eficiência.
- **Processamento sequencial em lotes**: Em cada lote, os usuários são processados um após o outro. Se a etapa de contexto incluir chamadas de [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call), a solicitação de Connected Content de cada usuário deverá ser concluída antes que o próximo usuário do lote seja processado.
- **Progressão independente de lotes**: Cada lote progride de forma independente. Quando um lote conclui o processamento, esses usuários avançam para a próxima etapa imediatamente, mesmo que outros lotes ainda estejam em processamento. Isso significa que usuários de lotes diferentes podem chegar a etapas subsequentes em momentos diferentes.

**Exemplo**: Se 3.500 usuários entrarem em uma etapa de contexto com conteúdo conectado, isso levará 650 ms por usuário:
- O Braze cria aproximadamente 4 lotes de usuários (612, 802, 1.000, 880 e 120 usuários neste exemplo).
- Cada lote processa os usuários sequencialmente, portanto, um lote de 1.000 usuários leva aproximadamente 11 minutos (1.000 × 650ms).
- Os lotes são concluídos em momentos diferentes, portanto, os usuários passam para a próxima etapa à medida que o lote é concluído.
- Os primeiros usuários podem chegar à próxima etapa vários minutos antes dos últimos usuários, dependendo do tamanho do lote e dos tempos de resposta da Connected Content.

Sem o Connected Content, as etapas do Context são processadas muito mais rapidamente porque não há chamadas de API externas a serem aguardadas.

## Considerações

- Você pode definir até 10 variáveis de contexto por etapa do Context.
- Cada variável requer um nome exclusivo (somente letras, números, sublinhados, até 100 caracteres).
- O tamanho total de todas as variáveis em uma etapa não pode exceder 50 KB.
- As variáveis passadas usando disparadores de API compartilham o mesmo espaço de nomes que as criadas nas etapas de contexto; a redefinição de uma variável em uma etapa de contexto substitui o valor da API.

Para obter mais detalhes e uso avançado, consulte [Referência de variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

## Criando uma etapa de contexto

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Etapa 1: Adicionar uma etapa

Adicione uma etapa do canva e, em seguida, arraste e solte o componente da barra lateral ou selecione o botão de adição <i class="fas fa-plus-circle"></i> e selecione **Context (Contexto**).

### Etapa 2: Definir as variáveis

{% alert note %}
Você pode definir até 10 variáveis de contexto para cada etapa do Contexto.
{% endalert %}

Para definir uma variável de contexto:

1. Dê um **nome** à sua variável de contexto.
2. Selecione um [tipo de dados](#context-variable-types).
3. Escreva uma expressão Liquid manualmente ou use **Add Personalization** para criar um snippet Liquid a partir de atribuições pré-existentes.
4. Selecione **Pré-visualização** para verificar o valor de sua variável de contexto.
5. (Opcional) Para adicionar outras variáveis, selecione **Add Context variable (Adicionar variável de contexto** ) e repita as etapas 1 a 4.
6. Quando terminar, selecione **Concluído**.

Agora, é possível usar a variável de contexto em qualquer lugar que use o Liquid, como nas etapas de Mensagem e Atualização do usuário, selecionando **Adicionar personalização**. Para obter um passo a passo completo, consulte [Referência de variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

### Filtros de variáveis de contexto

Você pode criar filtros usando variáveis de contexto nas jornadas [do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) e nas etapas de [divisão de decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split). Para obter informações sobre configuração de filtros, lógica de comparação e exemplos avançados, consulte [Referência de variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters).

## Pré-visualização das jornadas do usuário

Recomendamos testar e [fazer uma prévia das jornadas do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) para garantir que as mensagens sejam enviadas ao público certo e que as variáveis de contexto sejam avaliadas de acordo com os resultados esperados.

{% alert note %}
Se estiver visualizando seu Canva na seção **Preview & Test Send** do editor, o carimbo de data/hora na visualização da mensagem de teste **não será** padronizado para UTC porque esse painel gera visualizações como strings. Isso significa que, se um Canvas estiver configurado para aceitar um objeto `time`, a visualização da mensagem não prevê com precisão o que ocorre quando o Canvas está ativo. Para testar o Canva com mais precisão, recomendamos a prévia das jornadas do usuário.
{% endalert %}

Não deixe de observar os cenários comuns que criam variáveis de contexto inválidas. Ao fazer a prévia da jornada do usuário, é possível visualizar os resultados das etapas personalizadas de postergação usando variáveis de contexto e qualquer comparação de público, decisão ou etapa da jornada de ação que corresponda aos usuários com qualquer variável de contexto.

Se a variável de contexto for válida, você poderá fazer referência a ela em todo o seu Canva. No entanto, se a variável de contexto não tiver sido criada corretamente, as etapas futuras do Canva também não serão executadas corretamente. Por exemplo, se você criar uma etapa de Contexto para atribuir aos usuários um horário de compromisso e definir o valor do horário de compromisso como uma data passada, o e-mail de lembrete na etapa de Mensagem não será enviado.

## Conversão de strings de Connected Content em JSON

Ao fazer uma [chamada de Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) em uma etapa do Context, o JSON retornado da chamada é avaliado como um tipo de dados string para fins de consistência e prevenção de erros. Se você quiser converter essa string em JSON, converta-a usando `as_json_string`. Por exemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Padronização da consistência do fuso horário

Embora a maioria das propriedades de eventos que usam o tipo de carimbo de data/hora já esteja em UTC no Canva, há algumas exceções. Com a adição do Canvas Context, todas as propriedades padrão de eventos de registro de data e hora em Canvas baseadas em ações estão em UTC. Essa alteração faz parte de um esforço mais amplo para garantir uma experiência mais previsível e consistente ao editar etapas e mensagens do Canva. Note que essa alteração afeta todos os Canvas baseados em ações, independentemente de o Canvas específico estar usando uma etapa do Context ou não.

{% alert important %}
Em todas as circunstâncias, recomendamos enfaticamente o uso dos [filtros Liquid time_zone ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) para que os registros de data e hora sejam representados no fuso horário desejado. Você pode consultar esta [pergunta frequente](#faq-example) para obter um exemplo.
{% endalert %}

## Solução de problemas

### Variáveis de contexto inválidas

Uma variável de contexto é considerada inválida quando:

- Uma chamada para um Connected Content incorporado falha.
- A expressão Liquid em tempo de execução retorna um valor que não corresponde ao tipo de dados ou que está vazio (nulo).

Por exemplo, se o tipo de dados da variável de contexto for **Número**, mas a expressão Liquid retornar uma string, ela será inválida.

Nessas circunstâncias:
- O usuário avança para a próxima etapa.
- A análise de dados da etapa do canva considera isso como _Não atualizado_.

Ao solucionar problemas, monitore a métrica _Not Updated_ para verificar se sua variável de contexto está sendo atualizada corretamente. Se a variável de contexto for inválida, seus usuários poderão continuar no Canva após a etapa do Context, mas talvez não se qualifiquem para as etapas posteriores.

Consulte [Tipos de dados]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) para ver os exemplos de configurações para cada tipo de dados.

### Postergação no envio de conteúdo conectado

Quando o Connected Content falha em uma etapa do Context, os usuários bem-sucedidos avançam imediatamente para a próxima etapa, enquanto os usuários que falharam são tentados novamente, separadamente. Isso significa que um lote não espera que todos os usuários sejam bem-sucedidos antes de avançar - os usuários bem-sucedidos avançam assim que a chamada do Connected Content é concluída.

**Comportamento de repetição**: As etapas de contexto (e todas as etapas do Canva) usam mecanismos de repetição específicos do Canva, e não o comportamento padrão de repetição do Connected Content. Se uma chamada de Connected Content falhar, o Braze tentará novamente a etapa aproximadamente 13 vezes com backoff exponencial. Se todas as tentativas falharem, o usuário sairá do Canva.

**Nota**: A tag `:retry` usada no Connected Content padrão não se aplica às chamadas de Connected Content feitas nas etapas do Canva. As etapas do canva têm sua própria lógica de repetição otimizada para fluxos de trabalho do Canvas.

**Tempo de processamento**: O tempo necessário para processar todos os usuários em uma etapa do Contexto depende de:
- O número de usuários que entram na etapa
- Se o Connected Content é usado (e seu tempo de resposta)
- O tamanho do lote (padrão: 1.000 usuários por lote)

Se o seu endpoint Connected Content tiver limites de frequência, considere que as etapas do Context processam os usuários sequencialmente dentro de cada lote, o que ajuda a respeitar os limites de frequência naturalmente. No entanto, vários lotes são processados em paralelo, portanto, certifique-se de que seu endpoint possa lidar com solicitações simultâneas de vários lotes.

## Perguntas frequentes

### O que muda quando o Canva Context se torna disponível para todos?

Quando o Canva Context estiver disponível de forma geral, os seguintes detalhes se aplicam:

- Todos os registros de [data e]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) hora com um [tipo de data e hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) das [propriedades de eventos de gatilho]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) em Canvas baseados em ação estão em [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). 
- Essa alteração afeta todos os Canvas baseados em ações, independentemente de o Canvas específico estar usando uma etapa do Context ou não.

#### Qual é o motivo dessa mudança?

Essa alteração faz parte de um esforço mais amplo para criar uma experiência mais previsível e consistente ao editar etapas e mensagens do Canva.

#### Quando essa mudança entrará em vigor?

- Se estiver participando do acesso antecipado ao Canvas Context, essa alteração já foi aplicada. 
- Se não estiver participando do acesso antecipado ao Canvas Context, essa alteração será aplicada quando você participar do acesso antecipado ou quando o Canvas Context estiver disponível para todos.

#### Os Canvases disparados pela API ou programados são afetados por essa alteração?

Não.

#### Essa alteração afetará as propriedades de entrada do Canva?

Sim, isso afeta o `canvas_entry_properties` se o `canvas_entry_property` estiver sendo usado em um Canva baseado em ação e o tipo de propriedade for `time`. Em todas as circunstâncias, recomendamos o uso dos filtros Liquid `time_zone` para que os registros de data e hora sejam representados no fuso horário desejado.

Aqui está um exemplo de como fazer isso:

| Liquid na etapa de envio de mensagens | Resultado | Essa é a maneira de representar corretamente os fusos horários no Liquid? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Não |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Não
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Sim |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Qual é um exemplo prático de como o novo comportamento do carimbo de data/hora pode afetar minhas mensagens? {#faq-example}

Digamos que temos um Canva baseado em ação que tem o seguinte conteúdo em uma etapa do Message:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Isso resulta na seguinte mensagem: 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Como nenhum fuso horário é especificado usando Liquid, o registro de data e hora aqui está em UTC. 

Para especificar claramente um fuso horário, podemos usar filtros Liquid `time_zone` como este: 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Isso resulta na seguinte mensagem: 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Como o fuso horário da América/Los Angeles é especificado usando Liquid, o registro de data e hora aqui está em PST.

O fuso horário preferencial também pode ser enviado na carga útil das propriedades do evento e usado na lógica do Liquid:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### Como as variáveis de contexto diferem das propriedades de entrada do Canva?

Se estiver participando do acesso antecipado à etapa do contexto, as propriedades de entrada do Canva agora estão incluídas como variáveis de contexto do Canva. Isso significa que você pode enviar propriedades de entrada do Canvas usando a API do Braze e fazer referência a elas em outras etapas, de forma semelhante ao uso de uma variável de contexto com o snippet do Liquid.

### As variáveis podem fazer referência umas às outras em uma etapa do Context Singular?

Sim. Todas as variáveis em uma etapa de contexto são avaliadas em uma sequência, o que significa que você poderia ter as seguintes variáveis de contexto configuradas:

| Variável de contexto | Valor | Descrição |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | O tipo de cozinha favorito de um usuário. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | O código de desconto disponível para um usuário. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.promo_code}} "on delivery from your favorite" {{context.favorite_cuisine}} restaurants!"`{% endraw %} | Uma mensagem personalizada que combina as variáveis anteriores. Em uma etapa de mensagem, você pode usar o snippet Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} para fazer referência à variável de contexto e enviar uma mensagem personalizada a cada usuário. Você também pode usar uma etapa do Context para salvar o valor [do código promocional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) e modelá-lo em outras etapas em um Canva. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Isso também se aplica a várias etapas do contexto. Por exemplo, imagine esta sequência:
1. Uma etapa inicial do Context cria uma variável chamada `JobInfo` com o valor `job_title`.
2. Uma etapa de Mensagem faz referência a {% raw %}`{{context.${JobInfo}}}`{% endraw %} e exibe `job_title` para o usuário.
3. Posteriormente, uma etapa do Contexto atualiza a variável de contexto, alterando o valor de `JobInfo` para `job_description`.
4. Todas as etapas subsequentes que fazem referência a `JobInfo` agora usam o valor atualizado `job_description`.

As variáveis de contexto usam seu valor mais recente em todo o Canva, com cada atualização afetando todas as etapas seguintes que fazem referência a essa variável.

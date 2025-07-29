---
nav_title: Contexto 
article_title: Contexto 
alias: /context/
page_order: 1.5
page_type: reference
description: "Este artigo de referência aborda como criar e usar etapas de contexto em seu Canva."
tool: Canvas

---

# Contexto

> As etapas de contexto permitem criar e atualizar uma ou mais variáveis para um usuário à medida que ele se move pelo Canva. Por exemplo, se você tiver um Canva que gerencia descontos sazonais, poderá usar uma variável de contexto para armazenar um código de desconto diferente cada vez que um usuário entrar no Canvas.

{% alert important %}
As etapas de contexto estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Como funciona?

![Uma etapa de contexto como a primeira etapa de um Canva.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

As etapas do contexto permitem criar e usar dados temporários durante a jornada de um usuário em um Canva específico. Esses dados existem somente dentro dessa jornada do Canvas e não persistem em diferentes Canvas ou fora da sessão.

Dentro dessa estrutura, cada etapa do Context pode definir várias variáveis de contexto - dados temporários que ativam a personalização de postergações, o segmento de usuários dinamicamente e o enriquecimento do envio de mensagens sem alterar permanentemente as informações do perfil do usuário.

Por exemplo, se você estiver gerenciando reservas de voos, poderá criar uma variável de contexto para o horário de voo programado de cada usuário. Em seguida, é possível definir postergações relativas ao horário de voo de cada usuário e enviar lembretes personalizados a partir da mesma tela.

Você pode definir variáveis de contexto de duas maneiras:

- **Na entrada do canva:** Quando os usuários entram em um Canva, os dados do evento ou do disparo da API podem preencher automaticamente as variáveis de contexto.
- **Em uma etapa do Contexto:** Você pode definir ou atualizar as variáveis de contexto manualmente dentro do Canva, adicionando uma etapa do Context.

Cada variável de contexto inclui:

- Um nome (como `flight_time` ou `subscription_renewal_date`)
- Um [tipo de dados](#context-variable-types) (como número, string, hora ou matriz)
- Um valor que você atribui usando o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou por meio da ferramenta **Adicionar personalização**.

Quando definida, você pode usar uma variável de contexto em todo o Canva fazendo referência a ela no seguinte formato: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Por exemplo,
{% raw %}`{{context.${flight_time}}}{% endraw %}` poderia retornar o tempo de voo programado do usuário.

Cada vez que um usuário entrar no Canva, mesmo que já tenha entrado antes, as variáveis de contexto serão redefinidas com base nos dados de entrada mais recentes e na configuração do Canvas. Isso permite que as jornadas permaneçam personalizadas e precisas, mesmo para usuários com várias entradas.

## Criando uma etapa de contexto

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
5. (Opcional) Para variáveis adicionais, selecione **Add Context variable (Adicionar variável de contexto** ) e repita as etapas 1 a 4.
6. Quando terminar, selecione **Concluído**.

Agora, é possível usar sua variável de contexto em qualquer lugar que use o Liquid, como nas etapas de Mensagem e Atualização do usuário, selecionando **Adicionar personalização**. Para obter um passo a passo completo, consulte [Uso de variáveis de contexto](#using-context-variables).

### Etapa 3: Teste as jornadas do usuário (opcional)

Se a variável de contexto for válida, você poderá fazer referência a ela em todo o seu Canva. No entanto, se a variável de contexto não tiver sido criada corretamente, as etapas futuras do Canva também não serão executadas corretamente. Recomendamos testar e [fazer uma prévia das jornadas dos usuários]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) para garantir que as mensagens sejam enviadas ao público certo. Fique atento aos cenários comuns que criam [variáveis de contexto inválidas](#troubleshooting).

Por exemplo, se você criar uma etapa de Contexto para atribuir aos usuários um horário de compromisso, mas definir o valor do horário de compromisso como uma data passada, o e-mail de lembrete criado na etapa de Mensagem nunca será enviado. 

## Tipos de dados de variáveis de contexto {#context-variable-types}

As variáveis de contexto que são criadas ou atualizadas na etapa podem ser atribuídas aos seguintes tipos de dados.

{% alert note %}
As variáveis de contexto têm os mesmos formatos esperados para os tipos de dados que os [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format), mas as variáveis de contexto não são compatíveis com objetos aninhados.
{% endalert %}

| Tipo de dados | Exemplo de nome de variável | Exemplo de valor |
|---|---|---|
|Booleano| programa de fidelidade |{% raw %}<code>true</code>{% endraw %}| 
|Número| pontuação de crédito |{% raw %}<code>740{% endraw %}|
|String| nome_do_produto |{% raw %}<code>green_tea</code>{% endraw %} |
|Vetor| produtos favoritos|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Horário| last_purchase_date (data da última compra)|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objeto (achatado) | perfil_do_usuário|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Uso de variáveis de contexto {#using-context-variables}

Por exemplo, digamos que você queira notificar os passageiros sobre o acesso à sala VIP antes do próximo voo. Essa mensagem deve ser enviada apenas aos passageiros que compraram um bilhete de primeira classe. Uma variável de contexto é uma maneira flexível de rastrear essas informações.

Os usuários entrarão no Canva quando comprarem uma passagem aérea. Para determinar a elegibilidade de acesso ao lounge, criaremos uma variável de contexto chamada `lounge_access_granted` em uma etapa de Contexto e, em seguida, faremos referência a essa variável de contexto nas etapas subsequentes da jornada do usuário.

![Variável de contexto configurada para rastrear se um passageiro se qualifica para o acesso à sala VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Nesta etapa do Contexto, usaremos o site {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} para determinar se o tipo de voo que eles compraram é `first_class`.

Em seguida, criaremos uma etapa de mensagens para direcionamento aos usuários onde {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} é `true`. Essa mensagem será uma notificação por push que inclui informações personalizadas sobre o lounge. Com base nessa variável de contexto, os passageiros elegíveis receberão as mensagens relevantes antes de seu voo.

- Os passageiros de bilhetes de primeira classe receberão: "Aproveite o acesso exclusivo à sala VIP!"
- Os passageiros das classes econômica e executiva receberão: "Faça upgrade de seu voo para ter acesso exclusivo à sala VIP."

![Uma etapa de mensagens com diferentes mensagens a serem enviadas, dependendo do tipo de passagem aérea comprada.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
É possível adicionar [opções de postergação personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) com as informações da etapa Contexto, o que significa que você pode selecionar a variável que posterga os usuários.
{% endalert %}

## Conversão de strings de Connected Content em JSON

Ao fazer uma [chamada de Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) em uma etapa do Context, o JSON retornado da chamada será avaliado como um tipo de dados string para fins de consistência e prevenção de erros. Se você quiser converter essa string em JSON, converta-a usando `as_json_string`. Por exemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Solução de problemas {#troubleshooting}

### Variáveis de contexto inválidas

Uma variável de contexto é considerada inválida quando:
- Uma chamada para um Connected Content incorporado falha.
- A expressão Liquid em tempo de execução retorna um valor que não corresponde ao tipo de dados ou que está vazio (nulo).

Por exemplo, se o tipo de dados da variável de contexto for **Número**, mas a expressão Liquid retornar uma string, ela será inválida.

Nessas circunstâncias: 
- O usuário avançará para a próxima etapa. 
- A análise de dados da etapa do canva contará isso como _Não atualizado_.

Ao solucionar problemas, monitore a métrica _Not Updated_ para verificar se sua variável de contexto está sendo atualizada corretamente. Se a variável de contexto for inválida, os usuários poderão continuar no Canva após a etapa do Context, mas talvez não se qualifiquem para as etapas posteriores.

Consulte [Tipos de dados variáveis de contexto](#context-variable-types) para ver os exemplos de configuração de cada tipo de dados.

## Perguntas frequentes

### Como as variáveis de contexto diferem das propriedades de entrada do Canva?

Se estiver participando do acesso antecipado à etapa do contexto, as propriedades de entrada do Canva agora estão incluídas como variáveis de contexto do Canva. Isso significa que você pode enviar propriedades de entrada do Canvas usando a API do Braze e fazer referência a elas em outras etapas, de forma semelhante ao uso de uma variável de contexto com o snippet do Liquid.

### As variáveis podem fazer referência umas às outras em uma etapa singular do Context?

Sim. Todas as variáveis em uma etapa do Contexto são avaliadas em uma sequência, o que significa que você poderia ter a seguinte configuração de variáveis de contexto:

| Variável de contexto | Valor | Descrição |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | O tipo de cozinha favorito de um usuário. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | O código de desconto disponível para um usuário. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{promo_code}} "on delivery from your favorite" {{favorite_cuisine}} restaurants!"`{% endraw %} | Uma mensagem personalizada que combina as variáveis anteriores. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Em uma etapa de mensagem, você pode usar o snippet Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} para fazer referência à variável de contexto e enviar uma mensagem personalizada a cada usuário.

Isso também se aplica a várias etapas do contexto. Por exemplo, imagine esta sequência:
1. Uma etapa inicial do Context cria uma variável chamada `JobInfo` com o valor `job_title`.
2. Uma etapa de Mensagem faz referência a {% raw %}`{{context.${JobInfo}}}`{% endraw %} e exibe `job_title` para o usuário.
3. Posteriormente, uma etapa do Contexto atualiza a variável de contexto, alterando o valor de `JobInfo` para `job_description`.
4. Todas as etapas subsequentes que fazem referência a `JobInfo` agora usarão o valor atualizado `job_description`.

As variáveis de contexto usam seu valor mais recente em todo o Canva, com cada atualização afetando todas as etapas seguintes que fazem referência a essa variável.



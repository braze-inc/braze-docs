---
nav_title: Biblioteca de casos de uso Liquid
article_title: Biblioteca de casos de uso do Liquid
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "Essa landing page contém exemplos de casos de uso do Liquid organizados por categoria, como aniversários, uso do app, contagens regressivas e muito mais."

---

{% api %}

## Aniversários e feriados

{% apitags %}
Aniversários e feriados
{% endapitags %}

- [Personalize o envio de mensagens com base no ano de aniversário do usuário](#anniversary-year)
- [Personalize o envio de mensagens com base na semana de aniversário de um usuário](#birthday-week)
- [Envie campanhas aos usuários no mês de aniversário deles](#birthday-month)
- [Evite o envio de mensagens em feriados importantes](#holiday-avoid)

### Personalize o envio de mensagens com base no ano de aniversário do usuário {#anniversary-year}

Este caso de uso mostra como calcular o aniversário do app de um usuário com base na data de inscrição inicial e exibir mensagens diferentes com base em quantos anos ele está comemorando.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %} 
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${registration_date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${registration_date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${registration_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %} 
{% if this_day == anniversary_day %} 
{% if anniversary_year == '2021' %}
Exactly one year ago today we met for the first time!

{% elsif anniversary_year == '2020' %}
Exactly two years ago today we met for the first time!

{% elsif anniversary_year == '2019' %}
Exactly three years ago today we met for the first time!

{% else %}
{% abort_message("Not same year") %}
{% endif %}

{% else %} 
{% abort_message("Not same day") %} 
{% endif %}

{% else %}
{% abort_message("Not same month") %}
{% endif %}
```
{% endraw %}

**Explicação:** Aqui, usamos a variável reservada `now` para modelar a data e a hora atuais no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601). Os filtros `%B` (mês como "maio") e `%d` (dia como "18") formatam o mês e o dia atuais. Em seguida, usamos os mesmos filtros de data e hora nos valores de `signup_date` para garantir que possamos comparar os dois valores usando tags e lógica condicionais.

Em seguida, repetimos mais três declarações de variáveis para obter `%B` e `%d` para `signup_date`, mas também adicionamos `%Y` (ano como "2021"). Isso transforma a data e a hora do site `signup_date` em apenas o ano. Saber o dia e o mês nos permite verificar se o aniversário do usuário é hoje, e saber o ano nos informa quantos anos se passaram, o que nos permite saber por quantos anos devemos parabenizá-lo!

{% alert tip %} Você pode criar tantas condições quantos forem os anos em que estiver coletando datas de inscrição. {% endalert %}  

### Personalize o envio de mensagens com base na semana de aniversário de um usuário {#birthday-week}

Este caso de uso mostra como encontrar a data de aniversário de um usuário, compará-la com a data atual e, em seguida, exibir mensagens especiais de aniversário antes, durante e depois da semana de aniversário.

{% raw %}
```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = ${date_of_birth}  | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Happy birthday for last week!
{% elsif {{birthday_week}} == {{this_week}} %}
Happy birthday for this week!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Happy birthday for next week!
{% else %}
No birthday for you!
{% endif %}
```
{% endraw %}

**Explicação:** Semelhante ao caso de uso do [ano de aniversário](#anniversary-year), aqui pegamos a variável reservada `now` e usamos o filtro `%W` (semana, como a semana 12 de 52 em um ano) para obter o número da semana do ano em que o aniversário do usuário se enquadra. Se a semana de aniversário do usuário coincidir com a semana atual, enviaremos uma mensagem para parabenizá-lo! 

Também incluímos declarações para `last_week` e `next_week` para personalizar ainda mais seu envio de mensagens.

### Envie campanhas aos usuários no mês de aniversário deles {#birthday-month}

Este caso de uso mostra como calcular o mês de aniversário de um usuário, verificar se o aniversário dele cai no mês atual e, em caso afirmativo, enviar uma mensagem especial.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
Message body 
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

**Explicação:** Semelhante ao caso de uso da [semana de aniversário](#birthday-week), exceto que aqui usamos o filtro `%B` (mês como "maio") para calcular quais usuários fazem aniversário neste mês. Uma aplicação em potencial poderia ser a abordagem de usuários aniversariantes em um e-mail mensal.

### Evite o envio de mensagens em feriados importantes {#holiday-avoid}

Esse caso de uso mostra como enviar mensagens durante o período de férias, evitando os dias de feriados importantes, quando o engajamento provavelmente será baixo.

{% raw %}
```liquid
{% assign today = 'now' | date: '%Y-%m-%d' %}
{% if today == "2023-12-24" or today == "2023-12-25" or today == "2023-12-26" %}
{% abort_message %}
{% else %}
Message if today isn't one of the provided holidays.
{% endif %}
```
{% endraw %}

**Explicação:** Aqui atribuímos o termo `today` à variável reservada `now` (a data e a hora atuais), usando os filtros `%Y` (ano como "2023"), `%m` (mês como "12") e `%d` (dia como "25") para formatar a data. Em seguida, executamos nossa instrução condicional para dizer que, se a variável `today` corresponder aos dias de feriado de sua escolha, a mensagem será abortada. 

O exemplo fornecido usa a véspera de Natal, o dia de Natal e o Boxing Day (o dia após o Natal).

{% endapi %}

{% api %}

## Uso do app

{% apitags %}
Uso do app
{% endapitags %}

- [Envio de mensagens no idioma do usuário se ele tiver registrado uma sessão](#app-session-language)
- [Personalize o envio de mensagens com base na última vez que o usuário abriu o app](#app-last-opened)
- [Mostrar uma mensagem diferente se um usuário tiver usado o app pela última vez há menos de três dias](#app-last-opened-less-than)

### Envio de mensagens no idioma do usuário se ele não tiver registrado uma sessão {#app-session-language}

Esse caso de uso verifica se um usuário registrou uma sessão e, caso contrário, inclui a lógica para exibir uma mensagem com base no idioma coletado manualmente por meio de um atributo personalizado, se houver. Se não houver informações de idioma vinculadas à conta, a mensagem será exibida no idioma padrão. Se um usuário tiver registrado uma sessão, ele extrairá todas as informações de idioma vinculadas ao usuário e exibirá a mensagem apropriada. 

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message in English based on custom attribute
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message in French based on custom attribute
{% else %}
Does not have language - Default language
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message in English based on Language
{% elsif ${language} == 'fr' %}
Message in French based on Language
{% else %}
Has language - Default language
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**Explicação:** Aqui, estamos usando dois comandos `if` agrupados, aninhados. A primeira instrução `if` verifica se o usuário iniciou uma sessão, verificando se `last_used_app_date` é `nil`. Isso ocorre porque o `{{${language}}}` é coletado automaticamente pelo SDK quando um usuário registra uma sessão. Se o usuário não tiver registrado uma sessão, ainda não teremos o idioma dele, portanto, isso verifica se algum atributo personalizado relacionado ao idioma foi salvo e, com base nessas informações, exibirá uma mensagem nesse idioma, se possível.
{% endraw %}

A segunda atribuição `if` apenas verifica o atributo padrão (default) porque o usuário não tem `nil` para o `last_used_app_date`, o que significa que ele registrou uma sessão e nós temos o idioma dele.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) é uma variável reservada que é retornada quando o código Liquid não tem resultados. `Nil` é tratado como `false` em um bloco `if`.
{% endalert %}

### Personalize o envio de mensagens com base na última vez que o usuário abriu o app {#app-last-opened}

Esse caso de uso calcula a última vez que um usuário abriu seu app e exibirá uma mensagem personalizada diferente, dependendo do período de tempo.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### Mostrar uma mensagem diferente se um usuário tiver usado o app pela última vez há menos de três dias {#app-last-opened-less-than}

Esse caso de uso calcula há quanto tempo um usuário usou seu app e, dependendo do tempo, exibirá uma mensagem personalizada diferente.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message for a recently active user
{% else %}
Message for a less active user
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Contagem regressiva

{% apitags %}
Contagem regressiva
{% endapitags %}

- [Adicionar X dias à data de hoje](#countdown-add-x-days)
- [Calcular uma contagem regressiva a partir de um ponto definido no tempo](#countdown-difference-days)
- [Criar uma contagem regressiva para datas e prioridades específicas de remessa](#countdown-shipping-options)
- [Criar uma contagem regressiva em dias](#countdown-days)
- [Crie uma contagem regressiva de dias, horas e minutos](#countdown-dynamic)
- [Mostrar quantos dias faltam para uma determinada data](#countdown-future-date)
- [Exibir quantos dias faltam para a chegada de um atributo personalizado de data](#countdown-custom-date-attribute)
- [Exibir o tempo restante e interromper a mensagem se restar apenas X tempo](#countdown-abort-window)
- [Mensagem no app para enviar X dias antes do término da associação do usuário](#countdown-membership-expiry)
- [Personalize as mensagens no app com base na data e no idioma do usuário](#countdown-personalize-language)
- [Modelo na data de 30 dias a partir de agora, formatado como mês e dia](#countdown-template-date)

### Adicionar x dias à data de hoje {#countdown-add-x-days}

Esse caso de uso adiciona um número específico de dias à data atual para fazer referência e adicionar mensagens. Por exemplo, talvez você queira enviar uma mensagem no meio da semana que mostre os eventos na área para o fim de semana.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

O valor `plus` sempre estará em segundos, portanto, terminamos com o filtro `%F` para converter os segundos em dias.

{% alert important %}
Talvez queira incluir um URL ou deep linking para uma lista de eventos em sua mensagem para que possa enviar o usuário para uma lista de ações que acontecerão no futuro.
{% endalert %}

### Calcular uma contagem regressiva a partir de um ponto definido no tempo {#countdown-difference-days}

Esse caso de uso calcula a diferença em dias entre uma data específica e a data atual. Essa diferença pode ser usada para exibir uma contagem regressiva para seus usuários.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### Criar uma contagem regressiva para datas e prioridades específicas de remessa {#countdown-shipping-options}

Esse caso de uso captura diferentes opções de envio, calcula o tempo que levaria para receber e exibe mensagens incentivando os usuários a comprar a tempo de receber o pacote em uma determinada data.

{% raw %}
```liquid
{% assign standard_shipping_start = "2023-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2023-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2023-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2023-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping, so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
There is {{difference_s_days}} day left to order with standard shipping, so your order gets here on time for Christmas Eve!

{% else %}
There are {{difference_s_days}} days left to order with standard shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
There is {{difference_e_days}} day left to order with express shipping, so your order gets here on time for Christmas Eve!
{% else %}
There are {{difference_e_days}} days left to order with express shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
This is the last day for overnight shipping so your order gets here on time for Christmas Eve!
{% else %}
{% abort_message("Unable to order and ship in time") %}
{% endif %}
```
{% endraw %}

### Criar uma contagem regressiva em dias {#countdown-days}

Esse caso de uso calcula o tempo restante entre um evento específico e a data atual e exibe quantos dias faltam para o evento.

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Your order will arrive in {{ difference_days }} days!
```
{% endraw %}

{% alert important %}
Você precisará de um campo de atributo personalizado com um valor `date`.
{% endalert %}

### Crie uma contagem regressiva de dias, horas e minutos {#countdown-dynamic}

Esse caso de uso calcula o tempo restante entre um evento específico e a data atual. Dependendo do tempo restante até o evento, ele alterará o valor da mensagem (dias, horas, minutos) para exibir diferentes mensagens personalizadas.

Por exemplo, se faltarem dois dias para a chegada do pedido de um cliente, você pode dizer: "Seu pedido chegará em 2 dias". Por outro lado, se houver menos de um dia, você pode alterar para "Seu pedido chegará em 17 horas".

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left till your order arrives!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left till your order arrives!
{% else %}
You have {{difference_days}} days left till your order arrives!
{% endif %}
```
{% endraw %}

{% alert important %}
Você precisará de um campo de atributo personalizado com um valor `date`. Você também precisará definir limites de tempo para que a hora seja exibida em dias, horas e minutos.
{% endalert %}

### Mostrar quantos dias faltam para uma determinada data {#countdown-future-date}

Esse caso de uso calcula a diferença entre a data atual e a data do evento futuro e exibe uma mensagem notando quantos dias faltam para o evento.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### Exibir quantos dias faltam para a chegada de um atributo personalizado de data {#countdown-custom-date-attribute}

Esse caso de uso calcula a diferença em dias entre a data atual e a futura e exibe uma mensagem se a diferença corresponder a um número definido.

Neste exemplo, um usuário receberá uma mensagem dentro de dois dias do atributo personalizado de data. Caso contrário, a mensagem não será enviada.

{% raw %}
```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Exibir o tempo restante e interromper a mensagem se restar apenas x tempo {#countdown-abort-window}

Esse caso de uso calculará quanto tempo falta para uma determinada data e, dependendo da duração (ignorando o envio de mensagens se a data for muito próxima), exibirá diferentes mensagens personalizadas. 

Por exemplo, "Você tem x horas restantes para comprar sua passagem para Londres", mas não envie a mensagem se faltarem duas horas para o horário do voo para Londres.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours!
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now!
{% endif %}
```
{% endraw %}

{% alert important %} Você precisará de uma propriedade de evento personalizado. {% endalert %}

### Mensagem no app para enviar x dias antes do término da associação dos usuários {#countdown-membership-expiry}

Esse caso de uso captura a data de expiração de sua associação, calcula quanto tempo falta para o vencimento e exibe mensagens diferentes com base no tempo que falta para o vencimento de sua associação.

{% raw %}
```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days > 2 and difference_days <= 4 %}
HURRY! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days == 2 %}
LAST CHANCE! You have {{difference_days}} days left in your trial. Make sure you upgrade!

{% else %}
You have few days left in your trial. Make sure to upgrade!
{% endif %}
```
{% endraw %}

### Personalize as mensagens no app com base na data e no idioma dos usuários {#countdown-personalize-language}

Esse caso de uso calcula uma contagem regressiva para um evento e, com base na configuração de idioma do usuário, exibirá a contagem regressiva no idioma dele.

Por exemplo, você pode enviar uma série de mensagens de upsell aos usuários uma vez por mês para informá-los por quanto tempo uma oferta ainda é válida com quatro mensagens no app:

- Inicial
- 2 dias restantes
- 1 dia restante
- Último dia

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
The offer is valid until 16.04.

{% else %}
The offer is valid until 16.04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Hi, the offer is only valid today.
{% endif %}

{% else %}
{% abort_message("Calculation failed") %}
{% endif %}
```
{% endraw %}

{% alert important %}
Você precisará atribuir um valor `date` e incluir a lógica de abortar se a data fornecida estiver fora do intervalo de datas. Para cálculos de dias exatos, a data final atribuída deve incluir 23:59:59.
{% endalert %}

### Modelo na data de 30 dias a partir de agora, formatado como mês e dia {#countdown-template-date}

Esse caso de uso exibirá a data de 30 dias a partir de agora para uso no envio de mensagens.

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign thirty_days = today | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## Atributo personalizado

{% apitags %}
Atributo personalizado
{% endapitags %}

- [Personalize uma mensagem com base em atributos personalizados correspondentes](#attribute-matching)
- [Subtraia dois atributos personalizados para exibir a diferença como um valor monetário](#attribute-monetary-difference)
- [Faça referência ao nome de um usuário se o nome completo estiver armazenado no campo first_name ](#attribute-first-name)

### Personalize uma mensagem com base em atributos personalizados correspondentes {#attribute-matching}

Esse caso de uso verifica se um usuário tem atributos personalizados específicos e, se tiver, exibirá mensagens personalizadas diferentes. 

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
The ground is very hard. The dirt road goes East.
{% elsif custom_attribute.${hasShovel} == true %}
The dirt road goes East.
{% elsif custom_attribute.${VisitToStart} > 0 %}
The dirt road goes East.
The shovel here.
{% else %}
You are at a dead-end of a dirt road. The road goes to the east. In the distance, you can see that it will eventually fork off. The trees here are very tall royal palms, and they are spaced equidistant from each other.
There is a shovel here.
{% endif %}
```
{% endraw %}

### Subtraia dois atributos personalizados para exibir a diferença como um valor monetário {#attribute-monetary-difference}

Esse caso de uso captura dois atributos personalizados monetários e, em seguida, calcula e exibe a diferença para que os usuários saibam quanto falta para atingir a meta.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### Faça referência ao nome de um usuário se o nome completo estiver armazenado no campo first_name  {#attribute-first-name}

Esse caso de uso captura o primeiro nome do usuário (se o primeiro e o último nome estiverem armazenados em um único campo) e usa esse primeiro nome para exibir uma mensagem de boas-vindas.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**Explicação:** O filtro `split` transforma a string mantida em `{{${first_name}}}` em uma matriz. Ao usar `{{name[0]}}`, fazemos referência apenas ao primeiro item da matriz, que é o nome do usuário. 

{% endraw %}
{% endapi %}

{% api %}

## Evento personalizado

{% apitags %}
Evento personalizado
{% endapitags %}

- [Abortar a notificação por push se um evento personalizado estiver dentro de duas horas](#event-abort-push)
- [Envie uma campanha sempre que um usuário realizar um evento personalizado três vezes](#event-three-times)
- [Envie uma mensagem aos usuários que compraram apenas em uma categoria](#event-purchased-one-category)
- [Rastrear quantas vezes um evento personalizado ocorreu no último mês](#track)


### Abortar a notificação por push se um evento personalizado estiver dentro de duas horas {#event-abort-push}

Esse caso de uso calcula o tempo até um evento e, dependendo do tempo restante, exibirá diferentes mensagens personalizadas.

Por exemplo, você pode querer impedir que um push seja enviado se uma propriedade de evento personalizado for aprovada nas próximas duas horas. Este exemplo usa o cenário de um carrinho abandonado para uma passagem de trem.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now
{% endif %}
```
{% endraw %}

### Envie uma campanha sempre que um usuário realizar um evento personalizado três vezes {#event-three-times}

Esse caso de uso verifica se um usuário realizou um evento personalizado três vezes e, em caso afirmativo, exibirá uma mensagem ou enviará uma campanha. 

{% raw %}
```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message("Error calculating cadence") %}
{% elsif cadence != 0 %}
{% abort_message("Skip message") %}
{% endif %}
Did you forget something in your shopping cart?
```
{% endraw %}

{% alert important %} Você deve ter uma propriedade de evento da contagem de eventos personalizados ou usar um webhook em seu endpoint do Braze. Isso serve para incrementar um atributo personalizado (`example_event_count`) sempre que o usuário realizar o evento. Este exemplo usa uma cadência de três (1, 4, 7, 10, etc.). Para iniciar a cadência a partir do zero (0, 3, 6, 9, etc.), remova `minus: 1`.
{% endalert %}

### Envie uma mensagem aos usuários que compraram apenas em uma categoria {#event-purchased-one-category}

Esse caso de uso captura uma lista das categorias das quais um usuário comprou e, se houver apenas uma categoria de compra, ele exibirá uma mensagem.

{% raw %}
```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1%}
{{uniq_cat}}
{% else %}
{% abort_message("Purchase category doesn't exist") %}
{% endif %}
```
{% endraw %}

### Rastrear quantas vezes um evento personalizado ocorreu no último mês {#track}

Esse caso de uso calcula o número de vezes que um evento personalizado foi registrado entre o dia 1º do mês atual e o mês anterior. Em seguida, é possível executar uma chamada users/track para atualizar e armazenar esse valor como um atributo personalizado. Note que essa campanha precisaria ser executada por dois meses consecutivos para que os dados mensais pudessem ser usados.

{% raw %}
```liquid

{% capture body %}
{
 "braze_id": "{{${braze_id}}}",
 "fields_to_export": ["custom_events"]
}

{% endcapture %}

{% connected_content YOUR_BRAZE_ENDPOINT/users/export/ids
 :method post
  :headers { "Authorization": "Bearer YOUR_API_KEY" }
  :body {{body}}
 :content_type application/json
 :save response
  :retry %}

{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} The following custom event name will need to be amended for the target custom event. {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom_event.name}}: {{custom_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev_month_count = {{custom_attribute.${projects_exported_prev_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = "now" | date: "%s" %}
{% assign yesterday = {{now}} | minus: 86400 %}
{% assign previous_month = {{yesterday}} | date: "%B" %}
{% assign previous_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}The Custom Event name that is being tracked will be needed to be amended for the target Custom Event in the Attribute Name below. {% endcomment %}
```

```json
"attributes": [
  {
    "external_id":"{{${user_id}}}",
       "projects_exported_{{formatted_month}}_{{previous_year}}": "{{latest_count}}"
  }
]
```

{% endraw %}

{% endapi %}

{% api %}

## Idioma

{% apitags %}
Idioma
{% endapitags %}

- [Exibir os nomes dos meses em um idioma diferente](#language-display-month)
- [Exibir uma imagem com base no idioma do usuário](#language-image-display)
- [Personalize o envio de mensagens com base no dia da semana e no idioma do usuário](#language-personalize-message)

### Exibir os nomes dos meses em um idioma diferente {#language-display-month}

Esse caso de uso exibirá a data, o mês e o ano atuais, com o mês em um idioma diferente. O exemplo fornecido usa o sueco.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month)) == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month)) == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month)) == 'April' %}
{{day}} April {{year}}
{% elsif {{month)) == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month)) == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month)) == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month)) == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month)) == 'September' %}
{{day}} September {{year}}
{% elsif {{month)) == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month)) == 'November' %}
{{day}} November {{year}}
{% elsif {{month)) == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### Exibir uma imagem com base no idioma do usuário {#language-image-display}

Esse caso de uso exibirá uma imagem com base no idioma do usuário. Note que esse caso de uso só foi testado com imagens feitas upload na biblioteca de mídia da Braze.

{% raw %}
```liquid
{% if ${language} == 'en' %}
English image URL (for example, https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137)
{% elsif ${language} == 'ru' %}
Russian image URL
{% elsif ${language} == 'es' %}
Spanish image URL
{% else %}
Fallback image URL
{% endif %}
```
{% endraw %}

### Personalize o envio de mensagens com base no dia da semana e no idioma do usuário {#language-personalize-message}

Esse caso de uso verifica o dia da semana atual e, com base no dia, se o idioma do usuário estiver definido como uma das opções de idioma fornecidas, será exibida uma mensagem específica no idioma dele.

O exemplo fornecido para na terça-feira, mas pode ser repetido para cada dia da semana.

{% raw %}
```liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Purchase today and take your language learning to the next level. 🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
It's Monday, but the language doesn't match 
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
Don't forget to unlock the full version of your language. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

{% else %}
tuesday default
{% endif %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Diversos

{% apitags %}
Diversos
{% endapitags %}

- [Evite enviar e-mails para clientes que bloquearam e-mails de marketing](#misc-avoid-blocked-emails)
- [Use o estado da inscrição de um cliente para personalizar o conteúdo das mensagens](#misc-personalize-content)
- [Colocar a primeira letra de cada palavra em maiúscula em uma string](#misc-capitalize-words-string)
- [Comparar o valor do atributo personalizado com uma matriz](#misc-compare-array)
- [Criar um lembrete de evento futuro](#misc-event-reminder)
- [Encontre uma string em uma matriz](#misc-string-in-array)
- [Encontre o maior valor em uma matriz](#misc-largest-value)
- [Encontre o menor valor em uma matriz](#misc-smallest-value)
- [Consultar o final de uma string](#misc-query-end-of-string)
- [Consulta de valores em uma matriz de um atributo personalizado com várias combinações](#misc-query-array-values)
- [Formatar uma string em um número de telefone](#phone-number)

### Evite enviar e-mails para clientes que bloquearam e-mails de marketing {#misc-avoid-blocked-emails}

Esse caso de uso usa uma lista de usuários bloqueados salvos em um bloco de conteúdo e verifica se esses usuários bloqueados não são comunicados ou direcionados em campanhas ou telas futuras.

{% alert important %}
Para usar esse Liquid, primeiro salve a lista de e-mails bloqueados em um bloco de conteúdo. A lista não deve ter espaços ou caracteres adicionais inseridos entre os endereços de e-mail (por exemplo, `test@braze.com,abc@braze.com`).
{% endalert %}

{% raw %}
```liquid
{% assign blocked_emails = {{content_blocks.${BlockedEmailList}}} | split: ',' %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message("Email is blocked") %}
    {% break %}
    {% endif %}
{% endfor %} 
Your message here!
```
{% endraw %}

**Explicação:** Aqui, verificamos se o e-mail do destinatário em potencial está nessa lista, consultando o bloco de conteúdo dos e-mails bloqueados. Se o e-mail for encontrado, a mensagem não será enviada.

{% alert note %}
Os blocos de conteúdo têm um limite de tamanho de 5 MB.
{% endalert %}

### Use o estado da inscrição de um cliente para personalizar o conteúdo das mensagens {#misc-personalize-content}

Esse caso de uso usa o estado da inscrição de um cliente para enviar conteúdo personalizado. Os clientes que se inscreveram em um grupo de inscrições específico receberão uma mensagem exclusiva para grupos de inscrições para e-mail.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### Colocar a primeira letra de cada palavra em maiúscula em uma string {#misc-capitalize-words-string}

Esse caso de uso pega uma string de palavras, divide-as em uma matriz e coloca a primeira letra de cada palavra em maiúscula.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**Explicação:** Aqui, atribuímos uma variável ao nosso atributo de string escolhido e usamos o filtro `split` para dividir a string em uma matriz. Em seguida, usamos a tag `for` para atribuir a variável `words` a cada um dos itens em nossa matriz recém-criada, antes de exibir essas palavras com o filtro `capitalize` e o filtro `append` para adicionar espaços entre cada um dos termos.

### Comparar o valor do atributo personalizado com uma matriz {#misc-compare-array}

Esse caso de uso pega uma lista de lojas favoritas, verifica se alguma das lojas favoritas de um usuário está nessa lista e, em caso afirmativo, exibe uma oferta especial dessas lojas.

{% raw %}
```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
Today's offer from {{store}}

{% break %}

{% else %}
{% abort_message("No attribute found") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} Essa sequência tem uma tag `break` na instrução condicional primária. Isso faz com que o loop seja interrompido quando uma correspondência é encontrada. Se quiser exibir muitas ou todas as correspondências, remova a tag `break`. {% endalert %}

### Criar um lembrete de evento futuro {#misc-event-reminder}

Esse caso de uso permite que os usuários configurem lembretes futuros com base em eventos personalizados. O cenário de exemplo permite que um usuário defina um lembrete para uma data de renovação da apólice que esteja a 26 dias ou mais de distância, em que os lembretes são enviados 26, 13, 7 ou 2 dias antes da data de renovação da apólice.

Com esse caso de uso, o seguinte deve ir no corpo de uma [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) ou etapa do Canva.

{% raw %}
```liquid
{% comment %}
Depending on how the reminder_capture property is passed to Braze, with/without a timestamp, the number of days could impact whether a user falls on either side of the 26/13/7/2-day windows.
Once users have been assigned to a Reminder journey/flow, they are then scheduled to enter a subsequent Canvas.
This 'Event Listener' can be used to split out users into different journeys based on the Custom Event properties sent to Braze.
{% endcomment %}

{% comment %}
When testing, make sure the campaign ID, campaign API endpoint, Canvas ID, Canvas API endpoint are entered correctly. In this example, the Canvas ID and Canvas API endpoint have been set up for sharing with the client. In practice, this can be testing using a campaign ID and Campaign API endpoint.
{% endcomment %}

{% comment %}
The following step calculates how much there is between today's date and the Reminder Date as 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
The following step checks if the time_to_reminder is more than 26 days away; if this is true, then the user is scheduled to enter the subsequent Canvas 26 days before the reminder_date.
The time is converted from 'seconds from 1970' to the appropriate Reminder Date in the required ISO 8601 format.
N.B. Additional time zones would need to be catered for by adding an additional API Schedule property of "in_local_time"
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: '%Y-%m-%dT%H:%M' }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 26 days away but more than 13 days away.
Users are scheduled to enter the journey on day 13.
{% endcomment %}

{% elsif 1123200 > {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 13 days away but more than seven days away.
Users are scheduled to enter the journey on day 7.
{% endcomment %}

{% elsif 604800 > {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than seven days away but more than two days away.
Users are scheduled to enter the journey on day 2.
{% endcomment %}

{% else {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %} 

Você precisará de um evento personalizado `reminder_capture`, e as propriedades do evento personalizado devem incluir, no mínimo:

- `reminder-id`: Identificador do evento personalizado
- `reminder_date`: Data de vencimento do lembrete enviada pelo usuário
- `message_personalisation_X`: Quaisquer propriedades necessárias para personalizar a mensagem no momento do envio

{% endalert %}

### Encontre uma string em uma matriz {#misc-string-in-array}

Esse caso de uso verifica se uma matriz de atributos personalizados contém uma string específica e, se existir, exibirá uma mensagem específica.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### Encontre o maior valor em uma matriz {#misc-largest-value}

Esse caso de uso calcula o valor mais alto em uma determinada matriz de atributos personalizados para usar no envio de mensagens ao usuário.

Por exemplo, você pode querer mostrar a um usuário qual é a pontuação máxima atual ou o lance mais alto em um item.

{% raw %}
```liquid
{% assign maxValue = 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```
{% endraw %}

{% alert important %}
Você deve usar um atributo personalizado que tenha um valor inteiro e faça parte de uma matriz (lista). {% endalert %}

### Encontre o menor valor em uma matriz {#misc-smallest-value}

Este caso de uso calcula o valor mais baixo em uma determinada matriz de atributos personalizados para usar no envio de mensagens ao usuário.

Por exemplo, você pode querer mostrar a um usuário qual é a pontuação mais baixa ou o item mais barato.

{% raw %}
```liquid
{% assign minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```
{% endraw %}

{% alert important %} Você deve usar um atributo personalizado que tenha um valor inteiro e faça parte de uma matriz (lista). {% endalert %}

### Consultar o final de uma string {#misc-query-end-of-string}

Esse caso de uso consulta o final de uma string para uso no envio de mensagens.

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}} | first } %}
{% assign marketplace = {{{{interest}} | split: "" | reverse | join: "" |  truncate: 4, ""}} %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Consulta de valores em uma matriz de um atributo personalizado com várias combinações {#misc-query-array-values}

Esse caso de uso pega uma lista de programas que expiram em breve, verifica se algum dos programas favoritos do usuário está nessa lista e, em caso afirmativo, exibe uma mensagem notificando o usuário de que eles expirarão em breve.

{% raw %} 
```liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assign new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

All episodes of {{new_shows_clean | join: ', ' }} expire on 9/8 - watch them now before they're gone!

{% else %}
{% abort_message("Not found") %}
{% endif %}
```
{% endraw %}

{% alert important %} Você precisará encontrar correspondências entre as matrizes primeiro e, em seguida, criar uma lógica no final para dividir as correspondências. {% endalert %}

### Formatar uma string em um número de telefone {#phone-number}

Este caso de uso mostra como indexar o campo de perfil de usuário `phone_number` (por padrão, formatado como uma string de números inteiros) e reformatá-lo com base nos padrões locais de número de telefone. Por exemplo, 1234567890 para (123)-456-7890.

{% raw %} 
```liquid
{% assign phone = {{${phone_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
```
{% endraw %}

{% endapi %}

{% api %}

## Direcionamento de plataforma

{% apitags %}
Direcionamento de plataforma
{% endapitags %}

- [Diferenciar a cópia por sistema operacional do dispositivo](#platform-device-os)
- [Direcionamento apenas para uma plataforma específica](#platform-target)
- [Direcionamento apenas para dispositivos iOS com uma versão específica do sistema operacional](#platform-target-ios-version)
- [Direcionamento apenas para navegadores da Web](#platform-target-web)
- [Direcionamento para uma operadora de celular específica](#platform-target-carrier)

### Diferenciar a cópia por sistema operacional do dispositivo {#platform-device-os}

Esse caso de uso verifica em que plataforma o usuário está e, dependendo da plataforma, exibirá envios de mensagens específicos.

Por exemplo, talvez você queira mostrar aos usuários de celular versões mais curtas do texto da mensagem, enquanto mostra aos outros usuários a versão normal e mais longa do texto. Também é possível mostrar aos usuários móveis determinadas mensagens relevantes para eles, mas que não seriam relevantes para os usuários da Internet. Por exemplo, o envio de mensagens para iOS pode falar sobre o Apple Pay, mas as mensagens para Android devem mencionar o Google Pay.

{% raw %}
```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else %}
This is the regular copy and much longer than the short version. 
{% endif %}
```
{% endraw %}

{% alert note %}
O Liquid diferencia maiúsculas de minúsculas, `targeted_device.${platform}` retorna o valor em letras minúsculas.
{% endalert %}

### Direcionamento apenas para uma plataforma específica {#platform-target}

Esse caso de uso capturará a plataforma do dispositivo do usuário e, dependendo da plataforma, exibirá uma mensagem.

Por exemplo, você pode querer enviar uma mensagem apenas para usuários do Android. Isso pode ser usado como uma alternativa à seleção de um app na ferramenta Segmentação.

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %} 

This is a message for an Android user! 

{% else %}  
{% abort_message %} 
{% endif %}
```
{% endraw %}

### Direcionamento apenas para dispositivos com uma versão específica do sistema operacional {#platform-target-ios-version}

Esse caso de uso verifica se a versão do sistema operacional de um usuário está dentro de um determinado conjunto de versões e, se estiver, exibirá uma mensagem específica.

O exemplo usado envia um aviso aos usuários de um sistema operacional versão 10.0 ou anterior de que o suporte ao sistema operacional do dispositivo do usuário está sendo descontinuado.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == "10.0.3" or {{targeted_device.${os}}} == "10.1" or {{targeted_device.${os}}} == "10.2" or {{targeted_device.${os}}} == "10.2.1" or {{targeted_device.${os}}} == "10.3" or {{targeted_device.${os}}} == "10.3.1" or {{targeted_device.${os}}} == "10.3.2" or {{targeted_device.${os}}} == "10.3.3" or {{targeted_device.${os}}} == "10.3.4" or {{targeted_device.${os}}} == "9.3.1" or {{targeted_device.${os}}} == "9.3.2" or {{targeted_device.${os}}} == "9.3.3" or {{targeted_device.${os}}} == "9.3.4" or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Direcionamento apenas para navegadores da Web {#platform-target-web}

Esse caso de uso verifica se o dispositivo de destino de um usuário é executado no Mac ou no Windows e, se for o caso, exibirá uma mensagem específica.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' or {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

O caso de uso a seguir verifica se um usuário da Internet está no iOS ou no Android e, se estiver, exibirá uma mensagem específica.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'iOS' and {{targeted_device.${platform}}} == 'web' %}

Content for iOS.

{% elsif {{targeted_device.${os}}} == 'android' and {{targeted_device.${platform}}} == 'web' %}

Content for Android.

{% else %}
{% abort_message %} 
{% endif %}
```
{% endraw %}

### Direcionamento para uma operadora de celular específica {#platform-target-carrier}

Esse caso de uso verifica se a operadora do dispositivo do usuário é a Verizon e, se for o caso, exibirá uma mensagem específica.

Para notificações por push e canais de envio de mensagens no app, você pode especificar a operadora do dispositivo no corpo da mensagem usando o Liquid. Se a operadora do dispositivo do destinatário não corresponder, a mensagem não será enviada.

{% raw %}
```liquid
{% if {targeted_device.${carrier}} contains "verizon" or {targeted_device.${carrier}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## SMS

{% apitags %}
SMS
{% endapitags %}

- [Responda com diferentes envios de mensagens com base na palavra-chave do SMS recebido](#sms-keyword-response)

### Responda com diferentes envios de mensagens com base na palavra-chave do SMS recebido {#sms-keyword-response}

Esse caso de uso incorpora o processamento dinâmico de palavras-chave de SMS para responder a mensagens de entrada específicas com diferentes cópias de mensagens. Por exemplo, você pode enviar respostas diferentes quando alguém envia a mensagem "START" (iniciar) ou "JOIN" (participar).

{% raw %}
```liquid
{% assign inbound_message = {{sms.${inbound_message_body}}} | downcase | strip %}
{% if inbound_message contains 'start' %}
Thanks for joining our SMS program! Make sure your account is up to date for the best deals!

{% elsif inbound_message contains 'join' %}
Thanks for joining our SMS program! Create an account to get the best deals!

{% else %}
Thanks for joining our SMS program!

{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Fusos horários

{% apitags %}
Fusos horários
{% endapitags %}

- [Personalize uma mensagem de acordo com o fuso horário do usuário](#personalize-timezone)
- [Anexar o fuso horário CST a um atributo personalizado](#time-append-cst)
- [Inserir um registro de data e hora](#time-insert-timestamp)
- [Enviar um push do Canva somente durante uma janela de tempo no fuso local do usuário](#time-canvas-window)
- [Envie uma campanha recorrente de mensagens no app entre uma janela de tempo no fuso local do usuário](#time-reocurring-iam-window)
- [Envio de mensagens diferentes nos dias úteis e nos finais de semana no fuso local do usuário](#time-weekdays-vs-weekends)
- [Envio de mensagens diferentes com base na hora do dia no fuso local do usuário](#time-of-day)

### Personalize uma mensagem de acordo com o fuso horário do usuário {#personalize-timezone}

Esse caso de uso exibe mensagens diferentes com base no fuso horário do usuário.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'xx' %}
Message for time zone xx.
{% elsif {{$time_zone}}} == 'yy' %}
Message for time zone yy.
{% else %}
{% abort_message("Invalid time zone") %}
{% endif %}
```
{% endraw %}

### Anexar o fuso horário CST a um atributo personalizado {#time-append-cst}

Esse caso de uso exibe um atributo personalizado de data em um determinado fuso horário.

Opção 1:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

Opção 2:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### Inserir um registro de data e hora {#time-insert-timestamp}

Esse caso de uso exibe uma mensagem que inclui um registro de data e hora em seu fuso horário atual.

O exemplo fornecido a seguir exibirá a data como AAAA-mm-dd HH:MM:SS, como 2021-05-03 10:41:04.

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### Enviar um push do Canva somente durante uma janela de tempo no fuso local do usuário {#time-canvas-window}

Esse caso de uso verifica a hora de um usuário em seu fuso local e, se estiver dentro de um horário definido, exibirá uma mensagem específica.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Here's a message that will send between 8 am and 8 pm!
```
{% endraw %}

### Envie uma campanha recorrente de mensagens no app entre uma janela de tempo no fuso local do usuário {#time-reoccurring-iam-window}

Esse caso de uso exibirá uma mensagem se a hora atual de um usuário estiver dentro de uma janela definida.

Por exemplo, o cenário a seguir permite que um usuário saiba que uma loja está fechada.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %} 
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Store's closed. Come back between 11 am and 9 pm!

{% else %} 
{% abort_message("Not sent because the store is open") %}
{% endif %}
```
{% endraw %}

### Envio de mensagens diferentes nos dias úteis e nos finais de semana no fuso local do usuário {#time-weekdays-vs-weekends}

Esse caso de uso verificará se o dia da semana atual de um usuário é sábado ou domingo e, dependendo do dia, exibirá mensagens diferentes.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
It's {{today}}, why don't you open the app for your transactions?

{% else %}
It's {{today}}, why don't you visit the store?
{% endif %}
```
{% endraw %}

### Envio de mensagens diferentes com base na hora do dia no fuso local do usuário {#time-of-day}

Esse caso de uso exibirá uma mensagem se a hora atual de um usuário estiver fora de uma janela definida.

Por exemplo, você pode querer informar um usuário sobre uma oportunidade sensível ao tempo que depende da hora do dia.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

{% alert note %} Isso é o oposto do [Horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/time_based_campaign/#time-based-functionalities-for-campaigns). {% endalert %}

{% endapi %}

{% api %}

## Semana/Dia/Mês

{% apitags %}
Semana/Dia/Mês
{% endapitags %}

- [Coloque o nome do mês anterior em uma mensagem](#month-name)
- [Enviar uma campanha no final de cada mês](#month-end)
- [Enviar uma campanha no último dia do mês (dia da semana)](#day-of-month-last)
- [Envie uma mensagem diferente a cada dia do mês](#day-of-month)
- [Envie uma mensagem diferente a cada dia da semana](#day-of-week)

### Coloque o nome do mês anterior em uma mensagem {#month-name}

Esse caso de uso pegará o mês atual e exibirá o mês anterior para ser usado no envio de mensagens.

{% raw %}
```liquid
{% assign today = 'now' | date: "%m" %}
{% assign last_month = {{today}} | minus: 1 %}
{% if last_month == 1 %}
{% assign month = "January" %}
{% elsif last_month == 2 %}
{% assign month = "February" %}
{% elsif last_month == 3 %}
{% assign month = "March" %}
{% elsif last_month == 4 %}
{% assign month = "April" %}
{% elsif last_month == 5 %}
{% assign month = "May" %}
{% elsif last_month == 6 %}
{% assign month = "June" %}
{% elsif last_month == 7 %}
{% assign month = "July" %}
{% elsif last_month == 8 %}
{% assign month = "August" %}
{% elsif last_month == 9 %}
{% assign month = "September" %}
{% elsif last_month == 10 %}
{% assign month = "October" %}
{% elsif last_month == 11 %}
{% assign month = "November" %}
{% elsif last_month == 0 %}
{% assign month = "December" %}
{% endif %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

Como alternativa, você pode usar o seguinte para obter o mesmo resultado.

{% raw %}
```liquid
{% assign last_month_name = 'now' | date: "%Y-%m-01" | date: '%s' | minus: 1 | date: "%B" %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

### Enviar uma campanha no final de cada mês {#month-end}

Esse caso de uso verificará se a data atual está dentro de uma lista de datas e, dependendo da data, exibirá uma mensagem específica.

{% alert note %} Isso não leva em conta os anos bissextos (29 de fevereiro). {% endalert %}

{% raw %}
```liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

The date is correct

{% else %}
{% abort_message("Date is not listed") %}
{% endif %}
```
{% endraw %}

### Enviar uma campanha no último dia do mês (dia da semana) {#day-of-month-last}

Esse caso de uso captura o mês e o dia atuais e calcula se o dia atual está dentro do último dia útil do mês.

Por exemplo, talvez você queira enviar uma pesquisa aos seus usuários na última quarta-feira do mês solicitando feedback sobre o produto.

{% raw %}
```liquid
{% comment %}Pull the day, day name, month, and year from today's date.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Assign the correct number of days for the current month.{% endcomment %}

{% if current_month == "Jan" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Mar" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Apr" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "May" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Jun" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Jul" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Aug" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Sep" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Oct" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Nov" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Dec" %}
{% assign last_day_of_month = 31 %}
{% endif %}

{% comment %}Assign the correct number of days if the current month is February, taking into account leap years.{% endcomment %}

{% assign leap_year_remainder = {{current_year | modulo: 4 }} != "0" %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif leap_year_remainder != "0" and current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Check that today's date is within a week of the last day of the month. If not, abort the message. If so, check that today is Wednesday. If not, abort the message.{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%} 
{% if diff_in_days <= 7 %} 
{% unless current_day_name == "Wed" %} 
{% abort_message("Wrong day of the week") %} 
{% endunless %} 
{% else %} 
{% abort_message("Not the last week of the month") %} 
{% endif %}
```
{% endraw %}

### Envie uma mensagem diferente a cada dia do mês {#day-of-month}

Esse caso de uso verifica se a data atual corresponde a uma data em uma lista e, dependendo do dia, exibirá uma mensagem distinta.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}

{% if today == day_1 %}
Message for 2019-12-01

{% elsif today == day_2 %}
Message for 2019-12-02

{% elsif today == day_3%}
Message for 2019-12-03

{% else %}
{% abort_message("Date not listed") %}
{% endif %}
```
{% endraw %}

### Envie uma mensagem diferente a cada dia da semana {#day-of-week}

Esse caso de uso verifica o dia da semana atual e, dependendo do dia, exibirá uma mensagem distinta.

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case today %}
{% when 'Monday' %}
Monday copy

{% when 'Tuesday' %}
Tuesday copy

{% when 'Wednesday' %}
Wednesday copy

{% when  'Thursday' %}
Thursday copy

{% when  'Friday' %}
Friday copy

{% when 'Saturday' %}
Saturday copy

{% when 'Sunday' %}
Sunday copy

{% else %}
Default copy
{% endcase %}
```
{% endraw %}

{% alert note %}
Você pode substituir a linha "default copy" por {% raw %}`{% abort_message() %}`{% endraw %} para evitar que a mensagem seja enviada se o dia da semana for desconhecido.
{% endalert %}

{% endapi %}

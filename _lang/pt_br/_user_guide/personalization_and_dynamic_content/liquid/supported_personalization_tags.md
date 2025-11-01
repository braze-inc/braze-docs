---
nav_title: Tags de personalização compatíveis
article_title: Tags de personalização do Liquid compatíveis
page_order: 1
description: "Este artigo de referência abrange uma lista completa das tags de personalização do Liquid compatíveis."
search_rank: 1
---

# Tags de personalização compatíveis

> Este artigo de referência abrange uma lista completa das tags de personalização do Liquid compatíveis.

## Resumo das tags suportadas

Por conveniência, é fornecido um resumo das tags de personalização compatíveis. Para obter mais detalhes sobre cada tipo de tag e práticas recomendadas, continue lendo.

{% raw %}

| Tipo de etiqueta de personalização | Tags |
| -------------  | ---- |
| Atributos padrão (predefinidos) | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Atributos do dispositivo | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions'>Atributos da lista de e-mails</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Essa tag substitui a tag anterior `{{${unsubscribe_url}}}`. Embora a tag antiga ainda funcione em e-mails criados anteriormente, recomendamos que você use a tag mais recente. <br><br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| <a href='/docs/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/#trigger-messages'>Atributos de SMS</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/'>Atributos do WhatsApp</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` |
| Atributos da campanha | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Atributos do Canvas | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Atributos da etapa do Canvas | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Atributos do cartão | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Eventos de geofencing | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Propriedades do evento <br> (Elas são personalizadas para seu espaço de trabalho).| `{{event_properties.${your_custom_event_property}}}` |
| Variáveis de contexto do Canvas | `{{context}}` |
| Atributos personalizados <br> (Elas são personalizadas para seu espaço de trabalho). | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>Propriedades do acionador da API</a> |`{{api_trigger_properties}}` |
| Propriedades de entrada do Canvas | `{{canvas_entry_properties.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Atributos suportados

Os atributos Campaign, Card e Canvas são compatíveis apenas com seus modelos de mensagens correspondentes (por exemplo, `dispatch_id` não está disponível em campanhas de mensagens in-app).

Consulte este artigo de ajuda para saber mais sobre [como alguns desses atributos diferem entre as origens no Braze]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/).

### Diferenças entre o Canvas e a tag da campanha 

O comportamento das seguintes tags difere entre o Canvas e as campanhas:
{% raw %}
- `dispatch_id` O comportamento é diferente porque o Braze trata as etapas do Canvas como eventos acionados, mesmo quando são "programadas" (exceto as etapas de entrada, que podem ser programadas). Para saber mais, consulte [Comportamento da ID de despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- O uso da tag `{{campaign.${name}}}` com o Canvas exibirá o nome do componente do Canvas. Ao usar essa tag com campanhas, ela exibirá o nome da campanha.
{% endraw %}

## Informações sobre o dispositivo usado mais recentemente

É possível modelar os seguintes atributos para o dispositivo mais recente do usuário em todas as plataformas. Se um usuário não tiver usado seu aplicativo (por exemplo, você importou o usuário por meio da API REST), todos esses valores serão `null`.

{% raw %}

|Etiqueta | Descrição |
|---|---|
|`{{most_recently_used_device.${browser}}}` | O navegador usado mais recentemente no dispositivo do usuário. Os exemplos incluem "Chrome" e "Safari". |
|`{{most_recently_used_device.${id}}}` | O identificador de dispositivo Braze. No iOS, isso pode ser o Identificador de Fornecedor da Apple (IDFV) ou um UUID. Para Android e outras plataformas, é um UUID gerado aleatoriamente. |
| `{{most_recently_used_device.${carrier}}}` | A operadora de serviço telefônico do dispositivo usado mais recentemente, se disponível. Os exemplos incluem "Verizon" e "Orange". |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Se o dispositivo tem o rastreamento de anúncios ativado ou não. Esse é um valor booleano (`true` ou `false`). |
| `{{most_recently_used_device.${idfa}}}` | Para dispositivos iOS, esse valor será o Identificador para Publicidade (IDFA) se o seu aplicativo estiver configurado com nossa [coleção opcional de IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). Para dispositivos não iOS, esse valor será nulo. |
| `{{most_recently_used_device.${google_ad_id}}}` | Para dispositivos Android, esse valor será o identificador de publicidade do Google Play se seu aplicativo estiver configurado com nossa coleção opcional de IDs de publicidade do Google Play. Para dispositivos não Android, esse valor será nulo. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Para dispositivos Roku, esse valor será o Roku Advertising Identifier coletado quando seu aplicativo for configurado com o Braze. Para dispositivos não-Roku, esse valor será nulo. |
| `{{most_recently_used_device.${model}}}` | O nome do modelo do dispositivo, se disponível. Os exemplos incluem "iPhone 6S", "Nexus 6P" e "Firefox". |
| `{{most_recently_used_device.${os}}}` | O sistema operacional do dispositivo, se disponível. Os exemplos incluem "iOS 9.2.1", "Android (Lollipop)" e "Windows". |
| `{{most_recently_used_device.${platform}}}` | A plataforma do dispositivo, se disponível. Se definido, o valor será um dos seguintes: `ios`, `android`, `kindle`, `android_china`, `web`, ou `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Como há uma grande variedade de operadoras de dispositivos, nomes de modelos e sistemas operacionais, recomendamos que você teste minuciosamente qualquer Liquid que dependa condicionalmente de qualquer um desses valores. Esses valores serão `null` se não estiverem disponíveis em um determinado dispositivo.

## Informações sobre aplicativos direcionados

Para mensagens in-app, você pode usar os seguintes atributos de aplicativo no Liquid. Os valores são baseados na chave de API do SDK que seus aplicativos usam para solicitar mensagens.

|Etiqueta | Descrição |
|------------------|---|
| `{{app.${api_id}}}` | A chave de API do aplicativo que está solicitando a mensagem. Por exemplo, você usa essa chave em conjunto com `abort_message()` Liquid para evitar o envio de mensagens no aplicativo para determinados aplicativos, como plataformas de TV ou compilações de desenvolvimento que usam uma chave de API SDK separada.|
| `{{app.${name}}}` | O nome do aplicativo (conforme definido no painel do Braze) que está solicitando a mensagem. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por exemplo, esse código Liquid abortará uma mensagem se os aplicativos solicitantes não forem uma das duas chaves de API na lista:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Informações sobre dispositivos direcionados

Para notificações por push e canais de mensagens in-app, você pode criar modelos nos seguintes atributos para o dispositivo para o qual a mensagem está sendo enviada. Ou seja, uma notificação por push ou uma mensagem no aplicativo pode incluir atributos do dispositivo no qual a mensagem está sendo lida. Observe que esses atributos não funcionarão para cartões de conteúdo. 

|Etiqueta | Descrição |
|------------------|---|
| `{{targeted_device.${id}}}` | Esse é o identificador do dispositivo Braze. No iOS, isso pode ser o Identificador de Fornecedor da Apple (IDFV) ou um UUID. Para Android e outras plataformas, é um UUID gerado aleatoriamente. Por exemplo, se um usuário tiver cinco dispositivos, ocorrerá uma tentativa de envio para todos os cinco dispositivos, cada um usando o identificador de dispositivo correspondente. Se uma mensagem estiver configurada para ser enviada para o dispositivo usado mais recentemente por um usuário, ocorrerá apenas uma tentativa de envio para o dispositivo usado mais recentemente identificado pelo Braze. |
| `{{targeted_device.${carrier}}}` | A operadora de serviço telefônico do dispositivo usado mais recentemente, se disponível. Os exemplos incluem "Verizon" e "Orange". |
| `{{targeted_device.${idfa}}}` | Para dispositivos iOS, esse valor será o Identificador para Publicidade (IDFA) se o seu aplicativo estiver configurado com nossa [coleção opcional de IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). Para dispositivos não iOS, esse valor será nulo. |
| `{{targeted_device.${google_ad_id}}}` | Para dispositivos Android, esse valor será o identificador de publicidade do Google Play se seu aplicativo estiver configurado com nossa [coleção opcional de ID de publicidade do Google Play]. Para dispositivos não Android, esse valor será nulo. |
| `{{targeted_device.${roku_ad_id}}}` | Para dispositivos Roku, esse valor será o Roku Advertising Identifier coletado quando seu aplicativo for configurado com o Braze. Para dispositivos não-Roku, esse valor será nulo. |
| `{{targeted_device.${model}}}` | O nome do modelo do dispositivo, se disponível. Os exemplos incluem "iPhone 6S", "Nexus 6P" e "Firefox". |
| `{{targeted_device.${os}}}` | O sistema operacional do dispositivo, se disponível. Os exemplos incluem "iOS 9.2.1", "Android (Lollipop)" e "Windows". |
| `{{targeted_device.${platform}}}` | A plataforma do dispositivo, se disponível. Se definido, o valor será um dos seguintes: `ios`, `android`, `kindle`, `android_china`, `web`, ou `tvos`. Você também pode usar a etiqueta de personalização `most_recently_used_device`. |
| `{{targeted_device.${foreground_push_enabled}}}` | Esse valor será `true` quando o dispositivo de destino estiver habilitado para push de primeiro plano e `false` caso contrário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

Como há uma grande variedade de operadoras de dispositivos, nomes de modelos e sistemas operacionais, recomendamos que você teste minuciosamente qualquer lógica que dependa condicionalmente de qualquer um desses valores. Esses valores serão `null` se não estiverem disponíveis em um determinado dispositivo. 

Além disso, no caso das notificações por push, é possível que o Braze não consiga discernir o dispositivo anexado à notificação por push em determinadas circunstâncias, como se o token por push tivesse sido importado por meio da API, resultando em valores sendo `null` para essas mensagens.

\![Exemplo de uso de um valor padrão de "there" ao usar uma variável de primeiro nome em uma mensagem push.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Uso da lógica condicional em vez de um valor padrão

Em algumas circunstâncias, você pode optar por usar [a lógica condicional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) em vez de definir um valor padrão. A lógica condicional permite que você envie mensagens diferentes com base no valor de um atributo personalizado. Além disso, você pode usar a lógica condicional para [abortar mensagens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) para clientes com valores de atributos nulos ou em branco. 

#### Caso de uso

Por exemplo, digamos que você esteja enviando uma notificação de saldo de recompensas aos clientes. Não há uma boa maneira de contabilizar clientes com saldos baixos e nulos usando valores padrão.

Nesse caso, há duas opções que podem funcionar melhor do que definir um valor padrão:

1. Abortar a mensagem para clientes com saldos baixos, nulos e em branco.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Envie uma mensagem completamente diferente para esses clientes, como, por exemplo, "Não é uma mensagem de marketing":

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

Nesse caso de uso, um usuário com um primeiro nome em branco ou nulo receberá a mensagem "Thanks for downloading" (Obrigado pelo download). Você deve incluir um [valor padrão]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/) para o primeiro nome para garantir que seu cliente não veja o Liquid em caso de erro.

{% endraw %}

## Tags de variáveis

Você pode usar a tag `assign` para criar uma variável no compositor de mensagens. Recomendamos o uso de um nome exclusivo para sua variável. Se você criar uma variável com um nome semelhante ao das tags de personalização compatíveis (como `language`), isso poderá afetar sua lógica de mensagens.

Depois de criar uma variável, você pode fazer referência a ela em sua lógica de mensagens ou mensagem. Essa tag é útil quando você deseja reformatar o conteúdo que é retornado pelo nosso recurso [Connected Content]({% image_buster /assets/img_archive/personalized_firstname_.png %}) ]. Você pode ler mais na documentação da Shopify sobre [tags variáveis](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert tip %}
Você está atribuindo as mesmas variáveis em todas as mensagens? Em vez de escrever a tag `assign` várias vezes, você pode salvar essa tag como um bloco de conteúdo e colocá-la na parte superior da mensagem.

1. [Criar um bloco de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Dê um nome ao seu Content Block (sem espaços ou caracteres especiais).
3. Selecione **Edit (Editar** ) na parte inferior da página.
4. Digite suas tags `assign`.

Desde que o Content Block esteja na parte superior da mensagem, toda vez que a variável for inserida na mensagem como um objeto, ela fará referência ao atributo personalizado escolhido!
{% endalert %}

### Caso de uso

Digamos que você permita que seus clientes troquem seus pontos de recompensa por prêmios depois de acumularem 100 pontos de recompensa. Portanto, você só quer enviar mensagens aos clientes que teriam um saldo de pontos maior ou igual a 100 se fizessem essa compra adicional:

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## Tags de iteração

{% raw %}
As tags de iteração podem ser usadas para executar um bloco de código repetidamente. O caso de uso abaixo apresenta a tag `for`.

### Caso de uso

Digamos que você esteja fazendo uma venda de tênis Nike e queira enviar mensagens aos clientes que manifestaram interesse na Nike. Você tem uma variedade de marcas de produtos visualizadas no perfil de cada cliente. Essa matriz pode conter até 25 marcas de produtos, mas você só deseja enviar mensagens aos clientes que visualizaram um produto da Nike como uma das cinco visualizações de produto mais recentes.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

Nesse caso de uso, verificamos os cinco primeiros itens da matriz de marcas de tênis visualizadas. Se um desses itens for inverso, criaremos a variável `converse_viewer` e a definiremos como verdadeira.

Em seguida, enviamos a mensagem de venda quando `converse_viewer` é verdadeiro. Caso contrário, a mensagem será cancelada.

Este é um exemplo simples de como as tags de iteração podem ser usadas no compositor de mensagens do Braze. Você pode encontrar mais informações na documentação da Shopify sobre [tags de iteração](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Tags de sintaxe

As tags de sintaxe podem ser usadas para controlar como o Liquid é renderizado. Você pode usar a tag `echo` para retornar uma expressão. Isso é o mesmo que envolver uma expressão usando colchetes, exceto que você pode usar essa tag dentro de tags Liquid. Você também pode usar a tag `liquid` para ter um bloco de Liquid sem nenhum delimitador em cada tag. Cada tag deve estar em sua própria linha ao usar a tag `liquid`. Confira a documentação da Shopify sobre [tags de sintaxe](https://shopify.dev/api/liquid/tags#syntax-tags) para obter mais informações e exemplos.

Com o [controle de espaço em branco](https://shopify.github.io/liquid/basics/whitespace/), é possível remover espaços em branco ao redor das tags, o que ajuda a controlar ainda mais a aparência da saída do Liquid.

## Códigos de status HTTP {#http-personalization}

Você pode utilizar o status HTTP de uma chamada [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) salvando-o primeiro como uma variável local e, em seguida, usando a tecla `__http_status_code__`. Por exemplo:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Essa chave só será adicionada automaticamente ao objeto Connected Content se o ponto de extremidade retornar um objeto JSON. Se o ponto de extremidade retornar uma matriz ou outro tipo, essa chave não poderá ser definida automaticamente na resposta.
{% endalert %}

## Envio de mensagens com base no idioma, na localidade mais recente e no fuso horário

Em algumas situações, talvez você queira enviar mensagens específicas para determinados locais. Por exemplo, o português brasileiro é tipicamente diferente do português europeu.

### Caso de uso: Localizar com base na localidade recente

Aqui está um caso de uso de como você pode usar a localidade mais recente para localizar ainda mais uma mensagem internacionalizada.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

Nesse caso de uso, os clientes com uma localidade mais recente de `pt_BR` receberão uma mensagem em português do Brasil, e os clientes com uma localidade mais recente de `pt_PT` receberão uma mensagem em português europeu. Os clientes que não atenderem às duas primeiras condições, mas tiverem o idioma definido como português, receberão uma mensagem no tipo de idioma português padrão que você desejar.

### Caso de uso: Usuários-alvo por fuso horário

Você também pode segmentar os usuários por fuso horário. Por exemplo, envie uma mensagem se a pessoa estiver em EST e outra se estiver em PST. Para fazer isso, salve a hora atual em UTC e compare uma instrução if/else com a hora atual do usuário para enviar a mensagem certa para o fuso horário certo. Você deve configurar a campanha para ser enviada no fuso horário local do usuário, para que ele receba a campanha no momento certo. 

Veja o caso de uso a seguir para saber como escrever uma mensagem que será enviada entre 14h e 15h e terá uma mensagem específica para cada fuso horário.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags

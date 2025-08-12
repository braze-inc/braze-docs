---
nav_title: Buscando dados através do Conteúdo Conectado
article_title: Buscando dados através do Conteúdo Conectado com Voucherify
page_order: 2
alias: /partners/voucherify/connected_content/
description: "Este artigo de referência descreve como você pode buscar dados da API do Voucherify através do Braze Connected Content e enviar mensagens para segmentos específicos do Braze."
page_type: partner
search_tag: Partner
---

# Buscando dados através do Conteúdo Conectado

> Com o Braze Connected Content, você pode buscar dados da API da Voucherify e enviar mensagens para segmentos específicos da Braze. Este artigo de referência mostrará como configurar scripts de Conteúdo Conectado para publicar cupons do Voucherify, convidar novos indicados, recuperar o saldo de cartões de fidelidade e mais.

_Esta integração é mantida pelo Voucherify._

## Sobre a integração

O esquema básico do script é o seguinte:
{% raw %}
```json
{% connected content
  "voucherify-API-ENDPOINT-url"
  :method post
  :headers {
    "X-App-Id": "Voucherify-API-key",
    "X-App-Token": "Voucherify-Secret-key",
  }
  :content_type application/json
  :retry
  :save {{result_variable}}
}
```
{% endraw %}

Visite o repositório [GitHub](https://github.com/voucherifyio/braze-connected-content) do Voucherify para ver exemplos de scripts de Conteúdo Conectado.

## Configurações de segurança

Sem as seguintes configurações definidas cada vez que uma mensagem de Conteúdo Conectado é acionada, ela chamará a API da Voucherify pelo menos duas vezes. Essas configurações reduzem o número de chamadas de API faturadas para a Braze e diminuem o risco de atingir o limite de API, que pode interromper a entrega de mensagens.

{% tabs %}
{% tab Limitador de Taxa %}

**Limitador de taxa**

Certifique-se de [limitar o número de mensagens]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) enviadas pelo Braze por minuto. Isso protege as APIs do Braze e do Voucherify contra o excesso de tráfego da sua campanha. Ao direcionar usuários durante a configuração da campanha, limite a taxa de envio a 500 mensagens por minuto.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

{% endtab %}
{% tab Cache %}

**Cache em chamadas POST**

As chamadas de conteúdo conectado feitas via HTTP POST não são armazenadas em cache por padrão e farão duas solicitações de API para cada código publicado. Esse comportamento pode sobrecarregar os limites da sua API. O mecanismo de cache permitirá que você limite isso a uma chamada de API por publicação de voucher. 

{% alert important %}
Todos os exemplos de Conteúdo Conectado neste tutorial incluem cache padrão para reduzir o número de chamadas de API acionadas pelo Braze.
{% endalert %}

Para adicionar cache às chamadas POST:

1. Adicione um {% raw %}`:cache_max_age`{% endraw %} atributo. Por padrão, a duração do cache é de 5 minutos. Você pode personalizar a duração usando segundos. É possível escolher um valor entre 5 minutos e 4 horas. Exemplo: {% raw %}`:cache_max_age 3600`{% endraw %} armazenará em cache por 1 hora.
2. Forneça uma chave de cache {% raw %}`cache_id={{cache_id}}`{% endraw %} no parâmetro de consulta do endpoint de destino para que a Braze possa identificar uma publicação exclusiva. Primeiro, defina a variável e depois anexe a string de consulta única ao seu endpoint. Isso diferenciará cada publicação pelo {% raw %}`source_id`{% endraw %}.

![]({% image_buster /assets/img/voucherify/voucherify_cc_cache.png %})

_Nota as consequências:_ Braze armazena em cache as chamadas de API com base na URL. A string única usada como parâmetro de consulta é ignorada pelo Voucherify, mas distingue diferentes solicitações de API para o Braze e permite armazenar em cache cada tentativa única separadamente. Sem esse parâmetro de consulta, todos os clientes receberão o mesmo código de cupom durante a duração do cache.

{% endtab %}
{% tab Repetir atributo %}

**Repetir atributo**

O Conteúdo Conectado não valida a resposta do Voucherify, então recomendamos adicionalmente adicionar um atributo de [repetição]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries) no script do Conteúdo Conectado. A lógica de conteúdo conectado tentará repetir cinco vezes antes de abortar a mensagem (respeitará o limitador de frequência). Este método ajudará a prevenir casos de falha na publicação de código quando demorar um pouco mais para buscar dados do Voucherify.

Se você não usar {% raw %}`:retry`{% endraw %}, então, independentemente da resposta retornada pelo Voucherify, o Braze tentará enviar a distribuição, o que pode resultar na geração de e-mails sem um código publicado.

![]({% image_buster /assets/img/voucherify/voucherify_cc_retry.png %})

{% endtab %}
{% tab Publicações únicas %}

**Publicação única por cliente**

O parâmetro {% raw %}`source_id`{% endraw %} no corpo do script garante que cada cliente possa receber apenas um código único em uma única campanha do Braze. Como resultado, mesmo que a Braze multiplique a solicitação de forma não intencional, cada usuário receberá o mesmo código único que foi publicado para ele/ela na primeira mensagem.

![]({% image_buster /assets/img/voucherify/voucherify_cc_sourceId_unique_publication.png %})

Você pode modificar {% raw %}`{{source_id}}`{% endraw %} e seu efeito nas publicações usando as seguintes configurações:

| Configuração | Efeito |
| ------------- | ------ |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} | Os clientes dentro de um único envio usarão a mesma publicação. |
| {% raw %}`{{campaign.${api_id}}}`{% endraw %} | Todos os clientes dentro de uma única campanha usarão a mesma publicação. |
| {% raw %}`{{${user_id}}}`{% endraw %} ou {% raw %}`{{${braze_id}}}`{% endraw %} | Verifica se todos os clientes usarão a mesma publicação, independentemente da campanha enviada (você pode usar {% raw %}`${user_id}`{% endraw %}, que é um {% raw %}`external_id`{% endraw %}, e {% raw %}`${braze_id}`{% endraw %}, que é um id interno). |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} e {% raw %}`{{campaign.${user_id}}}`{% endraw %} | Cada cliente dentro de um único envio usará a mesma publicação única. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Participar uma vez %}

**Participar uma vez**

Se sua campanha Voucherify tiver um limite _Os clientes podem participar apenas uma vez_, remova o ID da fonte de publicação do corpo do script. A Voucherify confirmará que cada mensagem da Braze para o mesmo cliente entregará o mesmo código publicado em primeiro lugar.

![]({% image_buster /assets/img/voucherify/voucherify_cc_join_once.png %}){: style="max-width:50%;"}

Seu script de Conteúdo Conectado deve ser o seguinte:

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign cache_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}
{% endtab %}
{% endtabs %}

## Casos de uso

Tenha em mente que todos os casos de uso abaixo usam o ID da fonte de publicação do Voucherify e os parâmetros de cache e repetição do Braze para limitar as chamadas de API invocadas por uma campanha do Braze. Você deve estar ciente das seguintes consequências:

- Não é possível publicar e enviar códigos diferentes para o mesmo cliente em uma única campanha Braze.
- Se sua campanha Voucherify usar o _recurso de participar apenas uma vez_, você precisa remover `source_id` do corpo do Conteúdo Conectado conforme descrito na guia participar uma vez acima.

Visite o repositório [GitHub](https://github.com/voucherifyio/braze-connected-content) do Voucherify para ver exemplos de scripts de Conteúdo Conectado.

### Publicar e enviar código de cupom único

Neste caso de uso, o script de Conteúdo Conectado chama a API da Voucherify para publicar um código de cupom único e enviá-lo na mensagem da Braze. Cada usuário da Braze recebe apenas um código único.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Convidar novos indicados

Se você quiser que um cliente participe de um programa de indicação, você precisa atribuir um código de indicação a essa pessoa. O Conteúdo Conectado permanece o mesmo que no exemplo anterior. Este script de Conteúdo Conectado permite que você publique e envie códigos de referência únicos para usuários selecionados da Braze. Cada usuário recebe apenas um código de indicação para compartilhar com outros usuários e ganhar novas indicações. 

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Buscar saldo do cartão de fidelidade

Aqui está um caso de uso de um script de Conteúdo Conectado que puxa o saldo atual de fidelidade com base no código do cartão de fidelidade que foi enviado anteriormente para a Braze como um atributo personalizado. Nota que você precisa armazenar o código do cartão de fidelidade como um atributo personalizado no perfil do usuário do Braze antes de usar este script.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/loyalties/members/{{custom_attribute.${loyalty.card}}}?cache_id={{cache_id}}
   :method get
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age
   :retry
   :save member
 %}
```

{% endraw %}

### Criar código personalizado

O conteúdo conectado é uma ferramenta poderosa que permite a introdução de cenários criativos. Você pode criar um código de cupom personalizado com base nas informações do perfil do cliente.

Aqui está um trecho de código que levará em conta o número de telefone do cliente para gerar um código único. Neste caso de uso, o script de Conteúdo Conectado chama a API da Voucherify para publicar um código de cupom personalizado.

1.  Primeiro, defina todas as variáveis necessárias. Em seguida, crie um código de cupom começando com o prefixo "SummerTime-" e o restante do código será o número de telefone do cliente. Você pode decidir sobre o atributo personalizado no qual gostaria de basear seus códigos de cupom.  
    
    {% raw %}
    
    ```liquid
    {% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
    {% assign customer_id = {{${user_id}}} %}
    {% assign phoneNumber = {{${phone_number}}} %}
    {% assign source_id = braze_campaign_id | append: customer_id %}
    {% assign cache_id = source_id %}
    {% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
    {% assign prefix = "SummerTime-" %}
    ```
    
    {% endraw %}
    
2.  Em seguida, solicite ao Voucherify que gere um único código na campanha. Fornecemos o nome do código do cupom a ser criado na URL:  
    
    {% raw %}
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
       :method post
       :headers {
            "X-App-Id": "VOUCHERIFY-APP-ID",
            "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :content_type application/json
       :cache_max_age 
       :save voucher_created
       :retry
    %}  
    ```  
    
    {% endraw %}  

3.  Por fim, publique o código que você acabou de criar. O trecho de código parece quase o mesmo que você usou para gerar um voucher aleatório de uma campanha. No entanto, agora o objetivo é obter um código de voucher específico.  
    
    {% raw %}  
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
       :method post
       :headers {
           "X-App-Id": "VOUCHERIFY-APP-ID",
           "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
       :content_type application/json
       :cache_max_age 
       :save publication
       :retry
    %}
    ```
    
    {% endraw %}

Como resultado, o cliente recebe o seguinte e-mail:  

![]({% image_buster /assets/img/voucherify/voucherify_cc_custom_code_email.png %})

Aqui está o snippet completo usado neste exemplo:

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign phoneNumber = {{${phone_number}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign cache_id = source_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign prefix = "Your Prefix" %}

{% connected_content
   YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age 
   :save voucher_created
   :retry
%} 

{% connected_content
   YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
       "X-App-Id": "VOUCHERIFY-APP-ID",
       "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age 
   :save publication
   :retry
%}
```

{% endraw %}

## Exibir dados buscados em mensagens Braze

Presumimos que você já tenha uma campanha ou canva da Braze na qual deseja usar o script de conteúdo conectado.

### Etapa 1: Adicionar script de Conteúdo Conectado ao modelo de mensagem

1.  Copie e cole o script de Conteúdo Conectado sob a tag {% raw %}`<body>`{% endraw %} em um modelo de HTML de mensagem. Substitua **CAMPAIGN_ID** por um Voucherify {% raw %}`campaign_id`{% endraw %} copiado do endereço URL do dashboard da campanha do Voucherify.<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_campaignId.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}  
    ```
    assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce"
    ```
    {% endraw %}

2. Forneça seu endpoint da API Voucherify. Se você não souber qual é o seu endpoint da API, você pode verificá-lo em **Configurações do projeto** > **Geral** > **Endpoint da API**.<br>
    {% raw %}
    ```
    YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
    ```
    {% endraw %}
    
    | Cluster Compartilhado   | Endpoint para Braze Connected Content          |
    | ---------------- | --------------------------------------------- |
    | Europa (padrão) | https://api.voucherify.io/v1/publications     |
    | Estados Unidos    | https://us1.api.voucherify.io/v1/publications |
    | Ásia (Singapura) | https://as1.api.voucherify.io/v1/publications |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation" }
    
3.  Adicione suas chaves de API para autenticação. Você pode encontrar `Voucherify-App-Id` e `Voucherify-App-Token` em suas **Configurações do Projeto > Geral > Chaves de Aplicação.**<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_app_keys.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}
    ```
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    ```
    {% endraw %}
    
Agora seu script de conteúdo conectado está pronto.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce" %}
{% assign cache_id = source_id %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "490a3fb6-a",
        "X-App-Token": "328099d5-a"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Etapa 2: Crie um trecho para exibir os dados buscados

As respostas da API Voucherify são armazenadas pelo Conteúdo Conectado sob o valor do parâmetro {% raw %}`:save`{% endraw %}. Por exemplo:

{% raw %}

```liquid
:save member
```
{% endraw %}

Isso permite que você recupere e exiba dados de uma resposta do Voucherify em mensagens do Braze.

Você pode criar trechos que exibem o código publicado, saldo do cartão de fidelidade, data de expiração e outros parâmetros incluídos na resposta em formato JSON da API Voucherify.

Por exemplo, para exibir o código publicado em um modelo de mensagem, você deve criar um snippet que busque um código único do objeto de voucher.

Script de conteúdo conectado:

![Script de Conteúdo Conectado mostrando como salvar uma resposta do Voucherify no final da chamada de Conteúdo Conectado]({% image_buster /assets/img/voucherify/voucherify_cc_save_parameter.png %})

Snippet no modelo de mensagem da Braze:

{% raw %}

```liquid
{{publication.voucher.code}}
```

{% endraw %}

Como resultado, cada cliente recebe uma mensagem com um código único atribuído automaticamente ao seu perfil. Cada vez que um código é recebido pelo usuário, ele é publicado em seu perfil no Voucherify.

Para exibir o saldo do cartão de fidelidade obtido da API Voucherify, você precisa criar o seguinte trecho:

{% raw %}

```liquid
{{member.loyalty_card.balance}}
```

{% endraw %}

em que o membro é um valor do parâmetro {% raw %}`:save`{% endraw %} no script de conteúdo conectado.

{% raw %}

```liquid
:save member
```

{% endraw %}

Aconselhamos fortemente que você não dependa inteiramente do 'modo de prévia' e envie várias mensagens de teste para confirmar que tudo funciona como deveria.

### Etapa 3: Configurar limitador de taxa

Ao configurar um alvo de campanha, use as configurações avançadas para limitar o número de mensagens enviadas por minuto.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

Leia mais sobre o limitador de frequência e o limite de frequência na [documentação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) da Braze.


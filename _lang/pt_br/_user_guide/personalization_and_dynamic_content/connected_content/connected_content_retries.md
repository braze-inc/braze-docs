---
nav_title: Tentativas de Conteúdo Conectado
article_title: Tentativas de Conteúdo Conectado
page_order: 5
description: "Este artigo de referência cobre como lidar com as tentativas de Conteúdo Conectado."

---

# Usando lógica de tentativa para Conteúdo Conectado

> Esta página cobre como adicionar tentativas às suas chamadas de Conteúdo Conectado.

## Como as tentativas funcionam 

Como o Conteúdo Conectado depende de receber dados de APIs, uma API pode estar intermitentemente indisponível enquanto a Braze faz a chamada. Nesse caso, a Braze suporta lógica de tentativa para re-tentar a solicitação usando retrocesso exponencial.

{% alert note %}
Conteúdo Conectado `:retry` não está disponível para mensagens no aplicativo.
{% endalert %}

## Usando lógica de tentativa

Para usar a lógica de tentativa, adicione a tag `:retry` à chamada de Conteúdo Conectado, conforme mostrado no seguinte trecho de código:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Quando uma tag `:retry` é incluída na chamada de Conteúdo Conectado, a Braze tentará re-tentar a chamada até cinco vezes.

### Resultados das tentativas

#### Quando uma tentativa de re-tentativa é bem-sucedida

Se uma tentativa re-tentada for bem-sucedida, a mensagem é enviada e nenhuma nova tentativa é feita para essa mensagem.

#### Quando a chamada da API falha e as tentativas estão habilitadas

Se a chamada da API falhar e isso estiver habilitado, a Braze tentará re-tentar a chamada respeitando o [limite de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting) que você definiu para cada reenvio. A Braze moverá quaisquer mensagens falhadas para o final da fila e adicionará minutos adicionais, se necessário, ao total de minutos que levaria para enviar sua mensagem.

Se a chamada de Conteúdo Conectado falhar mais de cinco vezes, a mensagem é abortada, semelhante a como um [tag de mensagem abortada]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) é acionada.
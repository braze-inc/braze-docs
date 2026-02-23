---
nav_title: Outras tentativas no conteúdo conectado
article_title: Novas tentativas de conteúdo conectado
page_order: 5
description: "Este artigo de referência aborda como lidar com as novas tentativas do recurso conteúdo conectado."

---

# Usando lógica de repetição para Conteúdo Conectado

> Esta página aborda como adicionar novas tentativas às suas chamadas de Connected Content.

## Como as repetições funcionam 

Como o Conteúdo Conectado depende de receber dados de APIs, uma API pode estar intermitentemente indisponível enquanto o Braze faz a chamada. Nesse caso, a Braze oferece suporte à lógica de tentar novamente para tentar novamente a solicitação usando o backoff exponencial.

{% alert note %}
O recurso de conteúdo conectado `:retry` não está disponível para mensagens no app.
{% endalert %}

## Usando lógica de repetição

Para usar a lógica de repetição, adicione a tag `:retry` à chamada de Conteúdo Conectado, conforme mostrado no seguinte trecho de código:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Quando uma tag `:retry` é incluída na chamada de Conteúdo Conectado, o Braze tentará repetir a chamada até cinco vezes.

### Resultados de novas tentativas

#### Quando uma nova tentativa for bem-sucedida

Se uma tentativa repetida for bem-sucedida, a mensagem é enviada e nenhuma nova repetição é tentada para essa mensagem.

#### Quando a chamada à API falhar e as novas tentativas estiverem ativadas

Se a chamada API falhar e isso estiver ativado, o Braze tentará novamente a chamada, respeitando o [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting) que você definiu para cada reenvio. O Braze moverá todas as mensagens com falha para o final da fila e adicionará minutos adicionais, se necessário, ao total de minutos necessários para enviar sua mensagem.

Se a chamada de Conteúdo Conectado falhar mais de cinco vezes, a mensagem é abortada, semelhante a como uma [tag de mensagem abortar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) é acionada.
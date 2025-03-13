---
nav_title: Novas tentativas de conteúdo conectado
article_title: Novas tentativas de conteúdo conectado
page_order: 3
description: "Este artigo de referência aborda como lidar com as novas tentativas do recurso conteúdo conectado."

---

# Outras tentativas no conteúdo conectado

> Como o recurso depende do recebimento de dados de APIs, existe a possibilidade de que uma API esteja intermitentemente indisponível enquanto a Braze faz a chamada. Nesse caso, a Braze oferece suporte à lógica de tentar novamente para tentar novamente a solicitação usando o backoff exponencial. <br><br> Esta página aborda como adicionar novas tentativas às suas chamadas de Connected Content.

## Como ativar as novas tentativas

Para ativar as novas tentativas, adicione `:retry` na chamada do conteúdo conectado, conforme mostrado no seguinte trecho de código:
{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

## Resultados de novas tentativas

### Quando a chamada à API falhar e as novas tentativas estiverem ativadas

Se a chamada API falhar e isso estiver ativado, o Braze tentará novamente a chamada, respeitando o [limite de frequência][47] que você definiu para cada reenvio. O Braze moverá todas as mensagens com falha para o final da fila e adicionará minutos adicionais, se necessário, ao total de minutos necessários para enviar sua mensagem.

### Quando uma nova tentativa for bem-sucedida

Se uma nova tentativa for bem-sucedida, a mensagem será enviada e nenhuma outra tentativa será feita para essa mensagem. Se a chamada do conteúdo conectado errar 5 vezes, a mensagem será abortada de modo semelhante ao que ocorreria se uma [tag de mensagem abortada][1] fosse disparada.

{% alert note %}
O recurso de conteúdo conectado `:retry` não está disponível para mensagens no app.
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[16]: [success@braze.com](mailto:success@braze.com)
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting

---
nav_title: Novas tentativas de conteúdo conectado
article_title: Novas tentativas de conteúdo conectado
page_order: 5
description: "Este artigo de referência aborda como lidar com as novas tentativas do recurso conteúdo conectado."

---

# Uso da lógica de repetição para o Connected Content

> Esta página aborda como adicionar novas tentativas às suas chamadas de Connected Content.

## Como funcionam as novas tentativas 

Como o Connected Content depende do recebimento de dados de APIs, uma API pode estar intermitentemente indisponível enquanto o Braze faz a chamada. Nesse caso, a Braze oferece suporte à lógica de tentar novamente para tentar novamente a solicitação usando o backoff exponencial.

{% alert note %}
O recurso de conteúdo conectado `:retry` não está disponível para mensagens no app.
{% endalert %}

## Uso da lógica de repetição

Para usar a lógica de repetição, adicione a tag `:retry` à chamada do Connected Content, conforme mostrado no seguinte trecho de código:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Quando uma tag `:retry` for incluída na chamada de Connected Content, o Braze tentará repetir a chamada até cinco vezes.

### Resultados de novas tentativas

#### Quando uma nova tentativa for bem-sucedida

Se uma nova tentativa for bem-sucedida, a mensagem será enviada e nenhuma outra tentativa será feita para essa mensagem.

#### Quando a chamada à API falhar e as novas tentativas estiverem ativadas

Se a chamada API falhar e isso estiver ativado, o Braze tentará novamente a chamada, respeitando o [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting) que você definiu para cada reenvio. O Braze moverá todas as mensagens com falha para o final da fila e adicionará minutos adicionais, se necessário, ao total de minutos necessários para enviar sua mensagem.

Se a chamada do Connected Content apresentar erros mais de cinco vezes, a mensagem será abortada, de forma semelhante à maneira como uma [tag de mensagem abortada]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) é disparada.
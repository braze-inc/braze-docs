---
nav_title: Novas tentativas de conteúdo conectado
article_title: Novas tentativas de conteúdo conectado
page_order: 5
description: "Este artigo de referência aborda como lidar com as novas tentativas do recurso conteúdo conectado."

---

# 

> Esta página aborda como adicionar novas tentativas às suas chamadas de Connected Content.

##  

 Nesse caso, a Braze oferece suporte à lógica de tentar novamente para tentar novamente a solicitação usando o backoff exponencial.

{% alert note %}
O recurso de conteúdo conectado `:retry` não está disponível para mensagens no app.
{% endalert %}

## 




```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}



### Resultados de novas tentativas

#### Quando uma nova tentativa for bem-sucedida



#### Quando a chamada à API falhar e as novas tentativas estiverem ativadas

 O Braze moverá todas as mensagens com falha para o final da fila e adicionará minutos adicionais, se necessário, ao total de minutos necessários para enviar sua mensagem.


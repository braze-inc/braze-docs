---
nav_title: Cache de Respostas
article_title: Cache de Respostas de Conteúdo Conectado
page_order: 2.5
description: "Este artigo cobre como armazenar em cache as respostas de Conteúdo Conectado em diferentes campanhas ou mensagens no mesmo espaço de trabalho para otimizar as velocidades de envio."
---

# Cache de respostas de Conteúdo Conectado

> As respostas de Conteúdo Conectado podem ser armazenadas em cache em diferentes campanhas ou mensagens (no mesmo espaço de trabalho) para otimizar as velocidades de envio.

A Braze não registra ou armazena permanentemente as respostas de Conteúdo Conectado. Se você optar explicitamente por armazenar uma resposta de chamada de Conteúdo Conectado como uma variável Liquid, a Braze apenas armazena isso na memória, ou seja, em armazenamento temporário que é excluído após um curto período de tempo, para renderizar a variável Liquid e enviar a mensagem.

Para evitar o cache, você pode especificar `:no_cache`, o que pode causar aumento no tráfego de rede. Para ajudar a solucionar problemas e monitorar a integridade do sistema, a Braze também pode registrar chamadas de Conteúdo Conectado que falham (como `404` e `429`). Esses registros são mantidos por até 30 dias.

## Configurações de cache padrão

A idade do cache é de até cinco minutos (300 segundos). Você pode atualizar isso adicionando o parâmetro `:cache_max_age` à chamada de Conteúdo Conectado. Um exemplo é:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

As requisições GET são armazenadas em cache. Você pode configurar isso adicionando o parâmetro :no_cache à chamada de Conteúdo Conectado.

As requisições POST não são armazenadas em cache. Isso pode ser forçado adicionando o parâmetro :cache_max_age à chamada de Conteúdo Conectado. O tempo mínimo de cache é de 5 minutos, e o tempo máximo de cache é de 4 horas.

{% alert note %}
As configurações de cache não são garantidas. O cache pode reduzir chamadas para seus endpoints, então recomendamos usar múltiplas chamadas por endpoint dentro da duração do cache em vez de depender excessivamente do cache.
{% endalert %}

### Limite de tamanho do cache

O corpo da resposta do Conteúdo Conectado pode ter até 1 MB. Se o corpo da resposta for maior que 1 MB, ele não será armazenado em cache.

## Tempo de cache 

O Conteúdo Conectado armazenará em cache o valor que retorna dos endpoints GET por um mínimo de cinco minutos. Se um tempo de cache não for especificado, o tempo de cache padrão é de cinco minutos.

O tempo de cache do Conteúdo Conectado pode ser configurado para ser mais longo com :cache_max_age, conforme mostrado no exemplo a seguir. O tempo mínimo de cache é de cinco minutos e o tempo máximo de cache é de quatro horas. Os dados de conteúdo conectado são armazenados em cache na memória usando um sistema de cache volátil, como o Memcached. 

Como resultado, independentemente do tempo de cache especificado, os dados do Conteúdo Conectado podem ser removidos do cache em memória do Braze antes do especificado. Isso significa que as durações do cache são sugestões e podem não representar realmente a duração que os dados são garantidos a serem armazenados em cache pelo Braze e você pode ver mais solicitações de Conteúdo Conectado do que pode esperar com uma determinada duração de cache.

### Cache por segundos especificados

Este exemplo será armazenado em cache por 900 segundos (ou 15 minutos).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Cache busting

Para evitar que o conteúdo conectado armazene em cache o valor que retorna de uma solicitação GET, você pode usar a configuração `:no_cache`. No entanto, as respostas de hosts internos à Braze ainda serão armazenadas em cache.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Certifique-se de que o endpoint de Conteúdo Conectado fornecido pode lidar com grandes picos de tráfego antes de usar esta opção, ou você provavelmente verá um aumento na latência de envio (aumento dos atrasos ou intervalos de tempo mais amplos entre a solicitação e a resposta) devido ao Braze fazer solicitações de Conteúdo Conectado para cada mensagem.
{% endalert %}

Com um POST, você não precisa se preocupar com o cache, pois o Braze nunca armazena em cache os resultados de solicitações POST.

## Coisas para saber

- O armazenamento em cache pode ajudar a reduzir chamadas duplicadas de Conteúdo Conectado. No entanto, não é garantido que sempre resulte em uma única chamada de Conteúdo Conectado por usuário.
- O armazenamento em cache do Conteúdo Conectado é baseado na URL e no espaço de trabalho. Se a chamada do Conteúdo Conectado for para a URL idêntica, ela pode ser armazenada em cache entre campanhas e canvases.
- O cache é baseado em uma URL única, não em um ID de usuário ou campanha. Isso significa que a versão em cache de uma chamada de Conteúdo Conectado pode ser usada entre vários usuários e campanhas em um espaço de trabalho se a URL for a mesma.

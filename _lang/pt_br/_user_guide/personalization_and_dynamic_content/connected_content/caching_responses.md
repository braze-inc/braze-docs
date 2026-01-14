---
nav_title: Cache de respostas
article_title: Armazenamento em cache de respostas de conteúdo conectado
page_order: 2.5
description: "Este artigo aborda como armazenar em cache as respostas do Connected Content em diferentes campanhas ou mensagens no mesmo espaço de trabalho para otimizar as velocidades de envio."
---

# Armazenamento em cache das respostas do Connected Content

> As respostas do Connected Content podem ser armazenadas em cache em diferentes campanhas ou mensagens (no mesmo espaço de trabalho) para otimizar as velocidades de envio.

O Braze não registra nem armazena permanentemente as respostas do Connected Content. Se você optar explicitamente por armazenar uma resposta de chamada do Connected Content como uma variável Liquid, o Braze armazenará essa resposta apenas na memória, ou seja, em um armazenamento temporário que será excluído após um curto período de tempo, para renderizar a variável Liquid e enviar a mensagem.

Para evitar o armazenamento em cache, você pode especificar `:no_cache`, o que pode aumentar o tráfego de rede. Para ajudar a solucionar problemas e monitorar a integridade do sistema, o Braze também pode registrar chamadas de Connected Content que falham (como `404` e `429`). Esses registros são mantidos por até 30 dias.

## Configurações de cache padrão

A idade do cache é de até cinco minutos (300 segundos). Você pode atualizar isso adicionando o parâmetro `:cache_max_age` à chamada do Connected Content. Um exemplo é:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

As solicitações GET são armazenadas em cache. Você pode configurar isso adicionando o parâmetro :no_cache à chamada Connected Content.

As solicitações POST não são armazenadas em cache. Isso pode ser forçado adicionando o parâmetro :cache_max_age à chamada Connected Content. O tempo mínimo de cache é de 5 minutos e o tempo máximo de cache é de 4 horas.

{% alert note %}
As configurações de cache não são garantidas. O armazenamento em cache pode reduzir as chamadas para seus pontos de extremidade, portanto, recomendamos o uso de várias chamadas por ponto de extremidade dentro da duração do cache, em vez de depender excessivamente do armazenamento em cache.
{% endalert %}

### Limite de tamanho do cache

O corpo da resposta do Connected Content pode ter até 1 MB. Se o corpo da resposta for maior que 1 MB, ele não será armazenado em cache.

## Tempo de cache 

A Connected Content armazenará em cache o valor que retorna dos pontos de extremidade GET por um mínimo de cinco minutos. Se um tempo de cache não for especificado, o tempo de cache padrão será de cinco minutos.

O tempo de cache do Connected Content pode ser configurado para ser mais longo com :cache_max_age,, conforme mostrado no exemplo a seguir. O tempo mínimo de cache é de cinco minutos e o tempo máximo de cache é de quatro horas. Os dados do Connected Content são armazenados em cache na memória usando um sistema de cache volátil, como o Memcached. 

Como resultado, independentemente do tempo de cache especificado, os dados do Connected Content podem ser removidos do cache em memória do Braze antes do especificado. Isso significa que as durações do cache são sugestões e podem não representar de fato a duração garantida do cache dos dados pelo Braze, e você poderá ver mais solicitações de Connected Content do que o esperado com uma determinada duração de cache.

### Cache por segundos especificados

Este exemplo armazenará em cache por 900 segundos (ou 15 minutos).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Quebra de cache

Para evitar que o Connected Content armazene em cache o valor que retorna de uma solicitação GET, você pode usar a configuração `:no_cache`. No entanto, as respostas de hosts internos ao Braze ainda serão armazenadas em cache.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Certifique-se de que o ponto de extremidade Connected Content fornecido possa lidar com grandes explosões de tráfego antes de usar essa opção, ou você provavelmente verá um aumento na latência de envio (maiores atrasos ou intervalos de tempo maiores entre a solicitação e a resposta) devido ao fato de o Braze fazer solicitações de Connected Content para cada mensagem.
{% endalert %}

Com um POST, você não precisa armazenar o busto em cache, pois o Braze nunca armazena em cache os resultados de solicitações POST.

## Coisas para saber

- O armazenamento em cache pode ajudar a reduzir as chamadas duplicadas do Connected Content. No entanto, não é garantido que isso sempre resulte em uma única chamada de Connected Content por usuário.
- O cache do Connected Content é baseado no URL e no espaço de trabalho. Se a chamada do Connected Content for para o URL idêntico, ele poderá ser armazenado em cache em todas as campanhas e Canvases.
- O cache é baseado em um URL exclusivo, não em um ID de usuário ou campanha. Isso significa que a versão em cache de uma chamada de Connected Content pode ser usada por vários usuários e campanhas em um espaço de trabalho se o URL for o mesmo.

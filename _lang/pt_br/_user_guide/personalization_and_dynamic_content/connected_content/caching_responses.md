---
nav_title: Armazenando respostas
article_title: Respostas de Conteúdo Conectado em Cache
page_order: 2.5
description: "Este artigo cobre como armazenar em cache as respostas de Conteúdo Conectado em diferentes campanhas ou mensagens no mesmo espaço de trabalho para otimizar as velocidades de envio."
---

# Respostas de Conteúdo Conectado em Cache

> As respostas de Conteúdo Conectado podem ser armazenadas em cache em diferentes campanhas ou mensagens (no mesmo espaço de trabalho) para otimizar as velocidades de envio.

A Braze não registra ou armazena permanentemente os **corpos de resposta** de Conteúdo Conectado. Durante a renderização da mensagem, as respostas podem ser mantidas temporariamente (por exemplo, na memória e em cache) para que a Braze possa renderizar Liquid e enviar a mensagem.

Para evitar o armazenamento em cache, você pode especificar `:no_cache`, o que pode causar um aumento no tráfego de rede. Para ajudar a solucionar problemas e monitorar a integridade do sistema, a Braze registra os metadados de solicitação de Conteúdo Conectado (como a URL da solicitação totalmente renderizada e o código de status da resposta) para chamadas bem-sucedidas e falhadas. Esses registros são mantidos por até 30 dias.

{% details Connected Content rendering and data handling (advanced) %}
Esta seção fornece uma visão mais detalhada, de ponta a ponta, de como a Braze renderiza Liquid e Conteúdo Conectado e onde os dados podem existir temporariamente antes que uma mensagem seja enviada. Isso pode ajudar com revisões de privacidade e manuseio de dados.

#### O que é e o que não é armazenado

- **Corpo da resposta de Conteúdo Conectado:** Não armazenado permanentemente pela Braze. Pode ser mantido temporariamente na memória e, quando o cache está habilitado, armazenado em cache com um tempo de vida (TTL).
- **Metadados da solicitação de Conteúdo Conectado:** Os metadados da solicitação, como a URL totalmente renderizada, código de status HTTP e duração da resposta, são registrados para solução de problemas e monitoramento. Esses registros são mantidos por até 30 dias. 
- **Mensagem final renderizada:** Existe na memória durante a renderização. Isso também pode ser armazenado em outro lugar, dependendo da sua configuração e canal (por exemplo, Arquivamento de Mensagens ou Cartões de Conteúdo).

#### Fluxo de renderização (nível alto)

O fluxo a seguir descreve como o Braze renderiza e envia mensagens para canais baseados em provedores, como e-mail, SMS e push. Canais entregues pelo SDK, como Cartões de Conteúdo, usam a mesma renderização subjacente de Liquid e Conteúdo Conectado, mas diferem em quando o conteúdo é gerado e como é entregue.

1. Um trabalhador em segundo plano renderiza o modelo Liquid para uma mensagem quando a mensagem está preparada para ser entregue.
2. As tags de Conteúdo Conectado são avaliadas durante a renderização do Liquid.
3. Para cada tag de Conteúdo Conectado, o Braze verifica um cache em múltiplas camadas. Se nenhum valor em cache existir (ou se o cache estiver desativado), o Braze chama seu endpoint e recebe a resposta.
4. A resposta é injetada no modelo Liquid e a mensagem é totalmente renderizada.
5. Para canais baseados em provedores, a mensagem renderizada é enviada ao provedor do canal e, em seguida, ao usuário. Para canais entregues pelo SDK, como Cartões de Conteúdo, o conteúdo renderizado é sincronizado com o SDK do Braze e pode ser gerado na primeira impressão ou no momento da exibição, momento em que é mostrado ao usuário.

#### Onde as respostas de Conteúdo Conectado podem viver temporariamente

O Braze usa um cache em múltiplas camadas para respostas de Conteúdo Conectado com TTLs entre cinco minutos e quatro horas, dependendo do seu uso de `:cache_max_age` e outras regras de cache:

- **Cache de memória em processo:** Cache transitório dentro do processo do trabalhador. Os dados podem viver apenas durante a duração do trabalho (até ~11 minutos com base no tempo limite do trabalhador).
- **Cache local da máquina:** Um cache por trabalhador, como uma instância local do Memcached.
- **Cache em cluster:** Um cache distribuído compartilhado entre trabalhadores, como um cluster do Memcached.

Essas camadas de cache são voláteis e podem expulsar dados antes do TTL configurado.

#### O que muda quando você usa `:no_cache`

Para endpoints que não estão hospedados dentro da infraestrutura da Braze, usar `:no_cache` impede que o corpo da resposta do Conteúdo Conectado seja armazenado no Memcached. Nesses casos, a resposta só vive na memória do processo trabalhador durante a duração do trabalho de renderização (até ~11 minutos). Para endpoints que resolvem para hosts internos da Braze, as respostas ainda podem ser armazenadas em cache conforme descrito em [Cache busting](#cache-busting).

#### Onde a saída final renderizada pode viver

- **Arquivamento de Mensagens:** Se o Arquivamento de Mensagens estiver habilitado, a Braze pode gravar a mensagem final renderizada no seu bucket de armazenamento em nuvem configurado. Se sua resposta de Conteúdo Conectado estiver incluída na mensagem renderizada, ela será incluída na cópia arquivada.
- **Dispositivos dos usuários:** Após a entrega, o conteúdo totalmente renderizado da mensagem pode persistir nos dispositivos dos usuários por um tempo desconhecido.
- **Cartões de conteúdo:** O conteúdo renderizado para Cartões de Conteúdo é armazenado em um banco de dados da Braze até que o cartão expire.
{% enddetails %}

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

O tempo de cache do Conteúdo Conectado pode ser configurado para ser mais longo com :cache_max_age, como mostrado no exemplo a seguir. O tempo mínimo de cache é de cinco minutos e o tempo máximo de cache é de quatro horas. Os dados de conteúdo conectado são armazenados em cache na memória usando um sistema de cache volátil, como o Memcached. 

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

- O cache pode ajudar a reduzir chamadas duplicadas de Conteúdo Conectado. No entanto, não é garantido que sempre resulte em uma única chamada de Conteúdo Conectado por usuário.
- O cache do Conteúdo Conectado é baseado na URL e no espaço de trabalho. Se a chamada do Conteúdo Conectado for para a URL idêntica, ela pode ser armazenada em cache entre campanhas e canvases.
- O cache é baseado em uma URL única, não em um ID de usuário ou campanha. Isso significa que a versão em cache de uma chamada de Conteúdo Conectado pode ser usada entre múltiplos usuários e campanhas em um espaço de trabalho se a URL for a mesma.

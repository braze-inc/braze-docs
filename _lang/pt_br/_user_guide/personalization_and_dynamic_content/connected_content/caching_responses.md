---
nav_title: Cache de respostas
article_title: Cache de respostas de conteúdo conectado
page_order: 2.5
description: "Este artigo aborda como armazenar em cache as respostas do Connected Content em diferentes campanhas ou mensagens no mesmo espaço de trabalho para otimizar as velocidades de envio."
---

# Cache das respostas do Connected Content

> As respostas do Connected Content podem ser armazenadas em cache em diferentes campanhas ou mensagens (no mesmo espaço de trabalho) para otimizar a velocidade de envio.

O Braze não registra nem armazena permanentemente **os corpos de resposta do** Connected Content. Durante a renderização da mensagem, as respostas podem ser mantidas temporariamente (por exemplo, na memória e no cache) para que o Braze possa renderizar o Liquid e enviar a mensagem.

Para evitar o armazenamento em cache, você pode especificar `:no_cache`, o que pode aumentar o tráfego de rede. Para ajudar a solucionar problemas e monitorar a integridade do sistema, o Braze registra os metadados da solicitação de Connected Content (como o URL da solicitação totalmente renderizado e o código de status da resposta) para chamadas bem-sucedidas e com falha. Esses registros são mantidos por até 30 dias.

{% details Connected Content rendering and data handling (advanced) %}
Esta seção fornece uma visão mais detalhada, de ponta a ponta, de como o Braze renderiza Liquid e Connected Content e onde os dados podem existir temporariamente antes de uma mensagem ser enviada. Isso pode ajudar nas revisões de privacidade e manuseio de dados.

#### O que é e o que não é armazenado

- **Corpo da resposta do Connected Content:** Não armazenado permanentemente pelo Braze. Ele pode ser mantido temporariamente na memória e, quando a capacitação é ativada, armazenado no cache com um TTL (time-to-live).
- **Metadados de solicitação de conteúdo conectado:** Os metadados da solicitação, como o URL totalmente renderizado, o código de status HTTP e a duração da resposta, são registrados para solução de problemas e monitoramento. Esses registros são mantidos por até 30 dias. 
- **Envio de mensagens finais:** Existe na memória durante a renderização. Isso também pode ser armazenado em outro lugar, dependendo da sua configuração e do canal (por exemplo, Message Archiving ou cartões de conteúdo).

#### Fluxo de renderização (alto nível)

O fluxo a seguir descreve como o Braze renderiza e envia mensagens para canais baseados em provedores, como e-mail, SMS e push. Os canais fornecidos pelo SDK, como os cartões de conteúdo, usam a mesma renderização subjacente do Liquid e do Connected Content, mas diferem no momento em que o conteúdo é gerado e na forma como é fornecido.

1. Um trabalhador em segundo plano renderiza o modelo Liquid de uma mensagem quando a mensagem está preparada para ser entregue.
2. As tags Connected Content são avaliadas durante a renderização do Liquid.
3. Para cada tag de conteúdo conectado, o Braze verifica um cache de várias camadas. Se não houver nenhum valor em cache (ou se o cache estiver desativado), o Braze chamará seu endpoint e receberá a resposta.
4. A resposta é injetada no modelo Liquid e a mensagem é totalmente renderizada.
5. Para canais baseados em provedor, a mensagem renderizada é enviada para o provedor do canal e, em seguida, para o usuário. Para canais fornecidos por SDK, como os cartões de conteúdo, o conteúdo renderizado é sincronizado com o Braze SDK e pode ser gerado na primeira impressão ou no momento da exibição, momento em que é mostrado ao usuário.

#### Onde as respostas do Connected Content podem residir temporariamente

O Braze usa um cache de várias camadas para respostas de Connected Content com TTLs entre cinco minutos e quatro horas, dependendo do uso do site `:cache_max_age` e de outras regras de cache:

- **Cache de memória em processo:** Cache transitório dentro do processo de trabalho. Os dados podem permanecer apenas durante o trabalho (até cerca de 11 minutos com base no tempo limite do trabalhador).
- **Cache da máquina local:** Um cache por trabalhador, como uma instância local do Memcached.
- **Cache em todo o cluster:** Um cache distribuído compartilhado entre os trabalhadores, como um cluster do Memcached.

Essas camadas de cache são voláteis e podem despejar dados antes do TTL configurado.

#### O que muda quando você usa `:no_cache`

Para pontos de extremidade que não estão hospedados na infraestrutura do Braze, o uso de `:no_cache` impede que o corpo da resposta do Connected Content seja armazenado no Memcached. Nesses casos, a resposta só permanece na memória do processo de trabalho durante a duração do trabalho de renderização (até cerca de 11 minutos). Para endpoints que resolvem para hosts internos ao Braze, as respostas ainda podem ser armazenadas em cache, conforme descrito em [Cache busting](#cache-busting).

#### Onde o resultado final renderizado pode ficar

- **Envio de mensagens:** Se o Arquivamento de Mensagens estiver ativado, o Braze poderá gravar a mensagem final renderizada em seu bucket de armazenamento em nuvem configurado. Se sua resposta de Connected Content estiver incluída na mensagem renderizada, ela será incluída na cópia arquivada.
- **Dispositivos do usuário:** Após a entrega, o conteúdo da mensagem totalmente renderizado pode persistir nos dispositivos dos usuários por um período de tempo desconhecido.
- **Cartões de conteúdo:** O conteúdo renderizado dos cartões de conteúdo é armazenado em um banco de dados do Braze até que o cartão expire.
{% enddetails %}

## Configurações de cache padrão

A idade do cache é de até cinco minutos (300 segundos). Você pode atualizar isso adicionando o parâmetro `:cache_max_age` à chamada Connected Content. Um exemplo é:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

As solicitações GET são armazenadas em cache. Você pode configurar isso adicionando o parâmetro :no_cache à chamada Connected Content.

As solicitações POST não são armazenadas em cache. Isso pode ser forçado adicionando o parâmetro :cache_max_age à chamada Connected Content. O tempo mínimo de cache é de 5 minutos e o tempo máximo de cache é de 4 horas.

{% alert note %}
As configurações de cache não são garantidas. O armazenamento em cache pode reduzir as chamadas para seus pontos de extremidade, por isso recomendamos o uso de várias chamadas por ponto de extremidade dentro da duração do cache, em vez de depender excessivamente do armazenamento em cache.
{% endalert %}

### Limite de tamanho do cache

O corpo da resposta do Connected Content pode ter até 1 MB. Se o corpo da resposta for maior que 1 MB, ele não será armazenado em cache.

## Tempo de cache 

A Connected Content armazenará em cache o valor que retorna dos pontos de extremidade GET por um mínimo de cinco minutos. Se um tempo de cache não for especificado, o tempo de cache padrão será de cinco minutos.

O tempo de cache do Connected Content pode ser configurado para ser mais longo com :cache_max_age,, conforme mostrado no exemplo a seguir. O tempo mínimo de cache é de cinco minutos e o tempo máximo de cache é de quatro horas. Os dados de conteúdo conectado são armazenados em cache na memória usando um sistema de cache volátil, como o Memcached. 

Como resultado, independentemente do tempo de cache especificado, os dados do Connected Content podem ser removidos do cache em memória do Braze antes do especificado. Isso significa que as durações do cache são sugestões e podem não representar realmente a duração que os dados são garantidos a serem armazenados em cache pelo Braze e você pode ver mais solicitações de Conteúdo Conectado do que pode esperar com uma determinada duração de cache.

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

Com um POST, você não precisa armazenar o busto em cache, pois o Braze nunca armazena em cache os resultados de solicitações POST.

## Coisas para saber

- O armazenamento em cache pode ajudar a reduzir as chamadas duplicadas do Connected Content. No entanto, não é garantido que isso sempre resulte em uma única chamada de Connected Content por usuário.
- O cache do Connected Content é baseado no URL e no espaço de trabalho. Se a chamada do Connected Content for para o URL idêntico, ele poderá ser armazenado em cache em todas as campanhas e telas.
- O cache é baseado em um URL exclusivo, não em um ID de usuário ou campanha. Isso significa que a versão em cache de uma chamada de Connected Content pode ser usada por vários usuários e campanhas em um espaço de trabalho se o URL for o mesmo.

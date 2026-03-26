---
nav_title: Armazenando respostas em cache
article_title: Respostas de Conteúdo conectado em cache
page_order: 2.5
description: "Este artigo aborda como armazenar em cache as respostas de Conteúdo conectado em diferentes campanhas ou mensagens no mesmo espaço de trabalho para otimizar as velocidades de envio."
---

# Respostas de Conteúdo conectado em cache

> As respostas de Conteúdo conectado podem ser armazenadas em cache em diferentes campanhas ou mensagens (no mesmo espaço de trabalho) para otimizar as velocidades de envio.

A Braze não registra nem armazena permanentemente os **corpos de resposta** de Conteúdo conectado. Durante a renderização da mensagem, as respostas podem ser mantidas temporariamente (por exemplo, na memória e em cache) para que a Braze possa renderizar o Liquid e enviar a mensagem.

Para evitar o armazenamento em cache, você pode especificar `:no_cache`, o que pode causar um aumento no tráfego de rede. Para ajudar na solução de problemas e no monitoramento da integridade do sistema, a Braze registra os metadados de solicitação de Conteúdo conectado (como a URL da solicitação totalmente renderizada e o código de status da resposta) para chamadas bem-sucedidas e com falha. Esses registros são mantidos por até 30 dias.

{% details Connected Content rendering and data handling (advanced) %}
Esta seção fornece uma visão mais detalhada, de ponta a ponta, de como a Braze renderiza Liquid e Conteúdo conectado e onde os dados podem existir temporariamente antes que uma mensagem seja enviada. Isso pode ajudar em revisões de privacidade e tratamento de dados.

#### O que é e o que não é armazenado

- **Corpo da resposta de Conteúdo conectado:** Não é armazenado permanentemente pela Braze. Pode ser mantido temporariamente na memória e, quando o cache está ativado, armazenado em cache com um tempo de vida (TTL).
- **Metadados da solicitação de Conteúdo conectado:** Os metadados da solicitação, como a URL totalmente renderizada, código de status HTTP e duração da resposta, são registrados para solução de problemas e monitoramento. Esses registros são mantidos por até 30 dias. 
- **Mensagem final renderizada:** Existe na memória durante a renderização. Também pode ser armazenada em outro lugar, dependendo da sua configuração e canal (por exemplo, Arquivamento de Mensagens ou Cartões de conteúdo).

#### Fluxo de renderização (visão geral)

O fluxo a seguir descreve como a Braze renderiza e envia mensagens para canais baseados em provedores, como e-mail, SMS e push. Canais entregues pelo SDK, como Cartões de conteúdo, usam a mesma renderização subjacente de Liquid e Conteúdo conectado, mas diferem em quando o conteúdo é gerado e como é entregue.

1. Um worker em segundo plano renderiza o modelo Liquid para uma mensagem quando ela está preparada para ser entregue.
2. As tags de Conteúdo conectado são avaliadas durante a renderização do Liquid.
3. Para cada tag de Conteúdo conectado, a Braze verifica um cache em múltiplas camadas. Se nenhum valor em cache existir (ou se o cache estiver desativado), a Braze chama seu endpoint e recebe a resposta.
4. A resposta é injetada no modelo Liquid e a mensagem é totalmente renderizada.
5. Para canais baseados em provedores, a mensagem renderizada é enviada ao provedor do canal e, em seguida, ao usuário. Para canais entregues pelo SDK, como Cartões de conteúdo, o conteúdo renderizado é sincronizado com o SDK da Braze e pode ser gerado na primeira impressão ou no momento da exibição, quando então é mostrado ao usuário.

#### Onde as respostas de Conteúdo conectado podem existir temporariamente

A Braze usa um cache em múltiplas camadas para respostas de Conteúdo conectado com TTLs entre cinco minutos e quatro horas, dependendo do seu uso de `:cache_max_age` e outras regras de cache:

- **Cache de memória em processo:** Cache transitório dentro do processo do worker. Os dados existem apenas durante a duração do trabalho (até ~11 minutos com base no tempo limite do worker).
- **Cache local da máquina:** Um cache por worker, como uma instância local do Memcached.
- **Cache em cluster:** Um cache distribuído compartilhado entre workers, como um cluster do Memcached.

Essas camadas de cache são voláteis e podem remover dados antes do TTL configurado.

#### O que muda quando você usa `:no_cache`

Para endpoints que não estão hospedados dentro da infraestrutura da Braze, usar `:no_cache` impede que o corpo da resposta do Conteúdo conectado seja armazenado no Memcached. Nesses casos, a resposta só existe na memória do processo do worker durante a duração do trabalho de renderização (até ~11 minutos). Para endpoints que resolvem para hosts internos da Braze, as respostas ainda podem ser armazenadas em cache conforme descrito em [Cache busting](#cache-busting).

#### Onde a saída final renderizada pode existir

- **Arquivamento de Mensagens:** Se o Arquivamento de Mensagens estiver ativado, a Braze pode gravar a mensagem final renderizada no seu bucket de armazenamento em nuvem configurado. Se sua resposta de Conteúdo conectado estiver incluída na mensagem renderizada, ela será incluída na cópia arquivada.
- **Dispositivos dos usuários:** Após a entrega, o conteúdo totalmente renderizado da mensagem pode persistir nos dispositivos dos usuários por um tempo indeterminado.
- **Cartões de conteúdo:** O conteúdo renderizado para Cartões de conteúdo é armazenado em um banco de dados da Braze até que o cartão expire.
{% enddetails %}

## Configurações de cache padrão

A idade do cache é de até cinco minutos (300 segundos). Você pode atualizar isso adicionando o parâmetro `:cache_max_age` à chamada de Conteúdo conectado. Um exemplo:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

As requisições GET são armazenadas em cache. Você pode configurar isso adicionando o parâmetro `:no_cache` à chamada de Conteúdo conectado.

As requisições POST não são armazenadas em cache por padrão, mas podem ser armazenadas adicionando o parâmetro `:cache_max_age` à chamada de Conteúdo conectado. O tempo mínimo de cache é de 5 minutos, e o tempo máximo de cache é de 4 horas.

{% alert note %}
As configurações de cache não são garantidas. O cache pode reduzir chamadas para seus endpoints, então recomendamos usar múltiplas chamadas por endpoint dentro da duração do cache em vez de depender excessivamente do cache.
{% endalert %}

### Limite de tamanho do cache

O corpo da resposta do Conteúdo conectado pode ter até 1&nbsp;MB. Se o corpo da resposta for maior que 1&nbsp;MB, ele não será armazenado em cache.

## Tempo de cache 

O Conteúdo conectado armazenará em cache o valor retornado dos endpoints GET por um mínimo de cinco minutos. Se um tempo de cache não for especificado, o tempo de cache padrão é de cinco minutos.

O tempo de cache do Conteúdo conectado pode ser configurado para ser mais longo com `:cache_max_age`, como mostrado no exemplo a seguir. O tempo mínimo de cache é de cinco minutos e o tempo máximo de cache é de quatro horas. Os dados de Conteúdo conectado são armazenados em cache na memória usando um sistema de cache volátil, como o Memcached. 

Como resultado, independentemente do tempo de cache especificado, os dados do Conteúdo conectado podem ser removidos do cache em memória da Braze antes do previsto. Isso significa que as durações do cache são sugestões e podem não representar de fato a duração pela qual os dados ficam armazenados em cache pela Braze. Você pode ver mais solicitações de Conteúdo conectado do que esperaria com uma determinada duração de cache.

### Cache por segundos especificados

Este exemplo será armazenado em cache por 900 segundos (ou 15 minutos).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Cache busting

Para evitar que o Conteúdo conectado armazene em cache o valor retornado de uma solicitação GET, você pode usar a configuração `:no_cache`. No entanto, as respostas de hosts internos da Braze ainda serão armazenadas em cache.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Certifique-se de que o endpoint de Conteúdo conectado fornecido pode lidar com grandes picos de tráfego antes de usar esta opção, ou você provavelmente verá um aumento na latência de envio (atrasos maiores ou intervalos de tempo mais amplos entre a solicitação e a resposta) devido à Braze fazer solicitações de Conteúdo conectado para cada mensagem individual.
{% endalert %}

Com um POST, você não precisa se preocupar com o cache busting, pois as requisições POST não são armazenadas em cache por padrão. Para armazenar em cache uma resposta POST, adicione `:cache_max_age`; para evitar o cache de um POST, omita `:cache_max_age`.

## Bom saber

- O cache pode ajudar a reduzir chamadas duplicadas de Conteúdo conectado. No entanto, não é garantido que sempre resulte em uma única chamada de Conteúdo conectado por usuário.
- O cache do Conteúdo conectado é baseado na URL e no espaço de trabalho. Se a chamada do Conteúdo conectado for para a mesma URL, ela pode ser armazenada em cache entre campanhas e Canvas.
- O cache é baseado em uma URL única, não em um ID de usuário ou campanha. Isso significa que a versão em cache de uma chamada de Conteúdo conectado pode ser usada entre múltiplos usuários e campanhas em um espaço de trabalho se a URL for a mesma.
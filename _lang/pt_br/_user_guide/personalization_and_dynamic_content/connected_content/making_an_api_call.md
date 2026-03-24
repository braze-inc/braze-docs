---
nav_title: Como fazer uma chamada de conteúdo conectado
article_title: Como fazer uma chamada para a API Connected Content
page_order: 0
description: "Este artigo de referência aborda como fazer uma chamada à API Connected Content, bem como exemplos úteis e casos de uso avançados do Conteúdo conectado."
search_rank: 2
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"} Fazer uma chamada à API de Conteúdo conectado

> Use o Conteúdo conectado para inserir qualquer informação acessível pela API diretamente nas mensagens enviadas aos usuários. Você pode extrair conteúdo diretamente do seu servidor da Web ou de APIs acessíveis publicamente.<br><br>Esta página aborda como fazer chamadas à API de Conteúdo conectado, casos de uso avançados do Conteúdo conectado, tratamento de erros e muito mais.

## Entendendo o volume de chamadas do Conteúdo conectado

{% alert important %}
Um envio não equivale a uma chamada de Conteúdo conectado. A Braze não garante uma proporção de 1:1 entre envios de mensagens e solicitações de Conteúdo conectado. O sistema é projetado para priorizar a renderização e a entrega corretas das mensagens em vez de minimizar o número de chamadas. Seus endpoints devem ser construídos para lidar com mais solicitações do que o número de destinatários ou mensagens enviadas.
{% endalert %}

A Braze pode fazer a mesma chamada à API de Conteúdo conectado mais de uma vez por destinatário. Os motivos comuns incluem:

- **E-mail com várias partes:** Um único e-mail pode disparar passes de renderização separados para o corpo HTML, o corpo de texto simples e a versão Accelerated Mobile Pages (AMP) (se presente). Cada passe pode disparar o Conteúdo conectado naquela parte, então um destinatário pode gerar múltiplas chamadas idênticas ou semelhantes.
- **Validação e novas tentativas:** As cargas úteis de mensagens podem ser renderizadas várias vezes por destinatário para validação, lógica de nova tentativa ou outros fins internos.
- **Comportamento do canal:** O Conteúdo conectado é executado quando a mensagem é renderizada. Para mensagens no app, a mensagem é renderizada no momento da impressão.

Se você vir mais chamadas de Conteúdo conectado nos seus registros do que envios ou destinatários, esse comportamento é esperado. Para orientações sobre como reduzir a carga e planejar para escala, consulte [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints).

## Envio de uma chamada de Conteúdo conectado

{% raw %}

Para enviar uma chamada de Conteúdo conectado, use a tag `{% connected_content %}`. Com essa tag, você pode atribuir ou declarar variáveis usando `:save`. Os aspectos dessas variáveis podem ser referenciados posteriormente na mensagem com [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

Por exemplo, o corpo da mensagem a seguir acessará o URL `http://numbersapi.com/random/trivia` e incluirá um fato curioso na sua mensagem:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Adição de variáveis

Também é possível incluir atributos de perfil de usuário como variáveis na string de URL ao fazer solicitações de Conteúdo conectado. 

Por exemplo, você pode ter um serviço da Web que retorna conteúdo com base no endereço de e-mail e no ID de um usuário. Se estiver passando atributos que contenham caracteres especiais, como o sinal de arroba (@), certifique-se de usar o filtro Liquid `url_param_escape` para substituir quaisquer caracteres não permitidos em URLs por suas versões escapadas amigáveis ao URL, conforme mostrado no seguinte atributo de endereço de e-mail.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Os valores de atributo devem ser cercados por `${}` para funcionar corretamente na nossa versão da sintaxe Liquid.
{% endalert %}

As solicitações de Conteúdo conectado aceitam apenas solicitações GET e POST.

## Tratamento de erros

Se o URL não estiver disponível e chegar a uma página 404, a Braze renderizará uma string vazia em seu lugar. Se o URL chegar a uma página HTTP 500 ou 502, ele falhará na lógica de nova tentativa.

Se o endpoint retornar JSON, você poderá detectar isso verificando se o valor de `connected` é nulo e, em seguida, [abortar condicionalmente a mensagem]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/). A Braze só permite URLs que se comunicam pelas portas 80 (HTTP) e 443 (HTTPS).

### Detecção de host não íntegro

O Conteúdo conectado emprega um mecanismo de detecção de host não íntegro para detectar quando o host de destino apresenta uma alta taxa de lentidão ou sobrecarga significativa, resultando em tempos limite, excesso de solicitações ou outros resultados que impedem a Braze de se comunicar com sucesso com o endpoint de destino. Ele atua como uma salvaguarda para reduzir a carga desnecessária que pode estar causando dificuldades ao host de destino. Ele também serve para estabilizar a infraestrutura da Braze e manter velocidades rápidas de envio de mensagens.

Se o host de destino apresentar uma alta taxa de lentidão significativa ou sobrecarga, a Braze interromperá temporariamente as solicitações ao host de destino por um minuto, simulando respostas que indiquem a falha. Após um minuto, a Braze examinará a integridade do host usando um pequeno número de solicitações antes de retomar as solicitações em velocidade máxima se o host for considerado íntegro. Se o host ainda não estiver íntegro, a Braze aguardará mais um minuto antes de tentar novamente.

Se as solicitações ao host de destino forem interrompidas pelo detector de host não íntegro, a Braze continuará a renderizar mensagens e a seguir sua lógica Liquid como se tivesse recebido um código de resposta de erro. Se você quiser garantir que essas solicitações de Conteúdo conectado sejam repetidas quando forem interrompidas pelo detector de host não íntegro, use a opção `:retry`. Para saber mais sobre a opção `:retry`, consulte [Tentativas de Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Se achar que a detecção de host não íntegro pode estar causando problemas, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact/).

{% alert note %}
Você pode adicionar URLs específicos a uma lista de permissões para serem usados com o Conteúdo conectado. Para acessar esse recurso, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

{% alert tip %}
Visite [Solução de problemas de solicitações de webhook e Conteúdo conectado]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) para saber mais sobre como solucionar problemas de códigos de erro comuns.
{% endalert %}

### Limites de taxa (429) versus detecção de host não íntegro

Os seguintes são mecanismos diferentes:

- **429 Too Many Requests:** Seu endpoint (ou um serviço upstream) está retornando essa resposta. Isso significa que seu servidor ou middleware está recusando tráfego, geralmente porque tem seu próprio limite de taxa. A Braze não aplica um limite de taxa separado ao Conteúdo conectado; o volume de solicitações de Conteúdo conectado escala diretamente com o [limite de taxa de velocidade de entrega]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting). Como as mensagens podem ser renderizadas várias vezes por destinatário (por exemplo, para HTML de e-mail, texto simples e AMP), o número de solicitações de Conteúdo conectado pode exceder esse limite de taxa — não assuma que será menor ou igual às mensagens por minuto que você definiu. Se você estiver vendo 429s, escale seu endpoint ou middleware para lidar com o volume de solicitações esperado, ou reduza o limite de taxa da campanha ou etapa do canva para que menos mensagens (e, portanto, menos chamadas de Conteúdo conectado) sejam enviadas por minuto.
- **Detecção de host não íntegro:** Uma salvaguarda do lado da Braze que é acionada após uma alta taxa e volume de *falhas* em uma janela de um minuto. A contagem de falhas inclui os códigos de status `408`, `429`, `502`, `503`, `504` e `529`. Quando acionada, a Braze interrompe temporariamente as solicitações a esse host e simula uma resposta de falha. Isso é independente do seu próprio limite de taxa. Para limites de detecção e mais detalhes, consulte [Solução de problemas de solicitações de webhook e Conteúdo conectado]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/#unhealthy-host-detection). Para evitar acionar a detecção de host não íntegro, certifique-se de que seu endpoint pode lidar com o volume de chamadas descrito em [Entendendo o volume de chamadas do Conteúdo conectado](#understanding-connected-content-call-volume) e [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints).

## Permitindo uma performance eficiente

Como a Braze entrega mensagens em uma velocidade muito rápida, certifique-se de que seu servidor possa lidar com milhares de conexões simultâneas para que não fique sobrecarregado ao baixar o conteúdo. Ao usar APIs públicas, confirme que seu uso não violará nenhum limite de taxa que o provedor de API possa empregar. A Braze exige que o tempo de resposta do servidor seja inferior a dois segundos por motivos de performance; se o servidor demorar mais de dois segundos para responder, o conteúdo não será inserido.

Para saber mais sobre planejamento de capacidade de endpoints e redução do volume de chamadas, consulte [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints).

## Coisas para saber

* A Braze não cobra por chamadas de API e elas não serão contabilizadas no seu uso de pontos de dados.
* Há um limite de 1 MB para as respostas do Conteúdo conectado.
* O Conteúdo conectado é executado quando a mensagem é renderizada. Para mensagens no app, a mensagem é renderizada no momento da impressão.
* As chamadas de Conteúdo conectado não seguem redirecionamentos.

## Práticas recomendadas para endpoints de alto volume

Se suas mensagens usam Conteúdo conectado e você envia em alto volume, planeje para mais solicitações do que o número de destinatários ou envios:

1. **Estime a carga de pico:** Use um multiplicador conservador ao dimensionar seu endpoint ou middleware — as solicitações de Conteúdo conectado podem exceder o número de destinatários ou mensagens enviadas. Por exemplo, para e-mail, um único destinatário pode gerar múltiplas chamadas (HTML, texto simples e AMP), então destinatários × 2 ou × 3 é frequentemente usado como uma estimativa conservadora.
2. **Use cache quando apropriado:** Solicitações GET são armazenadas em cache por padrão. Para solicitações POST, adicione `:cache_max_age` quando a resposta puder ser reutilizada por um período (por exemplo, token ou conteúdo que não muda por solicitação). Consulte [Armazenamento de respostas em cache]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/) e as [Perguntas frequentes sobre cache de POST](#what-is-caching-behavior) abaixo.
3. **Defina o limite de taxa de velocidade de entrega:** O [limite de taxa de velocidade de entrega]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) em campanhas ou etapas do canva é a única alavanca para limitar indiretamente o volume de solicitações de Conteúdo conectado — a Braze não limita a taxa do Conteúdo conectado em si. É apenas um proxy, e não perfeito, porque as solicitações de Conteúdo conectado não são 1:1 com as mensagens. Use-o para manter o volume de mensagens (e, portanto, de Conteúdo conectado) dentro do que seu endpoint pode suportar.
4. **Projete para idempotência e novas tentativas:** A Braze pode chamar seu endpoint mais de uma vez por destinatário. Certifique-se de que seu endpoint pode tolerar solicitações duplicadas sem efeitos colaterais incorretos.

## Tipos de autenticação

### Usando a autenticação básica

Se o URL exigir autenticação básica, a Braze poderá armazenar uma credencial de autenticação básica para você usar em sua chamada à API. Você pode gerenciar as credenciais de autenticação básica existentes e adicionar novas credenciais em **Configurações** > **Conteúdo conectado**.

![As configurações do Conteúdo conectado no dashboard da Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Para adicionar uma nova credencial, selecione **Adicionar credencial** > **Autenticação básica**. 

![Menu suspenso "Adicionar credencial" com a opção de usar autenticação básica ou autenticação de token.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Dê um nome à sua credencial e digite o nome de usuário e a senha.

![A janela "Criar nova credencial" com a opção de inserir um nome, nome de usuário e senha.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Em seguida, você pode usar essa credencial de autenticação básica em suas chamadas de API fazendo referência ao nome do token:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Se você excluir uma credencial, lembre-se de que todas as chamadas de Conteúdo conectado que tentarem usá-la serão abortadas.
{% endalert %}

### Uso de autenticação por token

Ao usar o Conteúdo conectado da Braze, você poderá descobrir que certas APIs exigem um token em vez de um nome de usuário e senha. A Braze também pode armazenar credenciais que contêm valores de cabeçalho de autenticação de token.

Para adicionar uma credencial que contenha valores de token, selecione **Adicionar credencial** > **Autenticação de token**. Em seguida, adicione os pares de chave-valor para seus cabeçalhos de chamada de API e o domínio permitido.

![Um exemplo de token "token_credential_abc" com detalhes de autenticação de token.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Em seguida, você pode usar essa credencial em suas chamadas de API fazendo referência ao nome da credencial:

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Uso de Open Authentication (OAuth)

Algumas configurações de API exigem a recuperação de um token de acesso que pode ser usado para autenticar o endpoint da API que você deseja acessar.

#### Etapa 1: Recuperar o token de acesso

O exemplo a seguir ilustra a recuperação e o salvamento de um token de acesso em uma variável local, que pode ser usada para autenticar a chamada subsequente à API. Um parâmetro `:cache_max_age` pode ser adicionado para corresponder ao tempo de validade do token de acesso e reduzir o número de chamadas de saída do Conteúdo conectado. Para saber mais, consulte [Cache configurável]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching).

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Etapa 2: Autorizar a API usando o token de acesso recuperado

Depois que o token é salvo, ele pode ser modelado dinamicamente na chamada subsequente do Conteúdo conectado para autorizar a solicitação:

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

### Edição de credenciais

Você pode editar o nome da credencial para os tipos de autenticação.

- Para autenticação básica, é possível atualizar o nome de usuário e a senha. Note que a senha inserida anteriormente não estará visível.
- Para a autenticação de token, você pode atualizar os pares de chave-valor do cabeçalho e o domínio permitido. Observe que os valores de cabeçalho definidos anteriormente não estarão visíveis.

![A opção de editar credenciais.]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## Lista de permissões de IP do Conteúdo conectado

Quando uma mensagem usando Conteúdo conectado é enviada pela Braze, os servidores da Braze automaticamente fazem solicitações de rede aos servidores dos nossos clientes ou de terceiros para extrair dados. Com a lista de permissões de IP, você pode verificar se as solicitações de Conteúdo conectado estão realmente vindo da Braze, adicionando uma camada de segurança.

A Braze enviará solicitações de Conteúdo conectado dos seguintes intervalos de IP. Os intervalos listados são automática e dinamicamente adicionados a quaisquer chaves de API que tenham sido aceitas para a lista de permissões. 

A Braze tem um conjunto reservado de IPs usados para todos os serviços, sendo que nem todos estão ativos em um determinado momento. Isso foi projetado para que a Braze possa enviar de um data center diferente ou fazer manutenção, se necessário, sem afetar os clientes. A Braze poderá usar um, um subconjunto ou todos os seguintes IPs listados ao fazer solicitações de Conteúdo conectado.

{% multi_lang_include data_centers.md datacenters='ips' %}

### Cabeçalho `User-Agent`

A Braze inclui um cabeçalho `User-Agent` em todas as solicitações de Conteúdo conectado e webhook que é semelhante ao seguinte:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Lembre-se de que o valor do hash muda regularmente. Se estiver filtrando o tráfego por `User-Agent`, permita todos os valores que começam com `Braze Sender`.
{% endalert %}

## Solução de problemas

Use [Webhook.site](https://webhook.site/) para solucionar problemas nas suas chamadas de Conteúdo conectado. 

1. Altere o URL na sua chamada de Conteúdo conectado pelo URL exclusivo gerado no site.
2. Faça uma prévia e teste sua campanha ou etapa do canva para ver as solicitações que chegam a este site.

Usando essa ferramenta, você pode diagnosticar problemas com os cabeçalhos de solicitação, o corpo da solicitação e outras informações que estão sendo enviadas na chamada.

## Perguntas frequentes

### Por que há mais chamadas de Conteúdo conectado do que usuários ou envios? 

Esse é um comportamento esperado. A Braze pode fazer a mesma chamada à API de Conteúdo conectado mais de uma vez por destinatário porque as cargas úteis de mensagens podem ser renderizadas várias vezes (por exemplo, para HTML de e-mail, texto simples e AMP; para validação ou lógica de nova tentativa; ou outros fins internos). Não há uma proporção garantida de 1:1 entre envios e chamadas de Conteúdo conectado. Consulte [Entendendo o volume de chamadas do Conteúdo conectado](#understanding-connected-content-call-volume) e [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints) para detalhes e mitigação.

### Como o limite de taxa funciona com o Conteúdo conectado?

O Conteúdo conectado não tem seu próprio limite de taxa. Em vez disso, o limite de taxa é baseado na taxa de envio de mensagens. Recomendamos definir o limite de taxa de envio de mensagens abaixo do limite de taxa de Conteúdo conectado pretendido se houver mais chamadas de Conteúdo conectado do que mensagens enviadas.  

### Qual é o comportamento de cache?

Solicitações GET são armazenadas em cache por padrão (consulte [Armazenamento de respostas em cache]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/)). **Solicitações POST não são armazenadas em cache por padrão**, mas você pode ativar o cache adicionando `:cache_max_age` à chamada de Conteúdo conectado. Isso pode reduzir a carga no endpoint quando o mesmo POST (por exemplo, uma solicitação de token ou conteúdo) seria feito repetidamente dentro da janela de cache.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

O cache pode ajudar a reduzir chamadas duplicadas de Conteúdo conectado, mas não é garantido que resulte em uma única chamada por usuário. A duração do cache é entre cinco minutos e quatro horas. Para detalhes completos, consulte [Armazenamento de respostas em cache]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/).

### Qual é o comportamento padrão do HTTP do Conteúdo conectado? 

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}
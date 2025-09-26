---
nav_title: Como fazer uma chamada de conteúdo conectado
article_title: Como fazer uma chamada para a API Connected Content
page_order: 0
description: "Este artigo de referência aborda como fazer uma chamada à API Connected Content, bem como exemplos úteis e casos de uso avançados da conteúdo conectado."
search_rank: 2
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %}](https://learning.braze.com/connected-content) ){: style="float:right;width:120px;border:0;" class="noimgborder"}Fazer uma chamada da API de conteúdo conectado

> Use o Connected Content para inserir qualquer informação acessível pela API diretamente nas mensagens enviadas aos usuários. Você pode extrair conteúdo diretamente de seu servidor da Web ou de APIs acessíveis publicamente.<br><br>Esta página aborda como fazer chamadas à Connected Content API, casos de uso avançados da Connected Content, tratamento de erros e muito mais.

## Envio de uma chamada de Connected Content

{% raw %}

Para enviar uma chamada de conteúdo conectado, use a tag `{% connected_content %}`. Com essa tag, você pode atribuir ou declarar variáveis usando `:save`. Os aspectos dessas variáveis podem ser referenciados posteriormente na mensagem com [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

Por exemplo, o corpo da mensagem a seguir acessará o URL `http://numbersapi.com/random/trivia` e incluirá um fato curioso na sua mensagem:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Adição de variáveis

Também é possível incluir atribuições de perfil de usuário como variáveis na string de URL ao fazer solicitações de Connected Content. 

Por exemplo, você pode ter um serviço da Web que retorna conteúdo com base no endereço de e-mail e no ID de um usuário. Se estiver passando atribuições que contenham caracteres especiais, como o sinal de arroba (@), certifique-se de usar o filtro Liquid `url_param_escape` para substituir quaisquer caracteres não permitidos em URLs por suas versões escapadas amigáveis ao URL, conforme mostrado no seguinte atributo de endereço de e-mail.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Os valores de atribuição devem ser cercados por `${}` para funcionar corretamente em nossa versão da sintaxe Liquid.
{% endalert %}

As solicitações de conteúdo conectado aceitam apenas solicitações GET e POST.

## Tratamento de erros

Se o URL não estiver disponível e chegar a uma página 404, a Braze renderizará uma string vazia em seu lugar. Se o URL chegar a uma página HTTP 500 ou 502, ele falhará na lógica de nova tentativa.

Se o ponto de extremidade retornar JSON, você poderá detectar isso verificando se o valor de `connected` é nulo e, em seguida, [abortar condicionalmente a mensagem]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/). A Braze só permite URLs que se comunicam pelas portas 80 (HTTP) e 443 (HTTPS).

### Detecção de host não saudável

O Connected Content emprega um mecanismo de detecção de host não saudável para detectar quando o host de destino apresenta uma alta taxa de lentidão ou sobrecarga significativa, resultando em tempos limite, excesso de solicitações ou outros resultados que impedem que o Braze se comunique com sucesso com o endpoint de destino. Ele atua como uma salvaguarda para reduzir a carga desnecessária que pode estar causando dificuldades ao host de destino. Ele também serve para estabilizar a infraestrutura do Braze e manter velocidades rápidas de envio de mensagens.

Se o host de destino apresentar uma alta taxa de lentidão significativa ou sobrecarga, o Braze interromperá temporariamente as solicitações ao host de destino por um minuto, simulando respostas que indiquem a falha. Após um minuto, o Braze examinará a integridade do host usando um pequeno número de solicitações antes de retomar as solicitações em velocidade máxima se o host for considerado íntegro. Se o host ainda não estiver saudável, o Braze aguardará mais um minuto antes de tentar novamente.

Se as solicitações ao host de destino forem interrompidas pelo detector de host não saudável, o Braze continuará a renderizar mensagens e a seguir sua lógica Liquid como se tivesse recebido um código de resposta de erro. Se você quiser garantir que essas solicitações de Connected Content sejam repetidas quando forem interrompidas pelo detector de host não saudável, use a opção `:retry`. Para saber mais sobre a opção `:retry`, consulte [Tentativas de Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Se achar que a detecção de host não saudável pode estar causando problemas, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact/).

{% alert tip %}
Visite [Solução de problemas de solicitações de webhook e Connected Content]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) para saber mais sobre como solucionar problemas de códigos de erro comuns.
{% endalert %}

## Permitindo uma performance eficiente

Como o Braze entrega mensagens em uma velocidade muito rápida, certifique-se de que seu servidor possa lidar com milhares de conexões simultâneas para que os servidores não fiquem sobrecarregados ao baixar o conteúdo. Ao usar APIs públicas, confirme que seu uso não violará nenhum limite de frequência que o provedor de API possa empregar. O Braze exige que o tempo de resposta do servidor seja inferior a dois segundos por motivos de performance; se o servidor demorar mais de dois segundos para responder, o conteúdo não será inserido.

Os sistemas Braze podem fazer a mesma chamada à API Connected Content mais de uma vez por destinatário. Isso se deve ao fato de que a Braze pode precisar fazer uma chamada à API Connected Content para renderizar uma carga útil de mensagem, e as cargas úteis de mensagem podem ser renderizadas várias vezes por destinatário para validação, lógica de nova tentativa ou outros fins internos. Seus sistemas devem ser capazes de tolerar que a mesma chamada da Connected Content seja feita mais de uma vez por destinatário.

## Coisas para saber

* A Braze não cobra pelas chamadas de API e não será contabilizada em sua cota de dados.
* Há um limite de 1 MB para as respostas do Connected Content.
* As chamadas do Connected Content ocorrerão quando a mensagem for enviada, exceto no caso de mensagens no app, que farão essa chamada quando a mensagem for visualizada.
* As chamadas de Connected Content não seguem redirecionamentos.

## Tipos de autenticação

### Usando a autenticação básica

Se o URL exigir autenticação básica, a Braze poderá gerar uma credencial de autenticação básica para você usar em sua chamada de API. Você pode gerenciar as credenciais de autenticação básica existentes e adicionar novas credenciais em **Settings** > **Connected Content**.

![As configurações de "Connected Content" no dashboard do Braze.]({% image_buster /assets/img_archive/basic_auth_mgmt.png %})

Para adicionar uma nova credencial, selecione **Adicionar credencial**. Dê um nome à sua credencial e digite o nome de usuário e a senha.

![A janela 'Create New Credential' (Criar nova credencial) com a opção de inserir um nome, um nome de usuário e uma senha.]({% image_buster /assets/img_archive/basic_auth_token.png %}){: style="max-width:30%" }

Em seguida, você pode usar essa credencial de autenticação básica em suas chamadas de API fazendo referência ao nome do token:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Se você excluir uma credencial, lembre-se de que todas as chamadas de conteúdo conectado que tentarem usá-la serão abortadas.
{% endalert %}

### Uso de autenticação por token

Ao usar o conteúdo conectado na Braze, você poderá descobrir que certas APIs exigem um token em vez de um nome de usuário e senha. Incluído na chamada a seguir está um trecho de código para fazer referência e modelar suas mensagens.

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://your_API_link_here/
     :method post
     :headers {
       "X-App-Id": "YOUR-APP-ID",
       "X-App-Token": "YOUR-APP-TOKEN"
     }
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Uso de autenticação aberta (OAuth)

Algumas configurações de API exigem a recuperação de um token de acesso que pode ser usado para autenticar o endpoint da API que você deseja acessar.

#### Etapa 1: Recuperar o token de acesso

O exemplo a seguir ilustra a recuperação e o salvamento de um token de acesso em uma variável de localização, que pode ser usada para autenticar a chamada subsequente à API. Um parâmetro `:cache_max_age` pode ser adicionado para corresponder ao tempo de validade do token de acesso e reduzir o número de chamadas de saída do conteúdo conectado. Para saber mais, consulte [Cache configurável]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching).

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "Bearer YOUR-APP-TOKEN"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Etapa 2: Autorizar a API usando o token de acesso recuperado

Depois que o token é salvo, ele pode ser modelado dinamicamente na chamada subsequente do Connected Content para autorizar a solicitação:

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

## Lista de permissões de IP de conteúdo conectado

Quando uma mensagem usando Conteúdo Conectado é enviada pelo Braze, os servidores do Braze automaticamente fazem solicitações de rede aos servidores de nossos clientes ou de terceiros para extrair dados. Com a lista de permissões de IP, você pode verificar se as solicitações de conteúdo conectado estão realmente vindo da Braze, acrescentando uma camada adicional de segurança.

A Braze enviará solicitações de conteúdo conectado dos seguintes intervalos de IP. Os intervalos listados são automática e dinamicamente adicionados a quaisquer chaves de API que tenham sido aceitas para a listagem de permissões. 

A Braze tem um conjunto reservado de IPs usados para todos os serviços, sendo que nem todos estão ativos em um determinado momento. Isso foi projetado para que a Braze envie de um data center diferente ou faça manutenção, se necessário, sem afetar os clientes. A Braze poderá usar um, um subconjunto ou todos os seguintes IPs listados ao fazer solicitações de conteúdo conectado.

{% multi_lang_include data_centers.md datacenters='ips' %}

## Solução de problemas

Use [Webhook.site](https://webhook.site/) para solucionar problemas em suas chamadas de conteúdo conectado. 

1. Altere a URL em sua chamada de Connected Content com a URL exclusiva gerada no site.
2. Faça uma prévia e teste sua campanha ou etapa do canva para ver as solicitações que chegam a este site.

Usando essa ferramenta, você pode diagnosticar problemas com os cabeçalhos de solicitação, o corpo da solicitação e outras informações que estão sendo enviadas na chamada.

## Perguntas frequentes

### Por que há mais chamadas de Connected Content do que usuários ou envios? 

O Braze pode fazer a mesma chamada à Connected Content API mais de uma vez por destinatário porque talvez seja necessário fazer uma chamada à Connected Content API para renderizar uma carga útil de mensagem. As cargas úteis de mensagens podem ser processadas várias vezes por destinatário para validação, lógica de nova tentativa ou outros fins internos.

Espera-se que uma chamada à Connected Content API possa ser feita mais de uma vez por destinatário, mesmo que a lógica de repetição não seja usada na chamada. Recomendamos definir o limite de frequência de qualquer mensagem que contenha Conteúdo Conectado ou configurar seus servidores para que sejam mais capazes de lidar com o volume esperado.

### Como o limite de frequência funciona com o Connected Content?

O Connected Content não tem seu próprio limite de frequência. Em vez disso, o limite de frequência é baseado na taxa de envio de mensagens. Recomendamos definir o limite de frequência de envio de mensagens abaixo do limite de frequência de Connected Content pretendido se houver mais chamadas de Connected Content do que mensagens enviadas.  

### O que é comportamento de cache?

Por padrão, as solicitações POST não são armazenadas em cache. No entanto, você pode adicionar o parâmetro `:cache_max_age` para forçar a chamada POST para o cache.
O armazenamento em cache pode ajudar a reduzir as chamadas duplicadas do Connected Content. No entanto, não é garantido que isso sempre resulte em uma única chamada de Connected Content por usuário.


[16]: [success@braze.com](mailto:success@braze.com)

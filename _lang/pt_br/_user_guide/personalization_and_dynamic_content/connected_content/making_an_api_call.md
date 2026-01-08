---
nav_title: Fazendo uma chamada de Conteúdo Conectado
article_title: Fazendo uma Chamada de API de Conteúdo Conectado
page_order: 0
description: "Este artigo de referência cobre como fazer uma chamada de API de Conteúdo Conectado, bem como exemplos úteis e casos de uso avançados de Conteúdo Conectado."
search_rank: 2
---

# [![Curso de Aprendizado Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Fazendo uma Chamada de API de Conteúdo Conectado

> Use o Conteúdo Conectado para inserir qualquer informação acessível por API diretamente nas mensagens que você envia aos usuários. Você pode puxar conteúdo diretamente do seu servidor web ou de APIs publicamente acessíveis.<br><br>Esta página cobre como fazer chamadas de API de Conteúdo Conectado, casos de uso avançados de Conteúdo Conectado, tratamento de erros e mais.

## Enviando uma chamada de Conteúdo Conectado

{% raw %}

Para enviar uma chamada de Conteúdo Conectado, use a tag `{% connected_content %}`. Com esta tag, você pode atribuir ou declarar variáveis usando `:save`. Aspectos dessas variáveis podem ser referenciados mais tarde na mensagem com [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

Por exemplo, o seguinte corpo da mensagem acessará a URL `http://numbersapi.com/random/trivia` e incluirá um fato divertido na sua mensagem:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Adicionando variáveis

Você também pode incluir atributos de perfil de usuário como variáveis na string da URL ao fazer solicitações de Conteúdo Conectado. 

Por exemplo, você pode ter um serviço web que retorna conteúdo com base no endereço de e-mail e ID de um usuário. Se você estiver passando atributos contendo caracteres especiais, como o sinal de arroba (@), certifique-se de usar o filtro Liquid `url_param_escape` para substituir quaisquer caracteres não permitidos em URLs por suas versões escapadas amigáveis a URLs, como mostrado no seguinte atributo de endereço de e-mail.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Os valores dos atributos devem estar cercados por `${}` para operar corretamente dentro da nossa versão da sintaxe Liquid.
{% endalert %}

As solicitações de Conteúdo Conectado suportam apenas solicitações GET e POST.

## Tratamento de erros

Se a URL estiver indisponível e atingir uma página 404, o Braze renderizará uma string vazia em seu lugar. Se a URL atingir uma página HTTP 500 ou 502, a URL falhará na lógica de nova tentativa.

Se o endpoint retornar JSON, você pode detectar isso verificando se o valor `connected` é nulo e, em seguida, [abortar condicionalmente a mensagem]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/). O Braze permite apenas URLs que se comunicam pela porta 80 (HTTP) e 443 (HTTPS).

### Detecção de host não saudável

O Conteúdo Conectado emprega um mecanismo de detecção de host não saudável para detectar quando o host de destino experimenta uma alta taxa de lentidão significativa ou sobrecarga, resultando em timeouts, muitas solicitações ou outros resultados que impedem o Braze de se comunicar com sucesso com o endpoint de destino. Isso atua como uma salvaguarda para reduzir a carga desnecessária que pode estar causando dificuldades ao host de destino. Isso também serve para estabilizar a infraestrutura do Braze e manter velocidades de mensagens rápidas.

Se o host de destino experimentar uma alta taxa de lentidão significativa ou sobrecarga, o Braze temporariamente interromperá as solicitações ao host de destino por um minuto, simulando respostas que indicam a falha. Após um minuto, o Braze irá verificar a saúde do host usando um pequeno número de solicitações antes de retomar as solicitações em plena velocidade se o host for considerado saudável. Se o host ainda estiver não saudável, o Braze aguardará mais um minuto antes de tentar novamente.

Se as solicitações ao host de destino forem interrompidas pelo detector de host não saudável, o Braze continuará a renderizar mensagens e seguir sua lógica Liquid como se tivesse recebido um código de resposta de erro. Se você quiser garantir que essas solicitações de Conteúdo Conectado sejam tentadas novamente quando forem interrompidas pelo detector de host não saudável, use a opção `:retry`. Para mais informações sobre a opção `:retry`, veja [tentativas de Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Se você acredita que a detecção de host não saudável pode estar causando problemas, entre em contato com [Suporte Braze]({{site.baseurl}}/support_contact/).

{% alert tip %}
Visite [Resolução de problemas de webhook e solicitações de Conteúdo Conectado]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) para saber mais sobre como solucionar códigos de erro comuns.
{% endalert %}

## Permitindo um desempenho eficiente

Como o Braze entrega mensagens a uma taxa muito rápida, certifique-se de que seu servidor pode lidar com milhares de conexões simultâneas para que os servidores não fiquem sobrecarregados ao baixar conteúdo. Ao usar APIs públicas, confirme que seu uso não violará nenhum limite de taxa que o provedor da API possa empregar. O Braze requer que o tempo de resposta do servidor seja inferior a dois segundos por razões de desempenho; se o servidor demorar mais de dois segundos para responder, o conteúdo não será inserido.

Os sistemas Braze podem fazer a mesma chamada da API de Conteúdo Conectado mais de uma vez por destinatário. Isso ocorre porque o Braze pode precisar fazer uma chamada da API de Conteúdo Conectado para renderizar uma carga de mensagem, e as cargas de mensagem podem ser renderizadas várias vezes por destinatário para validação, lógica de repetição ou outros fins internos. Seus sistemas devem ser capazes de tolerar a mesma chamada de Conteúdo Conectado sendo feita mais de uma vez por destinatário.

## Coisas a saber

* O Braze não cobra por chamadas de API e não contará para o uso de pontos de dados fornecidos.
* Há um limite de 1 MB para respostas de Conteúdo Conectado.
* As chamadas de Conteúdo Conectado ocorrerão quando a mensagem for enviada, exceto para mensagens no aplicativo, que farão essa chamada quando a mensagem for visualizada.
* As chamadas de Conteúdo Conectado não seguem redirecionamentos.

## Tipos de autenticação

### Usando autenticação básica

Se a URL exigir autenticação básica, o Braze pode armazenar uma credencial de autenticação básica para você usar em sua chamada de API. Você pode gerenciar credenciais de autenticação básica existentes e adicionar novas em **Configurações** > **Conteúdo Conectado**.

\![As configurações de Conteúdo Conectado no painel do Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Para adicionar uma nova credencial, selecione **Adicionar credencial** > **Autenticação básica**. 

\!["Dropdown Adicionar credencial" com a opção de usar autenticação básica ou autenticação por token.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Dê um nome à sua credencial e insira o nome de usuário e a senha.

\![A janela "Criar Nova Credencial" com a opção de inserir um nome, nome de usuário e senha.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Você pode então usar essa credencial de autenticação básica em suas chamadas de API referenciando o nome do token:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Se você excluir uma credencial, tenha em mente que qualquer chamada de Conteúdo Conectado que tentar usá-la será abortada.
{% endalert %}

### Usando autenticação por token

{% alert important %}
O tipo de credencial de autenticação por token está atualmente em acesso antecipado. Entre em contato com seu gerente de conta da Braze se estiver interessado em participar deste acesso antecipado.
{% endalert %}

Ao usar o Conteúdo Conectado da Braze, você pode descobrir que certas APIs exigem um token em vez de um nome de usuário e senha. A Braze também pode armazenar credenciais que contêm valores de cabeçalho de autenticação por token.

Para adicionar uma credencial que contém valores de token, selecione **Adicionar credencial** > **Autenticação por token**. Em seguida, adicione os pares chave-valor para os cabeçalhos de chamada da sua API e o domínio permitido.

\![Um exemplo de token "token_credential_abc" com detalhes de autenticação por token.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Você pode então usar essa credencial em suas chamadas de API referenciando o nome da credencial:

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

### Usando Autenticação Aberta (OAuth)

Algumas configurações de API exigem a recuperação de um token de acesso que pode ser usado para autenticar o endpoint da API que você deseja acessar.

#### Passo 1: Recuperar o token de acesso

O seguinte exemplo ilustra a recuperação e o salvamento de um token de acesso em uma variável local, que pode ser usado para autenticar a chamada de API subsequente. Um parâmetro `:cache_max_age` pode ser adicionado para corresponder ao tempo que o token de acesso é válido e reduzir o número de chamadas de Conteúdo Conectado de saída. Veja [Cache Configurável]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching) para mais informações.

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

#### Passo 2: Autorizar a API usando o token de acesso recuperado

Após o token ser salvo, ele pode ser dinamicamente modelado na chamada de Conteúdo Conectado subsequente para autorizar a solicitação:

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

### Editando credenciais

Você pode editar o nome da credencial para tipos de autenticação.

- Para autenticação básica, você pode atualizar o nome de usuário e a senha. Observe que a senha inserida anteriormente não será visível.
- Para autenticação por token, você pode atualizar os pares chave-valor do cabeçalho e o domínio permitido. Observe que os valores de cabeçalho definidos anteriormente não serão visíveis.

\![A opção de editar credenciais.]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## Lista de permissões de IP do Conteúdo Conectado

Quando uma mensagem usando Conteúdo Conectado é enviada do Braze, os servidores do Braze automaticamente fazem solicitações de rede para os servidores de nossos clientes ou de terceiros para recuperar dados. Com a lista de permissões de IP, você pode verificar se as solicitações de Conteúdo Conectado estão realmente vindo do Braze, adicionando uma camada adicional de segurança.

O Braze enviará solicitações de Conteúdo Conectado dos seguintes intervalos de IP. Os intervalos listados são automaticamente e dinamicamente adicionados a quaisquer chaves de API que tenham sido optadas para a lista de permissões. 

O Braze tem um conjunto reservado de IPs usados para todos os serviços, nem todos os quais estão ativos em um determinado momento. Isso é projetado para que o Braze possa enviar de um centro de dados diferente ou fazer manutenção, se necessário, sem impactar os clientes. O Braze pode usar um, um subconjunto ou todos os seguintes IPs listados ao fazer solicitações de Conteúdo Conectado.

{% multi_lang_include data_centers.md datacenters='ips' %}

### `User-Agent` cabeçalho

O Braze inclui um cabeçalho `User-Agent` em todas as solicitações de Conteúdo Conectado e webhook que é semelhante ao seguinte:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Tenha em mente que o valor do hash muda regularmente. Se você estiver filtrando o tráfego por `User-Agent`, permita todos os valores que começam com `Braze Sender`.
{% endalert %}

## Solução de problemas

Use [Webhook.site](https://webhook.site/) para solucionar suas chamadas de Conteúdo Conectado. 

1. Troque a URL em sua chamada de Conteúdo Conectado pela URL única gerada no site.
2. Visualize e teste sua campanha ou etapa do Canvas para ver as solicitações chegarem a este site.

Usando esta ferramenta, você pode diagnosticar problemas com os cabeçalhos de solicitação, corpo da solicitação e outras informações que estão sendo enviadas na chamada.

## Perguntas frequentes

### Por que há mais chamadas de Conteúdo Conectado do que usuários ou envios? 

A Braze pode fazer a mesma chamada da API de Conteúdo Conectado mais de uma vez por destinatário porque pode ser necessário fazer uma chamada da API de Conteúdo Conectado para renderizar um payload de mensagem. Os payloads de mensagem podem ser renderizados várias vezes por destinatário para validação, lógica de repetição ou outros propósitos internos.

É esperado que uma chamada da API de Conteúdo Conectado possa ser feita mais de uma vez por destinatário, mesmo que a lógica de repetição não seja usada na chamada. Recomendamos definir o limite de taxa de qualquer mensagem que contenha Conteúdo Conectado ou configurar seus servidores para lidar melhor com o volume esperado.

### Como funciona a limitação de taxa com Conteúdo Conectado?

Conteúdo Conectado não tem seu próprio limite de taxa. Em vez disso, o limite de taxa é baseado na taxa de envio de mensagens. Recomendamos definir o limite de taxa de mensagens abaixo do seu limite de taxa de Conteúdo Conectado pretendido se houver mais chamadas de Conteúdo Conectado do que mensagens enviadas.  

### Qual é o comportamento de cache?

Por padrão, solicitações POST não armazenam em cache. No entanto, você pode adicionar o parâmetro `:cache_max_age` para forçar a chamada POST a armazenar em cache.

O cache pode ajudar a reduzir chamadas duplicadas de Conteúdo Conectado. No entanto, não é garantido que sempre resulte em uma única chamada de Conteúdo Conectado por usuário.

### Qual é o comportamento padrão do HTTP do Conteúdo Conectado? 

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}

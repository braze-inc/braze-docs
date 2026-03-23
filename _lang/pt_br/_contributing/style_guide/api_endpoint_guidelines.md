---
nav_title: Diretrizes de documentação de endpoints de API
article_title: Diretrizes de documentação de endpoints de API
description: "Diretrizes para documentar endpoints de API da Braze."
page_order: 3
noindex: true
---

# Diretrizes de documentação de endpoints de API

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

> Em geral, a documentação de endpoints de API deve seguir as diretrizes indicadas nas [Diretrizes gerais]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#general-guidelines). No entanto, existem tópicos específicos que podem exigir diretrizes de conteúdo diferentes, listadas neste documento.

A Braze oferece suporte aos seguintes métodos de API REST:

* GET  
* DELETE  
* PATCH  
* POST  
* PUT

## Criando um novo artigo de endpoint

Ao criar um novo artigo de endpoint, certifique-se de também adicionar esse endpoint no [Guia de API da Braze]({{site.baseurl}}/api/home) para que o endpoint seja pesquisável. Navegue até a pasta **`_docs`** **`> _api`** e o arquivo **`> home.md`** para adicionar o endpoint pelo seu caminho e uma descrição de uma frase.

## Referenciando endpoints

Em geral, não existe uma convenção clara para se referir a endpoints na documentação. Ao se referir a endpoints da Braze, use seu melhor julgamento para determinar como referenciar um endpoint dependendo do seu caso de uso.

Você pode se referir a um endpoint pelo seu caminho (por exemplo, `/users/track`) ou pelo nome do endpoint seguido da palavra "endpoint" (por exemplo, o endpoint track user). Se o caminho for especialmente longo, prefira usar o nome do endpoint.

Use estilo de frase ao se referir ao endpoint pelo nome. Use texto de código ao se referir ao endpoint pelo caminho.

Não coloque a palavra "endpoint" em maiúscula, a menos que esteja se referindo diretamente ao nome de uma seção. Não inclua a palavra "API" ao referenciar diretamente um endpoint.

Existem casos em que um endpoint é referido como uma API. Por exemplo, esta é uma afirmação precisa: "A Braze usa uma API REST com muitos endpoints" ao falar de forma geral sobre os endpoints da Braze.

Não coloque aspas ao redor do nome do endpoint. Não use texto simples ao se referir ao caminho.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Use o endpoint Generate preference center URL para concluir as próximas etapas.</td><td style="width: 50%;">Use <code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code> para concluir as próximas etapas.</td></tr>
<tr><td style="width: 50%;">Use o endpoint <code>/users/track</code>.</td><td style="width: 50%;">Use o endpoint de API "Users Track".</td></tr>
</tbody>
</table>
{:/}

### Vinculando artigos de endpoints

Ao referenciar artigos de endpoints, certifique-se de usar [texto de link significativo]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#writing-links) que faça sentido fora de contexto. Se estiver usando o caminho do endpoint como link, forneça detalhes no texto ao redor, pois o caminho pode não comunicar claramente a função do endpoint.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Exclua perfis de usuário usando o <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">endpoint Delete user</a> da Braze.</td><td style="width: 50%;">Exclua perfis de usuário usando o endpoint <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> da Braze.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/">endpoint <code>/users/export/id</code></a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a> endpoint</td></tr>
</tbody>
</table>
{:/}

## Títulos

A introdução de um artigo de endpoint deve incluir as seguintes informações:

* Tipo de requisição e URL do caminho do endpoint  
* Uma breve descrição do endpoint, começando com "Use este endpoint para…"  
* Link "Veja no Postman"  
* Um alerta de nota com a permissão de chave da API REST necessária

Use esta checklist para garantir que os títulos (e conteúdo) adequados estejam incluídos em cada artigo de endpoint e na sequência listada. Observe que pode haver subtítulos exclusivos de um endpoint, como diferentes tipos de exemplos de requisição.

* Limite de taxa  
* Parâmetros de caminho  
* Corpo da requisição  
* Parâmetros de requisição  
* Exemplo de requisição  
* Parâmetros de resposta  
* Exemplo de resposta  
* Solução de problemas (se aplicável)

Consulte [Títulos e cabeçalhos]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#headings-and-titles) para diretrizes de formatação.

### Parâmetros de caminho

Se houver parâmetros de caminho para o endpoint, inclua um título de Parâmetros de caminho e uma tabela (semelhante à tabela de Parâmetros de requisição).

Se não houver parâmetros de caminho para o endpoint, inclua um título de Parâmetros de caminho e o seguinte aviso: "Não há parâmetros de caminho para este endpoint."

Se não houver parâmetros de caminho ou de requisição para o endpoint, combine o aviso na mesma seção, conforme mostrado abaixo.

{% raw %}
{::nomarkdown}
<div style="margin-left: 2em;">
<code>
## Path and request parameters <br>
There are no path or request parameters for this endpoint.
</code>
</div>
{:/}
{% endraw %}

## Convenções de nomenclatura

Comece cada nome de endpoint com um verbo ativo após o método. Isso permite que os usuários saibam imediatamente a função do endpoint.

Não use o método da API como verbo inicial para o nome do endpoint.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">POST: Create new user alias</td><td style="width: 50%;">POST: New user alias</td></tr>
<tr><td style="width: 50%;">GET: Look up an existing dashboard user account</td><td style="width: 50%;">GET: Existing dashboard user account</td></tr>
</tbody>
</table>
{:/}

Exceções a essa convenção de nomenclatura são os endpoints na [seção Export]({{site.baseurl}}/api/endpoints/export), pois o nome da seção é um verbo que indica que as informações listadas podem ser exportadas.

## Permissões de chave de API

As permissões de chave de API são permissões que você pode atribuir a um usuário ou grupo para limitar o acesso a determinadas chamadas de API. Para cada documentação de endpoint, inclua o seguinte aviso após o link da documentação do Postman:

> Para usar este endpoint, você deve gerar uma chave de API com a permissão `permission_name_here`.

Para encontrar a lista completa de permissões de chave de API, acesse **Configurações > Chaves de API** em **Configuração e Teste** no dashboard da Braze. Selecione uma chave de API com acesso total (o nome da chave geralmente inclui a frase "full access"). Cada nome de permissão deve corresponder geralmente ao nome do endpoint.

Observe que os endpoints SCIM não possuem permissões de chave de API listadas, pois são específicos da integração SCIM que ocorre fora do console de desenvolvedor.

## Limites de taxa

Em geral, seu limite de taxa deve especificar o número de requisições e o tempo permitido.

Esteja atento aos endpoints que compartilham um limite de taxa total. Por exemplo, todos os endpoints assíncronos de itens de catálogo compartilham um limite de taxa total, então é importante indicar isso nos respectivos artigos.

### Como atualizar o arquivo de limite de taxa

Se a documentação do seu endpoint exigir a atualização ou listagem de um novo limite de taxa, acesse **_docs > _api > api_limits.md** para fazer as edições no limite de taxa.

## Parâmetros

Defina os parâmetros de requisição e de resposta em duas tabelas separadas. Essas tabelas devem conter as seguintes colunas:

* **Parâmetro**  
* **Obrigatória**  
* **Tipo de dados**  
* **Descrição**

Ao se referir diretamente aos parâmetros de um endpoint e ao listar os valores na coluna **Parâmetro**, use texto de código. Ao listar os valores nas colunas **Obrigatória**, **Tipo de dados** e **Descrição**, use iniciais maiúsculas.

### Texto de espaço reservado

Para texto de espaço reservado, use chaves com uma breve descrição do que o usuário deve incluir.

Para espaços reservados de chave de API, use `YOUR_REST_API_KEY`, não `YOUR-REST-API-KEY`.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code></td><td style="width: 50%;"><code>/preference_center/v1/[preferenceCenterExternalId]</code></td></tr>
<tr><td style="width: 50%;"><code>/scim/v2/Users/{userId}</code></td><td style="width: 50%;"><code>/url/[userId]/scim/v2/Users/userID</code></td></tr>
</tbody>
</table>
{:/}

Para espaços reservados de chave de API, use `YOUR_REST_API_KEY` (com underscores), não `YOUR-REST-API-KEY` (com hífens).

## Requisições e respostas

Uma requisição de API inclui o cabeçalho e os parâmetros de requisição. Os parâmetros de requisição devem ser formatados assim:

```bash
parameter": (required/optional, data type) A brief description
```

Aqui está um exemplo de corpo de requisição para o [endpoint Create new user alias]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/):

```bash
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "user_aliases": (required, array of new user alias object)
}
```

Use aspas duplas retas (" ") para identificar parâmetros que são strings ou arrays em um exemplo de requisição. Certifique-se de que todos os colchetes e parênteses abertos estejam fechados.

Uma resposta de API inclui o corpo da resposta, cabeçalhos e o código de status HTTP. Sempre inclua um exemplo de resposta. Este exemplo deve incluir um texto simples que descreva o parâmetro. Aqui está um exemplo de resposta para o [endpoint Update user alias]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/#example-request).

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

### Códigos de status e erro

Os códigos de status indicam se uma requisição específica do usuário foi concluída com sucesso. Pode ser útil incluir os códigos de status para que os usuários saibam o que é considerado um sucesso. Por exemplo, 400 e 404 podem ser indicadores de uma resposta de erro para o endpoint.

Se a documentação do seu endpoint exigir a listagem de códigos de erro, faça um link para o artigo [Erros e respostas de API]({{site.baseurl}}/api/errors/) na pasta **_docs** **> _api** e o arquivo **> errors.md**

## Código de exemplo

O código de exemplo, assim como requisições e respostas de exemplo, deve poder ser copiado e usado com o mínimo de trabalho. Com exceção do texto de espaço reservado (por exemplo, a chave de API no cabeçalho), os exemplos de requisição devem funcionar como estão. Use o Postman para garantir que sua requisição esteja formatada corretamente.

### Código formatado versus minificado

Se a requisição do endpoint contiver um corpo, formate o exemplo no Postman. Isso facilita para os desenvolvedores que estão aprendendo as convenções da Braze entenderem cada parte da requisição.

Se o corpo da requisição do endpoint for muito curto ou não contiver um corpo, minifique a requisição para que espaços em branco desnecessários sejam removidos. Use uma ferramenta como o [JSON Minifier](https://codebeautify.org/jsonminifier) para isso.

### Comentários inline

Use duas barras (//) para indicar comentários de linha única no código de exemplo.

Comentários inline são ferramentas valiosas para chamar a atenção do usuário para uma seção específica do código, explicar a função de um bloco de código ou fornecer contexto adicional.

Use comentários inline para mostrar rapidamente onde a camada de lógica do usuário seria colocada e como ela referenciaria o código do SDK. Use exemplos simples, mas realistas. Por exemplo, um atributo de exemplo como "favorite_movie" é mais forte do que "example_attribute". Mesmo que o negócio do usuário não rastreie ou se importe com o filme favorito de um usuário final, este exemplo mostra os *tipos* de casos de uso que podem ser rastreados por meio desse atributo. Exemplos genéricos não conseguem provocar o mesmo entendimento intuitivo.

Evite comentários inline que simplesmente repitam código ou nomes de métodos legíveis por humanos. Em vez disso, use uma variedade de sinônimos para os métodos e parâmetros específicos da Braze para fornecer suporte a falantes não nativos de inglês.

Em geral, siga as convenções padrão do inglês ao fornecer comentários inline. Por exemplo, comece frases com letra maiúscula, escreva as palavras por extenso e assim por diante.

## Recursos adicionais

- [Guia de estilo de documentação para desenvolvedores do Google](https://developers.google.com/style)  
  - [Código de referência de API e comentários](https://developers.google.com/style/api-reference-comments)
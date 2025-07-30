---
nav_title: Atributos personalizados aninhados
article_title: Atributos personalizados aninhados
alias: "/nested_custom_attribute_support/"
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o uso de atributos personalizados aninhados como um tipo de dados para atributos personalizados, incluindo limitações e exemplos de uso."
---

# Atributos personalizados aninhados

> Esta página aborda os atributos personalizados aninhados, que permitem definir um conjunto de atributos como uma propriedade de outro atributo. Em outras palavras, quando você define um objeto de atributo personalizado, pode definir um conjunto de atributos adicionais para esse objeto.

Digamos que você queira definir um atributo personalizado no perfil do usuário chamado `favorite_book`. Esse atributo personalizado pode ser definido como um objeto que tem os atributos aninhados `title`, `author` e `publishing_date`, da seguinte forma:

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```

Esses dados aninhados permitem que você crie segmentos usando informações de um objeto de atributo personalizado e personalize suas mensagens usando um objeto de atributo personalizado e o Liquid.

Os objetos de atributos personalizados podem conter [tipos de dados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types), como:

- Números
- Strings
- Booleanos
- Matrizes
- Horário
  - Ao filtrar um atributo personalizado de tempo aninhado, você pode optar por filtrar com base no "Dia do ano" ou na "Hora". "Dia do Ano" verificará apenas o mês e o dia para comparação. "Time" comparará o registro de data e hora completo, incluindo o ano.
- Outros objetos
- [Vetores de objetos]({{site.baseurl}}/array_of_objects/)

## Limitações

- Os atributos personalizados aninhados destinam-se a atributos personalizados enviados por meio do Braze SDK ou da API. 
- Os objetos têm um tamanho máximo de 100 KB.
- Os nomes das chaves e os valores das strings têm um limite de tamanho de 255 caracteres.
- Os nomes das chaves não podem conter espaços.
- Os pontos (`.`) e os cifrões (`$`) não são caracteres suportados em uma carga útil da API se você estiver tentando enviar um atributo personalizado aninhado a um perfil de usuário.
- Nem todos os Braze Partners suportam atributos personalizados aninhados. Consulte a [documentação do parceiro]({{site.baseurl}}/partners/home) para confirmar se as integrações com parceiros específicos suportam esse recurso.
- Os atributos personalizados aninhados não podem ser usados como um filtro ao fazer uma chamada à API do Connected Audience.

## Exemplo de API

{% tabs local %}
{% tab Criar %}
A seguir, um exemplo do site `/users/track` com um objeto "Most Played Song" (Música mais tocada). Para capturar as propriedades da música, enviaremos uma solicitação de API que lista `most_played_song` como um objeto, juntamente com um conjunto de propriedades do objeto.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Atualização %}
Para atualizar um objeto existente, envie um POST para `users/track` com o parâmetro `_merge_objects` na solicitação. Isso mesclará profundamente sua atualização com os dados de objeto existentes. A mesclagem profunda garante que todos os níveis de um objeto sejam mesclados em outro objeto, em vez de apenas o primeiro nível. Neste exemplo, já temos um objeto `most_played_song` na Braze e agora estamos adicionando um novo campo, `year_released`, ao objeto `most_played_song`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

Depois que essa solicitação for recebida, o objeto de atributo personalizado se parecerá com o seguinte:

```json
"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}
```

{% alert warning %}
Você deve definir `_merge_objects` como `true`, ou seus objetos serão substituídos. `_merge_objects` é `false` por padrão.
{% endalert %}

{% endtab %}
{% tab Excluir %}
Para excluir um objeto de atributo personalizado, envie um POST para `users/track` com o objeto de atributo personalizado definido como `null`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
Essa abordagem não pode ser usada para excluir uma chave aninhada em um [vetor de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects).
{% endalert %}

{% endtab %}
{% endtabs %}

## Exemplo de SDK

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab SDK para Android %}

**Criar**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**Atualizar**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**Excluir**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**Criar**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**Atualizar**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**Excluir**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab SDK da Web %}

**Criar**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**Atualizar**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**Excluir**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## Captura de datas como propriedades do objeto

Para capturar datas como propriedades do objeto, você deve usar a chave `$time`. No exemplo a seguir, um objeto "Important Dates" é usado para capturar o conjunto de propriedades do objeto, `birthday` e `wedding_anniversary`. O valor para essas datas é um objeto com uma chave `$time`, que não pode ser um valor nulo.

{% alert note %}
Caso não tenha capturado datas como propriedades do objeto inicialmente, recomendamos reenviar esses dados usando a chave `$time` para todos os usuários. Caso contrário, isso pode resultar em segmentos incompletos ao usar o atributo `$time`. No entanto, se o valor de `$time` em um atributo personalizado aninhado não estiver formatado corretamente, o atributo personalizado aninhado inteiro não será atualizado.
{% endalert %}

```json
{
  "attributes": [ 
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
Para atributos personalizados aninhados, se o ano for menor que 0 ou maior que 3000, o Braze não armazenará esses valores no usuário.
{% endalert %}

## Modelos do Liquid

O exemplo de modelo do Liquid a seguir mostra como fazer referência às propriedades do objeto de atributo personalizado salvas na solicitação anterior da API e usá-las no envio de mensagens.

Use a tag de personalização `custom_attribute` e a notação de ponto para acessar as propriedades de um objeto. Especifique o nome do objeto (e a posição no vetor se estiver fazendo referência a um vetor de objetos), seguido de um ponto (ponto final), seguido do nome da propriedade.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` - "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` - "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` - "1000"
{% endraw %}

![Uso do Liquid para modelar um nome de música e o número de vezes que um ouvinte tocou essa música em uma mensagem]({% image_buster /assets/img_archive/nca_liquid_2.png %})

## Segmentação

É possível criar segmentos com base em atributos personalizados aninhados para direcionar ainda mais seus usuários. Para fazer isso, filtre seu segmento com base no objeto de atributo personalizado e, em seguida, especifique a jornada para o nome da propriedade e o valor associado que deseja segmentar. Se não tiver certeza de como é essa jornada, você poderá [gerar um esquema](#generate-schema) e usar o explorador de objetos aninhados para que o Braze preencha essa jornada para você.

Depois de adicionar um caminho à sua propriedade, selecione **Validar** para verificar se o valor no campo jornada é válido.

![Filtragem com base em um atributo personalizado de música mais reproduzida, em que um ouvinte reproduziu uma música mais de um número especificado de vezes]({% image_buster /assets/img_archive/nca_segmentation_2.png %})

Para segmentar com atributos personalizados aninhados, selecione o filtro **Atributos personalizados aninhados** para expor um menu suspenso no qual você pode selecionar um atributo personalizado aninhado específico.

![]({% image_buster /assets/img_archive/nested_custom_attributes.png %}){: style="max-width:70%;"}

Ao trabalhar com segmentação de atributos personalizados aninhados, você terá acesso a um novo comparador agrupado por tipo de dados. Por exemplo, como `play_analytics.count` é um número, você pode selecionar um comparador na categoria **Número**.

![Um usuário escolhe um operador com base no tipo de dados do atributo personalizado aninhado]({% image_buster /assets/img_archive/nca_comparator.png %})

### Filtragem de tipos de dados de tempo

Ao filtrar um atributo personalizado de tempo aninhado, você pode optar por filtrar com operadores nas categorias **Dia do ano** ou **Hora** ao comparar o valor da data. 

Se você selecionar um operador na categoria **Dia do ano**, somente o mês e o dia serão verificados para comparação, em vez do registro de data e hora completo do valor do atributo personalizado aninhado. A seleção de um operador na categoria **Tempo** comparará o registro de data e hora completo, incluindo o ano.

### Segmentação multicritério

Use o **Multi-Criteria Segmentation** para criar um segmento que corresponda a vários critérios em um único objeto. Isso qualifica o usuário para o segmento se ele tiver pelo menos um vetor de objeto que corresponda a todos os critérios especificados. Por exemplo, os usuários só corresponderão a esse segmento se a chave não estiver em branco e se o número for maior que 0.

Você também pode usar o recurso **Copiar Liquid para segmento** para gerar o código Liquid para esse segmento e usá-lo em uma mensagem. Por exemplo, digamos que você tenha um vetor de objetos de conta e um segmento que direciona os clientes com contas ativas tributáveis. Para fazer com que os clientes contribuam para a meta da conta associada a uma de suas contas ativas e tributáveis, você deverá criar uma mensagem para incentivá-los. 

![Um exemplo de segmento com a caixa de seleção selecionada para Multi-Criteria Segmentation.]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

Quando você selecionar **Copiar Liquid para o segmento**, o Braze gerará automaticamente o código Liquid que retorna um vetor de objeto que contém apenas contas ativas e tributáveis.

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

A partir daí, você pode usar o site `segmented_nested_objects` e personalizar sua mensagem. Neste exemplo, queremos pegar uma meta da primeira conta ativa tributável e personalizá-la:

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

Isso retorna a seguinte mensagem para seu cliente: "Alcance sua meta de aposentadoria mais rapidamente, faça um depósito usando nosso novo recurso de depósito rápido!"

### Gerar um esquema usando o explorador de objetos aninhados {#generate-schema}

Você pode gerar um esquema para seus objetos para criar filtros de segmento sem precisar memorizar jornadas de objetos aninhados. Para fazer isso, execute as seguintes etapas.

#### Etapa 1: Gerar um esquema

Para este exemplo, suponha que tenhamos um vetor de objetos `accounts` que acabamos de enviar à Braze:

```json
"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true},
 ]
```

No dashboard da Braze, acesse **Configurações de dados** > **Atributos personalizados**.

Procure seu objeto ou vetor de objetos. Na coluna **Nome da atribuição**, selecione **Gerar esquema**.

![]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
Pode levar alguns minutos para que seu esquema seja gerado, dependendo da quantidade de dados que você nos enviou.
{% endalert %}

Depois que o esquema tiver sido gerado, um novo botão <i class="fas fa-plus"></i> plus será exibido no lugar do botão **Generate Schema**. Você pode clicar nele para ver o que o Braze sabe sobre esse atributo personalizado aninhado. 

Durante a geração do esquema, o Braze analisa os dados anteriores enviados e cria uma representação ideal de seus dados para essa atribuição. O Braze também analisa e adiciona um tipo de dados para seus valores aninhados. Isso é feito por meio da amostragem dos dados anteriores enviados ao Braze para o atributo aninhado fornecido.

Para o nosso vetor de objetos `accounts`, você pode ver que, dentro do vetor de objetos, há um objeto que contém o seguinte:

- Um tipo booleano com uma chave de `active` (independentemente de a conta estar ativa ou não)
- Um tipo de número com uma chave de `balance` (valor do saldo na conta)
- Um tipo de string com uma chave de `type` (conta não tributável ou tributável)

![]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:50%" }

Agora que analisamos e criamos uma representação dos dados, vamos criar um segmento.

#### Etapa 2: Criar um segmento

Vamos direcionar os clientes que têm um saldo inferior a 100 para que possamos enviar a eles uma mensagem incentivando-os a fazer um depósito.

Crie um segmento e adicione o filtro `Nested Custom Attribute` e, em seguida, pesquise e selecione seu objeto ou vetor de objetos. Aqui adicionamos o vetor de objetos `accounts`. 

![]({% image_buster /assets/img_archive/nca_segment_schema.png %})

Selecione o botão <i class="fas fa-plus"></i> plus no campo da jornada. Isso exibirá uma representação de seu objeto ou vetor de objetos. Você pode selecionar qualquer um dos itens listados e a Braze os inserirá no campo da jornada para você. Neste exemplo, precisamos obter o saldo. Selecione o saldo e a jornada (nesse caso, `[].balance`) é preenchida automaticamente no campo de jornada.

![]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

Você pode selecionar **Validar** para verificar se o conteúdo do campo de jornada é válido e, em seguida, criar o restante do filtro conforme necessário. Aqui, especificamos que o saldo deve ser menor que 100.

![]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

É isso aí! Você acabou de criar um segmento usando um atributo personalizado aninhado, tudo sem precisar saber como os dados estão estruturados. O explorador de objetos aninhados no Braze gerou uma representação visual de seus dados e permitiu que você explorasse e selecionasse exatamente o que precisava para criar um segmento.

### Disparar alterações em atributos personalizados aninhados

Você pode disparar quando um objeto de atributo personalizado aninhado for alterado. Essa opção não está disponível para alterações em vetores de objetos. Se você não vir uma opção para visualizar o explorador de jornada, verifique se gerou um esquema. 

![]({% image_buster /assets/img_archive/nca_triggered_changes2.png %})

Por exemplo, na seguinte campanha baseada em ação, é possível adicionar uma nova ação-gatilho para **Alterar valor de atributo personalizado** para direcionar os usuários que alteraram suas preferências de escritório no bairro. 

![]({% image_buster /assets/img_archive/nca_triggered_changes.png %})

### Personalização

Usando o modal **Add Personalization**, você também pode inserir atributos personalizados aninhados em seu envio de mensagens. Selecione **Atributos personalizados aninhados** como o tipo de personalização. Em seguida, selecione o atributo de nível superior e a chave do atributo. 

Por exemplo, no modal de personalização abaixo, isso insere o atributo personalizado aninhado de um escritório de localização com base nas preferências do usuário.

![]({% image_buster /assets/img_archive/nca_personalization.png %}){: style="max-width:70%" }

{% alert tip %}
Verifique se foi gerado um esquema se não estiver vendo a opção de inserir atributos personalizados aninhados.
{% endalert %}

### Regenerar esquemas {#regenerate-schema}

Depois que um esquema é gerado, ele pode ser regenerado uma vez a cada 24 horas. Esta seção descreve como gerar novamente o esquema. Para saber mais informações detalhadas sobre esquemas, consulte a seção deste artigo sobre [como gerar um esquema](#generate-schema).

Para gerar novamente o esquema de seu atributo personalizado aninhado:

1. Acesse **Configurações de dados** > **Atributos personalizados**.
2. Procure seu atributo personalizado aninhado.
3. Na coluna **Nome da atribuição** de seu atributo, selecione <i class="fas fa-plus"></i> para gerenciar o esquema.
4. Será exibido um modal. Selecione **Gerar esquema novamente**.

A opção de regenerar o esquema será desativada se houver menos de 24 horas desde que o esquema foi regenerado pela última vez. A regeneração do esquema só detectará novos objetos e não excluirá os objetos que existem atualmente no esquema.

{% alert important %}
Para redefinir o esquema de um vetor de objetos com um objeto existente, é necessário criar um novo atributo personalizado. A regeneração do esquema não exclui os objetos existentes.
{% endalert %}

Se os dados não aparecerem como esperado após a regeneração do esquema, a atribuição pode não estar sendo ingerida com frequência suficiente. Os dados de usuários são amostrados em dados anteriores enviados ao Braze para a atribuição aninhada dada. Se a atribuição não for ingerida o suficiente, ela não será selecionada para o esquema.

## Pontos de dados

Qualquer chave enviada consome um ponto de dados. Por exemplo, esse objeto inicializado no perfil do usuário conta como sete (7) pontos de dados:

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
A atualização de um objeto de atributo personalizado para `null` também consome um ponto de dados.
{% endalert %}


---
nav_title: Tag de mensagens extras
article_title: Tag de mensagens extras
page_order: 1
description: "Este artigo explica como usar a tag Liquid de extras de mensagens e como verificar a sintaxe."
alias: "/message_extras_tag/"
---

# Tag "Message extras" do Liquid

> Use a tag `message_extras` Liquid para anotar seus eventos de envio com dados dinâmicos de Connected Content, Catálogos, atributos personalizados (como idioma, país), propriedades de entrada do Canvas ou outras fontes de dados.

A tag `message_extras` Liquid anexa pares de valores-chave ao evento de envio correspondente no Currents e no Snowflake Data Sharing. 

Para enviar dados dinâmicos ou extras de volta ao evento de envio de compartilhamento de dados do Currents ou do Snowflake, insira a tag Liquid apropriada no corpo da mensagem. 

Aqui está um exemplo do formato de tag Liquid padrão para `message_extras`:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

Você pode adicionar essas tags conforme necessário para seus pares de valores-chave no corpo da mensagem. No entanto, o comprimento de todas as chaves e valores não deve exceder 1 KB. No Currents e no Snowflake Data Sharing, você verá um novo campo de evento chamado `message_extras` para seus eventos de envio. Isso gerará uma string serializada JSON em um campo.

## Canais suportados

A tag `message_extras` é compatível com todos os tipos de mensagens com um evento de envio, juntamente com eventos de impressão de mensagens no app. O uso do `message_extras` com mensagens no app requer o cumprimento de determinadas [versões mínimas do SDK](#iam-sdk).

## Como usar a tag `message_extras` 

1. No corpo da mensagem do canal, digite a tag `message_extras` Liquid. Ou, você pode usar o modal **Add Personalization** e selecionar **Message Extras** para o tipo de personalização. 

![O modal Adicionar personalização com Extras de mensagens selecionado como o tipo de personalização.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Digite o [par chave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para cada tag `message_extras`. 

![Um exemplo de pares de chave-valor para a tag de extras de mensagens. O campo de título diz "Seus novos favoritos". A mensagem lê pares de chave-valor para a tag de extras da mensagem e a frase a seguir: "Estamos entusiasmados em oferecer uma seleção de produtos novos e interessantes que certamente se tornarão seus novos favoritos"]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Após o envio da campanha ou do canva, a Braze anexará os dados dinâmicos no momento do envio por meio dos eventos de envio Currents ou Snowflake Data Sharing ao campo `message_extras`.

## Verificação da sintaxe

Qualquer outra entrada que não corresponda ao padrão de tag discutido acima pode não ser transmitida ao Currents ou ao Snowflake. Verifique se sua sintaxe ou formatação não inclui nenhum dos seguintes itens:

- Delimitadores inexistentes, vazios ou com erros de digitação
- Chaves duplicadas (o Braze enviará por padrão o par chave-valor que for encontrado primeiro)
- Texto extra antes da definição de chaves ou valores
- Chaves e valores fora de ordem 
  - {% raw %}Por exemplo, ```{% message_extras :value 123 :key test %}```{% endraw %}

## Considerações

- Se seus valores-chave excederem 1 KB, eles serão truncados. 
- Os espaços em branco serão contabilizados na contagem de caracteres. Note que a Braze omite os espaços em branco à esquerda e à direita.
- O JSON resultante produzirá apenas valores de string.
- Você pode incluir variáveis Liquid como chave ou valor, mas não pode usar outras tags Liquid em `message_extras`.
  - Por exemplo, você poderia usar o seguinte Liquid: {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## Perguntas frequentes

#### Como posso associar o campo message_extras nos eventos de envio aos meus eventos de engajamento, como aberturas e cliques? 

Um `dispatch_id` é gerado e fornecido em seus eventos de envio, que pode ser usado como um identificador exclusivo para vincular a eventos específicos de clique, abertura ou entrega. Você poderá usar e consultar esse campo no Currents ou no Snowflake. Saiba mais sobre o [comportamento do `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

#### Posso usar o message_extras com mensagens no app? {#iam-sdk}

Sim, é possível usar o `message_extras` em suas mensagens no app, desde que os dispositivos dos usuários tenham as seguintes versões mínimas de SDK:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}


---
nav_title: Visão geral
article_title: Visão geral da Central de Preferências
page_order: 1
description: "Este artigo descreve a Central de Preferências de e-mail e como personalizá-la."
channel:
  - email
---

# Visão geral da Central de Preferências

> A configuração de uma central de Preferências oferece um local único para os usuários editarem e gerenciarem suas preferências de notificação para o [envio de mensagens por e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/). Este artigo inclui etapas para a criação de um centro de preferências gerado pela API, mas você também pode criar um centro de preferências usando o [editor de arrastar e soltar]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/).

No dashboard do Braze, acesse **Público** > **Inscrições** > **Central de Preferências de E-mail**.

É aqui que você pode gerenciar e visualizar cada grupo de inscrições. Cada grupo de inscrições que você cria é adicionado a essa lista da Central de Preferências. Você pode criar várias Centrais de Preferências.

{% alert important %}
A Central de Preferências deve ser usada no canal de e-mail da Braze. Os links da Central de Preferências são dinâmicos com base em cada usuário e não podem ser hospedados externamente.
{% endalert %}

## Criação de uma Central de Preferências com API

Ao usar os [endpoints da Central de Preferências do Braze]({{site.baseurl}}/api/endpoints/preference_center), é possível criar uma central de preferências, um site hospedado pelo Braze, que pode exibir o estado da inscrição do usuário e os status do grupo de inscrições. Usando HTML e CSS, sua equipe de desenvolvedores pode criar a central de preferências usando HTML e CSS para que o estilo da página corresponda às diretrizes da marca.

O uso do Liquid ativa a recuperação dos nomes dos seus grupos de inscrições e o status de cada usuário. Dessa forma, a Braze armazena e recupera esses dados quando a página é carregada.

### Pré-requisitos

| Requisito | Descrição |
|---|---|
| Central de Preferências ativada | Seu dashboard do Braze tem permissões para usar o recurso da Central de Preferências. |
| Espaço de trabalho válido com um grupo de inscrições para e-mail, SMS ou WhatsApp | Um espaço de trabalho com usuários válidos e um grupo de inscrições para e-mail, SMS ou WhatsApp. |
| Usuário válido | Um usuário com um endereço de e-mail e uma ID externa. |
| Chave de API gerada com permissões do centro de preferências | No dashboard do Braze, acesse **Settings** > **API Keys** para confirmar que você tem acesso a uma chave de API com permissões da Central de Preferências. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 1: Use o ponto de extremidade Criar centro de preferências

Vamos começar a criar um centro de preferências usando o [endpoint Criar centro de preferências]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/). Para personalizar a Central de Preferências, é possível incluir HTML que se alinhe à sua marca nos campos `preference_center_page_html` e `confirmation_page_html`.

O [endpoint Gerar URL do centro de preferências]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) permite obter o URL do centro de preferências de um usuário específico fora de um e-mail enviado pelo Braze.

### Etapa 2: Inclua em sua campanha de e-mail

{% multi_lang_include preference_center_warning.md %}

Para colocar um link para a Central de Preferências em seus e-mails, use a seguinte tag Liquid no local desejado em seu e-mail, da mesma forma que inseriria URLs de cancelamento de inscrição.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Você também pode usar uma combinação de HTML que inclua o Liquid. Por exemplo, você pode colar o seguinte como URL no editor de HTML ou no editor de arrastar e soltar. Isso mostrará o layout básico da Central de Preferências que lista todos os grupos de inscrições para e-mail automaticamente. 

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}">Edit your preferences</a>
```
{%endraw%}

A Central de Preferências tem uma caixa de seleção que permitirá que os usuários cancelem a inscrição de todos os e-mails. Observe que não será possível salvar essas preferências se forem enviadas como uma mensagem de teste.

{% alert important %}
A Liquid tag acima só funcionará ao lançar uma campanha ou um Canva. O envio de um e-mail de teste não gerará um link válido.
{% endalert %}

#### Edição de uma Central de Preferências

Você pode editar e atualizar seu centro de preferências usando o [ponto de extremidade Update preference center (Atualizar centro de preferências]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)). 

#### Identificação de centros de preferências e detalhes

Para identificar seus centros de preferência, use o [ponto de extremidade Exibir detalhes do centro de preferência]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) para retornar informações relacionadas, como o último registro de data e hora atualizado, a ID do centro de preferência e muito mais.

## Personalização

O Braze gerencia as atualizações do estado da inscrição a partir do centro de preferências, o que mantém o centro de preferências sincronizado. No entanto, você também pode criar e hospedar seu próprio centro de preferências usando as [APIs de grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups/) com as seguintes opções.

### Opção 1: Link com parâmetros de consulta de string

Use pares de campo-valor da string de consulta no corpo do URL para passar o ID do usuário e a categoria de e-mail para a página, de modo que os usuários só precisem confirmar sua opção de cancelar a inscrição. Essa opção é boa para quem armazena um identificador de usuário em formato hash e ainda não tem um centro de inscrição.

Para essa opção, cada categoria de e-mail exigirá seu próprio link específico de cancelamento de inscrição:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Também é possível fazer o hash da ID externa do usuário no ponto de envio usando um filtro Liquid. Isso converterá o endereço `user_id` em um valor de hash MD5, por exemplo:
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Opção 2: Autenticação com token da Web JSON

Use um [token da Web JSON](https://auth0.com/learn/json-web-tokens/) para autenticar usuários em uma parte do seu servidor da Web (por exemplo, preferências de conta) que normalmente está por trás de uma camada de autenticação, como login de nome de usuário e senha. 

Essa abordagem não requer pares de valores de string de consulta incorporados no URL, pois eles podem ser passados na carga útil do token da Web JSON, por exemplo:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```

## Perguntas frequentes

### Não criei uma Central de Preferências. Por que estou vendo "PreferenceCenterBrazeDefault" em meu dashboard?

Isso é usado para renderizar a Central de Preferências quando o Liquid {%raw%}`${preference_center_url}`{%endraw%} legado é usado, o que significa que as etapas do canva ou os modelos que fazem referência a {%raw%}`${preference_center_url}` ou `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} não funcionarão. Isso também se aplica a mensagens enviadas anteriormente que incluíam o Liquid legado ou "PreferenceCenterBrazeDefault" como parte da mensagem. 

Se você fizer referência a {%raw%}`${preference_center_url}`{%endraw%} em uma nova mensagem novamente, uma Central de Preferências chamada "PreferenceCenterBrazeDefault" será criada novamente.

### As Centrais de Preferências oferecem suporte a vários idiomas?

Não. No entanto, você pode usar o Liquid ao escrever o HTML para páginas personalizadas de aceitação e exclusão. Se estiver usando links dinâmicos para gerenciar cancelamentos de inscrição, esse é um único link. 

Por exemplo, se estiver rastreando a taxa de cancelamento de inscrição de usuários de língua espanhola, será necessário usar campanhas separadas ou aproveitar a análise de dados do Currents (como observar quando um usuário cancela a inscrição e verificar o idioma preferido desse usuário).

Como outro exemplo, para rastreamento das taxas de cancelamento de inscrição de usuários de língua espanhola, é possível adicionar uma string de parâmetro de consulta como `?Spanish=true` ao URL de cancelamento de inscrição se o idioma dos usuários for alemão e usar um ink de cancelamento de inscrição normal se não for:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Em seguida, por meio do Currents, foi possível identificar quais usuários falam espanhol e quantos cliques ocorreram nesse ink de cancelamento de inscrição.

### Os links de cancelamento de inscrição e as centrais de preferências de e-mail são necessários para o envio?

Não. Se você vir a mensagem "Seu corpo de e-mail não inclui um link de cancelamento de inscrição" ao criar uma campanha de e-mail, esse aviso é esperado se o seu ink de cancelamento de inscrição estiver em um bloco de conteúdo.

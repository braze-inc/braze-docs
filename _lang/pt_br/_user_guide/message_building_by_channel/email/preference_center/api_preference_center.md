---
nav_title: Central de Preferências de e-mail via API
article_title: Central de Preferências de e-mail via API
page_order: 1
description: "Este artigo descreve a Central de Preferências de e-mail via API e como personalizá-la."
channel:
  - email
---

# Central de Preferências de e-mail via API

> A configuração de uma Central de Preferências oferece um local único para os usuários editarem e gerenciarem suas preferências de notificação para o [envio de mensagens por e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/). Este artigo inclui etapas para a criação de uma Central de Preferências gerada pela API, mas você também pode criar uma Central de Preferências usando o [editor de arrastar e soltar]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/).

No dashboard da Braze, acesse **Público** > **Centrais de Preferências de E-mail**.

É aqui que você pode gerenciar e visualizar cada grupo de inscrições. Cada grupo de inscrições que você cria é adicionado a essa lista da Central de Preferências. Você pode criar várias Centrais de Preferências.

{% alert important %}
A Central de Preferências deve ser usada no canal de e-mail da Braze. Os links da Central de Preferências são dinâmicos com base em cada usuário e não podem ser hospedados externamente.
{% endalert %}

## Criação de uma Central de Preferências com API

Ao usar os [endpoints da Central de Preferências da Braze]({{site.baseurl}}/api/endpoints/preference_center), é possível criar uma Central de Preferências, um site hospedado pela Braze, que pode exibir o estado da inscrição do usuário e os status do grupo de inscrições. Usando HTML e CSS, sua equipe de desenvolvedores pode criar a Central de Preferências para que o estilo da página corresponda às diretrizes da marca.

O uso do Liquid permite recuperar os nomes dos seus grupos de inscrições e o status de cada usuário. Dessa forma, a Braze armazena e recupera esses dados quando a página é carregada.

### Pré-requisitos

| Requisito | Descrição |
|---|---|
| Central de Preferências ativada | Seu dashboard da Braze tem permissões para usar o recurso da Central de Preferências. |
| Espaço de trabalho válido com um grupo de inscrições para e-mail, SMS ou WhatsApp | Um espaço de trabalho funcional com usuários válidos e um grupo de inscrições para e-mail, SMS ou WhatsApp. |
| Usuário válido | Um usuário com um endereço de e-mail e um ID externo. |
| Chave de API gerada com permissões da Central de Preferências | No dashboard da Braze, acesse **Configurações** > **Chaves de API** para confirmar que você tem acesso a uma chave de API com permissões da Central de Preferências. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 1: Use o endpoint Criar Central de Preferências

Vamos começar a criar uma Central de Preferências usando o [endpoint Criar Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/). Para personalizar a Central de Preferências, é possível incluir HTML que se alinhe à sua marca nos campos `preference_center_page_html` e `confirmation_page_html`.

O [endpoint Gerar URL da Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) permite obter a URL da Central de Preferências de um usuário específico fora de um e-mail enviado pela Braze.

### Etapa 2: Inclua em sua campanha de e-mail

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Para colocar um link para a Central de Preferências em seus e-mails, use a seguinte Liquid tag no local desejado em seu e-mail, da mesma forma que inseriria URLs de cancelamento de inscrição.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Você também pode usar uma combinação de HTML que inclua Liquid. Por exemplo, você pode colar o seguinte como URL no editor de HTML ou no editor de arrastar e soltar. Isso mostrará o layout básico da Central de Preferências que lista todos os grupos de inscrições para e-mail automaticamente. Se você usar [alias de link]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/), adicione um ponto de interrogação (`?`) após a Liquid tag para que a Braze possa anexar parâmetros de rastreamento.

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

A Central de Preferências tem uma caixa de seleção que permitirá que os usuários cancelem a inscrição de todos os e-mails. Observe que não será possível salvar essas preferências se forem enviadas como uma mensagem de teste.

{% alert important %}
A Liquid tag acima só funcionará ao lançar uma campanha ou um Canvas. O envio de um e-mail de teste não gerará um link válido. Para verificar o link da Central de Preferências, lance a mensagem em uma campanha direcionada apenas ao seu perfil de teste.
{% endalert %}

#### Edição de uma Central de Preferências

Você pode editar e atualizar sua Central de Preferências usando o [endpoint Atualizar Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/). 

#### Identificação de Centrais de Preferências e detalhes

Para identificar suas Centrais de Preferências, use o [endpoint Exibir detalhes da Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) para retornar informações relacionadas, como o último registro de data e hora atualizado, o ID da Central de Preferências e muito mais.

## Personalização

A Braze gerencia as atualizações do estado da inscrição a partir da Central de Preferências, o que mantém a Central de Preferências sincronizada. No entanto, você também pode criar e hospedar sua própria Central de Preferências usando as [APIs de grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups/) com as seguintes opções.

### Opção 1: Link com parâmetros de consulta de string

Use pares de campo-valor da string de consulta no corpo da URL para passar o ID do usuário e a categoria de e-mail para a página, de modo que os usuários só precisem confirmar sua opção de cancelar a inscrição. Essa opção é boa para quem armazena um identificador de usuário em formato hash e ainda não tem um centro de inscrição.

Para essa opção, cada categoria de e-mail exigirá seu próprio link específico de cancelamento de inscrição:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Também é possível fazer o hash do ID externo do usuário no ponto de envio usando um filtro Liquid. Isso converterá o `user_id` em um valor de hash MD5, por exemplo:
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Opção 2: Autenticação com JSON web token

Use um [JSON web token](https://auth0.com/learn/json-web-tokens/) para autenticar usuários em uma parte do seu servidor da web (por exemplo, preferências de conta) que normalmente está por trás de uma camada de autenticação, como login de nome de usuário e senha. 

Essa abordagem não requer pares de valores de string de consulta incorporados na URL, pois eles podem ser passados na carga útil do JSON web token, por exemplo:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": "offers"
}
```

## Perguntas frequentes

### Não criei uma Central de Preferências. Por que estou vendo "PreferenceCenterBrazeDefault" no meu dashboard?

Isso é usado para renderizar a Central de Preferências quando o Liquid legado {%raw%}`${preference_center_url}`{%endraw%} é usado, o que significa que as etapas do Canvas ou os modelos que fazem referência a {%raw%}`${preference_center_url}` ou `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} não funcionarão. Isso também se aplica a mensagens enviadas anteriormente que incluíam o Liquid legado ou "PreferenceCenterBrazeDefault" como parte da mensagem. 

Se você fizer referência a {%raw%}`${preference_center_url}`{%endraw%} em uma nova mensagem novamente, uma Central de Preferências chamada "PreferenceCenterBrazeDefault" será criada novamente.

### As Centrais de Preferências suportam múltiplos idiomas?

Não. No entanto, você pode aproveitar o Liquid ao escrever o HTML para páginas personalizadas de aceitação e cancelamento. Se você estiver usando links dinâmicos para gerenciar cancelamentos, este é um único link. 

Por exemplo, se você estiver rastreando a taxa de cancelamento de inscrição para usuários de língua espanhola, precisaria usar campanhas separadas ou aproveitar a análise de dados em torno do Currents (como verificar quando um usuário cancela a inscrição e checar o idioma preferido desse usuário).

Como outro exemplo, para rastrear taxas de cancelamento de inscrição para usuários de língua espanhola, você poderia adicionar uma string de parâmetro de consulta como `?Spanish=true` à URL de cancelamento de inscrição se o idioma dos usuários for espanhol e usar um link de cancelamento de inscrição regular se não for:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Então, através do Currents, você poderia identificar quais usuários falam espanhol e quantos eventos de clique houve para aquele link de cancelamento de inscrição.

### Os links de cancelamento de inscrição e as Centrais de Preferências de e-mail são obrigatórios para o envio?

Não. Se você ver a mensagem "O corpo do seu e-mail não inclui um link de cancelamento de inscrição" ao compor uma campanha de e-mail, esse aviso é esperado se o seu link de cancelamento de inscrição estiver em um bloco de conteúdo.

### Como atualizo o ícone padrão do navegador?

Por padrão, o ícone ao lado do nome da guia do navegador (favicon) usa o logo da Braze. Para adicionar um favicon personalizado, você o define através do atributo `links-tags` na sua chamada de API Criar ou Atualizar [Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center). A Braze então injeta a tag {% raw %}`<link rel="icon" ...>`{% endraw %} na página hospedada para você.

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}
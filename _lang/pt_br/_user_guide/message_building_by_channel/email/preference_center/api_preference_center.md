---
nav_title: Centro de preferências de e-mail da API
article_title: Centro de preferências de e-mail da API
page_order: 1
description: "Este artigo descreve o centro de preferências de e-mail da API e como personalizá-lo."
channel:
  - email
---

# Centro de preferências de e-mail da API

> A configuração de um centro de preferências oferece um local único para os usuários editarem e gerenciarem suas preferências de notificação para suas [mensagens de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/). Este artigo inclui etapas para a criação de um centro de preferências gerado pela API, mas você também pode criar um centro de preferências usando o [editor de arrastar e soltar]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/).

No painel do Braze, vá para **Audience** > **Email Preference Centers**.

É aqui que você pode gerenciar e visualizar cada grupo de assinatura. Cada grupo de assinatura que você cria é adicionado a essa lista do centro de preferências. Você pode criar vários centros de preferência.

{% alert important %}
O centro de preferências deve ser usado no canal de e-mail do Braze. Os links do centro de preferências são dinâmicos com base em cada usuário e não podem ser hospedados externamente.
{% endalert %}

## Criação de um centro de preferências com API

Ao usar os [endpoints do Preference Center Braze]({{site.baseurl}}/api/endpoints/preference_center), você pode criar um centro de preferências, um site hospedado pelo Braze, que pode exibir o estado da assinatura do usuário e os status do grupo de assinatura. Usando HTML e CSS, sua equipe de desenvolvedores pode criar o centro de preferências usando HTML e CSS para que o estilo da página corresponda às diretrizes da sua marca.

O uso do Liquid permite que você recupere os nomes dos grupos de assinatura e o status de cada usuário. Dessa forma, o Braze armazena e recupera esses dados quando a página é carregada.

### Pré-requisitos

| Requisito | Descrição |
|---|---|
| Centro de preferências ativado | Seu painel de controle do Braze tem permissões para usar o recurso do centro de preferências. |
| Espaço de trabalho válido com um grupo de assinatura de e-mail, SMS ou WhatsApp | Um espaço de trabalho com usuários válidos e um grupo de assinatura de e-mail, SMS ou WhatsApp. |
| Usuário válido | Um usuário com um endereço de e-mail e uma ID externa. |
| Chave de API gerada com permissões do centro de preferências | No painel do Braze, vá para **Settings** > **API Keys** ( **Configurações** > **Chaves de API** ) para confirmar que você tem acesso a uma chave de API com permissões do centro de preferências. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 1: Use o ponto de extremidade Criar centro de preferências

Vamos começar a criar um centro de preferências usando o [ponto de extremidade Criar centro de preferências]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/). Para personalizar o centro de preferências, você pode incluir HTML que se alinhe à sua marca no campo `preference_center_page_html` e no campo `confirmation_page_html`.

O [endpoint Gerar URL do centro de preferências]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) permite que você obtenha o URL do centro de preferências de um usuário específico fora de um e-mail enviado pelo Braze.

### Etapa 2: Inclua em sua campanha de e-mail

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Para colocar um link para o centro de preferências em seus e-mails, use a seguinte tag Liquid no local desejado em seu e-mail, da mesma forma que você inseriria URLs de cancelamento de assinatura.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Você também pode usar uma combinação de HTML que inclua o Liquid. Por exemplo, você pode colar o seguinte como URL no editor de HTML ou no editor de arrastar e soltar. Isso mostrará o layout básico do centro de preferências que lista todos os grupos de assinatura de e-mail automaticamente. 

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}">Edit your preferences</a>
```
{%endraw%}

A central de preferências tem uma caixa de seleção que permitirá que os usuários cancelem a assinatura de todos os e-mails. Observe que você não poderá salvar essas preferências se elas forem enviadas como uma mensagem de teste.

{% alert important %}
A tag Liquid acima só funcionará ao lançar uma campanha ou um Canvas. O envio de um e-mail de teste não gerará um link válido.
{% endalert %}

#### Edição de um centro de preferências

Você pode editar e atualizar seu centro de preferências usando o [ponto de extremidade Update preference center (Atualizar centro de preferências]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)). 

#### Identificação de centros de preferência e detalhes

Para identificar seus centros de preferência, use o [ponto de extremidade Exibir detalhes do centro de preferência]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) para retornar informações relacionadas, como o último registro de data e hora atualizado, a ID do centro de preferência e muito mais.

## Personalização

O Braze gerencia as atualizações do estado da assinatura a partir do centro de preferências, o que mantém o centro de preferências em sincronia. No entanto, você também pode criar e hospedar seu próprio centro de preferências usando as [APIs de grupos de assinatura]({{site.baseurl}}/api/endpoints/subscription_groups/) com as seguintes opções.

### Opção 1: Link com parâmetros de consulta de string

Use pares de campo-valor de string de consulta no corpo do URL para passar o ID do usuário e a categoria de e-mail para a página, de modo que os usuários só precisem confirmar sua opção de cancelar a assinatura. Essa opção é boa para quem armazena um identificador de usuário em um formato hash e ainda não tem um centro de assinatura.

Para essa opção, cada categoria de e-mail exigirá seu próprio link específico de cancelamento de assinatura:<br>
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

Essa abordagem não exige pares de valores de string de consulta incorporados no URL, pois eles podem ser passados na carga útil do token da Web JSON, por exemplo:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```

## Perguntas frequentes

### Não criei um centro de preferências. Por que estou vendo "PreferenceCenterBrazeDefault" no meu painel?

Isso é usado para renderizar o centro de preferências quando o Liquid {%raw%}`${preference_center_url}`{%endraw%} legado é usado, o que significa que as etapas ou modelos do Canvas que fazem referência a {%raw%}`${preference_center_url}` ou `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} não funcionarão. Isso também se aplica a mensagens enviadas anteriormente que incluíam o Liquid legado ou "PreferenceCenterBrazeDefault" como parte da mensagem. 

Se você fizer referência a {%raw%}`${preference_center_url}`{%endraw%} em uma nova mensagem novamente, um centro de preferências chamado "PreferenceCenterBrazeDefault" será criado novamente.

### Os centros de preferência oferecem suporte a vários idiomas?

Não. No entanto, você pode aproveitar o Liquid ao escrever o HTML para páginas personalizadas de opt-in e opt-out. Se estiver usando links dinâmicos para gerenciar os cancelamentos de assinatura, esse é um único link. 

Por exemplo, se você estiver monitorando a taxa de cancelamento de assinatura de usuários de língua espanhola, precisará usar campanhas separadas ou aproveitar a análise do Currents (como observar quando um usuário cancela a assinatura e verificar o idioma preferido desse usuário).

Como outro exemplo, para acompanhar as taxas de cancelamento de assinatura de usuários de língua espanhola, você pode adicionar uma string de parâmetro de consulta como `?Spanish=true` ao URL de cancelamento de assinatura se o idioma dos usuários for alemão e usar um link de cancelamento de assinatura normal se não for:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Em seguida, por meio do Currents, você poderia identificar quais usuários falam espanhol e quantos cliques ocorreram nesse link de cancelamento de assinatura.

### Os links de cancelamento de assinatura e os centros de preferência de e-mail são necessários para o envio?

Não. Se você vir a mensagem "Seu corpo de e-mail não inclui um link de cancelamento de assinatura" ao compor uma campanha de e-mail, esse aviso é esperado se o link de cancelamento de assinatura estiver em um bloco de conteúdo.

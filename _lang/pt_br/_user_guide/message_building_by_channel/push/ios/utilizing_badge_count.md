---
nav_title: Utilização da contagem de crachás
article_title: Utilização da contagem de crachás
page_order: 8

page_type: reference
description: "Este artigo aborda o uso da contagem de emblemas do iOS para reengajar usuários que não notaram um push ou que desativaram as notificações por push em primeiro plano."
platform: iOS
channel: 
- push
- in-app messages

---

# Utilização da contagem de crachás

> A contagem de emblemas do iOS exibe o número de notificações não lidas em seu aplicativo, na forma de um círculo vermelho no canto superior direito do ícone do app. Nos últimos anos, os ícones se tornaram um meio eficaz de reengajamento dos usuários de apps.

A contagem de emblemas pode ser usada para reengajar os usuários que não notaram um push ou que desativaram as notificações por push em primeiro plano. Da mesma forma, ele pode ser usado para notificar seus usuários sobre mensagens não visualizadas, como atualizações no app.

## Contagem de crachás com Braze

Você pode especificar a contagem de emblemas desejada ao criar uma notificação por push por meio do dashboard do Braze. Isso pode ser definido como uma atribuição do usuário com envio de mensagens personalizadas, permitindo uma lógica infinitamente personalizável. Se desejar enviar um push silencioso que atualize a contagem de emblemas sem incomodar o usuário, adicione o sinalizador "Content-Available" ao seu push e deixe o conteúdo da mensagem vazio.

{% alert note %}
Está se perguntando como definir a contagem de ícones para Android? O Android lida automaticamente com a identificação do app para push, portanto, não há configurações de personalização para a identificação no Braze.
{% endalert %}

### Remoção da contagem de crachás

Defina a contagem de emblemas como 0 ou "" para remover a contagem de emblemas do ícone do app. O Braze também limpará automaticamente o emblema quando uma notificação por push for recebida enquanto o app estiver em primeiro plano.

## Práticas recomendadas

Para otimizar o poder de reengajamento do crachá, é fundamental definir as configurações do crachá de forma a simplificar a experiência do usuário.

### Mantenha o número de ícones baixo
Pesquisas mostram que, depois que a contagem de emblemas ultrapassa os dois dígitos, os usuários geralmente perdem o interesse nas atualizações e, muitas vezes, param de usar o app.

> Pode haver exceções a essa regra, dependendo da natureza do seu app (por exemplo, aplicativos de e-mail e de envio de mensagens em grupo).

### Limite as coisas que uma contagem de ícones pode representar
Ao colocar crachás, você deve tornar as notificações o mais claras e diretas possível. Ao limitar o número de coisas que uma notificação de crachá pode representar, você pode proporcionar aos seus usuários uma sensação de familiaridade com os recursos e as atualizações do seu app.


---
nav_title: Redução do tamanho da carga útil da notificação por push
article_title: Redução do tamanho da carga útil da notificação por push
page_type: solution
description: "Este artigo de ajuda fornece algumas dicas para reduzir o tamanho da carga útil de suas notificações por push se você não conseguir lançar uma campanha ou etapa do Canva devido aos limites de tamanho da carga útil do push."
channel: push
---

# Redução do tamanho da carga útil da notificação por push

Se não for possível lançar uma campanha push ou etapa do Canva porque a carga útil do push é muito grande, confira estas dicas para reduzir o tamanho da carga útil da notificação por push.

{% alert note %}
Nosso tamanho máximo de carga útil é de **3.807 bytes**. Se seu push exceder esse tamanho, a mensagem poderá não ser enviada. Recomendamos que você mantenha sua carga útil em algumas centenas de bytes.
{% endalert %}

## O que é uma carga útil push?

Os provedores de notificação por push calculam se a notificação por push pode ser exibida para um usuário observando o tamanho em bytes de toda a carga útil do push. A carga útil é limitada a **4 KB (4.096 bytes)** para a maioria dos serviços push, incluindo:

- Serviço de Notificações por Push da Apple (APNs)
- Envio de mensagens do Firebase Cloud (FCM) para Android
- Web push
- Huawei push

Esses serviços push recusarão qualquer notificação que exceda esse limite.

A Braze reserva uma parte da carga útil do push para fins de integração e análise de dados. Com isso, nosso tamanho máximo de carga útil é de **3.807 bytes**. Se seu push exceder esse tamanho, a mensagem poderá não ser enviada. Recomendamos que você mantenha sua carga útil em algumas centenas de bytes.

Os seguintes elementos em seu push compõem a carga útil do push:

- Texto, como o título e o corpo da mensagem
- Renderização final de qualquer personalização Liquid
- URLs para imagens (mas não o tamanho da imagem em si)
- URLs para direcionamentos de cliques
- Nomes de botões
- Pares de valores chave

## Dicas para reduzir o tamanho da carga útil

Para reduzir o tamanho da carga útil:

- Mantenha sua mensagem breve. É importante que ela aponte para uma ação e tenha menos de 40 caracteres.
- Omita espaços em branco e quebras de linha em sua cópia.
- Considere como o Liquid será renderizado no envio. Como a renderização final de qualquer personalização Liquid varia de usuário para usuário, o Braze não pode determinar se uma carga útil push excederá o limite de tamanho quando o Liquid for incluído. Se o Liquid renderizar uma mensagem mais curta, talvez não haja problema. No entanto, se seu Liquid resultar em uma mensagem mais longa, seu push poderá exceder o limite de tamanho da carga útil. Sempre teste sua mensagem push em um dispositivo real antes de enviá-la aos usuários.
- Considere encurtar URLs usando um encurtador de URL.

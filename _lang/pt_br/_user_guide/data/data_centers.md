---
nav_title: Centros de dados
article_title: Centros de dados
page_order: 0.1
page_type: reference
description: "Este artigo de referência aborda informações sobre data centers, inclusive onde eles estão localizados e como inscrever-se em data centers específicos da região."
---

# Centros de dados

> Os data centers do Braze foram criados para oferecer opções sobre onde os dados de seus usuários são processados e armazenados. Isso permite que você gerencie com eficiência os riscos relacionados à soberania, flexibilidade e gerenciamento de dados.

## Como funciona?

A Braze opera vários data centers localizados em diferentes regiões do mundo. Esses data centers permitem que nossos serviços sejam confiáveis e escalonáveis. Essa distribuição geográfica ajuda a minimizar a latência, que é o tempo que os dados levam para viajar entre o servidor e o usuário. 

Isso também significa que, quando um usuário interage com seu app ou site, as solicitações são direcionadas para o data center mais próximo, otimizando a performance e reduzindo os tempos de carregamento. Ao se conectar ao data center mais próximo, seus usuários podem ter tempos de carregamento rápidos, o que é especialmente importante para o envio de mensagens em tempo real e o engajamento do usuário.

Digamos que você tenha um app móvel que envia notificações por push aos usuários. Se um usuário em Melbourne receber uma notificação, a solicitação de envio dessa notificação será encaminhada para a central de notificações mais próxima na Austrália. Caso o app móvel tenha um aumento de usuários durante um evento promocional, o Braze tem uma infraestrutura escalável com vários data centers que podem lidar com o aumento da demanda.

## Lista de data centers

### Austrália

{% multi_lang_include data_centers.md datacenters='AU' %}

### União Europeia

{% multi_lang_include data_centers.md datacenters='EU' %}

### Indonésia

{% multi_lang_include data_centers.md datacenters='ID' %}

### Estados Unidos

{% multi_lang_include data_centers.md datacenters='US' %}

## Inscrever-se em data centers específicos da região

Ao configurar sua conta Braze, você pode inscrever-se em data centers específicos da região. Entre em contato com o gerente da sua conta para obter informações e recomendações sobre quais data centers funcionam melhor para você com base nas regiões geográficas dos seus usuários.

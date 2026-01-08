---
nav_title: Centros de dados
article_title: Centros de dados
page_order: 1
page_type: reference
description: "Este artigo de referência aborda informações sobre data centers, incluindo onde eles estão localizados e como se inscrever em data centers específicos da região."
---

# Centros de dados

> Os data centers da Braze foram criados para oferecer opções sobre onde os dados dos seus usuários são processados e armazenados. Isso permite que você gerencie com eficiência os riscos relacionados à soberania, flexibilidade e gerenciamento de dados.

## Como funciona

A Braze opera vários data centers localizados em diferentes regiões do mundo. Esses data centers permitem que nossos serviços sejam confiáveis e escalonáveis. Essa distribuição geográfica ajuda a minimizar a latência, que é o tempo que os dados levam para viajar entre o servidor e o usuário. 

Isso também significa que, quando um usuário interage com seu aplicativo ou site, as solicitações são direcionadas para o data center mais próximo, otimizando o desempenho e reduzindo os tempos de carregamento. Ao se conectar ao data center mais próximo, seus usuários podem ter tempos de carregamento rápidos, o que é especialmente importante para mensagens em tempo real e envolvimento do usuário.

Digamos que você tenha um aplicativo móvel que envia notificações push aos usuários. Se um usuário em Melbourne receber uma notificação, a solicitação de envio dessa notificação será encaminhada para o data center mais próximo na Austrália. Caso o aplicativo móvel sofra um aumento no número de usuários durante um evento promocional, a Braze tem uma infraestrutura dimensionável com vários data centers que podem lidar com o aumento da demanda.

## Lista de data centers

### Austrália

{% multi_lang_include data_centers.md datacenters='AU' %}

### União Europeia

{% multi_lang_include data_centers.md datacenters='EU' %}

### Indonésia

{% multi_lang_include data_centers.md datacenters='ID' %}

### Estados Unidos

{% multi_lang_include data_centers.md datacenters='US' %}

## Inscrição em data centers específicos da região

Ao configurar sua conta Braze, você pode se inscrever em data centers específicos da região. Entre em contato com o gerente da sua conta para obter informações e recomendações sobre quais data centers funcionam melhor para você com base nas regiões geográficas dos seus usuários.

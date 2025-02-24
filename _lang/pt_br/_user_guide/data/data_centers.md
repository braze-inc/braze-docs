---
nav_title: Centros de dados
article_title: Centros de dados
page_order: 0.1
page_type: reference
description: "Este artigo de referência aborda informações sobre data centers, inclusive onde eles estão localizados e como inscrever-se em data centers específicos da região."
---

# Centros de dados

> Os data centers do Braze foram criados para oferecer opções sobre onde os dados de seus usuários são processados e armazenados. Isso permite que você gerencie com eficiência os riscos relacionados à soberania, flexibilidade e gerenciamento de dados. Ao selecionar um data center Braze, você pode ter certeza de que nossa plataforma atende ou excede todos os requisitos locais de gerenciamento de dados.

## Como funciona?

A Braze opera vários data centers localizados em diferentes regiões do mundo. Esses data centers permitem que nossos serviços sejam confiáveis e escalonáveis. Essa distribuição geográfica ajuda a minimizar a latência, que é o tempo que os dados levam para viajar entre o servidor e o usuário. 

Isso também significa que, quando um usuário interage com seu app ou site, as solicitações são direcionadas para o data center mais próximo, otimizando a performance e reduzindo os tempos de carregamento. Ao se conectar ao data center mais próximo, seus usuários podem ter tempos de carregamento rápidos, o que é especialmente importante para o envio de mensagens em tempo real e o engajamento do usuário.

Digamos que você tenha um app móvel que envia notificações por push aos usuários. Se um usuário em Melbourne receber uma notificação, a solicitação de envio dessa notificação será encaminhada para a central de notificações mais próxima na Austrália. Caso o app móvel tenha um aumento de usuários durante um evento promocional, o Braze tem uma infraestrutura escalável com vários data centers que podem lidar com o aumento da demanda.

## Lista de data centers

Consulte a tabela a seguir para obter uma lista dos data centers disponíveis.

<style>
table th:nth-child(1) {
    width: 10%;
}
table th:nth-child(2) {
    width: 33%;
}
table th:nth-child(3) {
    width: 33%;
}
table th:nth-child(4) {
    width: 24%;
}
table td {
    word-break: break-word;
}
</style>
<table>
  <thead>
    <tr>
      <th>Região do data center</th>
      <th>URL do dashboard</th>
      <th>Ponto de extremidade REST</th>
      <th>endpoint de SDK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Austrália</b></td>
      <td><code>https://dashboard.au-01.braze.com</code></td>
      <td><code>https://rest.au-01.braze.com</code></td>
      <td><code>sdk.au-01.braze.com</code></td>
    </tr>
    <tr>
      <td><b>Europa</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.eu</code></li>
          <li><code>https://dashboard-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.fra-01.braze.eu</code></li>
          <li><code>https://rest.fra-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.fra-01.braze.eu</code></li>
          <li><code>sdk.fra-02.braze.eu</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>EUA</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.com</code></li>
          <li><code>https://dashboard-02.braze.com</code></li>
          <li><code>https://dashboard-03.braze.com</code></li>
          <li><code>https://dashboard-04.braze.com</code></li>
          <li><code>https://dashboard-05.braze.com</code></li>
          <li><code>https://dashboard-06.braze.com</code></li>
          <li><code>https://dashboard-07.braze.com</code></li>
          <li><code>https://dashboard-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.iad-01.braze.com</code></li>
          <li><code>https://rest.iad-02.braze.com</code></li>
          <li><code>https://rest.iad-03.braze.com</code></li>
          <li><code>https://rest.iad-04.braze.com</code></li>
          <li><code>https://rest.iad-05.braze.com</code></li>
          <li><code>https://rest.iad-06.braze.com</code></li>
          <li><code>https://rest.iad-07.braze.com</code></li>
          <li><code>https://rest.iad-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.iad-01.braze.com</code></li>
          <li><code>sdk.iad-02.braze.com</code></li>
          <li><code>sdk.iad-03.braze.com</code></li>
          <li><code>sdk.iad-04.braze.com</code></li>
          <li><code>sdk.iad-05.braze.com</code></li>
          <li><code>sdk.iad-06.braze.com</code></li>
          <li><code>sdk.iad-07.braze.com</code></li>
          <li><code>sdk.iad-08.braze.com</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Inscrever-se em data centers específicos da região

Ao configurar sua conta Braze, você pode inscrever-se em data centers específicos da região. Entre em contato com o gerente da sua conta para obter informações e recomendações sobre quais data centers funcionam melhor para você com base nas regiões geográficas dos seus usuários.

---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "Este artigo de referência descreve a parceria entre a Braze e a Infillion, que permite aperfeiçoar a relevância do seu marketing usando dados de localização."
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/) permite que você aperfeiçoe a relevância do seu marketing usando dados de localização. Seu SDK local, combinado com software de geofencing e beacons, possibilita experiências móveis relevantes, personalizadas e com reconhecimento de proximidade.

Combine o suporte ao seu beacon ou geofence com os recursos de direcionamento e envio de mensagens da Braze para aprender mais sobre as ações físicas do seu usuário e enviar mensagens a eles de acordo. Essa integração de parceria abre uma série de casos de uso para:

- **Marketing:** Envie envios de mensagens contextualmente relevantes e crie jornadas experienciais para o consumidor.
- **Análise competitiva:** Defina disparos em locais competitivos para entender as tendências e os padrões dos consumidores.
- **Insights sobre o público:** Entenda os comportamentos de visitação de seus usuários e segmente mais com base nessas informações.

{% alert note %}
Esta integração funciona da mesma forma para beacons da Infillion e soluções de geofence da Infillion.
{% endalert %}

## Pré-requisitos

| Requisito| Descrição|
| ---| ---|
| [Conta de gerente da Infillion](https://manager.gimbal.com/login/users/sign_in) | Uma conta de gerente da Infillion é necessária para aproveitar esta parceria. |
|[SDK de Localização da Infillion](https://docs.gimbal.com/index.html) | O SDK de Localização da Infillion possibilita experiências móveis baseadas em localização macro e micro usando beacons de proximidade e geofences que permitem que você se comunique de forma mais eficaz com os usuários do seu app. É necessário ter o SDK implementado e as geofences (ou beacons) configuradas. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## integração de SDK

Para integrar a Braze e a Infillion, você deve implementar o SDK de Localização da Infillion e criar uma conta de gerente da Infillion. As seguintes integrações para Android, FireOS e iOS criarão um evento personalizado exclusivo para cada novo local em que um usuário entrar. Esses eventos podem ser usados para disparar e redirecionar suas campanhas e Canvas.

Se você prevê a criação de mais de 50 lugares, recomendamos a criação de um evento personalizado genérico `Places Entered` e a adição do nome do lugar como uma propriedade do evento. 

1. Integre o [SDK da Infillion](https://manager.gimbal.com/sdk_downloads) para Android e iOS no seu app seguindo as instruções na [documentação da Infillion](https://docs.gimbal.com/).
2. Use a [API REST de lugares da Infillion](https://docs.gimbal.com/rest.html) para obter `places` do usuário.
3. Vincule sua conta da Infillion à Braze inserindo a [chave da API REST](https://manager.gimbal.com/apps) da Braze.
4. Configure [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) no SDK do Braze. Você pode integrar a Infillion com a Braze para [Android e FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons).
5. Propriedades de registro para esses eventos (nome do local, tempo de permanência).
6. Use essas propriedades e eventos para disparar campanhas e Canvas no Braze. 


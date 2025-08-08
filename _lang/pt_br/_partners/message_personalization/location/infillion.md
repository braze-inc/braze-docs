---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "Este artigo de referência descreve a parceria entre o Braze e a Infillion, que ativa a capacitação para aperfeiçoar sua relevância de marketing usando dados locais."
page_type: partner
search_tag: Partner

---

# Infillion

> [O Infillion](https://infillion.com/) o capacita a aperfeiçoar sua relevância de marketing usando dados locais. Seu SDK local, combinado com software de geofencing e beacons, possibilita experiências móveis relevantes, personalizadas e com reconhecimento de proximidade.

Combine seu suporte a beacon ou geofence com os recursos de direcionamento e envio de mensagens do Braze para saber mais sobre as ações físicas do usuário e enviar as mensagens correspondentes. Essa integração de parceria abre uma série de casos de uso para:

- **Marketing:** Envie envios de mensagens contextualmente relevantes e crie jornadas experienciais para o consumidor.
- **Análise competitiva:** Defina disparos em locais competitivos para entender as tendências e os padrões dos consumidores.
- **Insights sobre o público:** Entenda os comportamentos de visitação de seus usuários e segmente mais com base nessas informações.

{% alert note %}
Essa integração funciona da mesma forma para os beacons da Infillion e para as soluções de geofence da Infillion.
{% endalert %}

## Pré-requisitos

| Requisito| Descrição|
| ---| ---|
| [Conta do gerente da Infillion](https://manager.gimbal.com/login/users/sign_in) | É necessário ter uma conta de gerente da Infillion para aproveitar essa parceria. |
|[Infillion Location SDK](https://docs.gimbal.com/index.html) | O Infillion Location SDK possibilita experiências móveis baseadas em macro e micro locais usando beacons de proximidade e geofences que permitem uma comunicação mais eficaz com os usuários do seu app. É necessário ter o SDK implementado e as geofences (ou beacons) configuradas. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## integração de SDK

Para integrar o Braze e o Infillion, você deve implementar o Infillion Location SDK e criar uma conta de gerente do Infillion. As seguintes integrações para Android, FireOS e iOS criarão um evento personalizado exclusivo para cada novo local em que um usuário entrar. Esses eventos podem ser usados para disparar e redirecionar suas campanhas e Canvas.

Se você prevê a criação de mais de 50 lugares, recomendamos a criação de um evento personalizado genérico `Places Entered` e a adição do nome do lugar como uma propriedade do evento. 

1. Integre o [Infillion SDK](https://manager.gimbal.com/sdk_downloads) para Android e iOS em seu app seguindo as instruções da [documentação do Infillion](https://docs.gimbal.com/).
2. Use a [API REST local](https://docs.gimbal.com/rest.html) da Infillion para obter o usuário `places`.
3. Vincule sua conta Infillion ao Braze inserindo a [chave da API REST](https://manager.gimbal.com/apps) do Braze.
4. Configure [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) no SDK do Braze. Você pode integrar o Infillion com o Braze para [Android e FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons).
5. Propriedades de registro para esses eventos (nome do local, tempo de permanência).
6. Use essas propriedades e eventos para disparar campanhas e Canvas no Braze. 


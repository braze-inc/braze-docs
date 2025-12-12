---
nav_title: Gerenciamento do consentimento
article_title: Gerenciando o consentimento
page_order: 10
page_type: reference
description: "Este artigo de referência fornece dicas sobre como gerenciar o consentimento usando o Braze."
---

# Gerenciamento do consentimento

> Este artigo de referência fornece dicas sobre como gerenciar o consentimento de seus usuários usando o Braze.

A Braze não pode fornecer conselhos específicos sobre a interpretação de leis e regulamentos nem oferecer orientação sobre como lidar com o gerenciamento de consentimento, pois isso dependerá da interpretação da lei pela sua equipe jurídica. No entanto, oferecemos uma série de ferramentas para apoiar o gerenciamento de assinaturas e consentimento.

Sua abordagem deve depender do rigor exigido pela sua equipe jurídica com base na interpretação da lei. Aqui estão algumas opções a serem consideradas, listadas da mais rigorosa para a menos rigorosa:

- **Equipes:** Use [as equipes do Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) para uma verdadeira governança. Isso envolve adicionar um atributo personalizado a todos os perfis de usuário para indicar seu status de consentimento, data de consentimento ou ambos. Em seguida, você deve migrar todas as campanhas e Canvases para a equipe designada e ajustar as permissões de usuário no painel de acordo.
- **Atributo de perfil de usuário:** Adicione um atributo de consentimento a todos os perfis de usuário. Esse atributo indicará se um usuário deu consentimento ou não. No futuro, você poderá incluir um segmento de usuários que consentiram (por exemplo, `consent = true`) em todas as suas campanhas e Canvases.
- **Grupos de assinatura específicos do canal:** Manipule grupos de assinatura para canais específicos (notificações push, e-mail, etc.) para gerenciar o consentimento. Inicialmente, marque os usuários como não inscritos nesses canais e só os marque como inscritos depois que eles consentirem.

{% alert important %}
Consulte sua equipe jurídica para determinar a abordagem apropriada para a conformidade da sua organização com os requisitos de gerenciamento de consentimento.
{% endalert %}


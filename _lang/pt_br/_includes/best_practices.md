### Preservação automática do histórico do usuário anônimo

| Contexto de identificação | Comportamento de preservação |
| ---------------------- | -------------------------- |
| O usuário **não foi** identificado anteriormente | O histórico anônimo **é mesclado** com o perfil do usuário após a identificação. |
| O usuário **foi** previamente identificado no app ou via API | O histórico anônimo **não é mesclado** com o perfil do usuário após a identificação. |
{: .reset-td-br-1 .reset-td-br-2}

Consulte [Perfis de usuários identificados]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) para saber mais sobre o que ocorre quando você identifica usuários anônimos.

### Notas adicionais e práticas recomendadas

Observe o seguinte:

- Se o seu app for usado por várias pessoas, é possível atribuir a cada usuário um identificador exclusivo para rastreá-los.
- Após a definição de um ID de usuário, não é possível reverter esse usuário para um perfil anônimo.
- Não altere o ID do usuário quando um usuário fizer o registro, pois isso pode separar o dispositivo do perfil do usuário.
  - Como resultado, não será possível direcionar mensagens de reengajamento para o usuário que se desconectou anteriormente. Se você prevê múltiplos usuários no mesmo dispositivo, mas deseja direcionar apenas um deles quando seu aplicativo estiver desconectado, recomendamos manter separadamente o rastreamento do ID do usuário que você deseja direcionar enquanto estiver desconectado e retornar a esse ID de usuário como parte do processo de logout do seu aplicativo. Por padrão, somente o último usuário registrado receberá notificações por push do seu app.
- Mudar de um usuário identificado para outro é uma operação relativamente cara.
  - Quando você solicita a troca de usuário, a sessão atual do usuário anterior é automaticamente encerrada e uma nova sessão é iniciada. O Braze fará automaticamente uma solicitação de atualização de dados para mensagens no app e outros recursos do Braze para o novo usuário.

{% alert tip %}
Se houver aceitação de usar um hash de um identificador exclusivo como ID de usuário, certifique-se de normalizar a entrada da função de hash. Por exemplo, se for usar um hash de um endereço de e-mail, confirme que está removendo os espaços em branco à esquerda e à direita da entrada e levando em conta a localização.
{% endalert %}
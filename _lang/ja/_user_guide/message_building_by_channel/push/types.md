---
nav_title: "プッシュ通知の種類"
article_title: プッシュ通知の種類
page_order: 1
page_type: glossary
description: "この用語集には、Brazeで送信できるプッシュ通知の種類が記載されている。"
channel: push

layout: glossary_page
glossary_top_header: "Types of push notifications"
glossary_top_text: "There are many types of push notifications you can use to interact with your customers. These can be narrowed by channel and used to meet the needs of many different users. You can configure most of these settings in your Push campaigns, but there are notes in the following descriptions that will indicate whether any backend configurations are needed and what those might be."

glossary_tag_name: Channels
glossary_filter_text: "Select any of the following channels to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: iOS
  - name: Android
  - name: Web

glossaries:
  - name: "レギュラープッシュ"
    description: "包括的なプッシュ・メッセージだ。ユーザーのデバイスで通知音を送出し、通知バーやスタックにメッセージをスライド表示します。"
    tags:
      - iOS
      - Android
      - Web
  - name: "ウェブプッシュ"
    description: "これらのプッシュメッセージは、ウェブアプリやブラウザに表示される。それでも、顧客にリーチするには許可が必要です。ユーザーが非表示のブラウザーを使用している場合、ウェブ・プッシュは機能しないことに注意。"
    tags:
      - Web
  - name: "プッシュプライマーキャンペーン"
    description: "ユーザーからプッシュ通知の明示的なオプトインまたはオプトアウトの意志を確認するために使用されるアプリ内メッセージのキャンペーン。プライマーを通じて、デバイスの設定でプッシュをオフにしている可能性の高いユーザーへの通知送信を避けることができる。iOS の場合、プッシュ通知のキャンペーンが重要です。これは、ユーザーが明示的に iOS のネイティブプッシュプロンプトにオプトインするまで、フォアグラウンドのプッシュ通知 (デバイスをスリープ解除する通知など) が有効にならないためです。"
    tags:
      - iOS
      - Android
      - Web
  - name: "プッシュ通知ストーリー"
    description: "プッシュストーリーは、カルーセルの形でユーザーを視覚的な旅に誘う没入型のメッセージだ。これらはモバイルデバイスでのみ使用できます。"
    tags:
      - iOS
      - Android
  - name: "アクションボタンによるプッシュ通知"
    description: "プッシュ・ウィズ・アクション・ボタンは、ユーザーに選択肢を提供し、いくつかの行動を呼びかけることができるメッセージだ。"
    tags:
      - iOS
      - Android
      - Web
  - name: "リッチなプッシュ通知"
    description: "リッチプッシュ通知とは、単純なアイコンと行動喚起のテキストだけでなく、没入感のある画像やクリエイティブなコンテンツを含む通知である。"
    tags:
      - iOS
      - Android
  - name: "iOS 向けの暫定プッシュ通知"
    description: "iOS12でアップルによって導入された仮承認は、iOSアプリのインストール時に自動的に発生し、ブランドはユーザーにプッシュプロンプトを表示することなくサイレント通知を送ることができる。サイレント・プッシュが送信され、デバイスの通知トレイに表示されると、ユーザーにはプッシュ通知を許可または中止するオプションが与えられる。"
    tags:
      - iOS
  - name: "HTML プッシュ通知"
    description: "HTMLプッシュ通知は、HTMLでハードコーディングされたプッシュメッセージで、Brazeが提供するあらかじめ設定されたプッシュテンプレートを使用しない。HTMLプッシュ通知を作成するオプションがあることで、プッシュメッセージをどのように見せるかに関して、御社は完全な創造的自由と一貫したブランディングを持つことができる。"
    tags:
      - Android
  - name: "通知IDとチャンネルID"
    description: "通知 ID とチャネル ID を使用すると、ユーザーがすでに受信したが開封していないプッシュ通知を置き換えたり更新したりできます。"
    tags:
      - iOS
      - Android
  - name: "バックグラウンドまたはサイレントプッシュ通知"
    description: "デバイス上でレンダリングされないプッシュ通知。通常、バックグラウンドプロセスとアンインストール追跡の目的で、情報のパケットをアプリに送信するために使用されます。バックグラウンド・プッシュまたはサイレント・プッシュを送信するには、バックグラウンド・イネーブル・プッシュトークンが必要である。"
    tags:
      - iOS
      - Android
      - Web
  - name: "ウェアラブルプッシュ通知"
    description: "これらのプッシュ通知によって、ブランドはApple Watchのようなウェアラブル端末に直接メッセージを送ることができる。"
    tags:
      - iOS

---

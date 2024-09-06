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
    description: "包括的なプッシュ・メッセージだ。これらは、通知音とメッセージとともにユーザーのデバイスに表示され、通知バーやスタックにスライド表示される。"
    tags:
      - iOS
      - Android
      - Web
  - name: "ウェブプッシュ"
    description: "これらのプッシュメッセージは、ウェブアプリやブラウザに表示される。それでも、顧客と接触するには許可が必要だ。ユーザーが非表示のブラウザーを使用している場合、ウェブ・プッシュは機能しないことに注意。"
    tags:
      - Web
  - name: "プッシュプライマーキャンペーン"
    description: "アプリ内メッセージキャンペーンは、ユーザーから明示的なプッシュオプトインまたはオプトアウトのシグナルを得るために使用される。プライマーを通じて、デバイスの設定でプッシュをオフにしている可能性の高いユーザーへの通知送信を避けることができる。iOSの場合、フォアグラウンド・プッシュ通知（デバイスをスリープ解除する通知など）は、ユーザーが明示的にiOSのネイティブ・プッシュ・プロンプトをオプトインするまで有効にならないため、プッシュ・キャンペーンが関連する。"
    tags:
      - iOS
      - Android
      - Web
  - name: "プッシュ通知ストーリー"
    description: "プッシュストーリーは、カルーセルの形でユーザーを視覚的な旅に誘う没入型のメッセージだ。これらはモバイル機器でのみ利用できる。"
    tags:
      - iOS
      - Android
  - name: "アクションボタンで押す"
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
  - name: "サイレント・プッシュ通知"
    description: "デバイス上でレンダリングする際、デバイスをスリープ解除しないプッシュ通知。代わりに、通知はデバイスの通知トレイに保存される。"
    tags:
      - iOS
      - Android
  - name: "iOS向け暫定プッシュ通知"
    description: "iOS12でアップルによって導入された仮承認は、iOSアプリのインストール時に自動的に発生し、ブランドはユーザーにプッシュプロンプトを表示することなくサイレント通知を送ることができる。サイレント・プッシュが送信され、デバイスの通知トレイに表示されると、ユーザーにはプッシュ通知を許可または中止するオプションが与えられる。"
    tags:
      - iOS
  - name: "HTML プッシュ通知"
    description: "HTMLプッシュ通知は、HTMLでハードコーディングされたプッシュメッセージで、Brazeが提供するあらかじめ設定されたプッシュテンプレートを使用しない。HTMLプッシュ通知を作成するオプションがあることで、プッシュメッセージをどのように見せるかに関して、御社は完全な創造的自由と一貫したブランディングを持つことができる。"
    tags:
      - Android
  - name: "通知IDとチャンネルID"
    description: "Notification IDとChannel IDは、ユーザーが既に受信したが開いていないプッシュ通知を置き換えたり更新したりすることを可能にする。"
    tags:
      - iOS
      - Android
  - name: "バックグラウンド・プッシュ通知"
    description: "デバイス用にレンダリングされていないプッシュ通知。通常、バックグラウンド・プロセスやアンインストール追跡のために、アプリに情報のパケットを送るために使われる。バックグラウンド・プッシュを送信するには、バックグラウンド対応プッシュ・トークンが必要である。"
    tags:
      - iOS
      - Android
      - Web
  - name: "ウェアラブル・プッシュ通知"
    description: "これらのプッシュ通知によって、ブランドはApple Watchのようなウェアラブル端末に直接メッセージを送ることができる。"
    tags:
      - iOS

---

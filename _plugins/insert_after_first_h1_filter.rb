# frozen_string_literal: true

module Jekyll
  module InsertAfterFirstH1Filter
    FIRST_H1_RE = %r{(<h1\b[^>]*>.*?</h1>)}mi

    # Inserts HTML snippet immediately after the first <h1>...</h1> in rendered content.
    # If there is no h1, prepends the snippet (still near top of article body).
    def insert_after_first_h1(html, snippet)
      body = html.to_s
      insert = snippet.to_s
      return body if insert.strip.empty?

      if (m = body.match(FIRST_H1_RE))
        body.sub(m[0], m[0] + insert)
      else
        insert + body
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::InsertAfterFirstH1Filter)

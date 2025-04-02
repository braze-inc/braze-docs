require 'cgi'
require 'kramdown'

module Jekyll
  class ScrollyCodeBlock < Liquid::Block
    @@counter = 0  # Class variable to generate unique IDs

    def initialize(tag_name, markup, tokens)
      super
    end

    def render(context)
      @@counter += 1
      unique_id = "scrolly-code-block-#{@@counter}"

      # Get the raw content inside {% scrolly %} ... {% endscrolly %}
      content = super.lstrip

      # --- 1) Extract the first code block for syntax highlighting ---
      code_match = content.match(/```(\w+)\s*\n([\s\S]*?)```/)
      if code_match
        language = code_match[1]
        raw_code = code_match[2].strip
      else
        language = "plaintext"
        raw_code = ""
      end

      # Remove that code block from the content so it's not processed as a step.
      content_wo_code = content.sub(code_match.to_s, '')

      # --- 2) Parse narrative steps marked by !!step on a line by itself. ---
      # We split on /^!!step\s*$/ so that the step marker must be alone on its line.
      # The first chunk (index 0) is anything before the first !!step (often empty).
      # Each subsequent chunk is one step's block, whose first line is lines=..., 
      # and the rest is pure Markdown.
      chunks = content_wo_code.split(/^!!step\s*$/)
      # If the user never wrote !!step, chunks[1..-1] is empty, so no steps.
      steps = []
      chunks[1..-1].each do |chunk|
        block = chunk.strip
        next if block.empty?

        # The first line must be lines=...
        lines_line, *narrative_lines = block.lines
        lines_line = lines_line.to_s.strip
        lines = lines_line[/lines=(\d[\d,-]*)/, 1] || ""

        # The rest is pure Markdown for the narrative
        narrative_markdown = narrative_lines.join
        narrative_html = Kramdown::Document.new(narrative_markdown).to_html

        steps << { "lines" => lines, "narrative" => narrative_html }
      end

      # --- 3) Build the final HTML structure ---
      html = []
      html << "<div id=\"#{unique_id}\" class=\"scrolly-code-block\">"
      html << '  <div class="scrolly-container">'

      # Left side: Steps
      html << '    <div class="scrolly-text">'
      steps.each_with_index do |step, idx|
        html << "      <div class=\"scrolly-step\" data-index=\"#{idx}\" data-lines=\"#{step['lines']}\">"
        # Wrap the narrative in its own container to enforce consistent top margins.
        html << "        <div class=\"scrolly-narrative\">#{step['narrative']}</div>"
        html << "      </div>"
      end
      html << '    </div>'

      # Right side: Code
      html << '    <div class="scrolly-code">'
      html << '      <div class="code-sticky">'
      html << "        <pre class=\"code-animate hljs language-#{language}\"><code data-full-code=\"#{CGI.escapeHTML(raw_code)}\"></code></pre>"
      html << '      </div>'
      html << '    </div>'

      html << '  </div>'
      # A buffer to ensure the last step can be scrolled fully into view
      html << '  <div class="scrolly-buffer" style="height: 30vh;"></div>'
      html << '</div>'

      html.join("\n")
    end
  end
end

Liquid::Template.register_tag('scrolly', Jekyll::ScrollyCodeBlock)

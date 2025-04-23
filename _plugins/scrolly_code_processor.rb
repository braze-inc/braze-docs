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

      # --- 1) Separate code from narrative ---
      # Everything before the first occurrence of "!!step" is treated as code.
      first_step_index = content.index("!!step")
      if first_step_index
        code_portion = content[0...first_step_index]
        narrative_portion = content[first_step_index..-1]
      else
        code_portion = content
        narrative_portion = ""
      end

      # --- 2) Extract all code blocks from the code portion ---
      # Code block syntax: ```<lang> file=filename (or file-filename) then newline, then code, then ```
      code_regex = /
        ```(\w+)(?:\s+(?:file=|file-)([^\s]+))\s*\n  # Capture language and required file name
        ([\s\S]*?)                                   # Capture code content
        ```/x

      code_blocks = []
      content.scan(code_regex) do |lang, file, code_content|
        if file.nil? || file.strip.empty?
          raise "Error in scrolly block: Code blocks must include a file name. Use syntax: ```#{lang} file=script.js"
        end
        original_file = file.strip
        code_blocks << {
          "language" => lang,
          "file" => original_file.downcase,
          "label" => original_file,
          "code" => code_content.strip
        }
      end

      # Remove all code blocks from the content so that narrative steps aren’t affected.
      content_wo_code = content.gsub(code_regex, '')

      # --- 3) Parse narrative steps from the content without code ---
      # Split on lines that contain only "!!step"
      chunks = content_wo_code.split(/^!!step\s*$/)
      steps = []
      # The first chunk (index 0) is before any step marker (often empty).
      chunks[1..-1]&.each do |chunk|
        block = chunk.strip
        next if block.empty?

        # The first line must contain the line setting in the format: lines-<filename>=<range>
        lines_line, *narrative_lines = block.lines
        lines_line = lines_line.to_s.strip
        if lines_line =~ /^lines-([\w\.\-]+)=\s*(\d[\d,-]*)\s*$/
          file_key = $1.strip.downcase
          range_value = $2.strip
        else
          raise "Error in scrolly block: Invalid lines setting syntax: #{lines_line.inspect}. Use 'lines-<filename>=<range>' (e.g., lines-index.js=1-3)."
        end
        narrative_markdown = narrative_lines.join
        narrative_html = Kramdown::Document.new(narrative_markdown).to_html

        steps << { "file" => file_key, "range" => range_value, "narrative" => narrative_html }
      end

      # --- 4) Build the final HTML structure ---
      html = []
      html << "<div id=\"#{unique_id}\" class=\"scrolly-code-block\">"
      html << "  <div class=\"scrolly-container\">"

      # Left side: Narrative steps with file-specific line data.
      html << "    <div class=\"scrolly-text\">"
      steps.each_with_index do |step, idx|
        file_attr = step["file"].gsub('.', '-')
        html << "      <div class=\"scrolly-step\" data-index=\"#{idx}\" data-lines-#{file_attr}=\"#{step['range']}\">"
        html << "        <div class=\"scrolly-narrative\">#{step['narrative']}</div>"
        html << "      </div>"
      end
      html << "    </div>"

      # Right side: Code tabs and panels.
      html << "    <div class=\"scrolly-code\">"
      html << "      <div class=\"scrolly-tab-selector\">"
      code_blocks.each_with_index do |cb, idx|
        file_attr = cb["file"].downcase.gsub('.', '-')
        active_class = idx == 0 ? "scrolly-active-tab" : ""
        html << "        <button class=\"scrolly-tab #{active_class}\" data-file=\"#{file_attr}\"><i class=\"fa fa-file\"></i> #{cb['label']}</button>"
      end
      html << "      </div>"
      html << "      <div class=\"code-blocks\">"
      code_blocks.each_with_index do |cb, idx|
        file_attr = cb["file"].downcase.gsub('.', '-')
        style = idx == 0 ? "" : " style=\"display: none;\""
        html << "        <pre class=\"code-animate hljs language-#{cb['language']}\" data-file=\"#{file_attr}\"#{style}><code data-full-code=\"#{CGI.escapeHTML(cb['code'])}\"></code></pre>"
      end
      html << "      </div>"
      html << "    </div>"

      html << "  </div>"
      # Buffer to allow the last narrative step to scroll fully into view.
      html << "</div>"

      html.join("\n")
    end
  end
end

Liquid::Template.register_tag('scrolly', Jekyll::ScrollyCodeBlock)

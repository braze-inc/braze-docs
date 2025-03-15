rule "BRZE_ALT_TEXT", "Missing Image/Link Alt Text" do
  tags :braze
  aliases 'alt-validator'
  docs 'Alt tag missing in image/link'
  check do |doc|
    offenses = []
    doc.lines.each_with_index do |line, line_number|
      # Check Markdown images: ![alt](url) or ![alt][reference]
      line.scan(/!\[([^\]]*)\](?:\(([^)]+)\)|\[([^\]]+)\])/) do |match|
        alt_text = match.first.strip
        if alt_text.empty?
          offenses.push(line_number + 1)
        end
      end

      # Check Markdown links (that aren’t images): [text](url) or [text][reference]
      # The regex uses a negative lookbehind to ensure the [ isn't preceded by !.
      line.scan(/(?<!!)\[([^\]]*)\](?:\(([^)]+)\)|\[([^\]]+)\])/) do |match|
        link_text = match.first.strip
        if link_text.empty?
          offenses.push(line_number + 1)
        end
      end
    end
    offenses
  end
end

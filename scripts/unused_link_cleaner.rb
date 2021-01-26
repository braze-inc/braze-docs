require 'fileutils'
require "readline"

INPUT_FILE = ARGV[0]

unless !INPUT_FILE.nil? && File.exists?(INPUT_FILE)
  puts "Expected input file #{INPUT_FILE} to exist. Exiting."
  exit()
end

def get_file_contents(file_path)
  return File.read(file_path)
end

def grep_with_index(string_lines, query)
  return string_lines.each_with_index.select{|e,| e =~ query}
end

def get_shortlink_lines(file_lines)
  return grep_with_index(file_lines, /\[.*\]: .*/)
end

def remove_unused_shortlink_lines(original_file_lines)
  shortlink_lines = get_shortlink_lines(lines)
  lines_to_remove = []

  ref_query = /\[(.*)\]: .*/
  shortlink_lines.each do |current_line|
    # Get the reference from the link itself to search for
    # "[1]: https://google.com" has a ref of "1"
    ref = current_line[0].match(ref_query)[1]

    # Search for that ref in the file
    is_in_file = original_file_lines.grep(/\[#{ref}\]/)
    if is_in_file.length < 2
      # This shortlink can be deleted
      lines_to_remove << current_line[1]
    end
  end

  # Since we're deleting the original list, the line number 
  # we actually want to delete will be off by 1 per previous deletion
  # Deletion always goes in order from smallest line to highest
  lines_deleted = 0
  lines_to_remove.each do |line_to_remove|
    original_file_lines.delete_at(line_to_remove - lines_deleted)
    lines_deleted += 1
  end
  puts "deleted #{lines_deleted} lines"
end

def is_md_file(full_file_path)
  return File.extname(full_file_path) == ".md"
end

def clean_single_file(full_file_path)
  contents = get_file_contents(full_file_path)
  lines = contents.lines
  # find the url shortlinks at the bottom of the file
  remove_unused_shortlink_lines(lines)

  # writeback to the original file with our changes
  File.open(full_file_path, 'w') do |out|
    out << lines.join()
  end  
end

def walk_directory(directory)
  Dir.foreach(directory) do |file|
    path = File.join(directory, file)
    if (file == '.' or file == '..' or file == '.DS_Store')
      # Always skip these files
      next
    elsif File.directory?(path)
      walk_directory(path)
    elsif is_md_file(path)
      puts "cleaning file #{file} with path #{path}"
      clean_single_file(path)
    end
  end
end

if File.directory?(INPUT_FILE)
  puts "Input directory #{INPUT_FILE}. Will recurse!"
  prompt_response = Readline.readline("Continue? [y/n] ") 

  if (prompt_response != "y")
    puts "Not continuing!"
    exit(0)
  end

  walk_directory(INPUT_FILE)
else
  puts "Input file #{INPUT_FILE}"
  if is_md_file(INPUT_FILE)
    clean_single_file(INPUT_FILE)
  end
end

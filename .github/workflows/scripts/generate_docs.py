import argparse
import openai
import os

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Generate documentation using OpenAI API.")
    parser.add_argument('--prompt', required=True, help='Custom prompt for the documentation')
    parser.add_argument('--specs', required=True, help='Path to the specs file')
    parser.add_argument('--style_guide', required=True, help='Path to the style guide file')
    parser.add_argument('--output', required=True, help='Path to the output user guide file')
    args = parser.parse_args()

    # Read input files
    prompt = args.prompt
    specs = read_file(args.specs)
    style_guide = read_file(args.style_guide)

    # Compose the full prompt for the LLM
    full_prompt = f"""
You are an expert technical writer for Braze. 
Your task is to update or author user guide documentation based on the following:

Prompt/Instructions:
{prompt}

Specs:
{specs}

Style Guide:
{style_guide}

Please ensure the documentation adheres to the style guide and information architecture, is clear and concise, and is suitable for Braze's documentation site. Output only the markdown content for the user guide.
"""

    # Call OpenAI API
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # or "gpt-4" if you don't have access to gpt-4o
        messages=[
            {"role": "system", "content": "You are a helpful technical writer."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=2000,
        temperature=0.3
    )

    # Extract the generated documentation
    generated_content = response['choices'][0]['message']['content']

    # Write to output file
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(generated_content)

    print(f"Documentation generated and written to {args.output}")

if __name__ == "__main__":
    main()

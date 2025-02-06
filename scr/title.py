import os
from block_to_html import SUPER_MEGA_markdown_to_html


def extract_title(file_path):
    header = ""

    
    with open(file_path,'r+') as f:
        for line in f:
            line = line.strip()
            if "# " == line[:2]:
                header = line


                f.closed

                return header[2:]
        raise Exception("Title not found!")

def generate_page(from_path, template_path, dest_path):

    markdown = ""
    template = ""
    title = ""
    content = ""

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()
    f.close

    with open(template_path) as f:
        template = f.read()
    f.close
    
    title = extract_title(from_path)

    content = SUPER_MEGA_markdown_to_html(markdown)

    template.replace("{{ Title }}",title)
    template.replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(template)
    f.close




from pathlib import Path
from docxtpl import DocxTemplate

template_path = Path(r"C:\Users\gabyn\OneDrive\Desktop\BARST 1 try") / "my_word_template.docx"
output_path = Path(r"C:\Users\gabyn\OneDrive\Desktop\BARST 1 try") / "generated_new5.docx"

doc = DocxTemplate(template_path)
context = {"NAME": "Gaabriel"}
doc.render(context)
doc.save(output_path)
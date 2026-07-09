from pdf2image import convert_from_path
import os

ws = "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/4_gen_paper_repo/_4_assemble_paper/paper/workspace"
pdf_path = os.path.join(ws, "paper.pdf")
out_dir = os.path.join(ws, "pages")
os.makedirs(out_dir, exist_ok=True)

pages = convert_from_path(pdf_path, dpi=150)
print(f"Total pages: {len(pages)}")
for i, page in enumerate(pages):
    out_path = os.path.join(out_dir, f"page_{i+1:02d}.png")
    page.save(out_path, "PNG")
    print(f"Saved page {i+1} -> {out_path}")
print("Done.")

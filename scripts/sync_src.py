import pathlib

root = pathlib.Path(__file__).parent.parent
index_path = root / "index.html"
src_index_path = root / "src" / "index.html"

content = index_path.read_text(encoding="utf-8")
src_content = content.replace("./assets/", "../assets/")
src_index_path.write_text(src_content, encoding="utf-8")
print(f"src/index.html atualizado ({len(src_content)} caracteres)!")

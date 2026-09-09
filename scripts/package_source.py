"""Ship the modified AGPL source without Cargo's build cache."""
from pathlib import Path
import os
import zipfile

root = Path(__file__).resolve().parents[1]
source = root / 'source/concat_tr'
with zipfile.ZipFile(root/'stage/Oblivion-0.2.2-source.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    for folder, directories, files in os.walk(source):
        directories[:] = [name for name in directories if name not in {'target', '.git', '__pycache__'}]
        for name in files:
            path = Path(folder)/name
            archive.write(path, 'Oblivion-source/'+path.relative_to(source).as_posix())
    archive.write(root/'OBLIVION_TR.md', 'Oblivion-source/OBLIVION_TR.md')

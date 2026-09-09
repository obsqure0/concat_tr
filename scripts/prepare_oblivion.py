"""Reproduce Oblivion source from the original licensed source plus one patch."""
from pathlib import Path
import subprocess
import zipfile

root = Path(__file__).resolve().parents[1]
target = root / 'source'
if target.exists():
    raise SystemExit('source already exists; use a clean checkout to reproduce the build')
with zipfile.ZipFile(root / 'Concat-0.2.1-TR-kaynak.zip') as archive:
    for item in archive.infolist():
        destination = (target / item.filename).resolve()
        if not destination.is_relative_to(target.resolve()):
            raise SystemExit('Archive path escapes source directory')
    archive.extractall(target)
patch = '.github/patches/08-oblivion.patch'
for check in [True, False]:
    args = ['git', 'apply', '--directory=source/concat_tr']
    if check:
        args.append('--check')
    subprocess.run(args + [patch], cwd=root, check=True)
source = target / 'concat_tr'
speech = (source/'engine/crates/concat-speech/src/transcribe.rs').read_text(encoding='utf-8')
studio = (source/'engine/crates/concat/src/studio.rs').read_text(encoding='utf-8')
ui = (source/'engine/crates/concat/ui/app.slint').read_text(encoding='utf-8')
assert 'sherpa-onnx-whisper-base' in speech
assert 'return transcribe_with_sherpa(' in speech
assert 'fn captions_import_srt(' in studio
assert 'title: "Oblivion";' in ui
print('Oblivion source prepared and patch application verified')

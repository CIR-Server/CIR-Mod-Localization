from pathlib import Path
import hashlib,zipfile
root=Path(__file__).resolve().parents[1]
out=root/'dist/CIR-Mod-Localization-Pro-v1.4.zip'
out.parent.mkdir(exist_ok=True)
files=[root/n for n in ['pack.mcmeta','pack.png','README.md','ATTRIBUTION.md','CREDITS.md','LICENSE','CONTRIBUTORS.md','CONTRIBUTING.md']]
for folder in ['assets','licenses']:
    files += [p for p in (root/folder).rglob('*') if p.is_file()]
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(files):
        info=zipfile.ZipInfo(p.relative_to(root).as_posix(),date_time=(2026,11,23,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o100644<<16
        z.writestr(info,p.read_bytes())
with zipfile.ZipFile(out) as z: assert z.testzip() is None
digest=hashlib.sha256(out.read_bytes()).hexdigest()
out.with_suffix('.zip.sha256').write_text(digest+'  '+out.name+'\n',encoding='utf-8')
print(out)
print(digest)

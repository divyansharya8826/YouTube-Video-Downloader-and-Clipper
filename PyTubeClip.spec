# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['PyTubeClip.py'],
    pathex=[],
    binaries=[],
    datas=[('Babasse-Old-School-Bobines-video.256.png','Images'),('i.ppm','Images'),('youtubevanced.png','Images')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PyTubeClip',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PyTubeClip',
)
app = BUNDLE(
    coll,
    name='PyTubeClip.app',
    icon='Babasse-Old-School-Bobines-video.256.icns',
    bundle_identifier=None,
)

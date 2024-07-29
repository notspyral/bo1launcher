# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Max\\Downloads\\python scripts\\bo1launcher\\bo1launcher.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Max\\Downloads\\python scripts\\bo1launcher\\black_ops_icon.ico', '.'), ('C:\\Users\\Max\\Downloads\\python scripts\\bo1launcher\\black_ops_mp_icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='bo1launcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Max\\Downloads\\python scripts\\bo1launcher\\black_ops_icon.ico'],
)

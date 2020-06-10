# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/guglielmosanchini/PycharmProjects/Personal/Clustering/src/main/python/gui.py'],
             pathex=['/Users/guglielmosanchini/PycharmProjects/Personal/Clustering/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/guglielmosanchini/PycharmProjects/Personal/Clustering/venv/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/guglielmosanchini/PycharmProjects/Personal/Clustering/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Clustering',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/guglielmosanchini/PycharmProjects/Personal/Clustering/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Clustering')
app = BUNDLE(coll,
             name='Clustering.app',
             icon='/Users/guglielmosanchini/PycharmProjects/Personal/Clustering/target/Icon.icns',
             bundle_identifier=None)

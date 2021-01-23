# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['ytd.py'],
             pathex=['C:\\Users\\Vaibhav Haswani\\Desktop\\PyYTD'],
             binaries=[],
             datas=[('c:\\program files\\python38\\lib\\site-packages\\pyfiglet', './pyfiglet')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
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
          name='ytd',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='ytd.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ytd')

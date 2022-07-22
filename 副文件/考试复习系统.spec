# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['考试复习系统.py', '考试复习系统界面.py', 'img_rc.py', '背单词总结页面.py', '记事本界面.py', '速算总结界面.py', '挑战失败背景.py', '物理单元总结界面.py', '信息界面.py', '用户登录界面.py'],
             pathex=['C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\venv\\Lib\\site-packages\\PyQt5\\Qt\\qsci\\api\\python\\PyQt5.api'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='考试复习系统',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='图标.ico')

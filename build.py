import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed'
    '-i nut.png',
    '--name nut',
    '--clean',
    '--specpath spec',
    '--upx-dir upx'
])
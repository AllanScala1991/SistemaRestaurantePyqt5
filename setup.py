from cx_Freeze import setup, Executable
setup(
    name = "teste",## NOME DO PROGRAMA
    version = "1.0.0", ## VERSAO DO PROGRAMA
    options = {"build_exe": {
        'packages': ["os","sys","ctypes"],
        'include_files': ['background.png','confirm.png','excel_icon.ico','excel_icon.png','help.png','icon.ico'],#IMAGENS DO PROGRAMA
        'include_msvcr': True,
    }},
    executables = [Executable("application.py",base="Win32GUI")] #SCRIPT PRINCIPAL DO PYTHON
    )
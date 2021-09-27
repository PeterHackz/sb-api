open("compiled.txt", "wb").write(__import__("requests").post("https://sb-apis.repl.co/sb9838/tools/frida-compile", open("sample.txt", "r").read()).content)

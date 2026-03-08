# smartcardfyi — Python Smart Card API Client Demo
Output demo.gif

Set FontSize 20
Set Width 1000
Set Height 560
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 30ms
Set Padding 24

Type "uv run --with smartcardfyi python3"
Enter
Sleep 2s

Type "from smartcardfyi import SmartCardFYI"
Enter
Sleep 1s

Type "client = SmartCardFYI()"
Enter
Sleep 1s

Type "# Search smart card types"
Enter
Sleep 0.5s

Type "client.search('emv')"
Enter
Sleep 2.5s

Type "# Look up a card type"
Enter
Sleep 0.5s

Type "client.card('emv-payment')"
Enter
Sleep 3s

Type "exit()"
Enter
Sleep 1s

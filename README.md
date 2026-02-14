# 🖥️ Terminal Portfolio

An interactive, beautiful terminal-based portfolio with ASCII art, colors, and autocomplete features.

![Terminal Portfolio](OIP.webp)

## ✨ Features

- 🎨 **Beautiful ASCII Art** - Eye-catching banner with your name
- 🌈 **Colorful Terminal UI** - ANSI colors for an amazing visual experience
- 💬 **Interactive Commands** - Multiple commands to explore your profile
- 🔍 **Autocomplete Suggestions** - Smart command suggestions
- 📜 **Command History** - Navigate through previous commands
- ⚡ **Fast & Lightweight** - Pure Python, no external dependencies

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation

1. Clone or download this repository
2. Navigate to the directory:
```bash
cd TERMINAL-PORTFOLIO
```

3. Run the portfolio:
```bash
python portfolio.py
```

## 📝 Available Commands

| Command | Description |
|---------|-------------|
| `help` | Show all available commands |
| `about` | Learn about me and my background |
| `skills` | View my technical skills with progress bars |
| `projects` | Browse my recent projects |
| `experience` | Check out my work experience and education |
| `contact` | Get my contact information |
| `social` | Find me on social media |
| `resume` | Download my resume |
| `banner` | Display the ASCII banner again |
| `clear` | Clear the terminal screen |
| `exit/quit` | Exit the portfolio |

## 🎨 Customization

### Update Your Information

Edit the `portfolio.py` file and customize:

1. **Banner/Name** - Modify the `print_banner()` function (line ~30)
2. **About Section** - Update `cmd_about()` function
3. **Skills** - Edit `cmd_skills()` to add/remove skills
4. **Projects** - Modify `cmd_projects()` with your projects
5. **Contact Info** - Update `cmd_contact()` with your details
6. **Social Links** - Change `cmd_social()` with your profiles

### Generate Custom ASCII Art

Visit [patorjk.com/software/taag](https://patorjk.com/software/taag/) to create custom ASCII art for your name.

## 🎯 Usage Examples

```bash
# Start the portfolio
$ python portfolio.py

# Type commands interactively
portfolio@terminal:~$ help
portfolio@terminal:~$ about
portfolio@terminal:~$ skills
portfolio@terminal:~$ projects
portfolio@terminal:~$ contact
portfolio@terminal:~$ exit
```

## 🔧 Advanced Features

### Adding New Commands

1. Create a new function:
```python
def cmd_yourcommand():
    print("Your custom content here")
```

2. Add it to the COMMANDS dictionary:
```python
COMMANDS = {
    'yourcommand': cmd_yourcommand,
    # ... other commands
}
```

### Changing Colors

Modify the `Colors` class to use different ANSI color codes:
```python
class Colors:
    CUSTOM = '\033[38;5;208m'  # Orange
    # Add more custom colors
}
```

## 📱 Share Your Portfolio

### Method 1: GitHub Repository
1. Push this to your GitHub
2. Share the repository link
3. Users can clone and run it

### Method 2: Replit
1. Create a new Repl
2. Upload the `portfolio.py` file
3. Set it as the main file
4. Share the Repl link

### Method 3: Video/GIF Demo
1. Record your terminal with tools like:
   - [asciinema](https://asciinema.org/) (Terminal recorder)
   - [ttygif](https://github.com/icholy/ttygif)
   - Windows: Use OBS or ShareX
2. Share the recording on social media

## 🌟 Tips

- **Autocomplete**: Start typing a command and see suggestions
- **Exit Anytime**: Press `Ctrl+C` or type `exit`/`quit`
- **Clear Screen**: Use `clear` command to refresh the view
- **Fast Navigation**: Commands are case-insensitive

## 📄 License

Feel free to use this template for your own portfolio!

## 🤝 Contributing

Have ideas to improve this? Feel free to:
- Add new features
- Improve the design
- Share your customized version

## 📞 Contact

Made with ❤️ by [Your Name]

---

**⭐ Star this repo if you found it helpful!**

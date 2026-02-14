# 🎨 Customization Guide

This guide will help you personalize your terminal portfolio with your own information.

## 📝 Quick Start Customization

### 1. Update Your Name in the Banner

**File:** `portfolio_enhanced.py` (or `portfolio.py`)  
**Function:** `print_banner()` (around line 50-65)

**Option A:** Use a custom ASCII art generator
1. Visit [patorjk.com/software/taag](https://patorjk.com/software/taag/)
2. Type your name
3. Choose a font (recommended: "ANSI Shadow", "Big", or "Standard")
4. Copy the ASCII art
5. Replace the text in the `print_banner()` function

**Option B:** Use a simple text banner
```python
banner = f"""{Colors.OKCYAN}
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║                     YOUR NAME HERE                        ║
    ║          Developer | Designer | Problem Solver            ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
{Colors.ENDC}"""
```

### 2. Update About Section

**Function:** `cmd_about()` (around line 130-160)

Replace the placeholder text with your own information:

```python
def cmd_about():
    about_text = f"""
{Colors.OKCYAN}{Colors.BOLD}About Me{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

Hi! 👋 I'm [YOUR NAME], a [YOUR TITLE/ROLE] based in [YOUR LOCATION].

[YOUR INTRODUCTION - 2-3 sentences about who you are and what you do]

{Colors.OKGREEN}What I Do:{Colors.ENDC}
  • [YOUR SKILL 1]
  • [YOUR SKILL 2]
  • [YOUR SKILL 3]
  • [YOUR SKILL 4]

{Colors.OKGREEN}My Philosophy:{Colors.ENDC}
[YOUR PERSONAL PHILOSOPHY OR APPROACH TO WORK]

{Colors.OKGREEN}When I'm Not Coding:{Colors.ENDC}
  • [YOUR HOBBY 1]
  • [YOUR HOBBY 2]
  • [YOUR HOBBY 3]

{Colors.YELLOW}💡 "[YOUR FAVORITE QUOTE]"{Colors.ENDC}
"""
    print(about_text)
```

### 3. Update Skills

**Function:** `cmd_skills()` (around line 165-210)

**A. Update Programming Languages:**
```python
skills = [
    ("Your Language 1", 90),  # Replace with your skill and proficiency %
    ("Your Language 2", 85),
    ("Your Language 3", 80),
    ("Your Language 4", 75),
    ("Your Language 5", 70),
]
```

**B. Update Web Development Skills:**
```python
web_skills = [
    "• Frontend: [Your Frontend Technologies]",
    "• Backend: [Your Backend Technologies]",
    "• Database: [Your Database Technologies]"
]
```

### 4. Update Projects

**Function:** `cmd_projects()` (around line 220-270)

Replace each project with your own:

```python
{Colors.YELLOW}[01]{Colors.ENDC} {Colors.BOLD}Your Project Name{Colors.ENDC}
     {Colors.GRAY}Brief description of your project{Colors.ENDC}
     {Colors.OKBLUE}Tech:{Colors.ENDC} Technologies you used
     {Colors.OKGREEN}⭐ Features:{Colors.ENDC} Key features | More features
     {Colors.GRAY}┗━► Status or achievement{Colors.ENDC}
```

### 5. Update Contact Information

**Function:** `cmd_contact()` (around line 300-325)

```python
{Colors.OKGREEN}📧 Email:{Colors.ENDC}         your.actual.email@gmail.com
{Colors.OKGREEN}📱 Phone:{Colors.ENDC}         +91 XXXXX-XXXXX
{Colors.OKGREEN}🌍 Location:{Colors.ENDC}      Your City, Your Country
{Colors.OKGREEN}💼 LinkedIn:{Colors.ENDC}      linkedin.com/in/your-actual-username
{Colors.OKGREEN}🐱 GitHub:{Colors.ENDC}        github.com/your-actual-username
{Colors.OKGREEN}🌐 Website:{Colors.ENDC}       your-actual-website.com
```

### 6. Update Social Media Links

**Function:** `cmd_social()` (around line 330-355)

Replace all the placeholder URLs with your actual profile links:

```python
{Colors.OKGREEN}🐱 GitHub:{Colors.ENDC}       https://github.com/yourusername
{Colors.OKGREEN}💼 LinkedIn:{Colors.ENDC}     https://linkedin.com/in/yourprofile
{Colors.OKGREEN}🐦 Twitter:{Colors.ENDC}      https://twitter.com/yourusername
{Colors.OKGREEN}📷 Instagram:{Colors.ENDC}    https://instagram.com/yourusername
{Colors.OKGREEN}🌐 Portfolio:{Colors.ENDC}    https://yourwebsite.com
```

### 7. Update Experience

**Function:** `cmd_experience()` (around line 275-300)

```python
{Colors.OKGREEN}📚 Education:{Colors.ENDC}
  {Colors.BOLD}Your Degree{Colors.ENDC}
  {Colors.GRAY}Your University/College{Colors.ENDC}
  • Your achievement 1
  • Your achievement 2

{Colors.OKGREEN}💼 Professional Experience:{Colors.ENDC}
  
  {Colors.BOLD}Your Job Title{Colors.ENDC} {Colors.GRAY}| Start Year - End Year{Colors.ENDC}
  • Your responsibility 1
  • Your responsibility 2
```

## 🎨 Advanced Customization

### Change Color Scheme

Edit the `Colors` class (around line 15-35):

```python
class Colors:
    # Choose your own color scheme
    PRIMARY = '\033[94m'      # Blue (change to your preference)
    SECONDARY = '\033[96m'    # Cyan
    SUCCESS = '\033[92m'      # Green
    WARNING = '\033[93m'      # Yellow
    DANGER = '\033[91m'       # Red
```

**Popular Color Codes:**
- Red: `\033[91m`
- Green: `\033[92m`
- Yellow: `\033[93m`
- Blue: `\033[94m`
- Magenta: `\033[95m`
- Cyan: `\033[96m`
- White: `\033[97m`

### Add Your Own Commands

1. Create a function for your command:
```python
def cmd_your_command():
    """Your command description"""
    text = f"""
{Colors.OKCYAN}{Colors.BOLD}Your Title{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

Your content here...
"""
    print(text)
```

2. Add it to the commands dictionary in `get_commands()` function:
```python
def get_commands(history):
    return {
        # ... existing commands ...
        'yourcommand': cmd_your_command,
    }
```

3. Update the help menu in `cmd_help()` to include your new command.

### Add Custom Easter Eggs

Add fun commands like the `matrix` and `hack` examples:

```python
def cmd_your_easter_egg():
    """Your easter egg"""
    print(f"{Colors.OKGREEN}Your surprise message!{Colors.ENDC}")
    # Add animations, ASCII art, or fun text here
```

## 🚀 Testing Your Changes

After making changes, test the portfolio:

```bash
python portfolio_enhanced.py
```

Type each command to make sure everything displays correctly:
- `help` - Check all commands are listed
- `about` - Verify your information
- `skills` - Check skill bars display correctly
- `projects` - Ensure projects show properly
- `contact` - Verify all links are correct

## 💡 Pro Tips

1. **Keep it concise**: Don't make text blocks too long
2. **Use emojis**: They add personality and visual interest
3. **Test colors**: Make sure colors look good in your terminal
4. **Proofread**: Check for typos before sharing
5. **Update regularly**: Keep your projects and skills current

## 🎯 Checklist

Before sharing your portfolio, make sure you've updated:

- [ ] Banner with your name
- [ ] About section with your info
- [ ] Skills with your actual skills
- [ ] Projects with your real projects
- [ ] Contact information
- [ ] Social media links
- [ ] Experience and education
- [ ] Resume download link
- [ ] Email address
- [ ] Website/portfolio URL

## 📊 Example Workflow

1. **Start with contact info** - Update all links and emails
2. **Add your projects** - Replace with 3-5 best projects
3. **Update skills** - Be honest about proficiency levels
4. **Personalize about section** - Make it uniquely you
5. **Test everything** - Run through all commands
6. **Share!** - GitHub, Replit, or video demo

---

Need more help? Check the README.md or create an issue!

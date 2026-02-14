#!/usr/bin/env python3
"""
Enhanced Terminal-Based Portfolio with Advanced Features
Includes: Progress animations, Easter eggs, and more interactivity
"""

import os
import sys
import time
import random
from datetime import datetime

# Color codes for terminal
class Colors:
    # Basic colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Extended colors
    GRAY = '\033[90m'
    WHITE = '\033[97m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, delay=0.03):
    """Print text with typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(text="Loading", duration=2):
    """Display a loading animation"""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{Colors.OKCYAN}{chars[i % len(chars)]} {text}...{Colors.ENDC}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print(f'\r{Colors.OKGREEN}✓ Done!{Colors.ENDC}           ')

def print_banner():
    """Print banner with name on left and ASCII art on right"""
    
    # Load and scale down ASCII art for side display
    ascii_lines = []
    try:
        ascii_art_path = os.path.join(os.path.dirname(__file__), 'ascii-art.txt')
        with open(ascii_art_path, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
        # Take every 6th line and limit to 30 characters for compact side display
        ascii_lines = [line[:30].rstrip() for i, line in enumerate(all_lines) if i % 6 == 0][:10]
    except FileNotFoundError:
        pass
    
    # Pad ASCII lines to ensure we have exactly 10 lines
    while len(ascii_lines) < 10:
        ascii_lines.append("")
    
    # Create side-by-side layout: Name on left, ASCII art on right
    print(f"""{Colors.OKCYAN}
╔═════════════════════════════════════════════════════════════╗
║                                                             ║
║   ██████╗██╗  ██╗ █████╗ ██████╗ ██╗     ██╗███████╗███████╗║
║  ██╔════╝██║  ██║██╔══██╗██╔══██╗██║     ██║██╔════╝██╔════╝║
║  ██║     ███████║███████║██████╔╝██║     ██║█████╗  █████╗  ║
║  ██║     ██╔══██║██╔══██║██╔══██╗██║     ██║██╔══╝  ██╔══╝  ║
║  ╚██████╗██║  ██║██║  ██║██║  ██║███████╗██║███████╗███████╗║
║   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚══════╝║
║                                                             ║
║                Developer | Designer | Builder               ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
{Colors.ENDC}""")

def print_welcome():
    """Print welcome message"""
    print(f"{Colors.OKGREEN}Welcome to my Interactive Portfolio!{Colors.ENDC}")
    print(f"{Colors.GRAY}Type 'help' to see available commands{Colors.ENDC}")
    print(f"{Colors.GRAY}Type 'exit' or 'quit' to leave{Colors.ENDC}\n")

def cmd_help():
    """Display help information"""
    help_text = f"""
{Colors.OKCYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════╗
║                    AVAILABLE COMMANDS                     ║
╚═══════════════════════════════════════════════════════════╝{Colors.ENDC}

{Colors.OKGREEN}📋 Information Commands:{Colors.ENDC}
  {Colors.BOLD}help{Colors.ENDC}          Show this help message
  {Colors.BOLD}about{Colors.ENDC}         About me and my background
  {Colors.BOLD}whoami{Colors.ENDC}        Quick introduction

{Colors.OKGREEN}💼 Professional:{Colors.ENDC}
  {Colors.BOLD}skills{Colors.ENDC}        My technical skills and expertise
  {Colors.BOLD}projects{Colors.ENDC}      View my recent projects
  {Colors.BOLD}experience{Colors.ENDC}    Work experience and education
  {Colors.BOLD}resume{Colors.ENDC}        Download my resume

{Colors.OKGREEN}📞 Contact & Social:{Colors.ENDC}
  {Colors.BOLD}contact{Colors.ENDC}       Get in touch with me
  {Colors.BOLD}social{Colors.ENDC}        My social media links
  {Colors.BOLD}email{Colors.ENDC}         Send me an email

{Colors.OKGREEN}🎮 Fun & Extras:{Colors.ENDC}
  {Colors.BOLD}quote{Colors.ENDC}         Random inspirational quote
  {Colors.BOLD}joke{Colors.ENDC}          Random programming joke
  {Colors.BOLD}matrix{Colors.ENDC}        Matrix effect (Easter egg!)
  {Colors.BOLD}hack{Colors.ENDC}          Hacking simulator (Easter egg!)

{Colors.OKGREEN}🔧 Utilities:{Colors.ENDC}
  {Colors.BOLD}clear{Colors.ENDC}         Clear the terminal screen
  {Colors.BOLD}banner{Colors.ENDC}        Display the banner again
  {Colors.BOLD}time{Colors.ENDC}          Show current time
  {Colors.BOLD}history{Colors.ENDC}       Show command history

{Colors.OKGREEN}🚪 Exit:{Colors.ENDC}
  {Colors.BOLD}exit/quit{Colors.ENDC}     Exit the portfolio

{Colors.GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Tip: Try typing partial commands for autocomplete suggestions!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.ENDC}
"""
    print(help_text)

def cmd_whoami():
    """Quick introduction"""
    text = f"""
{Colors.OKCYAN}{Colors.BOLD}$ whoami{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}Developer • Designer • Problem Solver{Colors.ENDC}

A passionate tech enthusiast who turns coffee into code ☕
and ideas into reality 💡

{Colors.YELLOW}Current Status:{Colors.ENDC} Available for exciting opportunities!
{Colors.YELLOW}Location:{Colors.ENDC} India 🇮🇳
{Colors.YELLOW}Interests:{Colors.ENDC} Web Dev, ML/AI, Automation, Open Source

{Colors.GRAY}Type 'about' for more details{Colors.ENDC}
"""
    print(text)

def cmd_about():
    """Display about information"""
    about_text = f"""
{Colors.OKCYAN}{Colors.BOLD}About Me{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

Hi! 👋 I'm a passionate developer who loves creating innovative solutions
and building amazing digital experiences. 

{Colors.OKGREEN}What I Do:{Colors.ENDC}
  • 🌐 Full-stack web development
  • 🤖 Machine Learning & AI
  • 📱 Mobile application development
  • 🎨 UI/UX design
  • ⚡ Automation & scripting

{Colors.OKGREEN}My Philosophy:{Colors.ENDC}
I believe in writing clean, efficient code and creating user experiences
that make a difference. Every project is an opportunity to learn something
new and push the boundaries of what's possible.

{Colors.OKGREEN}When I'm Not Coding:{Colors.ENDC}
  • 📚 Reading tech blogs and documentation
  • 🎮 Exploring new technologies
  • 💡 Working on side projects
  • 🌱 Contributing to open source

{Colors.YELLOW}💡 "Code is poetry written in logic"{Colors.ENDC}
"""
    print(about_text)

def cmd_skills():
    """Display skills with animated progress bars"""
    print(f"\n{Colors.OKCYAN}{Colors.BOLD}Technical Skills{Colors.ENDC}")
    print(f"{Colors.GRAY}{'═' * 60}{Colors.ENDC}\n")
    
    skills = [
        ("Python", 90),
        ("JavaScript", 85),
        ("C++", 80),
        ("Java", 75),
        ("TypeScript", 70),
    ]
    
    print(f"{Colors.OKGREEN}Programming Languages:{Colors.ENDC}")
    for skill, level in skills:
        filled = int(level / 5)
        empty = 20 - filled
        bar = f"{Colors.OKGREEN}{'█' * filled}{Colors.GRAY}{'░' * empty}{Colors.ENDC}"
        print(f"  ▸ {skill:<15} {bar}  {level}%")
        time.sleep(0.1)
    
    print(f"\n{Colors.OKGREEN}Web Development:{Colors.ENDC}")
    web_skills = [
        "• Frontend: React, Vue.js, HTML5, CSS3, TailwindCSS",
        "• Backend: Node.js, Express, Django, Flask",
        "• Database: MongoDB, PostgreSQL, MySQL, Firebase"
    ]
    for skill in web_skills:
        print(f"  {skill}")
        time.sleep(0.1)
    
    print(f"\n{Colors.OKGREEN}Mobile Development:{Colors.ENDC}")
    mobile_skills = ["React Native", "Android (Java/Kotlin)", "Flutter"]
    for skill in mobile_skills:
        print(f"  • {skill}")
        time.sleep(0.1)
    
    print(f"\n{Colors.OKGREEN}Tools & Technologies:{Colors.ENDC}")
    tools = [
        "• Version Control: Git, GitHub",
        "• DevOps: Docker, AWS, Firebase",
        "• ML/AI: TensorFlow, PyTorch, Scikit-learn, OpenCV",
        "• Automation: Selenium, Puppeteer, BeautifulSoup"
    ]
    for tool in tools:
        print(f"  {tool}")
        time.sleep(0.1)
    print()

def cmd_projects():
    """Display projects"""
    projects_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Featured Projects{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.YELLOW}[01]{Colors.ENDC} {Colors.BOLD}JEE-CODE Platform{Colors.ENDC}
     {Colors.GRAY}Competitive coding platform with multi-language support{Colors.ENDC}
     {Colors.OKBLUE}Tech:{Colors.ENDC} React, Node.js, Monaco Editor, Express
     {Colors.OKGREEN}⭐ Features:{Colors.ENDC} 25+ problems | Real-time execution | Test cases
     {Colors.GRAY}┗━► Status: Live & Production Ready{Colors.ENDC}

{Colors.YELLOW}[02]{Colors.ENDC} {Colors.BOLD}Indian Sign Language Detection{Colors.ENDC}
     {Colors.GRAY}ML-powered ISL recognition system{Colors.ENDC}
     {Colors.OKBLUE}Tech:{Colors.ENDC} Python, TensorFlow, OpenCV, Mediapipe
     {Colors.OKGREEN}⭐ Features:{Colors.ENDC} A-Z alphabets | 0-9 digits | Real-time detection
     {Colors.GRAY}┗━► Accuracy: 94%+ on test dataset{Colors.ENDC}

{Colors.YELLOW}[03]{Colors.ENDC} {Colors.BOLD}Google Form Automation Bot{Colors.ENDC}
     {Colors.GRAY}Intelligent form filling with human-like behavior{Colors.ENDC}
     {Colors.OKBLUE}Tech:{Colors.ENDC} Python, Selenium, Google Sheets API
     {Colors.OKGREEN}⭐ Features:{Colors.ENDC} Auto-resume | Smart delays | Error recovery
     {Colors.GRAY}┗━► Processed 1000+ forms successfully{Colors.ENDC}

{Colors.YELLOW}[04]{Colors.ENDC} {Colors.BOLD}Monkeytype Clone{Colors.ENDC}
     {Colors.GRAY}Speed typing application with real-time metrics{Colors.ENDC}
     {Colors.OKBLUE}Tech:{Colors.ENDC} HTML5, CSS3, Vanilla JavaScript
     {Colors.OKGREEN}⭐ Features:{Colors.ENDC} WPM tracking | Multiple modes | Dark theme
     {Colors.GRAY}┗━► 60 FPS smooth animation{Colors.ENDC}

{Colors.YELLOW}[05]{Colors.ENDC} {Colors.BOLD}Terminal Portfolio{Colors.ENDC}
     {Colors.GRAY}Interactive CLI portfolio (you're using it!){Colors.ENDC}
     {Colors.OKBLUE}Tech:{Colors.ENDC} Python, ANSI colors
     {Colors.OKGREEN}⭐ Features:{Colors.ENDC} Autocomplete | Easter eggs | Animations
     {Colors.GRAY}┗━► Pure Python, no dependencies{Colors.ENDC}

{Colors.GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
View all projects: github.com/yourusername
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.ENDC}
"""
    print(projects_text)

def cmd_experience():
    """Display experience"""
    experience_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Experience & Education{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}📚 Education:{Colors.ENDC}
  {Colors.BOLD}Bachelor of Technology in Computer Science{Colors.ENDC}
  {Colors.GRAY}Specialized in Machine Learning & Web Development{Colors.ENDC}
  • Graduated with Honors
  • Relevant Coursework: DS&A, DBMS, ML, AI, Web Technologies

{Colors.OKGREEN}💼 Professional Experience:{Colors.ENDC}
  
  {Colors.BOLD}Full-Stack Developer{Colors.ENDC} {Colors.GRAY}| 2023 - Present{Colors.ENDC}
  • Developed 10+ full-stack web applications
  • Implemented ML models in production environments
  • Created automation tools saving 100+ hours of manual work
  • Mentored junior developers and conducted code reviews

{Colors.OKGREEN}🏆 Achievements:{Colors.ENDC}
  • 🥇 Built coding platform serving 1000+ users
  • 🚀 Developed 5+ production-ready ML models
  • ⚡ Automated workflows reducing processing time by 80%
  • 💻 Contributed to 10+ open-source projects
  • 📊 Improved application performance by 60%

{Colors.OKGREEN}📜 Certifications:{Colors.ENDC}
  • Machine Learning Specialization
  • Full-Stack Web Development
  • Cloud Computing Fundamentals
"""
    print(experience_text)

def cmd_contact():
    """Display contact information"""
    contact_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Contact Information{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}📧 Email:{Colors.ENDC}         your.email@example.com
{Colors.OKGREEN}📱 Phone:{Colors.ENDC}         +91 XXXXX-XXXXX
{Colors.OKGREEN}🌍 Location:{Colors.ENDC}      India
{Colors.OKGREEN}💼 LinkedIn:{Colors.ENDC}      linkedin.com/in/yourprofile
{Colors.OKGREEN}🐱 GitHub:{Colors.ENDC}        github.com/yourusername
{Colors.OKGREEN}🌐 Website:{Colors.ENDC}       yourwebsite.com
{Colors.OKGREEN}💬 Discord:{Colors.ENDC}       yourusername#1234

{Colors.YELLOW}╔═══════════════════════════════════════════════════════════╗
║  💼 Currently open to exciting opportunities!             ║
║  📬 Feel free to reach out for collaborations!            ║
╚═══════════════════════════════════════════════════════════╝{Colors.ENDC}

{Colors.GRAY}Response time: Usually within 24 hours{Colors.ENDC}
"""
    print(contact_text)

def cmd_social():
    """Display social media links"""
    social_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Social Media & Links{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}🐱 GitHub:{Colors.ENDC}       https://github.com/yourusername
                    {Colors.GRAY}↳ Check out my open-source projects!{Colors.ENDC}

{Colors.OKGREEN}💼 LinkedIn:{Colors.ENDC}     https://linkedin.com/in/yourprofile
                    {Colors.GRAY}↳ Let's connect professionally!{Colors.ENDC}

{Colors.OKGREEN}🐦 Twitter:{Colors.ENDC}      https://twitter.com/yourusername
                    {Colors.GRAY}↳ Follow for tech updates!{Colors.ENDC}

{Colors.OKGREEN}📷 Instagram:{Colors.ENDC}    https://instagram.com/yourusername
                    {Colors.GRAY}↳ Behind the scenes content!{Colors.ENDC}

{Colors.OKGREEN}🌐 Portfolio:{Colors.ENDC}    https://yourwebsite.com
                    {Colors.GRAY}↳ Full portfolio website!{Colors.ENDC}

{Colors.OKGREEN}📝 Blog:{Colors.ENDC}         https://yourblog.com
                    {Colors.GRAY}↳ Tech articles and tutorials!{Colors.ENDC}
"""
    print(social_text)

def cmd_email():
    """Display email information"""
    print(f"\n{Colors.OKGREEN}📧 Opening email client...{Colors.ENDC}")
    loading_animation("Preparing email", 1)
    print(f"\n{Colors.OKCYAN}Send an email to:{Colors.ENDC} {Colors.BOLD}your.email@example.com{Colors.ENDC}")
    print(f"{Colors.GRAY}Subject: Portfolio Inquiry{Colors.ENDC}\n")

def cmd_resume():
    """Display resume download information"""
    print(f"\n{Colors.OKGREEN}📄 Preparing resume download...{Colors.ENDC}")
    loading_animation("Fetching resume", 1.5)
    
    resume_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Resume Download{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}📥 Download Links:{Colors.ENDC}
  • PDF Format:  https://yourwebsite.com/resume.pdf
  • DOCX Format: https://yourwebsite.com/resume.docx
  • LaTeX Source: https://github.com/yourusername/resume

{Colors.OKGREEN}📊 Resume Highlights:{Colors.ENDC}
  • 10+ projects showcased
  • 3+ years of experience
  • 15+ technical skills listed
  • 5+ certifications

{Colors.GRAY}Last updated: {datetime.now().strftime('%B %Y')}{Colors.ENDC}
{Colors.YELLOW}✨ Pro tip: Check my GitHub for a live resume repository!{Colors.ENDC}
"""
    print(resume_text)

def cmd_quote():
    """Display random inspirational quote"""
    quotes = [
        ("First, solve the problem. Then, write the code.", "John Johnson"),
        ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
        ("Make it work, make it right, make it fast.", "Kent Beck"),
        ("Programming isn't about what you know; it's about what you can figure out.", "Chris Pine"),
        ("The best error message is the one that never shows up.", "Thomas Fuchs"),
        ("Simplicity is the soul of efficiency.", "Austin Freeman"),
        ("Clean code always looks like it was written by someone who cares.", "Robert C. Martin"),
        ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "Martin Fowler"),
    ]
    
    quote, author = random.choice(quotes)
    
    print(f"\n{Colors.OKCYAN}{Colors.BOLD}💡 Inspirational Quote{Colors.ENDC}")
    print(f"{Colors.GRAY}{'═' * 60}{Colors.ENDC}\n")
    print(f"{Colors.YELLOW}\"{quote}\"{Colors.ENDC}")
    print(f"{Colors.GRAY}— {author}{Colors.ENDC}\n")

def cmd_joke():
    """Display random programming joke"""
    jokes = [
        "Why do programmers prefer dark mode?\nBecause light attracts bugs! 🐛",
        "How many programmers does it take to change a light bulb?\nNone. It's a hardware problem! 💡",
        "Why do Java developers wear glasses?\nBecause they don't C#! 👓",
        "What's a programmer's favorite place to hang out?\nThe Foo Bar! 🍺",
        "Why did the programmer quit his job?\nBecause he didn't get arrays! 📊",
        "How do you comfort a JavaScript bug?\nYou console it! 🐛",
        "Why did the developer go broke?\nBecause he used up all his cache! 💰",
    ]
    
    joke = random.choice(jokes)
    
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}😄 Programming Joke{Colors.ENDC}")
    print(f"{Colors.GRAY}{'═' * 60}{Colors.ENDC}\n")
    print(f"{Colors.YELLOW}{joke}{Colors.ENDC}\n")

def cmd_time():
    """Display current time"""
    now = datetime.now()
    time_text = f"""
{Colors.OKCYAN}{Colors.BOLD}🕐 Current Time{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}Date:{Colors.ENDC}  {now.strftime('%A, %B %d, %Y')}
{Colors.OKGREEN}Time:{Colors.ENDC}  {now.strftime('%I:%M:%S %p')}
{Colors.OKGREEN}Zone:{Colors.ENDC}  IST (UTC+5:30)
"""
    print(time_text)

def cmd_matrix():
    """Matrix effect Easter egg"""
    print(f"\n{Colors.OKGREEN}Initializing Matrix...{Colors.ENDC}")
    time.sleep(1)
    
    for _ in range(10):
        line = ''.join(random.choice('01') for _ in range(60))
        print(f"{Colors.OKGREEN}{line}{Colors.ENDC}")
        time.sleep(0.1)
    
    print(f"\n{Colors.OKCYAN}Wake up, Neo... 🕶️{Colors.ENDC}\n")

def cmd_hack():
    """Hacking simulator Easter egg"""
    print(f"\n{Colors.FAIL}{Colors.BOLD}[!] INITIALIZING HACKING SEQUENCE{Colors.ENDC}")
    time.sleep(0.5)
    
    steps = [
        "Connecting to mainframe...",
        "Bypassing firewall...",
        "Cracking encryption...",
        "Downloading data...",
        "Covering tracks...",
        "HACK COMPLETE!"
    ]
    
    for step in steps:
        loading_animation(step, 1)
    
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}[✓] Just kidding! You've been pranked! 😄{Colors.ENDC}\n")

def cmd_history(history):
    """Display command history"""
    print(f"\n{Colors.OKCYAN}{Colors.BOLD}Command History{Colors.ENDC}")
    print(f"{Colors.GRAY}{'═' * 60}{Colors.ENDC}\n")
    
    if not history:
        print(f"{Colors.GRAY}No commands in history yet.{Colors.ENDC}\n")
        return
    
    for i, cmd in enumerate(history[-10:], 1):  # Show last 10 commands
        print(f"{Colors.YELLOW}{i:2d}{Colors.ENDC}  {cmd}")
    print()

def cmd_unknown(cmd):
    """Handle unknown commands"""
    print(f"{Colors.FAIL}❌ Command not found: {Colors.BOLD}{cmd}{Colors.ENDC}")
    print(f"{Colors.GRAY}Type 'help' to see available commands{Colors.ENDC}\n")

# Command mapping
def get_commands(history):
    return {
        'help': cmd_help,
        'whoami': cmd_whoami,
        'about': cmd_about,
        'skills': cmd_skills,
        'projects': cmd_projects,
        'experience': cmd_experience,
        'contact': cmd_contact,
        'social': cmd_social,
        'email': cmd_email,
        'resume': cmd_resume,
        'quote': cmd_quote,
        'joke': cmd_joke,
        'time': cmd_time,
        'matrix': cmd_matrix,
        'hack': cmd_hack,
        'history': lambda: cmd_history(history),
        'banner': lambda: (clear_screen(), print_banner(), print_welcome()),
        'clear': lambda: (clear_screen(), print_banner(), print_welcome()),
    }

def get_suggestions(partial_cmd, commands):
    """Get command suggestions based on partial input"""
    if not partial_cmd:
        return list(commands.keys())
    return [cmd for cmd in commands.keys() if cmd.startswith(partial_cmd.lower())]

def main():
    """Main function"""
    clear_screen()
    print_banner()
    print_welcome()
    
    command_history = []
    
    while True:
        try:
            # Get user input
            user_input = input(f"{Colors.OKGREEN}portfolio@terminal{Colors.ENDC}:{Colors.OKBLUE}~${Colors.ENDC} ").strip()
            
            if not user_input:
                continue
            
            # Add to history
            command_history.append(user_input)
            
            # Parse command
            cmd = user_input.lower()
            
            # Get current commands (with history)
            COMMANDS = get_commands(command_history)
            
            # Check for exit commands
            if cmd in ['exit', 'quit', 'q']:
                print(f"\n{Colors.OKCYAN}╔═══════════════════════════════════════════════════════════╗")
                print(f"║  Thanks for visiting my portfolio!                        ║")
                print(f"║  Hope to hear from you soon! 👋                           ║")
                print(f"╚═══════════════════════════════════════════════════════════╝{Colors.ENDC}\n")
                break
            
            # Check if command exists
            if cmd in COMMANDS:
                print()
                COMMANDS[cmd]()
                print()
            else:
                # Show suggestions for partial matches
                suggestions = get_suggestions(cmd, COMMANDS)
                if suggestions and len(suggestions) <= 5:
                    print(f"\n{Colors.WARNING}💡 Did you mean:{Colors.ENDC}")
                    for suggestion in suggestions:
                        print(f"   → {Colors.OKGREEN}{suggestion}{Colors.ENDC}")
                    print()
                else:
                    cmd_unknown(cmd)
        
        except KeyboardInterrupt:
            print(f"\n\n{Colors.OKCYAN}╔═══════════════════════════════════════════════════════════╗")
            print(f"║  Thanks for visiting my portfolio!                        ║")
            print(f"║  Hope to hear from you soon! 👋                           ║")
            print(f"╚═══════════════════════════════════════════════════════════╝{Colors.ENDC}\n")
            break
        except EOFError:
            break
        except Exception as e:
            print(f"{Colors.FAIL}❌ Error: {str(e)}{Colors.ENDC}\n")

if __name__ == "__main__":
    main()

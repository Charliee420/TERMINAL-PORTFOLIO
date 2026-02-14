#!/usr/bin/env python3
"""
Terminal-Based Portfolio
A beautiful command-line portfolio with autocomplete and interactive features
"""

import os
import sys
import time
from datetime import datetime

# Color codes for terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'
    WHITE = '\033[97m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'

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
╔═══════════════════════════════════════════╗  {Colors.GRAY}{ascii_lines[0]:<30}{Colors.OKCYAN}
║                                           ║  {Colors.GRAY}{ascii_lines[1]:<30}{Colors.OKCYAN}
║   ██████╗██╗  ██╗ █████╗ ██████╗ ██╗   ██╗║  {Colors.GRAY}{ascii_lines[2]:<30}{Colors.OKCYAN}
║  ██╔════╝██║  ██║██╔══██╗██╔══██╗██║   ██║║  {Colors.GRAY}{ascii_lines[3]:<30}{Colors.OKCYAN}
║  ██║     ███████║███████║██████╔╝██║   ██║║  {Colors.GRAY}{ascii_lines[4]:<30}{Colors.OKCYAN}
║  ██║     ██╔══██║██╔══██║██╔══██╗██║   ██║║  {Colors.GRAY}{ascii_lines[5]:<30}{Colors.OKCYAN}
║  ╚██████╗██║  ██║██║  ██║██║  ██║███████╔╝║  {Colors.GRAY}{ascii_lines[6]:<30}{Colors.OKCYAN}
║   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ║  {Colors.GRAY}{ascii_lines[7]:<30}{Colors.OKCYAN}
║                                           ║  {Colors.GRAY}{ascii_lines[8]:<30}{Colors.OKCYAN}
║      Developer | Designer | Builder       ║  {Colors.GRAY}{ascii_lines[9]:<30}{Colors.OKCYAN}
║                                           ║  
╚═══════════════════════════════════════════╝
{Colors.ENDC}""")

def print_welcome():
    """Print welcome message"""
    print(f"{Colors.OKGREEN}Welcome to my Interactive Portfolio!{Colors.ENDC}")
    print(f"{Colors.GRAY}Type 'help' to see available commands{Colors.ENDC}")
    print(f"{Colors.GRAY}Type 'exit' or 'quit' to leave{Colors.ENDC}\n")

def cmd_help():
    """Display help information"""
    help_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Available Commands:{Colors.ENDC}

  {Colors.OKGREEN}help{Colors.ENDC}          Show this help message
  {Colors.OKGREEN}about{Colors.ENDC}         About me and my background
  {Colors.OKGREEN}skills{Colors.ENDC}        My technical skills and expertise
  {Colors.OKGREEN}projects{Colors.ENDC}      View my recent projects
  {Colors.OKGREEN}experience{Colors.ENDC}    Work experience and education
  {Colors.OKGREEN}contact{Colors.ENDC}       Get in touch with me
  {Colors.OKGREEN}social{Colors.ENDC}        My social media links
  {Colors.OKGREEN}resume{Colors.ENDC}        Download my resume
  {Colors.OKGREEN}clear{Colors.ENDC}         Clear the terminal screen
  {Colors.OKGREEN}banner{Colors.ENDC}        Display the banner again
  {Colors.OKGREEN}exit/quit{Colors.ENDC}     Exit the portfolio

{Colors.GRAY}Tip: Press TAB for autocomplete suggestions{Colors.ENDC}
"""
    print(help_text)

def cmd_about():
    """Display about information"""
    about_text = f"""
{Colors.OKCYAN}{Colors.BOLD}About Me{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

Hi! I'm a passionate developer who loves creating innovative solutions
and building amazing digital experiences. I specialize in:

  • Full-stack web development
  • Machine Learning & AI
  • Mobile application development
  • UI/UX design

With a strong foundation in computer science and a drive for continuous
learning, I'm always exploring new technologies and pushing the boundaries
of what's possible.

{Colors.OKGREEN}💡 "Code is poetry written in logic"{Colors.ENDC}
"""
    print(about_text)

def cmd_skills():
    """Display skills"""
    skills_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Technical Skills{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}Programming Languages:{Colors.ENDC}
  ▸ Python          ████████████████░░  90%
  ▸ JavaScript      ███████████████░░░  85%
  ▸ C++             ██████████████░░░░  80%
  ▸ Java            ████████████░░░░░░  75%
  ▸ TypeScript      ███████████░░░░░░░  70%

{Colors.OKGREEN}Web Development:{Colors.ENDC}
  • Frontend: React, Vue.js, HTML5, CSS3, TailwindCSS
  • Backend: Node.js, Express, Django, Flask
  • Database: MongoDB, PostgreSQL, MySQL

{Colors.OKGREEN}Mobile Development:{Colors.ENDC}
  • React Native
  • Android (Java/Kotlin)
  • Flutter

{Colors.OKGREEN}Tools & Technologies:{Colors.ENDC}
  • Git, GitHub, Docker
  • AWS, Firebase
  • Machine Learning: TensorFlow, PyTorch, Scikit-learn
  • Web Automation: Selenium, Puppeteer
"""
    print(skills_text)

def cmd_projects():
    """Display projects"""
    projects_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Recent Projects{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.YELLOW}[01]{Colors.ENDC} {Colors.BOLD}JEE-CODE Platform{Colors.ENDC}
     Online coding platform with multi-language support
     Tech: React, Node.js, Monaco Editor
     {Colors.GRAY}⭐ 25+ coding problems | Real-time code execution{Colors.ENDC}

{Colors.YELLOW}[02]{Colors.ENDC} {Colors.BOLD}Indian Sign Language Detection{Colors.ENDC}
     ML-powered ISL recognition for A-Z alphabets and 0-9 digits
     Tech: Python, TensorFlow, OpenCV
     {Colors.GRAY}⭐ Real-time webcam translation{Colors.ENDC}

{Colors.YELLOW}[03]{Colors.ENDC} {Colors.BOLD}Google Form Automation Bot{Colors.ENDC}
     Intelligent form filling with human-like behavior
     Tech: Python, Selenium, Google Sheets API
     {Colors.GRAY}⭐ Resume capability | Random delays for authenticity{Colors.ENDC}

{Colors.YELLOW}[04]{Colors.ENDC} {Colors.BOLD}Monkeytype Clone{Colors.ENDC}
     Speed typing application with real-time WPM tracking
     Tech: HTML5, CSS3, Vanilla JavaScript
     {Colors.GRAY}⭐ Minimalist dark theme | Multiple test modes{Colors.ENDC}

{Colors.YELLOW}[05]{Colors.ENDC} {Colors.BOLD}Terminal Portfolio{Colors.ENDC}
     Interactive command-line portfolio (you're looking at it!)
     Tech: Python
     {Colors.GRAY}⭐ ASCII art | Autocomplete | Command history{Colors.ENDC}
"""
    print(projects_text)

def cmd_experience():
    """Display experience"""
    experience_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Experience & Education{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}📚 Education:{Colors.ENDC}
  • Bachelor's in Computer Science
  • Specialized in Machine Learning & Web Development

{Colors.OKGREEN}💼 Work Experience:{Colors.ENDC}
  
  {Colors.BOLD}Full-Stack Developer{Colors.ENDC}
  {Colors.GRAY}Building scalable web applications and APIs{Colors.ENDC}
  • Developed 10+ full-stack projects
  • Implemented ML models in production
  • Automated workflows saving 100+ hours

{Colors.OKGREEN}🏆 Achievements:{Colors.ENDC}
  • Built coding platform with 25+ problems
  • Created multiple automation tools
  • Developed real-time ML detection systems
"""
    print(experience_text)

def cmd_contact():
    """Display contact information"""
    contact_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Contact Information{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}📧 Email:{Colors.ENDC}     your.email@example.com
{Colors.OKGREEN}📱 Phone:{Colors.ENDC}     +91 XXXXX-XXXXX
{Colors.OKGREEN}🌍 Location:{Colors.ENDC}  India
{Colors.OKGREEN}💼 LinkedIn:{Colors.ENDC}  linkedin.com/in/yourprofile
{Colors.OKGREEN}🐱 GitHub:{Colors.ENDC}    github.com/yourusername

{Colors.YELLOW}Feel free to reach out for collaborations or opportunities!{Colors.ENDC}
"""
    print(contact_text)

def cmd_social():
    """Display social media links"""
    social_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Social Media{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}GitHub:{Colors.ENDC}     https://github.com/yourusername
{Colors.OKGREEN}LinkedIn:{Colors.ENDC}   https://linkedin.com/in/yourprofile
{Colors.OKGREEN}Twitter:{Colors.ENDC}    https://twitter.com/yourusername
{Colors.OKGREEN}Instagram:{Colors.ENDC}  https://instagram.com/yourusername
{Colors.OKGREEN}Portfolio:{Colors.ENDC}  https://yourwebsite.com
"""
    print(social_text)

def cmd_resume():
    """Display resume download information"""
    resume_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Resume{Colors.ENDC}
{Colors.GRAY}{'═' * 60}{Colors.ENDC}

{Colors.OKGREEN}📄 Download my resume:{Colors.ENDC}
   https://yourwebsite.com/resume.pdf

{Colors.YELLOW}Or scan the QR code:{Colors.ENDC}
   [QR code would appear here in GUI version]

{Colors.GRAY}Last updated: {datetime.now().strftime('%B %Y')}{Colors.ENDC}
"""
    print(resume_text)

def cmd_unknown(cmd):
    """Handle unknown commands"""
    print(f"{Colors.FAIL}Command not found: {cmd}{Colors.ENDC}")
    print(f"{Colors.GRAY}Type 'help' to see available commands{Colors.ENDC}\n")

# Command mapping
COMMANDS = {
    'help': cmd_help,
    'about': cmd_about,
    'skills': cmd_skills,
    'projects': cmd_projects,
    'experience': cmd_experience,
    'contact': cmd_contact,
    'social': cmd_social,
    'resume': cmd_resume,
    'banner': lambda: (clear_screen(), print_banner(), print_welcome()),
    'clear': lambda: (clear_screen(), print_banner(), print_welcome()),
}

def get_suggestions(partial_cmd):
    """Get command suggestions based on partial input"""
    if not partial_cmd:
        return list(COMMANDS.keys())
    return [cmd for cmd in COMMANDS.keys() if cmd.startswith(partial_cmd.lower())]

def print_suggestions(suggestions):
    """Print autocomplete suggestions"""
    if suggestions:
        print(f"\n{Colors.GRAY}Suggestions: {', '.join(suggestions)}{Colors.ENDC}")

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
            
            # Check for exit commands
            if cmd in ['exit', 'quit', 'q']:
                print(f"\n{Colors.OKCYAN}Thanks for visiting my portfolio!{Colors.ENDC}")
                print(f"{Colors.GRAY}See you soon! 👋{Colors.ENDC}\n")
                break
            
            # Check if command exists
            if cmd in COMMANDS:
                print()
                COMMANDS[cmd]()
                print()
            else:
                # Show suggestions for partial matches
                suggestions = get_suggestions(cmd)
                if suggestions and len(suggestions) <= 5:
                    print(f"{Colors.WARNING}Did you mean:{Colors.ENDC}")
                    for suggestion in suggestions:
                        print(f"  • {Colors.OKGREEN}{suggestion}{Colors.ENDC}")
                    print()
                else:
                    cmd_unknown(cmd)
        
        except KeyboardInterrupt:
            print(f"\n\n{Colors.OKCYAN}Thanks for visiting my portfolio!{Colors.ENDC}")
            print(f"{Colors.GRAY}See you soon! 👋{Colors.ENDC}\n")
            break
        except EOFError:
            break
        except Exception as e:
            print(f"{Colors.FAIL}Error: {str(e)}{Colors.ENDC}\n")

if __name__ == "__main__":
    main()

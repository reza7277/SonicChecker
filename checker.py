import requests
import time
from rich.console import Console
from rich.panel import Panel

# Base URL for wallet allocation check
base_url = "https://airdrop.sonic.game/api/allocations"

# Headers (same as in DevTools)
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://airdrop.sonic.game/"
}

# Console for rich output
console = Console()

# Function to display a banner
def display_banner():
    banner = """
██████╗ ███████╗███████╗ █████╗     ███████╗██████╗ ███████╗███████╗
██╔══██╗██╔════╝╚══███╔╝██╔══██╗    ╚════██║╚════██╗╚════██║╚════██║
██████╔╝█████╗    ███╔╝ ███████║        ██╔╝ █████╔╝    ██╔╝    ██╔╝
██╔══██╗██╔══╝   ███╔╝  ██╔══██║       ██╔╝ ██╔═══╝    ██╔╝    ██╔╝ 
██║  ██║███████╗███████╗██║  ██║       ██║  ███████╗   ██║     ██║  
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝       ╚═╝  ╚══════╝   ╚═╝     ╚═╝  
"""
    console.print(Panel(banner, title="Wallet Checker", subtitle="Version 1.0", style="bold green"))

# Function to load wallets from file
def load_wallets(file_name="wallets.txt"):
    try:
        with open(file_name, "r") as file:
            wallets = [
                line.split(",")[0].strip()  # Only keep the part before the comma
                for line in file.readlines()
                if line.strip()  # Skip empty lines
            ]
            console.print(f"[bold green]Loaded {len(wallets)} wallets from {file_name}.[/bold green]")
            return wallets
    except FileNotFoundError:
        console.print(f"[bold red]{file_name} not found. Please create a file named '{file_name}' with wallet addresses (one per line).[/bold red]")
        exit()

# Save results to a file
def save_results(wallet, result, file_name="results.txt"):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"Wallet: {wallet}, Result: {result}\n")

# Check wallet eligibility
def check_wallets(wallets):
    for wallet in wallets:
        with console.status(f"[bold cyan]Checking wallet: {wallet}[/bold cyan]", spinner="dots"):
            try:
                response = requests.get(base_url, headers=headers, params={"wallet": wallet})
                if response.status_code == 200:
                    result = response.json()  # Parse JSON response
                    if result:  # If the response is not empty
                        console.print(f"[green]Wallet: {wallet}, Result: Eligible[/green]")
                        save_results(wallet, "Eligible")
                    else:
                        console.print(f"[red]Wallet: {wallet}, Result: Not Eligible[/red]")
                        save_results(wallet, "Not Eligible")
                else:
                    console.print(f"[red]Wallet: {wallet}, Result: Not Eligible[/red]")
                    save_results(wallet, "Not Eligible")
            except Exception:
                # Treat errors as "Eligible"
                console.print(f"[green]Wallet: {wallet}, Result: Eligible[/green]")
                save_results(wallet, "Eligible")
            time.sleep(1)

    console.print("[bold green]All wallets checked. Results saved in 'results.txt'.[/bold green]")

# Main function
if __name__ == "__main__":
    try:
        display_banner()  # Display the banner at the start
        wallets = load_wallets()
        check_wallets(wallets)
    except KeyboardInterrupt:
        console.print("\n[bold red]Program interrupted by user. Exiting gracefully.[/bold red]")

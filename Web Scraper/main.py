import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from scraper.scraper import scrape_website  # Import the scraper function from scraper.py

# Function to create the Scrapings folder on the desktop
def create_scrapings_folder():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    scrapings_folder = os.path.join(desktop, 'Scrapings')
    if not os.path.exists(scrapings_folder):
        os.makedirs(scrapings_folder)
    return scrapings_folder

# Function to start web scraping
def start_scraping():
    url = url_entry.get()  # Get the URL from the entry field
    if not url:
        messagebox.showerror("Error", "Please enter a website URL.")
        return
    
    scrapings_folder = create_scrapings_folder()  # Create the Scrapings folder
    output_file = os.path.join(scrapings_folder, 'scraped_data.csv')  # Save to desktop Scrapings folder
    try:
        scrape_website(url, output_file)  # Call the scrape_website function from scraper.py
        messagebox.showinfo("Success", f"Data successfully scraped and saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to create a context menu with Cut, Copy, Paste options
def create_context_menu(entry_widget):
    context_menu = tk.Menu(entry_widget, tearoff=0)
    context_menu.add_command(label="Cut", command=lambda: entry_widget.event_generate("<<Cut>>"))
    context_menu.add_command(label="Copy", command=lambda: entry_widget.event_generate("<<Copy>>"))
    context_menu.add_command(label="Paste", command=lambda: entry_widget.event_generate("<<Paste>>"))

    # Bind right-click event to the entry field
    entry_widget.bind("<Button-3>", lambda event: context_menu.tk_popup(event.x_root, event.y_root))

# Create the GUI window
app = tk.Tk()
app.title("Web Scraper App")

# Set window size and configure background image
app.geometry("800x600")

# Load the background image from assets folder
background_image_path = "assets/background.png"
bg_image = Image.open(background_image_path)
bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas for the background
canvas = tk.Canvas(app, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Add the title directly to the canvas (text with no background)
canvas.create_text(400, 100, text="Welcome to Web Scraper", font=("Helvetica", 18), fill="white")

# Add the website URL prompt directly to the canvas (text with no background)
canvas.create_text(400, 180, text="Enter Website URL to Scrape:", font=("Helvetica", 12), fill="white")

# Create an entry field for the URL with right-click context menu
url_entry = tk.Entry(app, font=("Helvetica", 12), width=50)
canvas.create_window(400, 220, window=url_entry)
create_context_menu(url_entry)  # Enable right-click options

# Button to start scraping
scrape_btn = tk.Button(app, text="Start Scraping", command=start_scraping,
                       font=("Helvetica", 14), bg="#9370DB", fg="white")
canvas.create_window(400, 280, window=scrape_btn)

# Add the "By Marvelous Mr Mayhem" tag directly to the canvas
canvas.create_text(80, 570, text="By Marvelous Mr Mayhem", font=("Helvetica", 10), fill="white", anchor="w")

# Start the GUI loop
app.mainloop()

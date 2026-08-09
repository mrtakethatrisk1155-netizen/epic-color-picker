import tkinter as tk
from tkinter import font, ttk
import colorsys


# Colorama color names mapping
COLORAMA_COLORS = {
    "BLACK": "BLACK", "RED": "RED", "GREEN": "GREEN", "YELLOW": "YELLOW",
    "BLUE": "BLUE", "MAGENTA": "MAGENTA", "CYAN": "CYAN", "WHITE": "WHITE",
}


class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker & Colorama Generator")
        self.root.geometry("700x900")
        self.root.configure(bg="#1a1a1a")
        
        # Color scheme
        self.bg_dark = "#1a1a1a"
        self.bg_light = "#2d2d2d"
        self.accent = "#4a9eff"
        self.text_light = "#e0e0e0"
        
        # Variables to store RGB values
        self.red = tk.IntVar(value=100)
        self.green = tk.IntVar(value=150)
        self.blue = tk.IntVar(value=200)
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.bg_dark)
        main_container.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Title
        title_font = font.Font(family="Segoe UI", size=16, weight="bold")
        title_label = tk.Label(
            main_container, 
            text="Color Picker & Colorama Generator", 
            font=title_font,
            bg=self.bg_dark,
            fg=self.text_light
        )
        title_label.pack(pady=(0, 15))
        
        # Color Display Area
        display_frame = tk.Frame(main_container, bg=self.bg_dark)
        display_frame.pack(fill="x", pady=(0, 15))
        
        self.color_display = tk.Canvas(
            display_frame,
            width=670,
            height=120,
            bg=self.rgb_to_hex(self.red.get(), self.green.get(), self.blue.get()),
            highlightthickness=0,
            relief="flat"
        )
        self.color_display.pack()
        
        # RGB Sliders Frame
        sliders_frame = tk.Frame(main_container, bg=self.bg_dark)
        sliders_frame.pack(fill="both", pady=(0, 15))
        
        # Red Slider
        self._create_slider_row(sliders_frame, "Red", self.red, 0)
        
        # Green Slider
        self._create_slider_row(sliders_frame, "Green", self.green, 1)
        
        # Blue Slider
        self._create_slider_row(sliders_frame, "Blue", self.blue, 2)
        
        # Color Formats Display
        formats_frame = tk.Frame(main_container, bg=self.bg_light, relief="flat")
        formats_frame.pack(fill="x", pady=(0, 15))
        
        formats_inner = tk.Frame(formats_frame, bg=self.bg_light)
        formats_inner.pack(padx=12, pady=10, fill="both")
        
        format_font = font.Font(family="Segoe UI", size=8, weight="bold")
        normal_font = font.Font(family="Consolas", size=9)
        
        # HEX
        tk.Label(formats_inner, text="HEX", font=format_font, bg=self.bg_light, fg=self.accent).grid(row=0, column=0, sticky="w", padx=(0, 8))
        self.hex_display = tk.Label(formats_inner, text="#6496C8", font=normal_font, bg=self.bg_light, fg=self.text_light)
        self.hex_display.grid(row=0, column=1, sticky="w", padx=(0, 20))
        
        # RGB
        tk.Label(formats_inner, text="RGB", font=format_font, bg=self.bg_light, fg=self.accent).grid(row=0, column=2, sticky="w", padx=(0, 8))
        self.rgb_display = tk.Label(formats_inner, text="rgb(100, 150, 200)", font=normal_font, bg=self.bg_light, fg=self.text_light)
        self.rgb_display.grid(row=0, column=3, sticky="w", padx=(0, 20))
        
        # HSL
        tk.Label(formats_inner, text="HSL", font=format_font, bg=self.bg_light, fg=self.accent).grid(row=0, column=4, sticky="w", padx=(0, 8))
        self.hsl_display = tk.Label(formats_inner, text="hsl(0, 0%, 0%)", font=normal_font, bg=self.bg_light, fg=self.text_light)
        self.hsl_display.grid(row=0, column=5, sticky="w")
        
        # HSV
        tk.Label(formats_inner, text="HSV", font=format_font, bg=self.bg_light, fg=self.accent).grid(row=1, column=0, sticky="w", padx=(0, 8), pady=(8, 0))
        self.hsv_display = tk.Label(formats_inner, text="hsv(0, 0%, 0%)", font=normal_font, bg=self.bg_light, fg=self.text_light)
        self.hsv_display.grid(row=1, column=1, sticky="w", padx=(0, 20), pady=(8, 0))
        
        # CMYK
        tk.Label(formats_inner, text="CMYK", font=format_font, bg=self.bg_light, fg=self.accent).grid(row=1, column=2, sticky="w", padx=(0, 8), pady=(8, 0))
        self.cmyk_display = tk.Label(formats_inner, text="cmyk(0%, 0%, 0%, 0%)", font=normal_font, bg=self.bg_light, fg=self.text_light)
        self.cmyk_display.grid(row=1, column=3, sticky="w", padx=(0, 20), pady=(8, 0))
        
        # Closest Colorama Color
        tk.Label(formats_inner, text="COLORAMA", font=format_font, bg=self.bg_light, fg=self.accent).grid(row=1, column=4, sticky="w", padx=(0, 8), pady=(8, 0))
        self.colorama_color = tk.Label(formats_inner, text="RED", font=normal_font, bg=self.bg_light, fg=self.text_light)
        self.colorama_color.grid(row=1, column=5, sticky="w", pady=(8, 0))
        
        # Copy Buttons
        button_frame = tk.Frame(main_container, bg=self.bg_dark)
        button_frame.pack(fill="x", pady=(0, 15))
        
        self._create_copy_button(button_frame, "📋 Copy HEX", self.copy_hex, 0)
        self._create_copy_button(button_frame, "📋 Copy RGB", self.copy_rgb, 1)
        self._create_copy_button(button_frame, "📋 Copy HSL", self.copy_hsl, 2)
        
        # Text Input for Colorama
        text_label_font = font.Font(family="Segoe UI", size=10, weight="bold")
        tk.Label(main_container, text="ASCII Art / Text for Colorama:", font=text_label_font, bg=self.bg_dark, fg=self.text_light).pack(anchor="w", pady=(10, 5))
        
        self.text_input = tk.Text(
            main_container,
            height=8,
            bg=self.bg_light,
            fg=self.text_light,
            font=("Consolas", 9),
            relief="flat",
            bd=0,
            insertbackground=self.accent,
            wrap="word"
        )
        self.text_input.pack(fill="both", expand=True, pady=(0, 10))
        
        # Generate Colorama Code
        generate_btn = tk.Button(
            main_container,
            text="🎨 Generate Colorama Code",
            command=self.generate_colorama,
            bg=self.accent,
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=15,
            pady=10,
            relief="flat",
            cursor="hand2",
            activebackground="#3a8eef",
            bd=0
        )
        generate_btn.pack(fill="x", pady=(0, 10))
        
        # Colorama Output
        tk.Label(main_container, text="Generated Code:", font=text_label_font, bg=self.bg_dark, fg=self.text_light).pack(anchor="w", pady=(5, 5))
        
        output_frame = tk.Frame(main_container, bg=self.bg_light, relief="flat")
        output_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        self.output_text = tk.Text(
            output_frame,
            height=6,
            bg=self.bg_light,
            fg=self.accent,
            font=("Consolas", 8),
            relief="flat",
            bd=0,
            state="disabled"
        )
        self.output_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Copy Generated Code
        copy_gen_btn = tk.Button(
            main_container,
            text="📋 Copy Generated Code",
            command=self.copy_generated,
            bg="#51cf66",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=15,
            pady=8,
            relief="flat",
            cursor="hand2",
            activebackground="#40c057",
            bd=0
        )
        copy_gen_btn.pack(fill="x")
        
        # Initial update
        self.update_color()
    
    def _create_slider_row(self, parent, label, var, row):
        """Create a labeled slider row with minimal dot slider."""
        row_frame = tk.Frame(parent, bg=self.bg_dark)
        row_frame.pack(fill="x", pady=6)
        
        # Label
        label_widget = tk.Label(row_frame, text=label, font=("Segoe UI", 9, "bold"), bg=self.bg_dark, fg=self.accent, width=6)
        label_widget.pack(side="left", padx=(0, 10))
        
        # Slider with minimal appearance (just a dot)
        slider = tk.Scale(
            row_frame,
            from_=0,
            to=255,
            orient="horizontal",
            variable=var,
            command=self.update_color,
            bg=self.bg_dark,
            fg=self.accent,
            troughcolor=self.bg_light,
            length=520,
            highlightthickness=0,
            relief="flat",
            bd=0,
            sliderrelief="flat"
        )
        slider.pack(side="left", padx=(0, 10), fill="x", expand=True)
        
        # Value display
        value_label = tk.Label(row_frame, text=str(var.get()), font=("Consolas", 11, "bold"), bg=self.bg_dark, fg=self.text_light, width=3, anchor="e")
        value_label.pack(side="left")
        
        # Store reference to update
        setattr(self, f"{label.lower()}_label", value_label)
    
    def _create_copy_button(self, parent, text, command, column):
        """Create a copy button in a grid."""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=self.accent,
            fg="white",
            font=("Segoe UI", 9, "bold"),
            padx=10,
            pady=6,
            relief="flat",
            cursor="hand2",
            activebackground="#3a8eef",
            bd=0
        )
        btn.grid(row=0, column=column, padx=3, sticky="ew")
        parent.grid_columnconfigure(column, weight=1)
        
    def rgb_to_hex(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def rgb_to_hsl(self, r, g, b):
        """Convert RGB to HSL."""
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return int(h * 360), int(s * 100), int(l * 100)
    
    def rgb_to_hsv(self, r, g, b):
        """Convert RGB to HSV."""
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        return int(h * 360), int(s * 100), int(v * 100)
    
    def rgb_to_cmyk(self, r, g, b):
        """Convert RGB to CMYK."""
        if (r, g, b) == (0, 0, 0):
            return 0, 0, 0, 100
        c = 1 - r / 255.0
        m = 1 - g / 255.0
        y = 1 - b / 255.0
        k = min(c, m, y)
        return int((c - k) / (1 - k) * 100), int((m - k) / (1 - k) * 100), int((y - k) / (1 - k) * 100), int(k * 100)
    
    def get_closest_colorama_color(self, r, g, b):
        """Find the closest Colorama color to RGB values."""
        colorama_colors = {
            "BLACK": (0, 0, 0),
            "RED": (255, 0, 0),
            "GREEN": (0, 128, 0),
            "YELLOW": (255, 255, 0),
            "BLUE": (0, 0, 255),
            "MAGENTA": (255, 0, 255),
            "CYAN": (0, 255, 255),
            "WHITE": (255, 255, 255),
        }
        
        closest = "WHITE"
        min_distance = float('inf')
        
        for color_name, (cr, cg, cb) in colorama_colors.items():
            distance = (r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2
            if distance < min_distance:
                min_distance = distance
                closest = color_name
        
        return closest
    
    def update_color(self, event=None):
        r = self.red.get()
        g = self.green.get()
        b = self.blue.get()
        
        # Update display canvas
        hex_color = self.rgb_to_hex(r, g, b)
        self.color_display.configure(bg=hex_color)
        
        # Update value labels
        self.red_label.config(text=str(r))
        self.green_label.config(text=str(g))
        self.blue_label.config(text=str(b))
        
        # Update color formats
        self.hex_display.config(text=hex_color.upper())
        self.rgb_display.config(text=f"rgb({r}, {g}, {b})")
        
        h, s, l = self.rgb_to_hsl(r, g, b)
        self.hsl_display.config(text=f"hsl({h}°, {s}%, {l}%)")
        
        h, s, v = self.rgb_to_hsv(r, g, b)
        self.hsv_display.config(text=f"hsv({h}°, {s}%, {v}%)")
        
        c, m, y, k = self.rgb_to_cmyk(r, g, b)
        self.cmyk_display.config(text=f"cmyk({c}%, {m}%, {y}%, {k}%)")
        
        colorama_color = self.get_closest_colorama_color(r, g, b)
        self.colorama_color.config(text=f"Fore.{colorama_color}")
    
    def copy_hex(self):
        self._copy_value(self.hex_display.cget("text"))
    
    def copy_rgb(self):
        self._copy_value(self.rgb_display.cget("text"))
    
    def copy_hsl(self):
        self._copy_value(self.hsl_display.cget("text"))
    
    def _copy_value(self, value):
        self.root.clipboard_clear()
        self.root.clipboard_append(value)
        self.root.update()
    
    def generate_colorama(self):
        """Generate colorama code for the text input."""
        text = self.text_input.get("1.0", "end-1c")
        
        if not text:
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "# Please enter some text or ASCII art")
            self.output_text.config(state="disabled")
            return
        
        colorama_color = self.get_closest_colorama_color(
            self.red.get(), 
            self.green.get(), 
            self.blue.get()
        )
        
        # Generate the code
        code = f'from colorama import Fore, init\ninit(autoreset=True)\n\nprint(Fore.{colorama_color}"""\n{text}\n""")'
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", code)
        self.output_text.config(state="disabled")
    
    def copy_generated(self):
        """Copy the generated colorama code to clipboard."""
        code = self.output_text.get("1.0", "end-1c")
        if code and code != "# Please enter some text or ASCII art":
            self._copy_value(code)


if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()

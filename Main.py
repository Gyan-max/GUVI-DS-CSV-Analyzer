import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, ttk
from tkinter import font as tkFont

class CSVAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 Advanced CSV File Analyzer")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")
        
        # Configure styles
        self.setup_styles()
        
        # Create main container
        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_frame)
        
        # File selection section
        self.create_file_section(main_frame)
        
        # Analysis results section
        self.create_results_section(main_frame)
        
        # Status bar
        self.create_status_bar()

    def setup_styles(self):
        # Define colors and fonts
        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#3498db',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'light': '#ecf0f1',
            'dark': '#34495e',
            'white': '#ffffff'
        }
        
        self.fonts = {
            'title': tkFont.Font(family="Arial", size=24, weight="bold"),
            'heading': tkFont.Font(family="Arial", size=16, weight="bold"),
            'subheading': tkFont.Font(family="Arial", size=12, weight="bold"),
            'normal': tkFont.Font(family="Arial", size=10),
            'small': tkFont.Font(family="Arial", size=9)
        }

    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg=self.colors['primary'], height=80)
        header_frame.pack(fill="x", pady=(0, 20))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="📊 CSV Data Analyzer & Cleaner",
            font=self.fonts['title'],
            bg=self.colors['primary'],
            fg=self.colors['white']
        )
        title_label.pack(expand=True)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Analyze, clean, and visualize your CSV data with ease",
            font=self.fonts['normal'],
            bg=self.colors['primary'],
            fg=self.colors['light']
        )
        subtitle_label.pack()

    def create_file_section(self, parent):
        # File selection frame
        file_frame = tk.LabelFrame(
            parent, 
            text="📁 File Selection", 
            font=self.fonts['heading'],
            bg=self.colors['white'],
            fg=self.colors['primary'],
            padx=20,
            pady=15
        )
        file_frame.pack(fill="x", pady=(0, 20))
        
        self.file_path = tk.StringVar()
        
        # File path display
        path_frame = tk.Frame(file_frame, bg=self.colors['white'])
        path_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(
            path_frame, 
            text="Selected File:", 
            font=self.fonts['subheading'],
            bg=self.colors['white'],
            fg=self.colors['dark']
        ).pack(anchor="w")
        
        self.file_entry = tk.Entry(
            path_frame, 
            textvariable=self.file_path, 
            font=self.fonts['normal'],
            bg=self.colors['light'],
            relief="solid",
            bd=1,
            state="readonly"
        )
        self.file_entry.pack(fill="x", pady=(5, 0))
        
        # Buttons frame
        button_frame = tk.Frame(file_frame, bg=self.colors['white'])
        button_frame.pack(fill="x")
        
        self.browse_btn = tk.Button(
            button_frame,
            text="🔍 Browse Files",
            command=self.browse_file,
            font=self.fonts['subheading'],
            bg=self.colors['secondary'],
            fg=self.colors['white'],
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        self.browse_btn.pack(side="left", padx=(0, 10))
        
        self.analyze_btn = tk.Button(
            button_frame,
            text="⚡ Analyze Data",
            command=self.analyze_csv,
            font=self.fonts['subheading'],
            bg=self.colors['success'],
            fg=self.colors['white'],
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            state="disabled"
        )
        self.analyze_btn.pack(side="left")

    def create_results_section(self, parent):
        # Results frame
        results_frame = tk.LabelFrame(
            parent,
            text="📈 Analysis Results",
            font=self.fonts['heading'],
            bg=self.colors['white'],
            fg=self.colors['primary'],
            padx=20,
            pady=15
        )
        results_frame.pack(fill="both", expand=True)
        
        # Create notebook for tabbed results
        self.notebook = ttk.Notebook(results_frame)
        self.notebook.pack(fill="both", expand=True, pady=(10, 0))
        
        # Create tabs
        self.create_tabs()

    def create_tabs(self):
        # Overview tab
        self.overview_frame = tk.Frame(self.notebook, bg=self.colors['white'])
        self.notebook.add(self.overview_frame, text="📊 Overview")
        
        self.overview_text = scrolledtext.ScrolledText(
            self.overview_frame,
            font=self.fonts['normal'],
            bg=self.colors['light'],
            relief="flat",
            padx=15,
            pady=15
        )
        self.overview_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Data Sample tab
        self.sample_frame = tk.Frame(self.notebook, bg=self.colors['white'])
        self.notebook.add(self.sample_frame, text="🔍 Data Sample")
        
        self.sample_text = scrolledtext.ScrolledText(
            self.sample_frame,
            font=tkFont.Font(family="Courier", size=9),
            bg=self.colors['light'],
            relief="flat",
            padx=15,
            pady=15
        )
        self.sample_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Statistics tab
        self.stats_frame = tk.Frame(self.notebook, bg=self.colors['white'])
        self.notebook.add(self.stats_frame, text="📈 Statistics")
        
        self.stats_text = scrolledtext.ScrolledText(
            self.stats_frame,
            font=self.fonts['normal'],
            bg=self.colors['light'],
            relief="flat",
            padx=15,
            pady=15
        )
        self.stats_text.pack(fill="both", expand=True, padx=10, pady=10)

    def create_status_bar(self):
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to analyze CSV files")
        
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=self.fonts['small'],
            bg=self.colors['dark'],
            fg=self.colors['white'],
            anchor="w",
            padx=10
        )
        status_bar.pack(side="bottom", fill="x")

    def browse_file(self):
        file = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file:
            self.file_path.set(file)
            self.analyze_btn.config(state="normal")
            self.status_var.set(f"File selected: {os.path.basename(file)}")

    def clear_all_tabs(self):
        """Clear content from all tabs"""
        self.overview_text.delete(1.0, tk.END)
        self.sample_text.delete(1.0, tk.END)
        self.stats_text.delete(1.0, tk.END)

    def format_number(self, num):
        """Format numbers with commas for better readability"""
        return f"{num:,}"

    def analyze_csv(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a CSV file")
            return

        try:
            self.status_var.set("Analyzing data...")
            self.root.update_idletasks()
            
            # Clear previous results
            self.clear_all_tabs()
            
            # Read the CSV file
            df = pd.read_csv(file_path)
            
            # Generate analysis
            self.generate_overview(df, file_path)
            self.generate_data_sample(df)
            self.generate_statistics(df)
            
            # Clean and save data
            self.clean_and_save_data(df, file_path)
            
            self.status_var.set("Analysis completed successfully!")
            
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{file_path}' not found")
            self.status_var.set("Error: File not found")
        except pd.errors.EmptyDataError:
            messagebox.showerror("Error", "The selected file is empty or not a valid CSV")
            self.status_var.set("Error: Invalid CSV file")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set("Error during analysis")

    def generate_overview(self, df, file_path):
        """Generate overview information"""
        overview = []
        
        # File information
        overview.append("📄 FILE INFORMATION")
        overview.append("=" * 50)
        overview.append(f"File Name: {os.path.basename(file_path)}")
        overview.append(f"File Size: {os.path.getsize(file_path) / 1024:.2f} KB")
        overview.append(f"Total Rows: {self.format_number(len(df))}")
        overview.append(f"Total Columns: {len(df.columns)}")
        overview.append("")
        
        # Data quality overview
        overview.append("🔍 DATA QUALITY OVERVIEW")
        overview.append("=" * 50)
        
        total_cells = len(df) * len(df.columns)
        missing_cells = df.isnull().sum().sum()
        duplicate_rows = df.duplicated().sum()
        
        overview.append(f"Total Cells: {self.format_number(total_cells)}")
        overview.append(f"Missing Values: {self.format_number(missing_cells)} ({missing_cells/total_cells*100:.2f}%)")
        overview.append(f"Duplicate Rows: {self.format_number(duplicate_rows)} ({duplicate_rows/len(df)*100:.2f}%)")
        overview.append("")
        
        # Column information
        overview.append("📊 COLUMN INFORMATION")
        overview.append("=" * 50)
        overview.append(f"{'Column Name':<25} {'Data Type':<15} {'Missing':<10} {'Unique':<10}")
        overview.append("-" * 65)
        
        for col in df.columns:
            missing_count = df[col].isnull().sum()
            unique_count = df[col].nunique()
            dtype = str(df[col].dtype)
            
            overview.append(f"{col[:24]:<25} {dtype:<15} {missing_count:<10} {unique_count:<10}")
        
        self.overview_text.insert(tk.END, "\n".join(overview))

    def generate_data_sample(self, df):
        """Generate data sample information"""
        sample = []
        
        # First 10 rows
        sample.append("🔝 FIRST 10 ROWS")
        sample.append("=" * 80)
        sample.append(df.head(10).to_string(max_cols=None, max_colwidth=20))
        sample.append("\n" * 2)
        
        # Last 10 rows
        sample.append("🔚 LAST 10 ROWS")
        sample.append("=" * 80)
        sample.append(df.tail(10).to_string(max_cols=None, max_colwidth=20))
        sample.append("\n" * 2)
        
        # Random sample
        if len(df) > 20:
            sample.append("🎲 RANDOM SAMPLE (10 ROWS)")
            sample.append("=" * 80)
            sample.append(df.sample(min(10, len(df))).to_string(max_cols=None, max_colwidth=20))
        
        self.sample_text.insert(tk.END, "\n".join(sample))

    def generate_statistics(self, df):
        """Generate detailed statistics"""
        stats = []
        
        # Numeric columns statistics
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        if len(numeric_cols) > 0:
            stats.append("📊 NUMERIC COLUMNS STATISTICS")
            stats.append("=" * 80)
            stats.append(df[numeric_cols].describe().to_string())
            stats.append("\n" * 2)
        
        # Categorical columns statistics
        categorical_cols = df.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            stats.append("📝 CATEGORICAL COLUMNS STATISTICS")
            stats.append("=" * 80)
            
            for col in categorical_cols[:5]:  # Show first 5 categorical columns
                stats.append(f"\n🏷️  Column: {col}")
                stats.append("-" * 40)
                value_counts = df[col].value_counts().head(10)
                
                for value, count in value_counts.items():
                    percentage = (count / len(df)) * 100
                    stats.append(f"{str(value)[:30]:<30} {count:>8} ({percentage:5.1f}%)")
        
        # Missing values analysis
        stats.append("\n\n🚫 MISSING VALUES ANALYSIS")
        stats.append("=" * 80)
        missing_data = df.isnull().sum()
        missing_data = missing_data[missing_data > 0].sort_values(ascending=False)
        
        if len(missing_data) > 0:
            stats.append(f"{'Column':<25} {'Missing Count':<15} {'Percentage'}")
            stats.append("-" * 50)
            for col, count in missing_data.items():
                percentage = (count / len(df)) * 100
                stats.append(f"{col[:24]:<25} {count:<15} {percentage:.2f}%")
        else:
            stats.append("✅ No missing values found!")
        
        self.stats_text.insert(tk.END, "\n".join(stats))

    def clean_and_save_data(self, df, file_path):
        """Clean data and save to new file"""
        try:
            # Create cleaned dataframe
            cleaned_df = df.copy()
            
            # Remove duplicates
            initial_rows = len(cleaned_df)
            cleaned_df = cleaned_df.drop_duplicates()
            duplicates_removed = initial_rows - len(cleaned_df)
            
            # Fill missing values
            # For numeric columns, fill with mean
            numeric_cols = cleaned_df.select_dtypes(include=['int64', 'float64']).columns
            for col in numeric_cols:
                cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mean())
            
            # For categorical columns, fill with mode or 'Unknown'
            categorical_cols = cleaned_df.select_dtypes(include=['object']).columns
            for col in categorical_cols:
                mode_value = cleaned_df[col].mode()
                if len(mode_value) > 0:
                    cleaned_df[col] = cleaned_df[col].fillna(mode_value[0])
                else:
                    cleaned_df[col] = cleaned_df[col].fillna('Unknown')
            
            # Save cleaned data
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            output_path = f"cleaned_{base_name}.csv"
            cleaned_df.to_csv(output_path, index=False)
            
            # Add cleaning summary to overview
            cleaning_summary = [
                "\n\n🧹 DATA CLEANING SUMMARY",
                "=" * 50,
                f"Original rows: {self.format_number(initial_rows)}",
                f"Duplicates removed: {self.format_number(duplicates_removed)}",
                f"Final rows: {self.format_number(len(cleaned_df))}",
                f"Cleaned file saved as: {output_path}",
                "✅ All missing values have been filled"
            ]
            
            self.overview_text.insert(tk.END, "\n".join(cleaning_summary))
            
        except Exception as e:
            error_msg = f"\n\n❌ Error during data cleaning: {str(e)}"
            self.overview_text.insert(tk.END, error_msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVAnalyzerApp(root)
    root.mainloop()
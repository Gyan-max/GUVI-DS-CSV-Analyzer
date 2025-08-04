# 📊 CSV File Analyzer

A powerful and user-friendly desktop application for analyzing CSV files with a modern graphical interface built using Python and Tkinter.

## 🌟 Features

### Core Analysis Features
- **Data Overview**: Comprehensive summary of your CSV data including shape, data types, and basic statistics
- **Data Sampling**: Preview of your data with customizable sample views
- **Statistical Analysis**: Detailed statistical summaries for numerical and categorical columns
- **Data Quality Check**: Identifies missing values, duplicates, and data inconsistencies
- **Data Cleaning**: Automated data cleaning with duplicate removal and missing value imputation

### User Interface Features
- **Modern GUI**: Clean and intuitive interface with tabbed navigation
- **File Browser**: Easy file selection with integrated file dialog
- **Responsive Design**: Scalable interface that adapts to different screen sizes
- **Status Updates**: Real-time feedback during analysis operations
- **Export Functionality**: Save cleaned datasets automatically

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.6+ installed on your system along with the following packages:

```bash
pip install pandas
```

Note: `tkinter` comes pre-installed with most Python distributions.

### Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the application:

```bash
python test.py
```

## 💻 Usage

### Basic Workflow

1. **Launch the Application**
   ```bash
   python test.py
   ```

2. **Select a CSV File**
   - Click the "Choose CSV File" button
   - Navigate to your CSV file using the file dialog
   - Select your file and click "Open"

3. **Analyze Your Data**
   - The application automatically loads and analyzes your CSV file
   - Navigate through different tabs to explore various aspects of your data:
     - **Overview**: Basic information about your dataset
     - **Data Sample**: Preview of your actual data
     - **Statistics**: Detailed statistical analysis

4. **Clean Your Data** (Optional)
   - Click the "Clean Data" button to automatically:
     - Remove duplicate rows
     - Fill missing values (mean for numeric, mode for categorical)
     - Save the cleaned dataset as `cleaned_[filename].csv`

### Features by Tab

#### 📊 Overview Tab
- Dataset dimensions (rows × columns)
- Column names and data types
- Memory usage information
- Missing value summary
- Data quality indicators

#### 🔍 Data Sample Tab
- First few rows of your dataset
- Column headers with proper formatting
- Data type identification

#### 📈 Statistics Tab
- Descriptive statistics for numerical columns
- Frequency distributions for categorical columns
- Correlation analysis (when applicable)

## 🎨 Interface Design

The application features a modern design with:
- **Color Scheme**: Professional blue and gray palette
- **Typography**: Clean Arial fonts with proper hierarchy
- **Layout**: Organized sections with clear visual separation
- **Icons**: Emoji-based icons for better visual appeal
- **Responsive Elements**: Adaptive sizing for different screen resolutions

## 🛠️ Technical Details

### Architecture
- **Main Class**: `CSVAnalyzerApp` - Handles the entire application logic
- **GUI Framework**: Tkinter with ttk styling
- **Data Processing**: Pandas for efficient CSV handling
- **File Operations**: OS module for file path management

### Key Methods
- `load_csv()`: Handles file loading and initial analysis
- `analyze_data()`: Performs comprehensive data analysis
- `clean_data()`: Implements data cleaning algorithms
- `format_number()`: Provides consistent number formatting

### Data Cleaning Strategy
- **Duplicate Removal**: Identifies and removes exact duplicate rows
- **Missing Value Imputation**:
  - Numerical columns: Filled with column mean
  - Categorical columns: Filled with mode or 'Unknown'

## 📁 Project Structure

```
project-1/
├── test.py          # Main application file
├── README.md        # This documentation
└── cleaned_*.csv    # Generated cleaned datasets (after cleaning operations)
```

## 🔧 Customization

### Adding New Analysis Features
To extend the analyzer with new features:

1. Add new methods to the `CSVAnalyzerApp` class
2. Create additional tabs in the `create_tabs()` method
3. Implement the analysis logic using pandas operations

### Styling Modifications
Customize the appearance by modifying the `setup_styles()` method:
- Update color schemes in the `self.colors` dictionary
- Modify fonts in the `self.fonts` dictionary

## 🐛 Troubleshooting

### Common Issues

**File Loading Errors**
- Ensure your CSV file is properly formatted
- Check for special characters in file paths
- Verify the file is not corrupted or in use by another application

**Memory Issues with Large Files**
- The application loads entire CSV files into memory
- For very large files (>1GB), consider using chunked processing

**Display Issues**
- Ensure your screen resolution supports the minimum window size (1200x800)
- Check if all required fonts are available on your system

## 🤝 Contributing

This project is part of the GUVI Data Science program. Contributions and improvements are welcome!

## 📄 License

This project is created for educational purposes as part of the GUVI Data Science curriculum.

## 🎯 Future Enhancements

- [ ] Support for Excel files (.xlsx, .xls)
- [ ] Data visualization charts and graphs
- [ ] Export analysis reports to PDF
- [ ] Advanced filtering and sorting options
- [ ] Database connectivity features
- [ ] Batch processing for multiple files

---

**Project**: GUVI Data Science - Project 1  
**Created**: August 2025  
**Technology Stack**: Python, Pandas, Tkinter

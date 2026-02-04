# Exercise 1: Vibe Coding - Trivial Tasks

These tasks are designed to be solved quickly with an AI agent in a single interaction. Each task should take under 5 minutes to complete.

## Task 1: Bulk File Renamer

**Description:** Create a script that renames all files in a directory by adding a prefix and replacing spaces with underscores.

**Specification:**
- Accept directory path and prefix as command-line arguments
- Find all files (not directories) in the specified directory
- Rename each file: `prefix_original_name_with_underscores.ext`
- Skip files that already have the prefix
- Print before/after names for each file

**Example:**
```
Input: photos/ with prefix "vacation"
Files: "my photo.jpg", "beach sunset.png"
Output: "vacation_my_photo.jpg", "vacation_beach_sunset.png"
```

**Success Criteria:**
- Script runs without errors
- All files renamed correctly
- Original files with prefix are not renamed again
- Non-file items (directories) are ignored

---

## Task 2: CSV to JSON Converter

**Description:** Convert a CSV file to a JSON file with proper structure.

**Specification:**
- Read a CSV file with headers
- Convert each row to a JSON object using headers as keys
- Write output as a JSON array to a new file
- Handle basic data types (strings, numbers)
- Accept input and output filenames as arguments

**Example:**
```
Input CSV:
name,age,city
Alice,30,Seattle
Bob,25,Portland

Output JSON:
[
  {"name": "Alice", "age": 30, "city": "Seattle"},
  {"name": "Bob", "age": 25, "city": "Portland"}
]
```

**Success Criteria:**
- Correctly parses CSV headers
- Creates valid JSON output
- Handles empty fields gracefully
- Numeric values converted to numbers, not strings

---

## Task 3: Duplicate Line Finder

**Description:** Find and report duplicate lines in a text file.

**Specification:**
- Accept filename as command-line argument
- Read file and identify duplicate lines
- Report duplicates with their line numbers and count
- Ignore leading/trailing whitespace when comparing
- Sort output by frequency (most common first)

**Example:**
```
Input file:
error: connection timeout
warning: retry attempt
error: connection timeout
error: connection timeout

Output:
Found 3 duplicates:
  "error: connection timeout" appears 3 times (lines 1, 3, 4)
  "warning: retry attempt" appears 1 time (line 2)
```

**Success Criteria:**
- Correctly identifies all duplicates
- Shows accurate line numbers
- Handles large files efficiently
- Ignores whitespace differences appropriately

---

## Task 4: Password Generator

**Description:** Generate secure random passwords with customizable criteria.

**Specification:**
- Accept length and complexity requirements as arguments
- Support options: include uppercase, lowercase, numbers, symbols
- Generate cryptographically secure random password
- Ensure at least one character from each required category
- Copy to clipboard if possible, otherwise print to stdout

**Example:**
```
Command: python password_gen.py --length 16 --upper --lower --numbers --symbols
Output: "K9#mPq2$xRtY8&jL"
```

**Success Criteria:**
- Password meets specified length
- Contains required character types
- Different password on each run
- Uses secure random number generation

---

## Task 5: Word Frequency Counter

**Description:** Analyze text and report the most common words.

**Specification:**
- Accept filename and optional number of top words (default: 10)
- Count word occurrences (case-insensitive)
- Remove common stop words (a, an, the, is, etc.)
- Display results as a sorted table
- Ignore punctuation attached to words

**Example:**
```
Input: analysis.txt, top 5 words
Output:
Word          Count
--------      -----
algorithm     42
efficiency    38
performance   31
optimization  27
system        24
```

**Success Criteria:**
- Accurate word counting
- Properly handles punctuation
- Stop words excluded
- Results sorted by frequency

---

## Task 6: Log File Date Filter

**Description:** Extract log entries within a specific date range from a log file.

**Specification:**
- Accept log filename, start date, and end date
- Assume log format: `YYYY-MM-DD HH:MM:SS [LEVEL] message`
- Extract all entries between dates (inclusive)
- Write filtered results to new file
- Support various date formats in input

**Example:**
```
Command: python filter_logs.py app.log 2024-01-15 2024-01-20
Output: Creates app_filtered.log with entries from Jan 15-20
```

**Success Criteria:**
- Correctly parses date formats
- Includes all entries in range
- Handles malformed lines gracefully
- Creates output file successfully

---

## Task 7: Directory Size Analyzer

**Description:** Calculate and display the size of all subdirectories in a given path.

**Specification:**
- Accept directory path as argument
- Calculate total size of each immediate subdirectory
- Display results sorted by size (largest first)
- Show sizes in human-readable format (KB, MB, GB)
- Include file count for each directory

**Example:**
```
Output:
videos/       15.3 GB  (127 files)
photos/       8.7 GB   (3,421 files)
documents/    245 MB   (892 files)
music/        122 MB   (48 files)
```

**Success Criteria:**
- Accurate size calculations
- Human-readable size formatting
- Sorted by size correctly
- Handles nested directories

---

## Task 8: JSON Formatter and Validator

**Description:** Pretty-print and validate JSON files.

**Specification:**
- Accept JSON filename as input
- Validate JSON syntax
- Reformat with proper indentation
- Option to write back to file or print to stdout
- Report any syntax errors with line numbers

**Example:**
```
Command: python json_format.py data.json --indent 2 --output formatted.json
Output: Creates properly indented JSON file
```

**Success Criteria:**
- Detects invalid JSON
- Produces correctly formatted output
- Preserves data structure
- Helpful error messages

---

## Task 9: Environment Variable Manager

**Description:** Simple tool to list, search, and export environment variables.

**Specification:**
- List all environment variables
- Search for variables by name or value (partial match)
- Export selected variables to a .env file format
- Option to filter by prefix (e.g., all "PATH_" variables)

**Example:**
```
Command: python env_manager.py --search PATH
Output: Lists all environment variables containing "PATH"
```

**Success Criteria:**
- Accurately reads environment variables
- Search works for names and values
- Exports to valid .env format
- Case-insensitive search option

---

## Task 10: Batch Image Resizer Info

**Description:** Get dimensions and size info for all images in a directory.

**Specification:**
- Accept directory path as argument
- Find all image files (jpg, png, gif, bmp)
- Display: filename, dimensions, file size, format
- Calculate total disk space used
- Option to filter by minimum/maximum dimensions

**Example:**
```
Output:
photo1.jpg     1920x1080    2.4 MB    JPEG
photo2.png     3840x2160    8.1 MB    PNG
...
Total: 45 images using 156 MB
```

**Success Criteria:**
- Correctly identifies image files
- Accurate dimension reading
- Handles various image formats
- Size calculations correct

---

## Task 11: Text File Line Shuffler

**Description:** Randomly shuffle the lines of a text file.

**Specification:**
- Accept input filename
- Read all lines from file
- Shuffle lines randomly
- Write to new file (original_shuffled.txt)
- Option to shuffle in-place
- Preserve line endings

**Example:**
```
Input lines: A, B, C, D
Output might be: C, A, D, B
```

**Success Criteria:**
- All lines preserved
- Random order on each run
- No duplicate or missing lines
- Line endings maintained

---

## Task 12: Simple HTTP Request Tester

**Description:** Send HTTP requests and display response details.

**Specification:**
- Accept URL and optional method (GET/POST)
- Make HTTP request
- Display: status code, headers, response time, body preview
- Handle redirects
- Support basic authentication if provided

**Example:**
```
Command: python http_test.py https://api.example.com/data
Output:
Status: 200 OK
Time: 245ms
Content-Type: application/json
Body: {"result": "success", ...}
```

**Success Criteria:**
- Successfully makes requests
- Displays all relevant info
- Handles errors gracefully
- Response time accurate

---

## Task 13: Todo List Extractor

**Description:** Extract TODO comments from source code files.

**Specification:**
- Accept directory path
- Search all .py files recursively
- Find comments containing TODO, FIXME, HACK, NOTE
- Display: filename, line number, comment text
- Group by keyword type
- Option to export to markdown file

**Example:**
```
Output:
TODO (3 items):
  utils.py:45 - TODO: Add error handling
  main.py:102 - TODO: Optimize this loop

FIXME (1 item):
  api.py:67 - FIXME: Memory leak here
```

**Success Criteria:**
- Finds all matching comments
- Accurate line numbers
- Supports Python comment syntax
- Markdown export works

---

## Task 14: File Backup with Timestamp

**Description:** Create timestamped backups of important files.

**Specification:**
- Accept list of files to backup
- Copy each file with timestamp appended
- Format: `filename_YYYYMMDD_HHMMSS.ext`
- Store backups in specified backup directory
- Report success/failure for each file
- Skip if file hasn't changed since last backup

**Example:**
```
Input: config.json
Output: backup/config_20240115_143022.json
```

**Success Criteria:**
- Creates proper backups
- Timestamp format correct
- Handles missing source files
- Skips unchanged files correctly

---

## Task 15: Tab to Space Converter

**Description:** Convert tabs to spaces in source code files.

**Specification:**
- Accept file or directory path
- Convert all tabs to specified number of spaces (default: 4)
- Option to modify in-place or create new files
- Report number of conversions made
- Preserve file permissions and attributes

**Example:**
```
Command: python tab_to_space.py src/ --spaces 2
Output: Converted 23 files (147 tabs replaced)
```

**Success Criteria:**
- All tabs converted
- Spacing consistent
- File structure preserved
- Safe in-place editing option

---

## Tips for Students

- Start with the simplest tasks first
- Ask the AI to explain its approach
- Try modifying the requirements slightly to explore AI adaptability
- Compare your understanding with the AI's solution
- Note which tasks the AI solves most easily

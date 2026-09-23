# Python Log Analyzer

A command-line tool that reads a log file, counts recognised entries, and saves a summary report.

This is my third Python project, following a Mini Calculator and a Number Guessing Game. I built it to practise file handling and basic log analysis as part of my journey towards Cloud and DevOps engineering.

## What It Does

- Reads entries from `server.log`.
- Counts `INFO`, `WARNING`, and `ERROR` entries.
- Calculates the total number of recognised entries.
- Displays the summary in the terminal.
- Saves the summary to `report.txt`.
- Shows a helpful message and stops if the input file is missing.

This tool analyses messages already recorded in a file. It does not monitor a live server, check disk space, or fix errors.

## Project Files

| File | Purpose |
|------|---------|
| `main.py` | Python log analyzer |
| `server.log` | Sample input data |
| `report.txt` | Generated summary report |
| `README.md` | Project documentation |

## Requirements

- Python 3
- No external packages required

## How to Run

Open a terminal inside the `03_log_analyzer` folder and run:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

Run the command from the project folder because file paths are relative to the terminal's current working directory.

## Sample Input

The sample `server.log` contains:

```text
INFO Server started
INFO User logged in
WARNING Disk space low
ERROR Database connection failed
INFO Backup completed
ERROR Request timed out
ERROR Upload failed
```

These are sample messages created for practice, not records of actual server incidents.

## Expected Terminal Output

```text
Total Errors: 3
Total Info: 3
Total Warnings: 1
Total recognised entries: 7
Report saved to report.txt!
```

## Generated Report

The program writes the following summary to `report.txt`:

```text
Total Errors: 3
Total Info: 3
Total Warnings: 1
Total recognised entries: 7
```

Each successful run replaces the previous report.

## How It Works

1. Open and read the input file.
2. Split the text into individual lines using `splitlines()`.
3. Check each line's prefix using `startswith()`.
4. Increment the matching counter.
5. Add the counters and display the results.
6. Write the summary to a text file.

## Concepts Practised

- Functions
- File reading and writing with `with open()`
- String methods: `splitlines()` and `startswith()`
- Lists and `for` loops
- Conditional statements
- Counters and arithmetic
- F-strings and newline characters
- `FileNotFoundError` handling
- Early exit from a function using `return`

## Manual Checks Completed

- Added another `ERROR` entry and confirmed that the error count increased.
- Confirmed that the report updated after running the program again.
- Temporarily renamed the input file and confirmed that the program displayed a message and stopped.
- Confirmed that the seven-entry sample produced 3 errors, 3 info entries, 1 warning, and a total of 7 recognised entries.

## Current Limitations

- Only exact uppercase prefixes `INFO `, `WARNING `, and `ERROR ` are recognised.
- Blank lines, lowercase labels, leading spaces, and other log formats are skipped.
- The total represents recognised entries, not every line in the file.
- The entire input file is loaded into memory, so this version is intended for small practice files.
- Permission errors and report-writing errors are not handled yet.
- If the input file is missing, an existing report remains unchanged.

## Possible Future Improvements

- Accept input and output filenames as arguments.
- Process large files one line at a time.
- Count unrecognised entries separately.
- Export error messages to a separate file.

## Author

**Hamza Abbas**

[GitHub Profile](https://github.com/hamzaabbas-dev)
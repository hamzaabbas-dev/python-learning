def analyze_logs():
    """Count recognised log entries and save a summary report."""

    # Read the log file from the current working directory.
    try:
        with open("server.log", "r") as f:
            content = f.read()
    except FileNotFoundError:
        # Stop before counting or writing a report if the file is missing.
        print("server.log was not found. Please check the file location.")
        return

    # Split the file content into individual log lines.
    lines = content.splitlines()

    error_count = 0
    info_count = 0
    warning_count = 0

    # Match exact uppercase labels followed by a space.
    # Blank lines and unrecognised formats are skipped.
    for line in lines:
        if line.startswith("ERROR "):
            error_count += 1
        elif line.startswith("INFO "):
            info_count += 1
        elif line.startswith("WARNING "):
            warning_count += 1

    # Calculate the total after all lines have been checked.
    total = error_count + info_count + warning_count

    print("Total Errors:", error_count)
    print("Total Info:", info_count)
    print("Total Warnings:", warning_count)

    # Create the report or replace its previous contents.
    with open("report.txt", "w") as f:
        f.write(f"Total Errors: {error_count}\n")
        f.write(f"Total Info: {info_count}\n")
        f.write(f"Total Warnings: {warning_count}\n")
        f.write(f"Total recognised entries: {total}\n")

    print("Total recognised entries:", total)
    print("Report saved to report.txt!")


# Run the log analyzer.
analyze_logs()
def analyze_logs():
    try:
        with open("app.log", "r") as file:
            logs = file.readlines()

        error_count = 0
        warning_count = 0
        info_count = 0

        for line in logs:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

        print("\n==== LOG ANALYZER REPORT ====")
        print(f"Total Logs: {len(logs)}")
        print(f"Errors: {error_count}")
        print(f"Warnings: {warning_count}")
        print(f"Info: {info_count}")

        print("\n==== INSIGHTS ====")

        if error_count > 0:
            print(" ⚠️ There are errors in the system. Needs attention.")
        else:
            print("✅ No critical errors found.")

        if warning_count > 0:
            print("⚠️ Some warnings detected. Review recommended.")
        
        print("System looks stable based on the logs.")

    except Exception as e:
        print("Error reading the log file:", str(e)             )

if __name__ == "__main__":
    analyze_logs()

from datetime import datetime
import csv

def dump_results_old_hackathon(results, name=None):
    if name is None:
        today_dt = datetime.today()
        name = today_dt.strftime("%d-%m-%YT%H:%M:%S")

    with open(f"./results/{name}.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(['row_id', 'results'])

        for idx, item in enumerate(results, start=1):
            writer.writerow([idx, item])

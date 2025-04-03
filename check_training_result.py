def parse_txt_file(txt_file_path):
    """Parse the text file containing classification results."""
    results = {}
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
        for line in lines:
            if not line.strip():
                continue
            parts = line.split(',')
            for i in range(len(parts)):
                if '檔案:' in parts[i]:
                    file_name = parts[i].split('檔案:')[1].strip()
                    pred_class = int(parts[i+1].split('預測類別:')[1].strip())
                    results[file_name] = pred_class
                    break
    return results

def parse_csv_file(csv_file_path):
    """Parse the CSV file containing ground truth labels."""
    ground_truth = {}
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split(',')
            if len(parts) >= 2:
                file_name = parts[0].strip()
                true_class = int(parts[1].strip())
                ground_truth[file_name] = true_class
    return ground_truth

def compare_classifications(txt_file_path, csv_file_path):
    """Compare classifications between text file and CSV file."""
    txt_results = parse_txt_file(txt_file_path)
    csv_ground_truth = parse_csv_file(csv_file_path)
    
    print(f"Found {len(txt_results)} entries in the text file")
    print(f"Found {len(csv_ground_truth)} entries in the CSV file")
    
    # Look for files in both datasets
    matching_files = set(txt_results.keys()) & set(csv_ground_truth.keys())
    only_in_txt = set(txt_results.keys()) - set(csv_ground_truth.keys())
    only_in_csv = set(csv_ground_truth.keys()) - set(txt_results.keys())
    
    print(f"\nFiles in both datasets: {len(matching_files)}")
    if only_in_txt:
        print(f"Files only in text file: {len(only_in_txt)}")
        for file in only_in_txt:
            print(f"  - {file}")
    
    if only_in_csv:
        print(f"Files only in CSV file: {len(only_in_csv)}")
        for file in only_in_csv:
            print(f"  - {file}")
    
    # Check for mismatches
    mismatches = []
    for file in matching_files:
        txt_class = txt_results[file]
        csv_class = csv_ground_truth[file]
        if txt_class != csv_class:
            mismatches.append((file, txt_class, csv_class))
    
    # Print comparison results
    print("\nResults:")
    if not mismatches:
        print("All classifications match! ✓")
    else:
        print(f"Found {len(mismatches)} mismatches:")
        print("File Name, Predicted Class, Ground Truth Class")
        for file, pred, true in mismatches:
            print(f"{file}, {pred}, {true}")
    
    # Print statistics
    match_percentage = (len(matching_files) - len(mismatches)) / len(matching_files) * 100 if matching_files else 0
    print(f"\nAccuracy: {match_percentage:.2f}% ({len(matching_files) - len(mismatches)}/{len(matching_files)})")

if __name__ == "__main__":
    # Replace these with your actual file paths
    txt_file_path = "training_result.txt"
    csv_file_path = "labels.csv"
    
    compare_classifications(txt_file_path, csv_file_path)
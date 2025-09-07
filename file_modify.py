from pathlib import Path
import sys
import re

def prompt_for_file():
    while True:
        fname = input("Enter the filename to read (or 'q' to quit): ").strip()
        if not fname:
            print("Please type a filename or 'q'to quit" )
            continue
        if fname.lower() == 'q':
            print("Exiting.")
            sys.exit(0)
        
        p = Path(fname)
        try:
            if not p.exists():
                raise FileNotFoundError(f"No such file: {p}")
            if p.is_dir():
                raise IsADirectoryError(f"This is a directory, not a file: {p}")
            with p.open("r", encoding="utf-8") as _:
                pass
            return p
        except FileNotFoundError as e:
            print(e)
        except IsADirectoryError as e:
            print(e)
        except PermissionError:
            print(f"Permission deniedwhen trying to read: {p}")
        except UnicodeDecodeError:
            print(f"Filr looks non-UTF-8; will try reading with a fallback encoding")
            return p
        except OSError as e:
            print(f"OS error: {e}")
            
def make_output_path(in_path: Path):
    base = in_path.with_name(in_path.stem + "_modified" + in_path.suffix)
    candidate = base
    i = 1
    while candidate.exists():
        candidate =  base.with_name(f"{in_path.stem}_modified_{i}{in_path.suffix}")
        i += 1
        return candidate
def choose_modification():
    menu="""
Choose a modification to apply:
1) Uppercase whole file
2)Lowercase whole file
3)Add line numbers
4)Remove blank lines
5)Replace a substring (simple find/replace)
6)Collapse repeated whitespace and trim each line
0)No change (copy as-is)
Enter choice[0-6]: """
    choice = input(menu).strip()
    if choice not in {str(i) for i in range(0,7)}:
        print("Invalid choice; defaulting to 'No change'.")
        return "0", {}
    params = {}
    if choice == "5":
        params['find'] = input("Enter the substring to find: ")
        params['replace'] = input("Enter the replacement text: ")
    return choice, params

def process_file(in_path: Path, out_path: Path, choice: str, params: dict):
    # attempt utf-8 first, fall back to latin-1
    encodings = ["utf-8", "latin-1"]
    for enc in encodings:
        try:
            with in_path.open("r", encoding=enc, errors="strict") as reader, \
                 out_path.open("w", encoding="utf-8", errors="replace") as writer:
                line_count = 0
                written_count = 0
                for i, raw_line in enumerate(reader, start=1):
                    line_count += 1
                    line = raw_line.rstrip("\n")  

                    if choice == "1":          
                        out = line.upper()
                    elif choice == "2":        
                        out = line.lower()
                    elif choice == "3":        
                        out = f"{i:4}: {line}"
                    elif choice == "4":        
                        if line.strip() == "":
                            continue
                        out = line
                    elif choice == "5":        
                        out = line.replace(params.get("find", ""), params.get("replace", ""))
                    elif choice == "6":        
                        out = re.sub(r'\s+', ' ', line).strip()
                    else:                      
                        out = line

                    writer.write(out + "\n")
                    written_count += 1

            print(f"Successfully wrote {written_count} lines to: {out_path}")
            return True
        except UnicodeDecodeError:
            
            print(f"Decoding error with encoding={enc}; trying next encoding.")
            continue
        except PermissionError:
            print(f"Permission denied writing to {out_path}.")
            return False
        except OSError as e:
            print(f"Error while processing file: {e}")
            return False
    print("Failed to decode the input file with tried encodings.")
    return False

def main():
    in_path = prompt_for_file()
    out_path = make_output_path(in_path)
    choice, params = choose_modification()
    print(f"Reading from: {in_path}")
    print(f"Will write to: {out_path}")
    ok = process_file(in_path, out_path, choice, params)
    if ok:
        print("Done.")
    else:
        print("There was a problem processing the file.")

if __name__ == "__main__":
    main()

            
            
        
            
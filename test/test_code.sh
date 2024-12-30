#!/bin/bash

CATALOG_PATH="../catalog"
TMP_FOLDER="./tmp"

# Remove previous execution data
rm -rf "$TMP_FOLDER"
mkdir -p "$TMP_FOLDER"

# Function to place "API usage" code of node files in the correct place
process_node_js_file() {
        awk '
        function process_node_js_file(file) {
            block_found = 0
            capture_lines = 0
            line_number = 0
            block_start_line = 0
            insert_position = 0
            indent = ""
            prev_indent = ""
            prev_insert_position = 0

            while ((getline line < file) > 0) {
                line_number++
                if (line ~ /app\.listen\(port, \(\) => {/) {
                    block_found = 1
                    block_start_line = line_number
                    capture_lines = 1
                }
                
                if (capture_lines) {
                    if (line ~ /^$/) {
                        capture_lines = 0
                    } else {
                        captured_lines[line_number] = line
                    }
                } else {
                    original_lines[line_number] = line
                    if (!block_found && (line ~ /^[[:space:]]*\}\)$/)) {
                        prev_insert_position = insert_position
                        insert_position = line_number - 1
                        prev_indent = indent "    "
                        indent = substr(line, 1, match(line, /\}\)/) - 1)
                    }
                }
            }

            if (prev_insert_position == 0) {
                prev_insert_position = insert_position
            }
            for (i = 1; i <= prev_insert_position; i++) {
                if (i in original_lines) {
                    print original_lines[i] > file
                }
            }
            
            for (i = block_start_line; i <= line_number; i++) {
                if (i in original_lines) {
                    print prev_indent original_lines[i] > file
                }
            }
            for (i = prev_insert_position + 1; i < block_start_line; i++) {
                if (i in original_lines) {
                    print original_lines[i] > file
                }
            }
            for (i in captured_lines) {
                if (captured_lines[i] != "") {
                    print indent captured_lines[i] > file
                }
            }
        }

        BEGIN {
            process_node_js_file(ARGV[1])
        }
        ' "$1"
    }

# Function to place "API usage" code of python files in the correct place
process_python_file() {
awk '
function process_python_file(file) {
    block_found = 0
    capture_lines = 0
    line_number = 0
    block_start_line = 0
    insert_position = 0
    indent = ""

    while ((getline line < file) > 0) {
        line_number++
        if (line ~ /if __name__ == '\''__main__'\''/) {
            block_found = 1
            block_start_line = line_number
            insert_position = line_number - 1
            indent = "    "
            capture_lines = 1
        }
        
        if (capture_lines) {
            if (line ~ /^$/) {
                capture_lines = 0
            } else {
                captured_lines[line_number] = line
            }
        } else {
            original_lines[line_number] = line
        }
    }

    for (i = 1; i <= insert_position; i++) {
        if (i in original_lines) {
            print original_lines[i] > file
        }
    }
    
    for (i = insert_position; i <= line_number; i++) {
        if (i in original_lines) {
            if (original_lines[i] != "") {
                print indent original_lines[i] > file
            }
        }
    }

    print "" > file
    print "" > file
    for (i in captured_lines) {
        print captured_lines[i] > file
    }
}

BEGIN {
    process_python_file(ARGV[1])
}
' "$1"
    }

# Loop through samplecode_ files
for samplecode_file in $(find "$CATALOG_PATH" -maxdepth 3 -type f -name "samplecode_*.md"); do
# Extract the part of the file name between samplecode_ and .md
    filename=$(basename "$samplecode_file")
    name=${filename#samplecode_}
    name=${name%.md}

    awk -v TMP_FOLDER="$TMP_FOLDER" -v name="$name" '
    BEGIN {
        blockCount = 0
        blockCode = ""
        fileName = ""
        fileExt = ""
    }

    /^### (Frontend|Frontend flow|Backend|Backend Flow)/ {
        blockCode = $0
        gsub(/### /, "", blockCode) # Remove ### 
        gsub(/Backend flow/, "CIBA", blockCode)
        gsub(/Frontend flow/, "Auth_code", blockCode)
        gsub(/Backend/, "Auth_code", blockCode)
        gsub(/Frontend/, "Auth_code", blockCode)
        gsub(/ /, "_", blockCode)
    }

    /^```/ {
        flag = !flag
        if (flag) {
            sub(/^```/, "", $1)
            language = $1
            title = substr($0, index($0, $2))
            gsub(/ /, "_", title)
            # Define the file type mapping
            fileExt = "txt"
            switch (language) {
                case "html":
                    fileExt = "html"
                    break
                case "java":
                    fileExt = "java"
                    break
                case "python":
                    fileExt = "py"
                    break
                case "node":
                case "javascript":
                case "ecmascript":
                    fileExt = "js"
                    break
            }
            blockCount++
            dir = TMP_FOLDER "/" fileExt "/" name
            fileName = dir "/" blockCode "_" title "." fileExt
            system("mkdir -p " dir)
        } else {
            print "" >> fileName  # Add a blank line at the end of the block
        }
        next
    }

    flag {
        print >> fileName
    }
    ' "$samplecode_file"
    # At this point, we have a folder for each programming language and all the code blocks 
    # that have the same title have been put together.
    # Reordering the code in the auth code node files
    for file in "$TMP_FOLDER/js/$name"/Auth_code*Node.js.js; do
        if [ -f "$file" ]; then
            process_node_js_file "$file"
        fi
    done

    # Reordering the code in the auth code python files
    for file in "$TMP_FOLDER/py/$name"/Auth_code*Python.py; do
        if [ -f "$file" ]; then
            process_python_file "$file"
        fi
    done
    echo "Processing $name ==> $samplecode_file"
done

# Execute test and linter
echo "################### Python test ##################################"
python python_test.py
echo "################### Node test ##################################"
npx jest nodeSandbox.test.js 
echo "################### Node linter ##################################"
npx eslint 'tmp/js/**/*.js'
echo "################### Python linter ##################################"
flake8 --ignore=E501,W391 tmp/py

import os

directory = 'technologies' # directory for files; script should be one level up from directory
to_replace = '1946' # string to be replaced
replace = '2005' # what to replace string to be replaced with

def main():
    for filename in os.listdir(directory):
        lines = []
        with open(directory + '/' + filename) as file:
            for line in file:
                lines.append(line.replace(to_replace, replace))
        with open(directory + '/' + filename, 'w') as f:
            for line in lines:
                f.write(line)

if __name__ == '__main__':
    main()

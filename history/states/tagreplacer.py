import os

directory = 'states' # directory for files; script should be one level up from directory
to_replace = 'DEN' # string to be replaced
replace = 'ALX' # what to replace string to be replaced with

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
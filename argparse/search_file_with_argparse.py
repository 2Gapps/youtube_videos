import argparse

parser = argparse.ArgumentParser()

parser.add_argument(    
    '-s',
    '--search_string',
    default= 'Verifying',
    help='Search string to be searched')

input_arguments = parser.parse_args()


search_string = input_arguments.search_string


with open('news.txt') as news_file:
    for line_no, line in enumerate(news_file, 1):
        if search_string.lower() in line.lower():
            print(line_no, ':', line)

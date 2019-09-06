import os
import csv
from datetime import date

def write_book_data():
    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'output_fahasa.csv'
    )

    script_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'script.sql'
    )


    print(input_file_path)
    with open(input_file_path, 'r', encoding='utf8', errors='ignore') as csvFile:
        with open(script_file_path, 'w', encoding='utf8', errors='ignore') as txt_file:
            csv_reader = csv.reader(csvFile, delimiter=',')
            for row in csv_reader:
                print(row)
                book_id = row[2]
                book_category_id = row[0]
                book_type = 'ebook'
                book_title = row[1]
                book_author = row[3]
                book_public_date = row[4]
                book_rating = row[5]
                book_rated_time = row[6]
                book_download = row[7]
                book_page = row[8]
                book_description = row[1]
                book_image = row[10]
                book_file = row[11]
                book_upload_date = date.today()

                txt_file.write(f"insert into Book values('{book_id}', {book_category_id},'{book_type}','{book_title}','{book_author}','{book_public_date}',{book_rating},{book_rated_time},{book_download},{book_page},'{book_description}','{book_image}','{book_file}','{book_upload_date}',0);")
                txt_file.write('\n')

write_book_data()


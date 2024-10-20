# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines_page = 50
str_line = 25
bytes_str = 4
size_mb = 1.44
size_bytes = size_mb * 1024 * 1024
str_page = lines_page * str_line
total_str = pages *  str_page
book = total_str * bytes_str
num_books = int(size_bytes // book)

print("Количество книг, помещающихся на дискету:", num_books)

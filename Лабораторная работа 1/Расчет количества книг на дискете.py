# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines_page = 50
line = 25
bytes = 4
size_mb = 1.44
size_bytes = size_mb * 1024 * 1024
page = lines_page * line
total = pages *  page
book = total * bytes
num_books = int(size_bytes // book)

print("Количество книг, помещающихся на дискету:", num_books)

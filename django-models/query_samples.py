from datetime import date
from relationship_app.models import Author, Book, Library

# إنشاء مؤلف جديد
author = Author.objects.create(name="Ahmed Ali", email="ahmed@example.com")

# إنشاء كتاب مرتبط بالمؤلف
book = Book.objects.create(title="Learning Django", publication_date=date(2024, 7, 1), author=author)

# إنشاء مكتبة وإضافة الكتاب إليها
library = Library.objects.create(name="Central Library")
library.books.add(book)

# استعلام: جلب كل كتب المؤلف
author_books = author.books.all()

# استعلام: جلب كل المكتبات التي تحتوي على كتاب معين
book_libraries = book.libraries.all()

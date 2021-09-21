import pymongo
from pymongo import MongoClient

def get_db_handle(db_name,book_id, book_Title, author_Name):

 client = MongoClient(book_id = book_id,
                    book_Title = book_Title,
                      author_Name = author_Name,
                     )

 db_handle = client['db_name']
 return db_handle, client
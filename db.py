class connect_db:
    import pymongo
    __client__ = pymongo.MongoClient("mongodb+srv://spr:spr771@new.su8ufya.mongodb.net/?retryWrites=true&w=majority")
    db = __client__.Hotels
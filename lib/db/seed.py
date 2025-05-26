from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed():
    a1 = Author(name="Ignatius")
    a1.save()

    m1 = Magazine(name="Tech Weekly", category="Technology")
    m1.save()

    Article(title="AI in 2025", author_id=a1.id, magazine_id=m1.id).save()

if __name__ == "__main__":
    seed()

from lib.models.author import Author

def test_create_author():
    author = Author(name="Test Author")
    author.save()
    assert author.id is not None

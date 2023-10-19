from db.database import Session
from db.models import User

def test_database_connection():
    # Create a session
    session = Session()

    # Add a user to the database
    user = User(username='testuser', email='testuser@example.com')
    session.add(user)
    session.commit()

    # Query the user from the database
    queried_user = session.query(User).filter_by(username='testuser').first()

    # Assert that the queried user is the same as the added user
    assert queried_user.username == user.username
    assert queried_user.email == user.email

    # Delete the user from the database
    session.delete(user)
    session.commit()

    # Close the session
    session.close()
    assert True

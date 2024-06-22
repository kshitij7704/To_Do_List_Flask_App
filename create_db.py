from app import db, app

with app.app_context():
    # Creating all databases defined in app
    db.create_all()
    print("Database tables created successfully.")

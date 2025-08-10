from src.eloApp.database.database import SessionLocal
from eloApp.database import acolhedor_service

def main():
    # The 'get_db' function is designed to be used with a web framework's
    # dependency injection system (like FastAPI).
    # For a simple script, you can use the session directly:

    db = SessionLocal()

    # Create a new Acolhedor
    new_acolhedor = acolhedor_service.create_acolhedor(db, name="John Doe", email="john.doe@example.com")
    print(f"Created Acolhedor: {new_acolhedor}")

    # Get all Acolhedores
    all_acolhedores = acolhedor_service.get_all_acolhedores(db)
    print("All Acolhedores:")
    for acolhedor in all_acolhedores:
        print(acolhedor)

    # Update an Acolhedor's email
    updated_acolhedor = acolhedor_service.update_acolhedor_email(db, acolhedor_id=new_acolhedor.id, new_email="john.doe.new@example.com")
    print(f"Updated Acolhedor: {updated_acolhedor}")

    # Delete the Acolhedor
    acolhedor_service.delete_acolhedor(db, acolhedor_id=new_acolhedor.id)
    print("Acolhedor deleted.")

    db.close()


if __name__ == "__main__":
    main()

from app import create_app

app = create_app()


if __name__ == "__main__":
    # Runs the development server. For production use a WSGI server.
    app.run(debug=True)

from website import create_app
import os

app = create_app()

if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
        # Change to debug=False before submitting for security purposes.
        # It is only for development.
    )

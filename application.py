from dotenv import load_dotenv

load_dotenv()

import app



if __name__ == "__main__":
    instance_app = app.create_app()
    instance_app.run(debug=True, host='0.0.0.0', port=5000)

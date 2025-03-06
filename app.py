from flask import Flask
from Course import create_course_app

app = create_course_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


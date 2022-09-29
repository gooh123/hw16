from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.run(debug=True)


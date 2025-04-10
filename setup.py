def crear_pagina():

    html = """

    <!DOCTYPE html>

    <html lang="es">

    <head>

        <meta charset="UTF-8">

        <title>DevOps</title>

    </head>

    <body>

        <h1>¡Hola desde el script Python de DevOps!</h1>

    </body>

    </html>

    """

    with open("/tmp/index.html", "w", encoding="utf-8") as f:

        f.write(html)

    run("sudo mv /tmp/index.html /var/www/html/index.html")

if __name__ == "__main__":

    instalar_apache()

    crear_pagina()


